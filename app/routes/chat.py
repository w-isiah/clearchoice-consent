from flask import Blueprint, request, jsonify, render_template, session
from app.services.gpt_service import chat_advice

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")


@chat_bp.route("/", methods=["GET"])
def chat_page():
    """Render the chat UI page."""
    return render_template("chat.html")


@chat_bp.route("/", methods=["POST"])
def chat_api():
    """Handle interactive chat with session-based memory."""
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    question = data.get("question")

    if not user_id or not question:
        return jsonify({"error": "Both user_id and question are required"}), 400

    # Ensure conversations exist in session
    if "conversations" not in session:
        session["conversations"] = {}
    if user_id not in session["conversations"]:
        session["conversations"][user_id] = []

    try:
        # Load user history
        history = session["conversations"][user_id]

        # Add user message
        history.append({"role": "user", "content": question})

        # Get GPT advice (with context from history)
        answer = chat_advice(user_id, history)

        # Add assistant response
        history.append({"role": "assistant", "content": answer})

        # Save history back to session
        session["conversations"][user_id] = history

        return jsonify({"answer": answer, "history": history})

    except Exception as e:
        print(f"❌ Chat error: {e}")
        return jsonify({"error": "Something went wrong while processing your request."}), 500


@chat_bp.route("/history", methods=["GET"])
def get_history():
    """Return full chat history for a user."""
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    history = session.get("conversations", {}).get(user_id, [])
    return jsonify({"history": history})


@chat_bp.route("/clear", methods=["POST"])
def clear_chat():
    """Clear a user's chat history."""
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    if "conversations" in session and user_id in session["conversations"]:
        session["conversations"][user_id] = []

    return jsonify({"message": "Chat history cleared."})

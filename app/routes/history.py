from flask import Blueprint, request, jsonify, render_template
from app.db import get_db_connection

history_bp = Blueprint('history', __name__, url_prefix="/history")

@history_bp.route('/', methods=['GET'])
def history_page():
    """Render the history page template."""
    return render_template("history.html")


@history_bp.route('/api', methods=['GET'])
def get_history():
    """Return user history as JSON."""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT action, model, tokens_used, success, timestamp 
        FROM user_history 
        WHERE user_id=%s 
        ORDER BY timestamp DESC
    """, (user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({"history": rows})


@history_bp.route('/clear', methods=['DELETE'])
def clear_history():
    """Clear all history for a given user."""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_history WHERE user_id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "History cleared"})

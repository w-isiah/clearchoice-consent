from flask import Blueprint, request, jsonify, render_template
from app.services.gpt_service import summarize_text

summarize_bp = Blueprint('summarize', __name__)

@summarize_bp.route('/', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        data = request.json
        user_id = data.get('user_id')
        text = data.get('text')
        if not user_id or not text:
            return jsonify({"error": "user_id and text required"}), 400
        try:
            summary = summarize_text(user_id, text)
            return jsonify({"summary": summary})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template("summarize.html")

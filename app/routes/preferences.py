from flask import Blueprint, request, jsonify, render_template
from app.db import get_db_connection

preferences_bp = Blueprint('preferences', __name__)

@preferences_bp.route('/', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        data = request.json
        user_id = data.get('user_id')
        preference = data.get('preference')
        if not user_id or not preference:
            return jsonify({"error": "user_id and preference required"}), 400
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user_preferences (user_id, preference)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE preference = %s
        """, (user_id, preference, preference))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Preference saved"})
    return render_template("preferences.html")

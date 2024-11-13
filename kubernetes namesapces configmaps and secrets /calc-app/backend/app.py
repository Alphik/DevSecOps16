from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )
    return conn

def initialize_db():
    """Create the calculations table if it does not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calculations (
        id SERIAL PRIMARY KEY,
        formula TEXT NOT NULL,
        result NUMERIC NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Run this function to set up the database when the app starts
initialize_db()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    formula = data.get('formula')
    try:
        result = eval(formula, {'__builtins__': None}, {})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO calculations (formula, result) VALUES (%s, %s)",
        (formula, result)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"formula": formula, "result": result})

@app.route('/history', methods=['GET'])
def get_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT formula, result FROM calculations ORDER BY id DESC")
    history = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')

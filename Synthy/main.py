from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
import random

app = Flask(__name__)
db = TinyDB("quiz.json")

@app.route("/api/get-random-question", methods=["GET"])
def get_random_question():
    questions = db.all()
    if questions:
        question = random.choice(questions)
        return jsonify({"id": question.doc_id, "text": question["text"]})
    else:
        return jsonify({"error": "Ni razpoložljivih vprašanj"}), 404

@app.route("/api/check-answer", methods=["POST"])
def check_answer():
    data = request.json
    question_id = data.get("id")
    user_answer = data.get("answer").strip().lower()
    
    Question = Query()
    question = db.get(doc_id=question_id)
    
    if question:
        is_correct = user_answer == question["answer"].strip().lower()
        return jsonify({"correct": is_correct})
    else:
        return jsonify({"error": "Vprašanje ne obstaja"}), 404

if __name__ == "__main__":
    app.run(debug=True)

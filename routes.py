from flask import Blueprint, request, jsonify, session
from data import syllabus_data

chatbot_bp = Blueprint("chatbot", __name__)

# Initialize session state
@chatbot_bp.before_request
def init_session():
    if "state" not in session:
        session["state"] = "start"

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip().lower()

    if user_input == "back":
        return go_back()

    state = session["state"]

    if state == "start":
        session["state"] = "select_branch"
        return jsonify({"bot": "Hi! What are you interested in?", "options": list(syllabus_data.keys())})

    elif state == "select_branch":
        if user_input in syllabus_data:
            session["branch"] = user_input
            session["state"] = "select_year"
            return jsonify({"bot": "Which year are you in?", "options": ["Second Year", "Third Year", "Final Year"]})
        else:
            return jsonify({"bot": "I don't understand. Choose from the given options.", "options": list(syllabus_data.keys())})

    elif state == "select_year":
        if user_input in ["second year", "third year", "final year"]:
            session["year"] = user_input
            session["state"] = "select_semester"
            return jsonify({"bot": "Which semester?", "options": ["Sem 1", "Sem 2"]})
        else:
            return jsonify({"bot": "I don't understand. Choose from the given options.", "options": ["Second Year", "Third Year", "Final Year"]})

    elif state == "select_semester":
        if user_input in ["sem 1", "sem 2"]:
            session["semester"] = user_input
            branch = session["branch"]
            year = session["year"]
            semester = session["semester"]
            subjects = syllabus_data[branch][year][semester]
            session["state"] = "select_subject"
            return jsonify({"bot": "Choose a subject:", "options": list(subjects.keys())})
        else:
            return jsonify({"bot": "I don't understand. Choose from the given options.", "options": ["Sem 1", "Sem 2"]})

    elif state == "select_subject":
        branch = session["branch"]
        year = session["year"]
        semester = session["semester"]
        subjects = syllabus_data[branch][year][semester]

        if user_input in subjects:
            session["subject"] = user_input
            session["state"] = "show_units"
            return jsonify({"bot": "Here are the units:", "options": subjects[user_input]})
        else:
            return jsonify({"bot": "I don't understand. Choose from the given options.", "options": list(subjects.keys())})

    return jsonify({"bot": "Something went wrong. Try again."})

def go_back():
    state = session["state"]

    if state == "select_year":
        session["state"] = "select_branch"
        return jsonify({"bot": "Hi! What are you interested in?", "options": list(syllabus_data.keys())})

    elif state == "select_semester":
        session["state"] = "select_year"
        return jsonify({"bot": "Which year are you in?", "options": ["Second Year", "Third Year", "Final Year"]})

    elif state == "select_subject":
        session["state"] = "select_semester"
        return jsonify({"bot": "Which semester?", "options": ["Sem 1", "Sem 2"]})

    elif state == "show_units":
        session["state"] = "select_subject"
        branch = session["branch"]
        year = session["year"]
        semester = session["semester"]
        subjects = syllabus_data[branch][year][semester]
        return jsonify({"bot": "Choose a subject:", "options": list(subjects.keys())})

    return jsonify({"bot": "You're at the start. No previous step."})

from flask import Flask, jsonify, request

attendance = Flask(__name__)

attendees = [
    {"attendee_id": 1, "name": "John", "checked_in": "true"},
    {"attendee_id": 2, "name": "Lily", "checked_in": "true"},
    {"attendee_id": 3, "name": "Denia", "checked_in": "true"},
    {"attendee_id": 4, "name": "Nihilux", "checked_in": "false"},
    {"attendee_id": 5, "name": "Firefly", "checked_in": "false"}
]

# Endpoint 1
@attendance.route('/attendees', methods=['GET'])
def get_attendees():
    if not attendees:
        return jsonify({"message": "No attendees found."}), 404
    return jsonify(attendees), 200

# Endpoint 2
@attendance.route('/attendees/<int:attendee_id>', methods=['GET'])
def get_attendee(attendee_id):
    for attendee in attendees:
        if attendee["attendee_id"] == attendee_id:
            return jsonify(attendee), 200
    return jsonify({"error": "Attendee not found."}), 404

# Endpoint 3
# Endpoint 4

if __name__ == '__main__':
    attendance.run(debug=True)

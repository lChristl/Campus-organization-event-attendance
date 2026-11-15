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
# Endpoint 2
# Endpoint 3
# Endpoint 4
@attendance.route('/attendees/<int:attendee_id>', methods=['DELETE'])
def delete_attendee(attendee_id):
    for attendee in attendees:
        if attendee["attendee_id"] == attendee_id:
            attendees.remove(attendee)
            return jsonify({"message": f"Attendee {attendee_id} deleted"}), 200
    return jsonify({"error": f"Attendee {attendee_id} not found"}), 404

if __name__ == '__main__':
    attendance.run(debug=True)

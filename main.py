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

if __name__ == '__main__':
    attendance.run(debug=True)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "Fire Base URL"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Nithin G",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 19,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-07-21 00:55:34"
        },
    "1SP21CS006":
        {
            "name": "Ajay Jangir",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2024-07-21 00:54:34"
        },
}
for key, value in data.items():
    ref.child(key).set(value)
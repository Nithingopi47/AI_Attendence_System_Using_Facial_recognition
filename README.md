# Face Attendance System with Real-time Recognition and Firebase Integration

A real-time face attendance system that uses computer vision to detect faces, match them against a database of known students, and automatically record attendance in Firebase. The system provides immediate visual feedback and maintains attendance records with timestamps.

The system combines OpenCV and face_recognition libraries for accurate face detection and recognition, with Firebase integration for secure data storage and retrieval. It features a professional user interface that displays student information, attendance status, and profile images in real-time. The system includes cooldown periods to prevent duplicate attendance entries and supports multiple operational modes for different stages of the attendance process.

## Repository Structure
```
.
├── main.py                     # Core application with face recognition and attendance logic
├── EncodeGenerator.py          # Generates face encodings from student images
├── AddDatatoDatabase.py        # Utility to add student records to Firebase
├── requirements.txt            # Project dependencies
├── test.py                     # Image processing and face recognition testing
├── testing.py                  # Camera device testing utility
├── serviceAccountKey.json      # Firebase service account credentials
└── uninstall_packages.py       # Utility script for package management
```

## Usage Instructions
### Prerequisites
- Python 3.7 or higher
- Webcam or compatible camera device
- Firebase account with Realtime Database and Storage configured
- `serviceAccountKey.json` with valid Firebase credentials
- Student images in an 'Images' folder (named with student IDs)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd face-attendance-system

# Install required packages
pip install -r requirements.txt

# Configure Firebase credentials
# Place your serviceAccountKey.json in the root directory
```

### Quick Start
1. Add student data to Firebase:
```python
python AddDatatoDatabase.py
```

2. Generate face encodings:
```python
python EncodeGenerator.py
```

3. Run the main application:
```python
python main.py
```

### More Detailed Examples
1. Adding a new student to the database:
```python
# In AddDatatoDatabase.py
data = {
    "student_id": {
        "name": "Student Name",
        "major": "Department",
        "starting_year": 2024,
        "total_attendance": 0,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2024-01-01 00:00:00"
    }
}
```

2. Testing camera setup:
```python
python testing.py
```

### Troubleshooting
1. Camera Access Issues
   - Error: "Could not open camera"
   - Solution: Check if another application is using the camera
   - Run `testing.py` to verify camera accessibility

2. Face Recognition Problems
   - Error: "No face found"
   - Solution: 
     - Ensure proper lighting
     - Check image quality
     - Run `test.py` with specific image path to debug

3. Firebase Connection Issues
   - Error: Firebase initialization failed
   - Solution:
     - Verify `serviceAccountKey.json` is present and valid
     - Check database URLs in configuration
     - Ensure proper Firebase permissions

## Data Flow
The system processes attendance data through a streamlined pipeline from face detection to database storage.

```ascii
[Camera Input] -> [Face Detection] -> [Face Recognition] -> [Student Lookup]
       |                                                           |
       v                                                          v
[Frame Processing] <- [UI Update] <- [Attendance Recording] <- [Firebase DB]
```

Key component interactions:
1. Camera captures frames at 640x480 resolution
2. Face detection processes downscaled images (0.25x) for efficiency
3. Face recognition compares detected faces against stored encodings
4. Firebase Realtime Database stores and retrieves student information
5. Firebase Storage manages student profile images
6. UI updates show real-time attendance status and student details
7. Cooldown system prevents duplicate attendance entries (30-second window)

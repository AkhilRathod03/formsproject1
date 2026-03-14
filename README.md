 # 🎓 Student Management System (Django)

 A simple and responsive Student Management application built with **Django** and **Bootstrap**. This project allows users to register students, upload their images, and perform full CRUD (Create, Read, Update, Delete) operations.
    
✨ Features
   **Register Student:** Add student details including name, ID, marks, and image.
   **Student List:** View all students in a clean, styled table.
   **Edit/Update:** Modify existing student information and images.
   **Delete:** Remove student records from the database.
   **Image Sharpness:** Custom CSS for crisp, clear student thumbnails (60x70).
   **Auto-Capitalization:** Student names are automatically capitalized when saved.

🛠️ Tech Stack
   **Backend:** Python 3.x, Django 5.x
   **Frontend:** HTML5, CSS3, Bootstrap 5, Animate.css
   **Database:** SQLite (default for easy sharing)
   **Images:** Django ImageField with Pillow

🚀 How to Run Locally

1.  **Clone the project:**
      git clone https://github.com/AkhilRathod03/formsproject1.git


2.  **Install dependencies:**
      pip install -r requirements.txt
3.  **Run Migrations:**
      python manage.py migrate
4.  **Start the Server:**
      python manage.py runserver


5.  **Open in Browser:**
     Go to `http://127.0.0.1:8000/`

   
   📂 Project Structure
   `myapp/`: Contains the core logic (models, views, forms).
   `templates/`: HTML files for registration, editing, and listing students.
   `media/`: Stores uploaded student profile images.
   `db.sqlite3`: Pre-loaded with sample student data.
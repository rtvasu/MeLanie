#this file is meant to be a placeholder for embedded pages on the website
from app import app

@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin dashboard"
# LMS App hooks

app_name = "lms_app"
app_title = "LMS App"
app_publisher = "Abigael Lemba"
app_description = "Learning Management System"
app_email = "mbitheabigail20@gmail.com"
app_license = "MIT"

# Fixtures to export specific doctypes and configurations
fixtures = [
    # Export core LMS Doctypes
    {"dt": "DocType", "filters": [["name", "in", [
        "Enrollment",
        "Lesson",
        "Trainer",
        "Ministry Interest",
        "Student",
        "Course",
        "Certificate"
    ]]]},

    # Export Custom Fields created in the LMS App
    {"dt": "Custom Field", "filters": [["module", "=", "Lms App"]]},

    # Export LMS Workspace (for sidebar UI)
    {"dt": "Workspace", "filters": [["module", "=", "Lms App"]]},

    # Export Trainer and Student roles if custom-created
    {"dt": "Role", "filters": [["name", "in", ["Trainer", "Student"]]]}
]

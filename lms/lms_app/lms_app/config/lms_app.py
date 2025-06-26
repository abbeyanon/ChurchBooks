# lms_app/config/lms_app.py

from frappe import _

def get_data():
    return [
        {
            "module_name": "LMS APP",
            "type": "module",
            "label": _("LMS APP")
        }
    ]

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class Enrollment(Document):
    def on_update(self):
        if self.status == "Completed":
            generate_certificate_for_enrollment(self)

def generate_certificate_for_enrollment(enrollment):
    student = frappe.get_doc("Student", enrollment.student)

    # Avoid duplicates
    existing = [cert.course for cert in student.certificates]
    if enrollment.course in existing:
        return

    # Add new certificate row
    student.append("certificates", {
        "course": enrollment.course,
        "issue_date": nowdate(),
        "template": "Default Certificate Template",
        "certificate_id": f"CERT-{enrollment.student}-{frappe.utils.now().split()[0]}"
    })

    student.save()
    frappe.db.commit()
    frappe.msgprint(f"✅ Certificate generated for {student.name}")


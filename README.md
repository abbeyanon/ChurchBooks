# ChurchBooks

**ChurchBooks** is a consolidated Frappe-based ERP system for managing church finances, operations, and ministry tasks. It combines the capabilities of the **cfms_plus** (Church Finance Management System) and LMS apps in one repository.

## 📦 Apps Included

- `cfms_plus`: An Enhanced Church Finance and ERP System
- `lms`: A Learning Management System for church training and discipleship (coming soon)

---

## ✨ Features of `cfms_plus`

- Church branch setup and automatic Chart of Accounts creation
- Member registration with auto-generated Member ID
- Event and program management with informative notices and workflow approvals
- Attendance tracking for both events and church services
- Member-linked giving and auto-journal entries
- Daily scheduler for updating event statuses
- Custom Workflows, Roles, Email Templates, and Client Scripts

---

## ⚙️ Installation Guide

Follow these steps to get started with ChurchBooks:
Note: Ensure you have a working Frappe Bench And ERPnext

### 🚀 Full Installation Steps (1–4 Combined)

```bash
# Step 1: Clone the ChurchBooks repo and move the apps into bench
cd ~/frappe-bench/apps
git clone https://github.com/abbeyanon/ChurchBooks.git
mv ChurchBooks/cfms_plus .
mv ChurchBooks/lms .

# Step 2–4: Install apps, migrate, and start the server
cd ~/frappe-bench
bench --site your_site_name install-app cfms_plus
bench --site your_site_name install-app lms        
bench --site your_site_name migrate
bench start

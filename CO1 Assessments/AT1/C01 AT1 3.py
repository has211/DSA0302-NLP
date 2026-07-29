import re

# -----------------------------------------
# Validation Functions
# -----------------------------------------

# Register Number (Example: 22CSE1012)
def validate_register_number(reg_no):
    pattern = r'^\d{2}[A-Z]{2,4}\d{4}$'
    return bool(re.match(pattern, reg_no))


# Institutional Email (Example: student@university.edu)
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@university\.edu$'
    return bool(re.match(pattern, email))


# Course Code (Example: CS301, MA205, AI401)
def validate_course_code(course):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(pattern, course))


# Semester (Semester 1 to Semester 8)
def validate_semester(semester):
    pattern = r'^[1-8]$'
    return bool(re.match(pattern, semester))


# Mobile Number (Indian Mobile Number)
def validate_mobile(mobile):
    pattern = r'^(?:\+91[- ]?)?[6-9]\d{9}$'
    return bool(re.match(pattern, mobile))


# -----------------------------------------
# Display Validation Result
# -----------------------------------------
def display_result(field, status):
    if status:
        print(field, ": Valid")
    else:
        print(field, ": Invalid")


# -----------------------------------------
# Main Program
# -----------------------------------------

register_number = "22CSE1012"
email = "rahul@university.edu"
course_code = "CS301"
semester = "5"
mobile = "9876543210"

print("=" * 55)
print("UNIVERSITY REGISTRATION VALIDATION SYSTEM")
print("=" * 55)

reg_status = validate_register_number(register_number)
email_status = validate_email(email)
course_status = validate_course_code(course_code)
semester_status = validate_semester(semester)
mobile_status = validate_mobile(mobile)

display_result("Register Number", reg_status)
display_result("Institutional Email", email_status)
display_result("Course Code", course_status)
display_result("Semester", semester_status)
display_result("Mobile Number", mobile_status)

print("\n" + "=" * 55)

if (reg_status and email_status and course_status
        and semester_status and mobile_status):
    print("Registration Status : SUCCESSFUL")
else:
    print("Registration Status : FAILED")

print("=" * 55)

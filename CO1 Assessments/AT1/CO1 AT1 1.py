import re

# -----------------------------
# Function to extract Name
# -----------------------------
def extract_name(text):
    lines = text.strip().split("\n")
    if lines:
        return lines[0].strip()
    return "Not Found"


# -----------------------------
# Function to extract Email
# -----------------------------
def extract_email(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    emails = re.findall(pattern, text)
    return emails if emails else ["Not Found"]


# -----------------------------
# Function to extract Mobile Number
# -----------------------------
def extract_mobile(text):
    pattern = r'(?:\+91[- ]?)?[6-9]\d{9}'
    mobiles = re.findall(pattern, text)
    return mobiles if mobiles else ["Not Found"]


# -----------------------------
# Function to extract Skills
# -----------------------------
def extract_skills(text):
    skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
    found_skills = []

    for skill in skill_list:
        if re.search(skill, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


# -----------------------------
# Function to extract Experience
# -----------------------------
def extract_experience(text):
    pattern = r'(\d+)\+?\s*(?:years|year)'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return int(match.group(1))
    else:
        return 0


# -----------------------------
# Function to generate Summary
# -----------------------------
def generate_summary(resume):
    name = extract_name(resume)
    email = extract_email(resume)
    mobile = extract_mobile(resume)
    skills = extract_skills(resume)
    experience = extract_experience(resume)

    profile = {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Skills": skills,
        "Experience": experience
    }

    return profile


# -----------------------------
# Function to check Eligibility
# -----------------------------
def is_eligible(profile):

    if profile["Experience"] >= 2 and "Python" in profile["Skills"]:
        return True
    return False


# -----------------------------
# Sample Resumes
# -----------------------------

resume1 = """
Rahul Sharma
Email: rahul.sharma@gmail.com
Mobile: +91 9876543210
Skills: Python, Java, SQL, Machine Learning
Experience: 4 years
"""

resume2 = """
Priya Verma
Email: priya@gmail.com
Phone: 9123456789
Skills: Java, SQL
Experience: 1 year
"""

resume3 = """
Ankit Kumar
Email: ankit@yahoo.com
Phone: 9876501234
Skills: Python, NLP
Experience: 3 years
"""

resumes = [resume1, resume2, resume3]

# -----------------------------
# Main Program
# -----------------------------

print("="*60)
print("RESUME INFORMATION EXTRACTION SYSTEM")
print("="*60)

eligible_candidates = []

for i, resume in enumerate(resumes, start=1):

    profile = generate_summary(resume)

    print("\nCandidate", i)
    print("-"*40)

    print("Name       :", profile["Name"])
    print("Email      :", profile["Email"])
    print("Mobile     :", profile["Mobile"])
    print("Skills     :", profile["Skills"])
    print("Experience :", profile["Experience"], "Years")

    if is_eligible(profile):
        eligible_candidates.append(profile["Name"])

print("\n" + "="*60)
print("Eligible Candidates")
print("="*60)

if eligible_candidates:
    for candidate in eligible_candidates:
        print(candidate)
else:
    print("No eligible candidates found.")

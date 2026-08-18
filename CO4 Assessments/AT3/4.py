subject = {"word":"She","number":"singular","person":"third"}
verb = {"word":"eats","number":"singular","person":"third"}
if subject["number"] == verb["number"] and subject["person"] == verb["person"]:
    print("Correct subject-verb agreement")
else:
    print("Incorrect subject-verb agreement")
frames = {
    "eat":["Subject","Object"],
    "sleep":["Subject"],
    "give":["Subject","Object","Recipient"]
}
verb = "eat"
arguments = ["Subject","Object"]
if frames[verb] == arguments:
    print("Correct argument structure")
else:
    print("Incorrect argument structure")

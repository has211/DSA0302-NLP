import re

def parse(expression):
    expression = expression.replace(" ", "")

    if re.match(r'^[A-Za-z]+\([A-Za-z,]+\)$', expression):
        print("Valid atomic expression")
    elif re.match(r'^[A-Za-z]+\([A-Za-z]+\)$', expression):
        print("Valid predicate expression")
    elif "AND" in expression or "OR" in expression:
        print("Valid logical expression")
    elif expression.startswith("NOT"):
        print("Valid negation expression")
    else:
        print("Invalid expression")

expression = input("Enter FOPC expression: ")
parse(expression)
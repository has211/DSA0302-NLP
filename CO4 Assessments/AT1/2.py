# AT1 - Q2
# First-Order Predicate Calculus for Smart Manufacturing

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

# Predicate rules
def production_status(machine, status):
    if status == "Active":
        return f"Producing({machine})"
    elif status == "Maintenance":
        return f"Not Producing({machine})"


print("Machine Production Status")
print("=" * 40)

for machine, status in machines.items():
    result = production_status(machine, status)
    print(machine, ":", result)

print("\nPredicate Rules")
print("=" * 40)

print("Active(x) -> Producing(x)")
print("Produces(x,y) AND Active(x) -> Available(y)")
print("Maintenance(x) -> NOT Producing(x)")

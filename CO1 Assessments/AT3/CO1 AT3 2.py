# DFA for strings ending with "ab"

transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter input string: ")

state = start_state
path = [state]

valid = True

for ch in string:
    if (state, ch) in transitions:
        state = transitions[(state, ch)]
        path.append(state)
    else:
        valid = False
        break

print("Transition Path:")
print(" -> ".join(path))

if valid and state in final_states:
    print("Accepted")
else:
    print("Rejected")

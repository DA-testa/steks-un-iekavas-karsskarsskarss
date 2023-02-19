from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    input_choice = input("Enter 'F' to input from a file or 'I' to input from the console: ")
    if "F" in input_choice:
        file_path = input("Enter the path to the file: ")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            print(mismatch)
    elif "I" in input_choice:
        text = input("Enter the string to check: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        print("Invalid input choice.")

if __name__ == "__main__":
    main()

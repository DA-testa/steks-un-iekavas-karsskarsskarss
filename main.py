# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
 def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text: str) -> Union[str, int]:
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append((char, i))
        elif char in ")]}":
            if not opening_brackets_stack:
                return i + 1
            last_open = opening_brackets_stack.pop()
            if not are_matching(last_open[0], char):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0][1] + 1
    return 'Success'

def main() -> None:
    input_choice = input("Ievadiet F vai I: ")
    if "F" in input_choice:
        file_path = input("Ievadiet ceļu lidz failam: ")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == 'Success':
                print("Success")
            else:
                print(mismatch)
    elif "I" in input_choice:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == 'Success':
            print("Success")
        else:
            print(mismatch)
    else:
        print("Invalid input choice.")

if __name__ == "__main__":
    main()

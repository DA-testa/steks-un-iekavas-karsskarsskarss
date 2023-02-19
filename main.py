from collections import namedtuple
from typing import List, Union

Bracket = namedtuple("Bracket",["char", "position"])

def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text: str) -> Union[str, int]:
    def recurse(i: int, stack: List[Bracket]) -> Union[str, int]:
        if not text:
            return 'Success'
        elif text[0] in "([{":
            return recurse(i+1, [(text[0], i)] + stack)
        elif text[0] in ")]}":
            if not stack:
                return i + 1
            last_open = stack[0]
            if not are_matching(last_open[0], text[0]):
                return i + 1
            else:
                return recurse(i+1, stack[1:])
        else:
            return recurse(i+1, stack)
    return recurse(0, [])

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
ffffffffff
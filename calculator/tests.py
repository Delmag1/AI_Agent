from functions.get_file_content import get_file_content
from .calculator.pkg import Calculator

def test():
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)


if __name__ == "__main__":
    test()

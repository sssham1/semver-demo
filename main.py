import sys


def greet(name="World"):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet(sys.argv[1] if len(sys.argv) > 1 else "World")

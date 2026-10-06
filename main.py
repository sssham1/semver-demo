import sys


def greet(name="World"):
    name = name.strip() or "World"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet(sys.argv[1] if len(sys.argv) > 1 else "World")

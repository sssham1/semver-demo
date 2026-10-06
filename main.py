import sys

GREETINGS = {"en": "Hello", "ru": "Привет", "es": "Hola"}


def greet(name="World", lang="en"):
    name = name.strip() or "World"
    word = GREETINGS.get(lang, GREETINGS["en"])
    print(f"{word}, {name}!")


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"
    greet(name, lang)


def farewell(name="World"):
    name = name.strip() or "World"
    print(f"Goodbye, {name}!")

import os

LINE = "Think of a library and a post office joined by wires, where a letter reaches the other side of the world in a blink and any page can be read the moment you ask for it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    validate(path)


def validate(path):
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    assert text == text.strip(), "no leading/trailing whitespace allowed"
    print(text)
    print("chars:", len(text))
    print("bytes:", len(raw))


if __name__ == "__main__":
    main()

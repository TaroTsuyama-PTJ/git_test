def test_func(text: str) -> int:
    print(text)
    return len(text)

if __name__ == "__main__":
    num = test_func("message")
    print(num)
from io import BytesIO

import micropython


@micropython.viper
def reader(f) -> int:
    f.read(1)
    try:
        return int(f.read(1)[0])
    except IndexError:
        return -1


def main():
    with open("test.bin", "wb") as f:
        f.write(b"t")

    with open("test.bin", "rb") as f:
        result = reader(f)
        assert result == -1

    with BytesIO(b"t") as f:
        result = reader(f)
        assert result == -1


if __name__ == "__main__":
    main()

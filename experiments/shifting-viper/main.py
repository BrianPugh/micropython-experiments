from io import BytesIO


@micropython.viper
def foo(f):
    buffer = 0
    bit_pos = 0
    proposed_code = 0
    full_mask = int(0xFFFFFFFF)

    while True:
        if bit_pos == 0:
            try:
                buffer |= int(f.read(1)[0]) << 24
                bit_pos += 8
            except IndexError:
                break
        proposed_code = (proposed_code << 1) | (buffer >> 31)
        buffer = (buffer << 1) & full_mask
        bit_pos -= 1
        print(bin(proposed_code))


def main():
    # func()

    with BytesIO(b"\x55") as f:
        foo(f)


if __name__ == "__main__":
    main()

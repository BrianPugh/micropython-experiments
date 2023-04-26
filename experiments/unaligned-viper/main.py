import micropython


@micropython.viper
def viper_function(data) -> uint:
    memoryview(data)[1:]  # Causes a seg fault.

    ptr1 = ptr16(data)
    # ptr2 = ptr16(data_1)

    return uint((ptr1[0] << 16) | (ptr1[0]))


def main():
    data = bytearray([0, 1, 2, 3, 4, 5, 6, 7])
    print(viper_function(data))


if __name__ == "__main__":
    main()

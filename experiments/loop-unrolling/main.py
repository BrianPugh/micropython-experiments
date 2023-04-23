import micropython
import uprofiler


@uprofiler.profile
def loop(iters):
    a = 0
    for _i in range(iters):
        a += 1
    return a


@uprofiler.profile(name="loop_viper")
@micropython.viper
def loop_viper(iters: int) -> int:
    a = int(0)
    for _i in range(iters):
        a += 1
    return a


@uprofiler.profile
def loop_unrolled(iters):
    a = 0
    for _i in range(iters // 8):
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
    return a


@uprofiler.profile(name="loop_unrolled_viper")
@micropython.viper
def loop_unrolled_viper(iters: int) -> int:
    a = int(0)
    for _i in range(iters // 8):
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
        a += 1
    return a


def main():
    iters = 8 * 10_000
    loop(iters)
    loop_unrolled(iters)
    loop_viper(iters)
    loop_unrolled_viper(iters)


if __name__ == "__main__":
    main()
    uprofiler.print_results()

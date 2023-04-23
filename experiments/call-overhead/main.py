import micropython
import uprofiler

uprofiler.print_period = 0


class MyClass:
    @uprofiler.profile
    def method(self, a):
        return a + 1

    @uprofiler.profile(name="method_viper")
    @micropython.viper
    def method_viper(self, a: int) -> int:
        return a + 1


@uprofiler.profile
def function(a):
    return a + 1


def _function_inner(a):
    return a + 1


@uprofiler.profile
def function_function(a):
    return _function_inner(a)


@micropython.viper
def _function_inner_viper(a: int) -> int:
    return a + 1


@uprofiler.profile(name="function_function_viper")
@micropython.viper
def function_function_viper(a: int) -> int:
    return int(_function_inner_viper(a))


@uprofiler.profile(name="function_viper_function")
@micropython.viper
def function_viper_function(a: int) -> int:
    return int(_function_inner(a))


@uprofiler.profile(name="function_viper")
@micropython.viper
def function_viper(a: int) -> int:
    return a + 1


@uprofiler.profile
def no_function(iters):
    a = 0
    for i in range(iters):
        a = i + 1
    return a


@uprofiler.profile(name="no_function_viper")
@micropython.viper
def no_function_viper(iters: int) -> int:
    a = 0
    for i in range(iters):
        a = i + 1
    return a


def main():
    my_class = MyClass()
    iters = 10_000

    for i in range(iters):
        function(i)
        function_function(i)
        function_function_viper(i)
        function_viper(i)
        function_viper_function(i)
        my_class.method(i)
        my_class.method_viper(i)

    no_function(iters)
    no_function_viper(iters)


if __name__ == "__main__":
    main()
    uprofiler.print_results()

# Question
How much overhead is there for various function calls?

# Output

```
Name                        Calls    Total (%)     Total (ms)   Average (ms)
----------------------------------------------------------------------------
function_function           10000         1.03         417.75       0.041775
function_viper_function     10000         0.97        392.747      0.0392747
method                      10000         0.84        342.812      0.0342812
function_function_viper     10000         0.82        334.705      0.0334705
function                    10000         0.81        330.515      0.0330515
method_viper                10000         0.71         287.51       0.028751
function_viper              10000         0.69        279.264      0.0279264
no_function                     1         0.14         55.485         55.485
no_function_viper               1         0.01          2.588          2.588
```

# Conclusion
* Not using a vanilla function (`no_function`) is 6x faster than using a function (`function`).

* A viper loop is 21.4x faster than a vanilla loop.

* Invoking a vanilla function is slightly more costly than a viper function, whether from a vanilla or viper function.

* Calling a vanilla function inside a viper function has similar overhead to calling a vanilla function from a vanilla function.

* Invoking a method is ever so slightly slower than invoking a function, probably due to additional lookup overhead.

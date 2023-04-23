# Question

# Output
```
Name                                Calls  Total (%)    Total (ms)  Average (ms)
--------------------------------------------------------------------------------
substring_finder_reverse                1      38.15        84.186        84.186
substring_finder_ring                   1      28.45        62.777        62.777
substring_finder                        1      28.42        62.728        62.728
substring_finder_viper                  1       0.33         0.729         0.729
substring_finder_reverse_viper          1       0.31         0.694         0.694
```

# Conclusion
It doesn't really matter searching front-to-back or back-to-front (there's not going to be a locality cache improvement). Certainly use viper, and using a ringbuffer will have no real impact.

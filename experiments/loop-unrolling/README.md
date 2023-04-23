# Question
Is loop unrolling effective in micropython?

# Output
Here the loop has been unrolled 8x.

```
Name                                Calls  Total (%)    Total (ms)  Average (ms)
--------------------------------------------------------------------------------
loop                                    1      68.35       443.712       443.712
loop_unrolled                           1      26.51       172.102       172.102
loop_viper                              1       3.17         20.56         20.56
loop_unrolled_viper                     1       0.75         4.864         4.864
```

# Conclusion
Loop unrolling is effective.

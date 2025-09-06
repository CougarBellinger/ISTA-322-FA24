
## Aggregating

#### `.groupby` in pandas:
``` python
(baby                # the dataframe
 .groupby('Year')    # column(s) to group
 ['Count']           # column(s) to aggregate
 .sum()              # how to aggregate
)
```
#### `.agg` in pandas:
```python
(baby
.groupby('Year')
.agg({'Count':['sum']}) # keys = column name; value = agg function(s) to apply
)
```


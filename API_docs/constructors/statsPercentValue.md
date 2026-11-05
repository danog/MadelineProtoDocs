# statsPercentValue

> Channel statistics percentage.

[Back to constructors index](/API_docs/constructors/index.html)



[Channel statistics percentage](https://core.telegram.org/api/stats).  
Compute the percentage simply by doing `part * total / 100`

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|part|[double](/API_docs/types/double.html) | Yes|Partial value|
|total|[double](/API_docs/types/double.html) | Yes|Total value|



### Type: [StatsPercentValue](/API_docs/types/StatsPercentValue.html)


### Example:

```
$statsPercentValue = ['_' => 'statsPercentValue', 'part' => double, 'total' => double];
```

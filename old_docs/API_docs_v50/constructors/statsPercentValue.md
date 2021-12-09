---
title: statsPercentValue
description: [Channel statistics percentage](https://core.telegram.org/api/stats).  
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsPercentValue  
[Back to constructors index](index.md)



[Channel statistics percentage](https://core.telegram.org/api/stats).  
Compute the percentage simply by doing `part * total / 100`

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|part|[double](../types/double.md) | Yes|Partial value|
|total|[double](../types/double.md) | Yes|Total value|



### Type: [StatsPercentValue](../types/StatsPercentValue.md)


### Example:

```php
$statsPercentValue = ['_' => 'statsPercentValue', 'part' => double, 'total' => double];
```  


Or, if you're into Lua:

```lua
statsPercentValue={_='statsPercentValue', part=double, total=double}

```



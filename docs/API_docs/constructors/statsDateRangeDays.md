---
title: "statsDateRangeDays"
description: "Channel statistics date range"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsDateRangeDays  
[Back to constructors index](index.md)



[Channel statistics](https://core.telegram.org/api/stats) date range

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_date|[int](../types/int.md) | Yes|Initial date|
|max\_date|[int](../types/int.md) | Yes|Final date|



### Type: [StatsDateRangeDays](../types/StatsDateRangeDays.md)


### Example:

```php
$statsDateRangeDays = ['_' => 'statsDateRangeDays', 'min_date' => int, 'max_date' => int];
```  

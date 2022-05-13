---
title: "statsDateRangeDays"
description: "Channel statistics date range"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsDateRangeDays  
[Back to constructors index](/API_docs/constructors/index.html)



[Channel statistics](https://core.telegram.org/api/stats) date range

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_date|[int](/API_docs/types/int.html) | Yes|Initial date|
|max\_date|[int](/API_docs/types/int.html) | Yes|Final date|



### Type: [StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.html)


### Example:

```
$statsDateRangeDays = ['_' => 'statsDateRangeDays', 'min_date' => int, 'max_date' => int];
```  

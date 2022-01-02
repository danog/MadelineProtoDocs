---
title: "statsAbsValueAndPrev"
description: "Statistics value couple; intial and final value for period of time currently in consideration"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsAbsValueAndPrev  
[Back to constructors index](index.md)



Statistics value couple; intial and final value for period of time currently in consideration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|current|[double](../types/double.md) | Yes|Current value|
|previous|[double](../types/double.md) | Yes|Previous value|



### Type: [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md)


### Example:

```php
$statsAbsValueAndPrev = ['_' => 'statsAbsValueAndPrev', 'current' => double, 'previous' => double];
```  


Or, if you're into Lua:

```lua
statsAbsValueAndPrev={_='statsAbsValueAndPrev', current=double, previous=double}

```



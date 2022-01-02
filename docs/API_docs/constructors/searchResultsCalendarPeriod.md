---
title: "searchResultsCalendarPeriod"
description: "searchResultsCalendarPeriod attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: searchResultsCalendarPeriod  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|date|[int](../types/int.md) | Yes|
|min\_msg\_id|[int](../types/int.md) | Yes|
|max\_msg\_id|[int](../types/int.md) | Yes|
|count|[int](../types/int.md) | Yes|



### Type: [SearchResultsCalendarPeriod](../types/SearchResultsCalendarPeriod.md)


### Example:

```php
$searchResultsCalendarPeriod = ['_' => 'searchResultsCalendarPeriod', 'date' => int, 'min_msg_id' => int, 'max_msg_id' => int, 'count' => int];
```  


Or, if you're into Lua:

```lua
searchResultsCalendarPeriod={_='searchResultsCalendarPeriod', date=int, min_msg_id=int, max_msg_id=int, count=int}

```



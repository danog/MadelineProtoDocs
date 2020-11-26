---
title: statsGroupTopPoster
description: statsGroupTopPoster attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopPoster  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|messages|[int](../types/int.md) | Yes|
|avg\_chars|[int](../types/int.md) | Yes|



### Type: [StatsGroupTopPoster](../types/StatsGroupTopPoster.md)


### Example:

```php
$statsGroupTopPoster = ['_' => 'statsGroupTopPoster', 'user_id' => int, 'messages' => int, 'avg_chars' => int];
```  


Or, if you're into Lua:

```lua
statsGroupTopPoster={_='statsGroupTopPoster', user_id=int, messages=int, avg_chars=int}

```



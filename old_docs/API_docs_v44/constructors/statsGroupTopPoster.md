---
title: statsGroupTopPoster
description: Information about an active user in a supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopPoster  
[Back to constructors index](index.md)



Information about an active user in a supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|messages|[int](../types/int.md) | Yes|Number of messages for [statistics](https://core.telegram.org/api/stats) period in consideration|
|avg\_chars|[int](../types/int.md) | Yes|Average number of characters per message|



### Type: [StatsGroupTopPoster](../types/StatsGroupTopPoster.md)


### Example:

```php
$statsGroupTopPoster = ['_' => 'statsGroupTopPoster', 'user_id' => int, 'messages' => int, 'avg_chars' => int];
```  


Or, if you're into Lua:

```lua
statsGroupTopPoster={_='statsGroupTopPoster', user_id=int, messages=int, avg_chars=int}

```



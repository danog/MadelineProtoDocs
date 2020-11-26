---
title: statsGraphAsync
description: This [channel statistics graph](https://core.telegram.org/api/stats) must be generated asynchronously using [stats.loadAsyncGraph](../methods/stats.loadAsyncGraph.md) to reduce server load
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGraphAsync  
[Back to constructors index](index.md)



This [channel statistics graph](https://core.telegram.org/api/stats) must be generated asynchronously using [stats.loadAsyncGraph](../methods/stats.loadAsyncGraph.md) to reduce server load

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|token|[string](../types/string.md) | Yes|Token to use for fetching the async graph|



### Type: [StatsGraph](../types/StatsGraph.md)


### Example:

```php
$statsGraphAsync = ['_' => 'statsGraphAsync', 'token' => 'string'];
```  


Or, if you're into Lua:

```lua
statsGraphAsync={_='statsGraphAsync', token='string'}

```



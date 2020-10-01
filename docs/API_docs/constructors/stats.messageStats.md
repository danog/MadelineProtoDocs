---
title: stats.messageStats
description: stats.messageStats attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_messageStats.html
---
# Constructor: stats.messageStats  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|views\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|



### Type: [stats.MessageStats](../types/stats.MessageStats.md)


### Example:

```php
$stats.messageStats = ['_' => 'stats.messageStats', 'views_graph' => StatsGraph];
```  


Or, if you're into Lua:

```lua
stats.messageStats={_='stats.messageStats', views_graph=StatsGraph}

```



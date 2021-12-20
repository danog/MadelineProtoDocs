---
title: "stats.messageStats"
description: "Message statistics"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_messageStats.html
---
# Constructor: stats.messageStats  
[Back to constructors index](index.md)



Message statistics

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Message view graph|



### Type: [stats.MessageStats](../types/stats.MessageStats.md)


### Example:

```php
$stats_messageStats = ['_' => 'stats.messageStats', 'views_graph' => StatsGraph];
```  


Or, if you're into Lua:

```lua
stats_messageStats={_='stats.messageStats', views_graph=StatsGraph}

```



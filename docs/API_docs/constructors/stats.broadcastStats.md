---
title: stats.broadcastStats
description: stats.broadcastStats attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastStats.html
---
# Constructor: stats.broadcastStats  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|period|[StatsDateRangeDays](../types/StatsDateRangeDays.md) | Yes|
|followers|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|views\_per\_post|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|shares\_per\_post|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|enabled\_notifications|[StatsPercentValue](../types/StatsPercentValue.md) | Yes|
|growth\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|followers\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|mute\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|top\_hours\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|interactions\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|iv\_interactions\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|views\_by\_source\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|new\_followers\_by\_source\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|languages\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|recent\_message\_interactions|Array of [MessageInteractionCounters](../types/MessageInteractionCounters.md) | Yes|



### Type: [stats.BroadcastStats](../types/stats.BroadcastStats.md)


### Example:

```php
$stats.broadcastStats = ['_' => 'stats.broadcastStats', 'period' => StatsDateRangeDays, 'followers' => StatsAbsValueAndPrev, 'views_per_post' => StatsAbsValueAndPrev, 'shares_per_post' => StatsAbsValueAndPrev, 'enabled_notifications' => StatsPercentValue, 'growth_graph' => StatsGraph, 'followers_graph' => StatsGraph, 'mute_graph' => StatsGraph, 'top_hours_graph' => StatsGraph, 'interactions_graph' => StatsGraph, 'iv_interactions_graph' => StatsGraph, 'views_by_source_graph' => StatsGraph, 'new_followers_by_source_graph' => StatsGraph, 'languages_graph' => StatsGraph, 'recent_message_interactions' => [MessageInteractionCounters, MessageInteractionCounters]];
```  


Or, if you're into Lua:

```lua
stats.broadcastStats={_='stats.broadcastStats', period=StatsDateRangeDays, followers=StatsAbsValueAndPrev, views_per_post=StatsAbsValueAndPrev, shares_per_post=StatsAbsValueAndPrev, enabled_notifications=StatsPercentValue, growth_graph=StatsGraph, followers_graph=StatsGraph, mute_graph=StatsGraph, top_hours_graph=StatsGraph, interactions_graph=StatsGraph, iv_interactions_graph=StatsGraph, views_by_source_graph=StatsGraph, new_followers_by_source_graph=StatsGraph, languages_graph=StatsGraph, recent_message_interactions={MessageInteractionCounters}}

```



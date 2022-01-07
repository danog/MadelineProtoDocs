---
title: "stats.broadcastStats"
description: "Channel statistics."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastStats.html
---
# Constructor: stats.broadcastStats  
[Back to constructors index](index.md)



[Channel statistics](https://core.telegram.org/api/stats).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[StatsDateRangeDays](../types/StatsDateRangeDays.md) | Yes|Period in consideration|
|followers|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|Follower count change for period in consideration|
|views\_per\_post|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|`total_viewcount/postcount`, for posts posted during the period in consideration (`views_per_post`). <br>Note that in this case, `current` refers to the `period` in consideration (`min_date` till `max_date`), and `prev` refers to the previous period (`(min_date - (max_date - min_date))` till `min_date`).|
|shares\_per\_post|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|`total_viewcount/postcount`, for posts posted during the period in consideration (`views_per_post`). <br>Note that in this case, `current` refers to the `period` in consideration (`min_date` till `max_date`), and `prev` refers to the previous period (`(min_date - (max_date - min_date))` till `min_date`)|
|enabled\_notifications|[StatsPercentValue](../types/StatsPercentValue.md) | Yes|Percentage of subscribers with enabled notifications|
|growth\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Channel growth graph (absolute subscriber count)|
|followers\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Followers growth graph (relative subscriber count)|
|mute\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Muted users graph (relative)|
|top\_hours\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Views per hour graph (absolute)|
|interactions\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Interactions graph (absolute)|
|iv\_interactions\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|IV interactions graph (absolute)|
|views\_by\_source\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Views by source graph (absolute)|
|new\_followers\_by\_source\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|New followers by source graph (absolute)|
|languages\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|Subscriber language graph (piechart)|
|recent\_message\_interactions|Array of [MessageInteractionCounters](../types/MessageInteractionCounters.md) | Yes|Recent message interactions|



### Type: [stats.BroadcastStats](../types/stats.BroadcastStats.md)


### Example:

```php
$stats_broadcastStats = ['_' => 'stats.broadcastStats', 'period' => StatsDateRangeDays, 'followers' => StatsAbsValueAndPrev, 'views_per_post' => StatsAbsValueAndPrev, 'shares_per_post' => StatsAbsValueAndPrev, 'enabled_notifications' => StatsPercentValue, 'growth_graph' => StatsGraph, 'followers_graph' => StatsGraph, 'mute_graph' => StatsGraph, 'top_hours_graph' => StatsGraph, 'interactions_graph' => StatsGraph, 'iv_interactions_graph' => StatsGraph, 'views_by_source_graph' => StatsGraph, 'new_followers_by_source_graph' => StatsGraph, 'languages_graph' => StatsGraph, 'recent_message_interactions' => [MessageInteractionCounters, MessageInteractionCounters]];
```  

---
title: stats.megagroupStats
description: stats.megagroupStats attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_megagroupStats.html
---
# Constructor: stats.megagroupStats  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|period|[StatsDateRangeDays](../types/StatsDateRangeDays.md) | Yes|
|members|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|messages|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|viewers|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|posters|[StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md) | Yes|
|growth\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|members\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|new\_members\_by\_source\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|languages\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|messages\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|actions\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|top\_hours\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|weekdays\_graph|[StatsGraph](../types/StatsGraph.md) | Yes|
|top\_posters|Array of [StatsGroupTopPoster](../types/StatsGroupTopPoster.md) | Yes|
|top\_admins|Array of [StatsGroupTopAdmin](../types/StatsGroupTopAdmin.md) | Yes|
|top\_inviters|Array of [StatsGroupTopInviter](../types/StatsGroupTopInviter.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [stats.MegagroupStats](../types/stats.MegagroupStats.md)


### Example:

```php
$stats.megagroupStats = ['_' => 'stats.megagroupStats', 'period' => StatsDateRangeDays, 'members' => StatsAbsValueAndPrev, 'messages' => StatsAbsValueAndPrev, 'viewers' => StatsAbsValueAndPrev, 'posters' => StatsAbsValueAndPrev, 'growth_graph' => StatsGraph, 'members_graph' => StatsGraph, 'new_members_by_source_graph' => StatsGraph, 'languages_graph' => StatsGraph, 'messages_graph' => StatsGraph, 'actions_graph' => StatsGraph, 'top_hours_graph' => StatsGraph, 'weekdays_graph' => StatsGraph, 'top_posters' => [StatsGroupTopPoster, StatsGroupTopPoster], 'top_admins' => [StatsGroupTopAdmin, StatsGroupTopAdmin], 'top_inviters' => [StatsGroupTopInviter, StatsGroupTopInviter], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
stats.megagroupStats={_='stats.megagroupStats', period=StatsDateRangeDays, members=StatsAbsValueAndPrev, messages=StatsAbsValueAndPrev, viewers=StatsAbsValueAndPrev, posters=StatsAbsValueAndPrev, growth_graph=StatsGraph, members_graph=StatsGraph, new_members_by_source_graph=StatsGraph, languages_graph=StatsGraph, messages_graph=StatsGraph, actions_graph=StatsGraph, top_hours_graph=StatsGraph, weekdays_graph=StatsGraph, top_posters={StatsGroupTopPoster}, top_admins={StatsGroupTopAdmin}, top_inviters={StatsGroupTopInviter}, users={User}}

```



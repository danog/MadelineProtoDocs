---
title: "stats.megagroupStats"
description: "Supergroup statistics"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_megagroupStats.html
---
# Constructor: stats.megagroupStats  
[Back to constructors index](/API_docs/constructors/index.md)



Supergroup [statistics](https://core.telegram.org/api/stats)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.md) | Yes|Period in consideration|
|members|[StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md) | Yes|Member count change for period in consideration|
|messages|[StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md) | Yes|Message number change for period in consideration|
|viewers|[StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md) | Yes|Number of users that viewed messages, for range in consideration|
|posters|[StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md) | Yes|Number of users that posted messages, for range in consideration|
|growth\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Supergroup growth graph (absolute subscriber count)|
|members\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Members growth (relative subscriber count)|
|new\_members\_by\_source\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|New members by source graph|
|languages\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Subscriber language graph (piechart)|
|messages\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Message activity graph (stacked bar graph, message type)|
|actions\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Group activity graph (deleted, modified messages, blocked users)|
|top\_hours\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Activity per hour graph (absolute)|
|weekdays\_graph|[StatsGraph](/API_docs/types/StatsGraph.md) | Yes|Activity per day of week graph (absolute)|
|top\_posters|Array of [StatsGroupTopPoster](/API_docs/types/StatsGroupTopPoster.md) | Yes|Info about most active group members|
|top\_admins|Array of [StatsGroupTopAdmin](/API_docs/types/StatsGroupTopAdmin.md) | Yes|Info about most active group admins|
|top\_inviters|Array of [StatsGroupTopInviter](/API_docs/types/StatsGroupTopInviter.md) | Yes|Info about most active group inviters|
|users|Array of [User](/API_docs/types/User.md) | Yes|Info about users mentioned in statistics|



### Type: [stats.MegagroupStats](/API_docs/types/stats.MegagroupStats.md)


### Example:

```php
$stats_megagroupStats = ['_' => 'stats.megagroupStats', 'period' => StatsDateRangeDays, 'members' => StatsAbsValueAndPrev, 'messages' => StatsAbsValueAndPrev, 'viewers' => StatsAbsValueAndPrev, 'posters' => StatsAbsValueAndPrev, 'growth_graph' => StatsGraph, 'members_graph' => StatsGraph, 'new_members_by_source_graph' => StatsGraph, 'languages_graph' => StatsGraph, 'messages_graph' => StatsGraph, 'actions_graph' => StatsGraph, 'top_hours_graph' => StatsGraph, 'weekdays_graph' => StatsGraph, 'top_posters' => [StatsGroupTopPoster, StatsGroupTopPoster], 'top_admins' => [StatsGroupTopAdmin, StatsGroupTopAdmin], 'top_inviters' => [StatsGroupTopInviter, StatsGroupTopInviter], 'users' => [User, User]];
```  

---
title: "stats.storyStats"
description: "stats.storyStats attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_storyStats.html
---
# Constructor: stats.storyStats  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|views\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|
|reactions\_by\_emotion\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|



### Type: [stats.StoryStats](/API_docs/types/stats.StoryStats.html)


### Example:

```
$stats_storyStats = ['_' => 'stats.storyStats', 'views_graph' => StatsGraph, 'reactions_by_emotion_graph' => StatsGraph];
```  

# stats.storyStats

> Contains statistics about a story.

[Back to constructors index](/API_docs/constructors/index.html)



Contains [statistics](https://core.telegram.org/api/stats) about a [story](https://core.telegram.org/api/stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|A graph containing the number of story views and shares|
|reactions\_by\_emotion\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|A bar graph containing the number of story reactions categorized by "emotion" (i.e. Positive, Negative, Other, etc...)|



### Type: [stats.StoryStats](/API_docs/types/stats.StoryStats.html)


### Example:

```
$stats_storyStats = ['_' => 'stats.storyStats', 'views_graph' => StatsGraph, 'reactions_by_emotion_graph' => StatsGraph];
```

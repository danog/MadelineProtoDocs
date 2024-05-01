---
title: "statsGraphAsync"
description: "This channel statistics graph must be generated asynchronously using stats.loadAsyncGraph to reduce server load"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGraphAsync  
[Back to constructors index](/API_docs/constructors/index.html)



This [channel statistics graph](https://core.telegram.org/api/stats) must be generated asynchronously using [stats.loadAsyncGraph](../methods/stats.loadAsyncGraph.html) to reduce server load

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|token|[string](/API_docs/types/string.html) | Yes|Token to use for fetching the async graph|



### Type: [StatsGraph](/API_docs/types/StatsGraph.html)


### Example:

```
$statsGraphAsync = ['_' => 'statsGraphAsync', 'token' => 'string'];
```  

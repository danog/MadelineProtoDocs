---
title: "statsGraph"
description: "Channel statistics graph"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGraph  
[Back to constructors index](/API_docs/constructors/index.html)



[Channel statistics graph](https://core.telegram.org/api/stats)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|json|[DataJSON](/API_docs/types/DataJSON.html) | Yes|Statistics data|
|zoom\_token|[string](/API_docs/types/string.html) | Optional|Zoom token|



### Type: [StatsGraph](/API_docs/types/StatsGraph.html)


### Example:

```
$statsGraph = ['_' => 'statsGraph', 'json' => DataJSON, 'zoom_token' => 'string'];
```  

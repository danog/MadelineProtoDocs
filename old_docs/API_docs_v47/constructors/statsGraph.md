---
title: statsGraph
description: [Channel statistics graph](https://core.telegram.org/api/stats)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGraph  
[Back to constructors index](index.md)



[Channel statistics graph](https://core.telegram.org/api/stats)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|json|[DataJSON](../types/DataJSON.md) | Yes|Statistics data|
|zoom\_token|[string](../types/string.md) | Optional|Zoom token|



### Type: [StatsGraph](../types/StatsGraph.md)


### Example:

```php
$statsGraph = ['_' => 'statsGraph', 'json' => DataJSON, 'zoom_token' => 'string'];
```  


Or, if you're into Lua:

```lua
statsGraph={_='statsGraph', json=DataJSON, zoom_token='string'}

```



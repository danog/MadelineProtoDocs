---
title: "statsGraphError"
description: "An error occurred while generating the statistics graph"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGraphError  
[Back to constructors index](index.md)



An error occurred while generating the [statistics graph](https://core.telegram.org/api/stats)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|error|[string](../types/string.md) | Yes|The error|



### Type: [StatsGraph](../types/StatsGraph.md)


### Example:

```php
$statsGraphError = ['_' => 'statsGraphError', 'error' => 'string'];
```  


Or, if you're into Lua:

```lua
statsGraphError={_='statsGraphError', error='string'}

```



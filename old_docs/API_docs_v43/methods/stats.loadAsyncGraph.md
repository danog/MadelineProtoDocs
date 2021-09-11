---
title: stats.loadAsyncGraph
description: Load [channel statistics graph](https://core.telegram.org/api/stats) asynchronously
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_loadAsyncGraph.html
---
# Method: stats.loadAsyncGraph
[Back to methods index](index.md)



Load [channel statistics graph](https://core.telegram.org/api/stats) asynchronously

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[string](../types/string.md) | Graph token from [statsGraphAsync](../constructors/statsGraphAsync.md) constructor | Yes|
|x|[long](../types/long.md) | Zoom value, if required | Optional|


### Return type: [StatsGraph](../types/StatsGraph.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$StatsGraph = $MadelineProto->stats->loadAsyncGraph(['token' => 'string', 'x' => long, ]);
```

Or, if you're into Lua:

```lua
StatsGraph = stats.loadAsyncGraph({token='string', x=long, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|GRAPH_EXPIRED_RELOAD|This graph has expired, please obtain a new graph token|
|400|GRAPH_INVALID_RELOAD|Invalid graph token provided, please reload the stats and provide the updated token|
|400|GRAPH_OUTDATED_RELOAD|The graph is outdated, please get a new async token using stats.getBroadcastStats|
|-503|Timeout|Timeout while fetching data|



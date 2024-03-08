---
title: "stats.getStoryStats"
description: "Get [statistics](https://core.telegram.org/api/stats) for a certain [story](https://core.telegram.org/api/stories)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getStoryStats.html
---
# Method: stats.getStoryStats
[Back to methods index](index.html)



Get [statistics](https://core.telegram.org/api/stats) for a certain [story](https://core.telegram.org/api/stories).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Whether to enable the dark theme for graph colors | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer that posted the story | Optional|
|id|[int](/API_docs/types/int.html) | Story ID | Optional|


### Return type: [stats.StoryStats](/API_docs/types/stats.StoryStats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_StoryStats = $MadelineProto->stats->getStoryStats(dark: $Bool, peer: $InputPeer, id: $int, );
```


---
title: "stats.getStoryPublicForwards"
description: "Obtain forwards of a [story](https://core.telegram.org/api/stories) as a message to public chats and reposts by public channels."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getStoryPublicForwards.html
---
# Method: stats.getStoryPublicForwards
[Back to methods index](index.html)



Obtain forwards of a [story](https://core.telegram.org/api/stories) as a message to public chats and reposts by public channels.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the story was originally posted | Optional|
|id|[int](/API_docs/types/int.html) | [Story](https://core.telegram.org/api/stories) ID | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination, from [stats.PublicForwards](../constructors/stats.publicForwards.html).`next_offset`. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stats.PublicForwards](/API_docs/types/stats.PublicForwards.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_PublicForwards = $MadelineProto->stats->getStoryPublicForwards(peer: $InputPeer, id: $int, offset: 'string', limit: $int, );
```


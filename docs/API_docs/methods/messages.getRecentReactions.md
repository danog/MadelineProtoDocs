---
title: "messages.getRecentReactions"
description: "Get recently used [message reactions](https://core.telegram.org/api/reactions)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getRecentReactions.html
---
# Method: messages.getRecentReactions
[Back to methods index](index.html)



Get recently used [message reactions](https://core.telegram.org/api/reactions)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.Reactions](/API_docs/types/messages.Reactions.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Reactions = $MadelineProto->messages->getRecentReactions(limit: int, hash: [long, long], );
```


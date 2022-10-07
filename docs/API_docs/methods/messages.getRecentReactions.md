---
title: "messages.getRecentReactions"
description: "messages.getRecentReactions parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getRecentReactions.html
---
# Method: messages.getRecentReactions
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|limit|[int](/API_docs/types/int.html) | Yes|
|hash|Array of [long](/API_docs/types/long.html) | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$messages_Reactions = $MadelineProto->messages->getRecentReactions(limit: int, hash: [long, long], );
```


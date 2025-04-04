---
title: "messages.getRecentLocations"
description: "Get live location history of a certain user"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getRecentLocations.html
---
# Method: messages.getRecentLocations
[Back to methods index](index.html)



Get live location history of a certain user

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | User | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

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

$messages_Messages = $MadelineProto->messages->getRecentLocations(peer: $InputPeer, limit: $int, hash: [$long\|string, $long\|string], );
```


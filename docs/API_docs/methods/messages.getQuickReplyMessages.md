---
title: "messages.getQuickReplyMessages"
description: "Fetch (a subset or all) messages in a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getQuickReplyMessages.html
---
# Method: messages.getQuickReplyMessages
[Back to methods index](index.html)



Fetch (a subset or all) messages in a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Quick reply shortcut ID. | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of the messages to fetch, if empty fetches all of them. | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getQuickReplyMessages(shortcut_id: $int, id: [$int, $int], hash: [$long\|string, $long\|string], );
```


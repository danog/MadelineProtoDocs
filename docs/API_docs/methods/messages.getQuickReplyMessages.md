---
title: "messages.getQuickReplyMessages"
description: "messages.getQuickReplyMessages parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getQuickReplyMessages.html
---
# Method: messages.getQuickReplyMessages
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Optional|
|id|Array of [int](/API_docs/types/int.html) | Optional|
|hash|Array of [long\|string](/API_docs/types/long|string.html) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getQuickReplyMessages(shortcut_id: $int, id: [$int, $int], hash: [$long|string, $long|string], );
```


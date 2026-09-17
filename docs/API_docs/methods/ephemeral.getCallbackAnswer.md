---
title: "ephemeral.getCallbackAnswer"
description: "ephemeral.getCallbackAnswer parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/ephemeral_getCallbackAnswer.html
---
# Method: ephemeral.getCallbackAnswer
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|id|[int](/API_docs/types/int.html) | Optional|
|data|[bytes](/API_docs/types/bytes.html) | Optional|


### Return type: [messages.BotCallbackAnswer](/API_docs/types/messages.BotCallbackAnswer.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotCallbackAnswer = $MadelineProto->ephemeral->getCallbackAnswer(peer: $InputPeer, id: $int, data: 'bytes', );
```


---
title: "messages.savePreparedInlineMessage"
description: "messages.savePreparedInlineMessage parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_savePreparedInlineMessage.html
---
# Method: messages.savePreparedInlineMessage
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|result|[InputBotInlineResult](/API_docs/types/InputBotInlineResult.html) | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|peer\_types|Array of [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Optional|


### Return type: [messages.BotPreparedInlineMessage](/API_docs/types/messages.BotPreparedInlineMessage.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotPreparedInlineMessage = $MadelineProto->messages->savePreparedInlineMessage(result: $InputBotInlineResult, user_id: $InputUser, peer_types: [$InlineQueryPeerType, $InlineQueryPeerType], );
```


---
title: "messages.savePreparedInlineMessage"
description: "Save a [prepared inline message](https://core.telegram.org/api/bots/inline#21-using-a-prepared-inline-message), to be shared by the user of the mini app using a [web\_app\_send\_prepared\_message event](https://core.telegram.org/api/web-events#web-app-send-prepared-message)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_savePreparedInlineMessage.html
---
# Method: messages.savePreparedInlineMessage
[Back to methods index](index.html)



Save a [prepared inline message](https://core.telegram.org/api/bots/inline#21-using-a-prepared-inline-message), to be shared by the user of the mini app using a [web\_app\_send\_prepared\_message event](https://core.telegram.org/api/web-events#web-app-send-prepared-message)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|result|[InputBotInlineResult](/API_docs/types/InputBotInlineResult.html) | The message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user to whom the [web\_app\_send\_prepared\_message event](https://core.telegram.org/api/web-events#web-app-send-prepared-message) event will be sent | Optional|
|peer\_types|Array of [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Types of chats where this message can be sent | Optional|


### Return type: [messages.BotPreparedInlineMessage](/API_docs/types/messages.BotPreparedInlineMessage.html)

### Can userbots use this method: **YES**

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


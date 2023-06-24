---
title: "messages.getAttachMenuBot"
description: "Returns attachment menu entry for a [bot web app that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAttachMenuBot.html
---
# Method: messages.getAttachMenuBot
[Back to methods index](index.html)



Returns attachment menu entry for a [bot web app that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot ID | Optional|


### Return type: [AttachMenuBotsBot](/API_docs/types/AttachMenuBotsBot.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$AttachMenuBotsBot = $MadelineProto->messages->getAttachMenuBot(bot: $InputUser, );
```


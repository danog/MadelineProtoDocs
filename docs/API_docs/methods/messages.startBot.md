---
title: "messages.startBot"
description: "Start a conversation with a bot using a [deep linking parameter](https://core.telegram.org/bots#deep-linking)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_startBot.html
---
# Method: messages.startBot
[Back to methods index](index.html)



Start a conversation with a bot using a [deep linking parameter](https://core.telegram.org/bots#deep-linking)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat where to start the bot, can be the bot's private chat or a group | Optional|
|start\_param|[string](/API_docs/types/string.html) | [Deep linking parameter](https://core.telegram.org/bots#deep-linking) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->startBot(bot: InputUser, peer: InputPeer, start_param: 'string', );
```


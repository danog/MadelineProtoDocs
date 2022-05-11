---
title: "channels.getChannels"
description: "Get info about [channels/supergroups](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getChannels.html
---
# Method: channels.getChannels
[Back to methods index](index.html)



Get info about [channels/supergroups](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | IDs of channels/supergroups to get info about | Yes|


### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_Chats = $MadelineProto->channels->getChannels(id: [InputChannel, InputChannel], );
```


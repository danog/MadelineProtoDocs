---
title: "channels.getMessages"
description: "Get [channel/supergroup](https://core.telegram.org/api/channel) messages"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getMessages.html
---
# Method: channels.getMessages
[Back to methods index](index.html)



Get [channel/supergroup](https://core.telegram.org/api/channel) messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel/supergroup | Optional|
|id|Array of [Message ID or InputMessage](/API_docs/types/InputMessage.html) | IDs of messages to get | Yes|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

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
$messages_Messages = $MadelineProto->channels->getMessages(channel: InputChannel, id: [InputMessage, InputMessage], );
```


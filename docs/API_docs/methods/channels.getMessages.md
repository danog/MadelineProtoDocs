---
title: "channels.getMessages"
description: "Please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getMessages.html
---
# Method: channels.getMessages
[Back to methods index](index.html)



# Warning: flood wait
**Warning: this method is prone to rate limiting with flood waits, please use the [updates event handler, instead &raquo;](/docs/UPDATES.html#async-event-driven)**

# Warning: non-realtime results
**Warning: this method is not suitable for receiving messages in real-time from chats and users, please use the [updates event handler, instead &raquo;](/docs/UPDATES.html#async-event-driven)**

# Warning: this is probably NOT what you need
You probably need to use the [updates event handler, instead &raquo;](/docs/UPDATES.html#async-event-driven) :)

Please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html)

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

$messages_Messages = $MadelineProto->channels->getMessages(channel: $InputChannel, id: [$InputMessage, $InputMessage], );
```


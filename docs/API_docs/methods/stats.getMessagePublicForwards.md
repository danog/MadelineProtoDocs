---
title: "stats.getMessagePublicForwards"
description: "Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessagePublicForwards.html
---
# Method: stats.getMessagePublicForwards
[Back to methods index](index.html)



Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  
Will return a list of [messages](../constructors/message.html) with `peer_id` equal to the public channel to which this message was forwarded.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Source channel | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Source message ID | Yes|
|offset\_rate|[int](/API_docs/types/int.html) | Initially 0, then set to the `next_rate` parameter of [messages.messagesSlice](../constructors/messages.messagesSlice.html) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$messages_Messages = $MadelineProto->stats->getMessagePublicForwards(channel: InputChannel, msg_id: int, offset_rate: int, offset_peer: InputPeer, offset_id: int, limit: int, );
```


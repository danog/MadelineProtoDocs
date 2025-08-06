---
title: "messages.getMessageReactionsList"
description: "Get [message reaction](https://core.telegram.org/api/reactions) list, along with the sender of each reaction."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessageReactionsList.html
---
# Method: messages.getMessageReactionsList
[Back to methods index](index.html)



Get [message reaction](https://core.telegram.org/api/reactions) list, along with the sender of each reaction.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|
|id|[int](/API_docs/types/int.html) | Message ID | Optional|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Get only reactions of this type | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination (taken from the `next_offset` field of the returned [messages.MessageReactionsList](../types/messages.MessageReactionsList.html)); empty in the first request. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [messages.MessageReactionsList](/API_docs/types/messages.MessageReactionsList.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_MessageReactionsList = $MadelineProto->messages->getMessageReactionsList(peer: $InputPeer, id: $int, reaction: $Reaction, offset: 'string', limit: $int, );
```


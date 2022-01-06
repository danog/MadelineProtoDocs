---
title: "messages.getMessageReactionsList"
description: "Get full message reaction list"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessageReactionsList.html
---
# Method: messages.getMessageReactionsList
[Back to methods index](index.md)



Get full message reaction list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|id|[int](../types/int.md) | Message ID | Yes|
|reaction|[string](../types/string.md) | Get only reactions of this type (UTF8 emoji) | Optional|
|offset|[string](../types/string.md) | Offset (typically taken from the `next_offset` field of the returned [MessageReactionsList](../types/MessageReactionsList.md)) | Optional|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.MessageReactionsList](../types/messages.MessageReactionsList.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_MessageReactionsList = $MadelineProto->messages->getMessageReactionsList(['peer' => InputPeer, 'id' => int, 'reaction' => 'string', 'offset' => 'string', 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_MessageReactionsList = messages.getMessageReactionsList({peer=InputPeer, id=int, reaction='string', offset='string', limit=int, })
```


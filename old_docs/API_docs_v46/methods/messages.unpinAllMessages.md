---
title: messages.unpinAllMessages
description: [Unpin](https://core.telegram.org/api/pin) all pinned messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_unpinAllMessages.html
---
# Method: messages.unpinAllMessages
[Back to methods index](index.md)



[Unpin](https://core.telegram.org/api/pin) all pinned messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Chat where to unpin | Optional|


### Return type: [messages.AffectedHistory](../types/messages.AffectedHistory.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->messages->unpinAllMessages(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.unpinAllMessages({peer=InputPeer, })
```


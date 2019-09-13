---
title: messages.getScheduledHistory
description: Get scheduled history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getScheduledHistory  
[Back to methods index](index.md)


Get scheduled history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|hash|Array of [int](../types/int.md) | Hash | Optional|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getScheduledHistory(['peer' => InputPeer, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getScheduledHistory({peer=InputPeer, hash={int}, })
```


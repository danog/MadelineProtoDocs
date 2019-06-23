---
title: messages.getOnlines
description: Get online users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getOnlines  
[Back to methods index](index.md)


Get online users

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|


### Return type: [ChatOnlines](../types/ChatOnlines.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ChatOnlines = $MadelineProto->messages->getOnlines(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
ChatOnlines = messages.getOnlines({peer=InputPeer, })
```


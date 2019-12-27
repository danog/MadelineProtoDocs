---
title: messages.readChannelHistory
description: Mark channel/supergroup history as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readChannelHistory.html
---
# Method: messages.readChannelHistory  
[Back to methods index](index.md)


Mark channel/supergroup history as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The channel/supergruop | Optional|
|max\_id|[int](../types/int.md) | Maximum message ID to mark as read | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->readChannelHistory(['peer' => InputPeer, 'max_id' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.readChannelHistory({peer=InputPeer, max_id=int, })
```


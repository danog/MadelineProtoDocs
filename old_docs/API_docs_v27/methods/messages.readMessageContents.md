---
title: messages.readMessageContents
description: Notifies the sender about the recipient having listened a voice message or watched a video.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readMessageContents.html
---
# Method: messages.readMessageContents
[Back to methods index](index.md)



Notifies the sender about the recipient having listened a voice message or watched a video.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [int](../types/int.md) | Message ID list | Yes|


### Return type: [messages.AffectedMessages](../types/messages.AffectedMessages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.AffectedMessages = $MadelineProto->messages->readMessageContents(['id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.AffectedMessages = messages.readMessageContents({id={int}, })
```


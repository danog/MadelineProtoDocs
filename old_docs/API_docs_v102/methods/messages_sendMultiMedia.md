---
title: messages.sendMultiMedia
description: Send an album
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendMultiMedia  
[Back to methods index](index.md)


Send an album

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Disable notifications? | Optional|
|background|[Bool](../types/Bool.md) | Disable background notification? | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Clear draft? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to send the album | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Reply to message by ID | Optional|
|multi\_media|Array of [InputSingleMedia](../types/InputSingleMedia.md) | The album | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendMultiMedia(['silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'multi_media' => [InputSingleMedia, InputSingleMedia], ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendMultiMedia({silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, multi_media={InputSingleMedia}, })
```


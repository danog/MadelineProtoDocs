---
title: messages.acceptUrlAuth
description: Use this to accept a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.acceptUrlAuth  
[Back to methods index](index.md)


Use this to accept a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|write\_allowed|[Bool](../types/Bool.md) | Set this flag to allow the bot to send messages to you (if requested) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The location of the message | Optional|
|msg\_id|[int](../types/int.md) | Message ID of the message with the login button | Yes|
|button\_id|[int](../types/int.md) | ID of the login button | Yes|


### Return type: [UrlAuthResult](../types/UrlAuthResult.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$UrlAuthResult = $MadelineProto->messages->acceptUrlAuth(['write_allowed' => Bool, 'peer' => InputPeer, 'msg_id' => int, 'button_id' => int, ]);
```

Or, if you're into Lua:

```lua
UrlAuthResult = messages.acceptUrlAuth({write_allowed=Bool, peer=InputPeer, msg_id=int, button_id=int, })
```


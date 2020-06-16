---
title: messages.sendBroadcast
description: messages.sendBroadcast parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendBroadcast.html
---
# Method: messages.sendBroadcast
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|contacts|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Yes|
|message|[string](../types/string.md) | Yes|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | Optional|


### Return type: [messages.StatedMessages](../types/messages.StatedMessages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.StatedMessages = $MadelineProto->messages->sendBroadcast(['contacts' => [InputUser, InputUser], 'message' => 'string', 'media' => InputMedia, ]);
```

Or, if you're into Lua:

```lua
messages.StatedMessages = messages.sendBroadcast({contacts={InputUser}, message='string', media=InputMedia, })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [messages.StatedMessages](../types/messages.StatedMessages.md) will be returned instead.



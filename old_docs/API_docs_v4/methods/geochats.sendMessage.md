---
title: geochats.sendMessage
description: geochats.sendMessage parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_sendMessage.html
---
# Method: geochats.sendMessage
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|message|[string](../types/string.md) | Yes|


### Return type: [geochats.StatedMessage](../types/geochats.StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_StatedMessage = $MadelineProto->geochats->sendMessage(['peer' => InputGeoChat, 'message' => 'string', ]);
```

Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.sendMessage({peer=InputGeoChat, message='string', })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [geochats.StatedMessage](../types/geochats.StatedMessage.md) will be returned instead.



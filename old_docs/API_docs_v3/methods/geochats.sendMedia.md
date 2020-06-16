---
title: geochats.sendMedia
description: geochats.sendMedia parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_sendMedia.html
---
# Method: geochats.sendMedia
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | Optional|


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

$geochats.StatedMessage = $MadelineProto->geochats->sendMedia(['peer' => InputGeoChat, 'media' => InputMedia, ]);
```

Or, if you're into Lua:

```lua
geochats.StatedMessage = geochats.sendMedia({peer=InputGeoChat, media=InputMedia, })
```


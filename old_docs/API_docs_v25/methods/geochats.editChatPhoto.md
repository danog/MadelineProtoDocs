---
title: geochats.editChatPhoto
description: Edit geochat photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.editChatPhoto  
[Back to methods index](index.md)


Edit geochat photo

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|
|photo|[InputChatPhoto](../types/InputChatPhoto.md) | The new photo | Optional|


### Return type: [geochats\_StatedMessage](../types/geochats_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_StatedMessage = $MadelineProto->geochats->editChatPhoto(['peer' => InputGeoChat, 'photo' => InputChatPhoto, ]);
```

Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.editChatPhoto({peer=InputGeoChat, photo=InputChatPhoto, })
```


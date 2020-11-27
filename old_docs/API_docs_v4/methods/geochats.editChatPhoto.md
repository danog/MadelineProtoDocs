---
title: geochats.editChatPhoto
description: geochats.editChatPhoto parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_editChatPhoto.html
---
# Method: geochats.editChatPhoto
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|photo|[InputChatPhoto](../types/InputChatPhoto.md) | Optional|


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

$geochats_StatedMessage = $MadelineProto->geochats->editChatPhoto(['peer' => InputGeoChat, 'photo' => InputChatPhoto, ]);
```

Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.editChatPhoto({peer=InputGeoChat, photo=InputChatPhoto, })
```


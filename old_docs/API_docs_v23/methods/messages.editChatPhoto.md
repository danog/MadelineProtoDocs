---
title: messages.editChatPhoto
description: Changes chat photo and sends a service message on it
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatPhoto.html
---
# Method: messages.editChatPhoto  
[Back to methods index](index.md)


Changes chat photo and sends a service message on it

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The ID of the chat | Optional|
|photo|[InputChatPhoto](../types/InputChatPhoto.md) | Photo to be set | Optional|


### Return type: [messages.StatedMessage](../types/messages.StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.StatedMessage = $MadelineProto->messages->editChatPhoto(['chat_id' => InputPeer, 'photo' => InputChatPhoto, ]);
```

Or, if you're into Lua:

```lua
messages.StatedMessage = messages.editChatPhoto({chat_id=InputPeer, photo=InputChatPhoto, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|INPUT_CONSTRUCTOR_INVALID|The provided constructor is invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PHOTO_CROP_SIZE_SMALL|Photo is too small|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|



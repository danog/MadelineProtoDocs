---
title: messages.uploadMedia
description: Upload a file and associate it to a chat (without actually sending it to the chat)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.uploadMedia  
[Back to methods index](index.md)


Upload a file and associate it to a chat (without actually sending it to the chat)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat, can be an [inputPeerEmpty](../constructors/inputPeerEmpty.md) for bots | Optional|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | File uploaded in chunks as described in [files »](https://core.telegram.org/api/files) | Optional|


### Return type: [MessageMedia](../types/MessageMedia.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$MessageMedia = $MadelineProto->messages->uploadMedia(['peer' => InputPeer, 'media' => InputMedia, ]);
```

Or, if you're into Lua:

```lua
MessageMedia = messages.uploadMedia({peer=InputPeer, media=InputMedia, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_MISSING|This method can only be run by a bot|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|MEDIA_INVALID|Media invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|



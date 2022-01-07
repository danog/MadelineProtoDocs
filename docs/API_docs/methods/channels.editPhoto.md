---
title: "channels.editPhoto"
description: "Change the photo of a [channel/supergroup](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editPhoto.html
---
# Method: channels.editPhoto
[Back to methods index](index.md)



Change the photo of a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel/supergroup whose photo should be edited | Optional|
|photo|[InputChatPhoto](../types/InputChatPhoto.md) | New photo | Optional|


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

$Updates = $MadelineProto->channels->editPhoto(['channel' => InputChannel, 'photo' => InputChatPhoto, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|FILE_REFERENCE_INVALID|The specified [file reference](https://core.telegram.org/api/file_reference) is invalid|
|400|PHOTO_CROP_SIZE_SMALL|Photo is too small|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|PHOTO_INVALID|Photo invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|



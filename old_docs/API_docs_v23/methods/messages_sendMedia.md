---
title: messages.sendMedia
description: Send a media
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendMedia  
[Back to methods index](index.md)


Send a media

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to send the media | Optional|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | The media to send | Optional|


### Return type: [messages\_StatedMessage](../types/messages_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessage = $MadelineProto->messages->sendMedia(['peer' => InputPeer, 'media' => InputMedia, ]);
```

Or, if you're into Lua:

```lua
messages_StatedMessage = messages.sendMedia({peer=InputPeer, media=InputMedia, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_RESTRICTED|You can't send messages in this chat, you were restricted|
|400|EXTERNAL_URL_INVALID|External URL invalid|
|400|FILE_PART_LENGTH_INVALID|The length of a file part is invalid|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|IMAGE_PROCESS_FAILED|Failure while processing image|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MEDIA_CAPTION_TOO_LONG|The caption is too long|
|400|MEDIA_EMPTY|The provided media object is invalid|
|400|MEDIA_INVALID|Media invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|PHOTO_INVALID_DIMENSIONS|The photo dimensions are invalid|
|400|PHOTO_SAVE_FILE_INVALID||
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_IS_BLOCKED|You were blocked by this user|
|400|USER_IS_BOT|Bots can't send messages to other bots|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|400|WEBPAGE_MEDIA_EMPTY|Webpage media empty|
|403|CHAT_SEND_MEDIA_FORBIDDEN|You can't send media in this chat|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|-503|Timeout|Timeout while fetching data|



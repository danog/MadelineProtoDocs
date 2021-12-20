---
title: "messages.uploadMedia"
description: "Upload a file and associate it to a chat (without actually sending it to the chat)"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadMedia.html
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
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_RESTRICTED|You can't send messages in this chat, you were restricted|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|IMAGE_PROCESS_FAILED|Failure while processing image|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MEDIA_INVALID|Media invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|PHOTO_INVALID_DIMENSIONS|The photo dimensions are invalid|
|400|PHOTO_SAVE_FILE_INVALID|Internal issues, try again later|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|-503|Timeout|Timeout while fetching data|



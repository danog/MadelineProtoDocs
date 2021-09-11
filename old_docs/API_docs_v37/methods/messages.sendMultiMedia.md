---
title: messages.sendMultiMedia
description: Send an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMultiMedia.html
---
# Method: messages.sendMultiMedia
[Back to methods index](index.md)



Send an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Whether to send the album silently (no notification triggered) | Optional|
|background|[Bool](../types/Bool.md) | Send in background? | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Whether to clear [drafts](https://core.telegram.org/api/drafts) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The destination chat | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | The message to reply to | Optional|
|multi\_media|Array of [InputSingleMedia](../types/InputSingleMedia.md) | The medias to send | Yes|
|schedule\_date|[int](../types/int.md) | Scheduled message date for scheduled messages | Optional|


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

$Updates = $MadelineProto->messages->sendMultiMedia(['silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'multi_media' => [InputSingleMedia, InputSingleMedia], 'schedule_date' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendMultiMedia({silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, multi_media={InputSingleMedia}, schedule_date=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|420|SLOWMODE_WAIT_X|Slowmode is enabled in this chat: wait X seconds before sending another message to this chat.|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|MEDIA_CAPTION_TOO_LONG|The caption is too long|
|400|MEDIA_EMPTY|The provided media object is invalid|
|400|MEDIA_INVALID|Media invalid|
|400|MULTI_MEDIA_TOO_LONG|Too many media files for album|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|RANDOM_ID_EMPTY|Random ID empty|
|400|SCHEDULE_TOO_MUCH|There are too many scheduled messages|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|



---
title: "messages.sendMultiMedia"
description: "Send an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMultiMedia.html
---
# Method: messages.sendMultiMedia
[Back to methods index](index.html)



Send an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Whether to send the album silently (no notification triggered) | Optional|
|background|[Bool](/API_docs/types/Bool.html) | Send in background? | Optional|
|clear\_draft|[Bool](/API_docs/types/Bool.html) | Whether to clear [drafts](https://core.telegram.org/api/drafts) | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | Only for bots, disallows forwarding and saving of the messages, even if the destination chat doesn't have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The destination chat | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | The message to reply to | Optional|
|multi\_media|Array of [InputSingleMedia](/API_docs/types/InputSingleMedia.html) | The medias to send | Yes|
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for scheduled messages | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Send this message as the specified peer | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->messages->sendMultiMedia(silent: Bool, background: Bool, clear_draft: Bool, noforwards: Bool, peer: InputPeer, reply_to_msg_id: int, multi_media: [InputSingleMedia, InputSingleMedia], schedule_date: int, send_as: InputPeer, );
```


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
|update\_stickersets\_order|[Bool](/API_docs/types/Bool.html) | Whether to move used stickersets to top, [see here for more info on this flag »](https://core.telegram.org/api/stickers#recent-stickersets) | Optional|
|invert\_media|[Bool](/API_docs/types/Bool.html) | If set, any eventual webpage preview will be shown on top of the message instead of at the bottom. | Optional|
|allow\_paid\_floodskip|[Bool](/API_docs/types/Bool.html) | Bots only: if set, allows sending up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The destination chat | Optional|
|reply\_to|[InputReplyTo](/API_docs/types/InputReplyTo.html) | If set, indicates that the message should be sent in reply to the specified message or story. | Optional|
|multi\_media|Array of [InputSingleMedia](/API_docs/types/InputSingleMedia.html) | The medias to send | Yes|
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for scheduled messages | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Send this message as the specified peer | Optional|
|quick\_reply\_shortcut|[InputQuickReplyShortcut](/API_docs/types/InputQuickReplyShortcut.html) | Add the message to the specified [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts), instead. | Optional|
|effect|[long](/API_docs/types/long.html) | Specifies a [message effect »](https://core.telegram.org/api/effects) to use for the message. | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendMultiMedia(silent: $Bool, background: $Bool, clear_draft: $Bool, noforwards: $Bool, update_stickersets_order: $Bool, invert_media: $Bool, allow_paid_floodskip: $Bool, peer: $InputPeer, reply_to: $InputReplyTo, multi_media: [$InputSingleMedia, $InputSingleMedia], schedule_date: $int, send_as: $InputPeer, quick_reply_shortcut: $InputQuickReplyShortcut, effect: $long, );
```


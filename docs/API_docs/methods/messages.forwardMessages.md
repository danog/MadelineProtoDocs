---
title: "messages.forwardMessages"
description: "Forwards messages by their IDs."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_forwardMessages.html
---
# Method: messages.forwardMessages
[Back to methods index](index.html)



Forwards messages by their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Whether to send messages silently (no notification will be triggered on the destination clients) | Optional|
|background|[Bool](/API_docs/types/Bool.html) | Whether to send the message in background | Optional|
|with\_my\_score|[Bool](/API_docs/types/Bool.html) | When forwarding games, whether to include your score in the game | Optional|
|drop\_author|[Bool](/API_docs/types/Bool.html) | Whether to forward messages without quoting the original author | Optional|
|drop\_media\_captions|[Bool](/API_docs/types/Bool.html) | Whether to strip captions from media | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | Only for bots, disallows further re-forwarding and saving of the messages, even if the destination chat doesn't have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled | Optional|
|allow\_paid\_floodskip|[Bool](/API_docs/types/Bool.html) | Bots only: if set, allows sending up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. | Optional|
|from\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Source of messages | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of messages | Yes|
|to\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Destination peer | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | Destination [forum topic](https://core.telegram.org/api/forum#forum-topics) | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for scheduled messages | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Forward the messages as the specified peer | Optional|
|quick\_reply\_shortcut|[InputQuickReplyShortcut](/API_docs/types/InputQuickReplyShortcut.html) | Add the messages to the specified [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts), instead. | Optional|
|video\_timestamp|[int](/API_docs/types/int.html) |  | Optional|
|allow\_paid\_stars|[long](/API_docs/types/long.html) |  | Optional|


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

$Updates = $MadelineProto->messages->forwardMessages(silent: $Bool, background: $Bool, with_my_score: $Bool, drop_author: $Bool, drop_media_captions: $Bool, noforwards: $Bool, allow_paid_floodskip: $Bool, from_peer: $InputPeer, id: [$int, $int], to_peer: $InputPeer, top_msg_id: $int, schedule_date: $int, send_as: $InputPeer, quick_reply_shortcut: $InputQuickReplyShortcut, video_timestamp: $int, allow_paid_stars: $long, );
```


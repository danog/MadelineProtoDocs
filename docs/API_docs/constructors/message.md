---
title: "message"
description: "A message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: message  
[Back to constructors index](index.md)



A message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Is this an outgoing message|
|mentioned|[Bool](../types/Bool.md) | Optional|Whether we were [mentioned](https://core.telegram.org/api/mentions) in this message|
|media\_unread|[Bool](../types/Bool.md) | Optional|Whether there are unread media attachments in this message|
|silent|[Bool](../types/Bool.md) | Optional|Whether this is a silent message (no notification triggered)|
|post|[Bool](../types/Bool.md) | Optional|Whether this is a channel post|
|from\_scheduled|[Bool](../types/Bool.md) | Optional|Whether this is a [scheduled message](https://core.telegram.org/api/scheduled-messages)|
|legacy|[Bool](../types/Bool.md) | Optional|This is a legacy message: it has to be refetched with the new layer|
|edit\_hide|[Bool](../types/Bool.md) | Optional|Whether the message should be shown as not modified to the user, even if an edit date is present|
|pinned|[Bool](../types/Bool.md) | Optional|Whether this message is [pinned](https://core.telegram.org/api/pin)|
|noforwards|[Bool](../types/Bool.md) | Optional|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[Peer](../types/Peer.md) | Optional|ID of the sender of the message|
|peer\_id|[Peer](../types/Peer.md) | Yes|Peer ID, the chat where this message was sent|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Info about forwarded messages|
|via\_bot\_id|[long](../types/long.md) | Optional|
|reply\_to|[MessageReplyHeader](../types/MessageReplyHeader.md) | Optional|Reply information|
|date|[int](../types/int.md) | Yes|Date of the message|
|message|[string](../types/string.md) | Yes|The message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media attachment|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup (bot/inline keyboards)|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text|
|views|[int](../types/int.md) | Optional|View count for channel posts|
|forwards|[int](../types/int.md) | Optional|Forward counter|
|replies|[MessageReplies](../types/MessageReplies.md) | Optional|Info about [post comments (for channels) or message replies (for groups)](https://core.telegram.org/api/threads)|
|edit\_date|[int](../types/int.md) | Optional|Last edit date of this message|
|post\_author|[string](../types/string.md) | Optional|Name of the author of this message for channel posts (with signatures enabled)|
|grouped\_id|[long](../types/long.md) | Optional|Multiple media messages sent using [messages.sendMultiMedia](../methods/messages.sendMultiMedia.md) with the same grouped ID indicate an [album or media group](https://core.telegram.org/api/files#albums-grouped-media)|
|restriction\_reason|Array of [RestrictionReason](../types/RestrictionReason.md) | Optional|Contains the reason why access to this message must be restricted.|
|ttl\_period|[int](../types/int.md) | Optional|



### Type: [Message](../types/Message.md)


### Example:

```php
$message = ['_' => 'message', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'from_scheduled' => Bool, 'legacy' => Bool, 'edit_hide' => Bool, 'pinned' => Bool, 'noforwards' => Bool, 'id' => int, 'from_id' => Peer, 'peer_id' => Peer, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'date' => int, 'message' => 'string', 'media' => MessageMedia, 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'views' => int, 'forwards' => int, 'replies' => MessageReplies, 'edit_date' => int, 'post_author' => 'string', 'grouped_id' => long, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'ttl_period' => int];
```  


Or, if you're into Lua:

```lua
message={_='message', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, post=Bool, from_scheduled=Bool, legacy=Bool, edit_hide=Bool, pinned=Bool, noforwards=Bool, id=int, from_id=Peer, peer_id=Peer, fwd_from=MessageFwdHeader, via_bot_id=long, reply_to=MessageReplyHeader, date=int, message='string', media=MessageMedia, reply_markup=ReplyMarkup, entities={MessageEntity}, views=int, forwards=int, replies=MessageReplies, edit_date=int, post_author='string', grouped_id=long, restriction_reason={RestrictionReason}, ttl_period=int}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  



---
title: message
description: A message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: message  
[Back to constructors index](index.md)



A message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Is this an outgoing message|
|mentioned|[Bool](../types/Bool.md) | Optional|Whether we were mentioned in this message|
|media\_unread|[Bool](../types/Bool.md) | Optional|Whether there are unread media attachments in this message|
|silent|[Bool](../types/Bool.md) | Optional|Whether this is a silent message (no notification triggered)|
|post|[Bool](../types/Bool.md) | Optional|Whether this is a channel post|
|from\_scheduled|[Bool](../types/Bool.md) | Optional|Whether this is a scheduled post|
|legacy|[Bool](../types/Bool.md) | Optional|This is a legacy message: it has to be refetched with the new layer|
|edit\_hide|[Bool](../types/Bool.md) | Optional|Whether the message should be shown as not modified to the user, even if an edit date is present|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[int](../types/int.md) | Optional|ID of the sender of the message|
|to\_id|[Peer](../types/Peer.md) | Yes|ID of the chat were the message was sent|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Info about forwarded messages|
|via\_bot\_id|[int](../types/int.md) | Optional|ID of the inline bot that generated the message|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|ID of the message this message replies to|
|date|[int](../types/int.md) | Yes|Date of the message|
|message|[string](../types/string.md) | Yes|The message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media attachment|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup (bot/inline keyboards)|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text|
|views|[int](../types/int.md) | Optional|View count for channel posts|
|edit\_date|[int](../types/int.md) | Optional|Last edit date of this message|
|post\_author|[string](../types/string.md) | Optional|Name of the author of this message for channel posts (with signatures enabled)|
|grouped\_id|[long](../types/long.md) | Optional|Multiple media messages sent using [messages.sendMultiMedia](../methods/messages.sendMultiMedia.md) with the same grouped ID indicate an album|
|restriction\_reason|Array of [RestrictionReason](../types/RestrictionReason.md) | Optional|Contains the reason why access to this message must be restricted.|



### Type: [Message](../types/Message.md)


### Example:

```php
$message = ['_' => 'message', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'from_scheduled' => Bool, 'legacy' => Bool, 'edit_hide' => Bool, 'id' => int, 'from_id' => int, 'to_id' => Peer, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => int, 'reply_to_msg_id' => int, 'date' => int, 'message' => 'string', 'media' => MessageMedia, 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'views' => int, 'edit_date' => int, 'post_author' => 'string', 'grouped_id' => long, 'restriction_reason' => [RestrictionReason, RestrictionReason]];
```  


Or, if you're into Lua:

```lua
message={_='message', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, post=Bool, from_scheduled=Bool, legacy=Bool, edit_hide=Bool, id=int, from_id=int, to_id=Peer, fwd_from=MessageFwdHeader, via_bot_id=int, reply_to_msg_id=int, date=int, message='string', media=MessageMedia, reply_markup=ReplyMarkup, entities={MessageEntity}, views=int, edit_date=int, post_author='string', grouped_id=long, restriction_reason={RestrictionReason}}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  



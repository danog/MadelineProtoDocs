---
title: message
description: Message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: message  
[Back to constructors index](index.md)



Message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Out?|
|mentioned|[Bool](../types/Bool.md) | Optional|Mentioned?|
|media\_unread|[Bool](../types/Bool.md) | Optional|Media unread?|
|silent|[Bool](../types/Bool.md) | Optional|Silent?|
|post|[Bool](../types/Bool.md) | Optional|Post?|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Optional|From ID|
|to\_id|[Peer](../types/Peer.md) | Yes|To ID|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Forwarded from|
|via\_bot\_id|[int](../types/int.md) | Optional|Via bot ID|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|Reply to msg ID|
|date|[int](../types/int.md) | Yes|Date|
|message|[string](../types/string.md) | Yes|Message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|
|views|[int](../types/int.md) | Optional|Views|
|edit\_date|[int](../types/int.md) | Optional|Edit date|
|post\_author|[string](../types/string.md) | Optional|Post author|



### Type: [Message](../types/Message.md)


### Example:

```php
$message = ['_' => 'message', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'id' => int, 'from_id' => int, 'to_id' => Peer, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => int, 'reply_to_msg_id' => int, 'date' => int, 'message' => 'string', 'media' => MessageMedia, 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'views' => int, 'edit_date' => int, 'post_author' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "message", "out": Bool, "mentioned": Bool, "media_unread": Bool, "silent": Bool, "post": Bool, "id": int, "from_id": int, "to_id": Peer, "fwd_from": MessageFwdHeader, "via_bot_id": int, "reply_to_msg_id": int, "date": int, "message": "string", "media": MessageMedia, "reply_markup": ReplyMarkup, "entities": [MessageEntity], "views": int, "edit_date": int, "post_author": "string"}
```


Or, if you're into Lua:

```lua
message={_='message', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, post=Bool, id=int, from_id=int, to_id=Peer, fwd_from=MessageFwdHeader, via_bot_id=int, reply_to_msg_id=int, date=int, message='string', media=MessageMedia, reply_markup=ReplyMarkup, entities={MessageEntity}, views=int, edit_date=int, post_author='string'}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  



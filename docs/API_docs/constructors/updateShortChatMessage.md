---
title: "updateShortChatMessage"
description: "Shortened constructor containing info on one new incoming text message from a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Shortened constructor containing info on one new incoming text message from a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is outgoing|
|mentioned|[Bool](/API_docs/types/Bool.html) | Optional|Whether we were mentioned in this message|
|media\_unread|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message contains some **unread** mentions|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](/API_docs/types/int.html) | Yes|ID of the message|
|from\_id|[long](/API_docs/types/long.html) | Yes|ID of the sender of the message|
|chat\_id|[long](/API_docs/types/long.html) | Yes|ID of the chat where the message was sent|
|message|[string](/API_docs/types/string.html) | Yes|Message|
|pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.html) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](/API_docs/types/MessageFwdHeader.html) | Optional|Info about a forwarded message|
|via\_bot\_id|[long](/API_docs/types/long.html) | Optional|Info about the inline bot used to generate this message|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.html) | Optional|Reply (thread) information|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time To Live of the message, once updateShortChatMessage.date+updateShortChatMessage.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well.|



### Type: [Updates](/API_docs/types/Updates.html)


### Example:

```
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'from_id' => long, 'chat_id' => long, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  

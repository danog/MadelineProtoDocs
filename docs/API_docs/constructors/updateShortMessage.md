---
title: "updateShortMessage"
description: "Info about a message sent to (received from) another user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a message sent to (received from) another user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is outgoing|
|mentioned|[Bool](/API_docs/types/Bool.html) | Optional|Whether we were mentioned in the message|
|media\_unread|[Bool](/API_docs/types/Bool.html) | Optional|Whether there are some **unread** mentions in this message|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](/API_docs/types/int.html) | Yes|The message ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|The ID of the sender (if `outgoing` will be the ID of the destination) of the message|
|message|[string](/API_docs/types/string.html) | Yes|The message|
|pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.html) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](/API_docs/types/MessageFwdHeader.html) | Optional|Info about a forwarded message|
|via\_bot\_id|[long](/API_docs/types/long.html) | Optional|Info about the inline bot used to generate this message|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.html) | Optional|Reply and [thread](https://core.telegram.org/api/threads) information|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time To Live of the message, once message.date+message.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well.|



### Type: [Updates](/API_docs/types/Updates.html)


### Example:

```
$updateShortMessage = ['_' => 'updateShortMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'user_id' => long, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  

---
title: "updateShortMessage"
description: "Info about a message sent to (received from) another user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortMessage  
[Back to constructors index](/API_docs/constructors/index.md)



Info about a message sent to (received from) another user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.md) | Optional|Whether the message is outgoing|
|mentioned|[Bool](/API_docs/types/Bool.md) | Optional|Whether we were mentioned in the message|
|media\_unread|[Bool](/API_docs/types/Bool.md) | Optional|Whether there are some **unread** mentions in this message|
|silent|[Bool](/API_docs/types/Bool.md) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](/API_docs/types/int.md) | Yes|The message ID|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|message|[string](/API_docs/types/string.md) | Yes|The message|
|pts|[int](/API_docs/types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](/API_docs/types/MessageFwdHeader.md) | Optional|Info about a forwarded message|
|via\_bot\_id|[long](/API_docs/types/long.md) | Optional|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.md) | Optional|Reply and [thread](https://core.telegram.org/api/threads) information|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](/API_docs/types/int.md) | Optional|



### Type: [Updates](/API_docs/types/Updates.md)


### Example:

```php
$updateShortMessage = ['_' => 'updateShortMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'user_id' => long, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  

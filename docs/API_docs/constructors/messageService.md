---
title: "messageService"
description: "Indicates a service message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageService  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a service message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is outgoing|
|mentioned|[Bool](/API_docs/types/Bool.html) | Optional|Whether we were mentioned in the message|
|media\_unread|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message contains unread media|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is silent|
|post|[Bool](/API_docs/types/Bool.html) | Optional|Whether it's a channel post|
|legacy|[Bool](/API_docs/types/Bool.html) | Optional|This is a legacy message: it has to be refetched with the new layer|
|id|[int](/API_docs/types/int.html) | Yes|Message ID|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|ID of the sender of this message|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|Sender of service message|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.html) | Optional|Reply (thread) information|
|date|[int](/API_docs/types/int.html) | Yes|Message date|
|action|[MessageAction](/API_docs/types/MessageAction.html) | Optional|Event connected with the service message|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time To Live of the message, once message.date+message.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well.|



### Type: [Message](/API_docs/types/Message.html)


### Example:

```
$messageService = ['_' => 'messageService', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'legacy' => Bool, 'id' => int, 'from_id' => Peer, 'peer_id' => Peer, 'reply_to' => MessageReplyHeader, 'date' => int, 'action' => MessageAction, 'ttl_period' => int];
```  

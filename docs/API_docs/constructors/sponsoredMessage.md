---
title: "sponsoredMessage"
description: "A sponsored message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A [sponsored message](https://core.telegram.org/api/sponsored-messages).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|recommended|[Bool](/API_docs/types/Bool.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|ID of the sender of the message|
|chat\_invite|[ChatInvite](/API_docs/types/ChatInvite.html) | Optional|Information about the chat invite hash specified in `chat_invite_hash`|
|chat\_invite\_hash|[string](/API_docs/types/string.html) | Optional|Chat invite|
|channel\_post|[int](/API_docs/types/int.html) | Optional|Optional link to a channel post if `from_id` points to a channel|
|start\_param|[string](/API_docs/types/string.html) | Optional|Parameter for the bot start message if the sponsored chat is a chat with a bot.|
|message|[string](/API_docs/types/string.html) | Yes|Sponsored message|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [SponsoredMessage](/API_docs/types/SponsoredMessage.html)


### Example:

```
$sponsoredMessage = ['_' => 'sponsoredMessage', 'recommended' => Bool, 'from_id' => Peer, 'chat_invite' => ChatInvite, 'chat_invite_hash' => 'string', 'channel_post' => int, 'start_param' => 'string', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  

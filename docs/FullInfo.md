---
title: full chat info
description: chat attributes, type and example
nav_exclude: true
---
## Constructor: FullInfo  



### Attributes:

| Name     |    Type       | Required |Description|
|----------|---------------|----------|-----------|
|type|[string](API_docs/types/string.html) | Yes|bot, user, channel, supergroup or chat|
|Chat|[Chat](API_docs/types/Chat.html) | Optional|Info about the current chat|
|User|[User](API_docs/types/User.html) | Optional|Info about the current user|
|bot\_api\_id|[long](API_docs/types/long.html) | Yes|bot API chat id|
|InputPeer|[InputPeer](API_docs/types/InputPeer.html) | Yes|InputPeer object|
|Peer|[Peer](API_docs/types/Peer.html) | Optional|Peer object|
|user\_id|[int](API_docs/types/int.html) | Optional|MTProto user id|
|chat\_id|[int](API_docs/types/int.html) | Optional|MTProto chat id|
|channel\_id|[int](API_docs/types/int.html) | Optional|MTProto channel id|
|InputUser|[InputUser](API_docs/types/InputUser.html) | Optional|InputUser object|
|InputChannel|[InputChannel](API_docs/types/InputChannel.html) | Optional|InputChannel object|
|last_update|[int](API_docs/types/int.html) | Yes|When was info about this peer cached|
|full|[ChatFull](API_docs/types/ChatFull.html) or [UserFull](API_docs/types/UserFull.html) | Yes|full info|

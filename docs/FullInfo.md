---
title: full chat info
description: chat attributes, type and example
---
## Constructor: FullInfo  



### Attributes:

| Name     |    Type       | Required |Description|
|----------|---------------|----------|-----------|
|type|[string](API_docs/types/string.md) | Yes|bot, user, channel, supergroup or chat|
|Chat|[Chat](API_docs/types/Chat.md) | Optional|Info about the current chat|
|User|[User](API_docs/types/User.md) | Optional|Info about the current user|
|bot\_api\_id|[long](API_docs/types/long.md) | Yes|bot API chat id|
|InputPeer|[InputPeer](API_docs/types/InputPeer.md) | Yes|InputPeer object|
|Peer|[Peer](API_docs/types/Peer.md) | Optional|Peer object|
|user\_id|[int](API_docs/types/int.md) | Optional|MTProto user id|
|chat\_id|[int](API_docs/types/int.md) | Optional|MTProto chat id|
|channel\_id|[int](API_docs/types/int.md) | Optional|MTProto channel id|
|InputUser|[InputUser](API_docs/types/InputUser.md) | Optional|InputUser object|
|InputChannel|[InputChannel](API_docs/types/InputChannel.md) | Optional|InputChannel object|
|last_update|[int](API_docs/types/int.md) | Yes|When was info about this peer cached|
|full|[ChatFull](API_docs/types/ChatFull.md) or [UserFull](API_docs/types/UserFull.md) | Yes|full info|

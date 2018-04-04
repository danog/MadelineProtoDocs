---
title: chatEventMemberRestricted
description: A chat member restricted/unrestircted or banned/unbanned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatEventMemberRestricted  
[Back to constructors index](index.md)



A chat member restricted/unrestircted or banned/unbanned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|Chat member user identifier|
|old\_status|[ChatMemberStatus](../types/ChatMemberStatus.md) | Yes|Old chat member status|
|new\_status|[ChatMemberStatus](../types/ChatMemberStatus.md) | Yes|New chat member status|



### Type: [ChatEventAction](../types/ChatEventAction.md)



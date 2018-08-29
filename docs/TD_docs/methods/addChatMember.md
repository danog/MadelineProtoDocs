---
title: addChatMember
description: Adds new member to chat. Members can't be added to private or secret chats. Member will not be added until chat state will be synchronized with the server
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: addChatMember  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Adds new member to chat. Members can't be added to private or secret chats. Member will not be added until chat state will be synchronized with the server

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|user\_id|[int](../types/int.md) | Identifier of the user to add | Yes|
|forward\_limit|[int](../types/int.md) | Number of previous messages from chat to forward to new member, ignored for channel chats. Can't be greater than 300 | Yes|


### Return type: [Ok](../types/Ok.md)


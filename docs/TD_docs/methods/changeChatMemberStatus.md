---
title: changeChatMemberStatus
description: Changes status of the chat member, need appropriate privileges. This function is currently not suitable for adding new members to the chat, use addChatMember instead. Status will not be changed until chat state will be synchronized with the server
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: changeChatMemberStatus  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Changes status of the chat member, need appropriate privileges. This function is currently not suitable for adding new members to the chat, use addChatMember instead. Status will not be changed until chat state will be synchronized with the server

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|user\_id|[int](../types/int.md) | Identifier of the user to edit status | Yes|
|status|[ChatMemberStatus](../types/ChatMemberStatus.md) | New status of the member in the chat | Yes|


### Return type: [Ok](../types/Ok.md)


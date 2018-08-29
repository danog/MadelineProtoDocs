---
title: addChatMembers
description: Adds many new members to the chat. Currently, available only for channels. Can't be used to join the channel. Members can't be added to broadcast channel if it has more than 200 members. Members will not be added until chat state will be synchronized with the server
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: addChatMembers  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Adds many new members to the chat. Currently, available only for channels. Can't be used to join the channel. Members can't be added to broadcast channel if it has more than 200 members. Members will not be added until chat state will be synchronized with the server

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|user\_ids|Array of [int](../types/int.md) | Identifiers of the users to add | Yes|


### Return type: [Ok](../types/Ok.md)


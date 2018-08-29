---
title: getChats
description: Returns list of chats in the right order, chats are sorted by (order, chat_id) in decreasing order. For example, to get list of chats from the beginning, the offset_order should be equal 2^63 - 1
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getChats  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns list of chats in the right order, chats are sorted by (order, chat_id) in decreasing order. For example, to get list of chats from the beginning, the offset_order should be equal 2^63 - 1

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset\_order|[int64](../constructors/int64.md) | Chat order to return chats from | Yes|
|offset\_chat\_id|[int53](../types/int53.md) | Chat identifier to return chats from | Yes|
|limit|[int](../types/int.md) | Maximum number of chats to be returned. There may be less than limit chats returned even the end of the list is not reached | Yes|


### Return type: [Chats](../types/Chats.md)


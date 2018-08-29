---
title: getCommonChats
description: Returns list of common chats with an other given user. Chats are sorted by their type and creation date
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getCommonChats  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns list of common chats with an other given user. Chats are sorted by their type and creation date

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[int](../types/int.md) | User identifier | Yes|
|offset\_chat\_id|[int53](../types/int53.md) | Chat identifier to return chats from, use 0 for the first request | Yes|
|limit|[int](../types/int.md) | Maximum number of chats to be returned, up to 100 | Yes|


### Return type: [Chats](../types/Chats.md)


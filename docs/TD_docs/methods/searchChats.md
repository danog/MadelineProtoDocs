---
title: searchChats
description: Searches for specified query in the title and username of known chats, offline request. Returns chats in the order of them in the chat list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchChats  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for specified query in the title and username of known chats, offline request. Returns chats in the order of them in the chat list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query|[string](../types/string.md) | Query to search for, if query is empty, returns up to 20 recently found chats | Yes|
|limit|[int](../types/int.md) | Maximum number of chats to be returned | Yes|


### Return type: [Chats](../types/Chats.md)


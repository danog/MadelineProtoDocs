---
title: searchChatMembers
description: Searches for the specified query in the first name, last name and username among members of the specified chat. Requires administrator rights in broadcast channels
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchChatMembers  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for the specified query in the first name, last name and username among members of the specified chat. Requires administrator rights in broadcast channels

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|query|[string](../types/string.md) | Query to search for | Yes|
|limit|[int](../types/int.md) | Maximum number of users to be returned | Yes|


### Return type: [ChatMembers](../types/ChatMembers.md)


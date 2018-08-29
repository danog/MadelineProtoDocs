---
title: searchMessages
description: Searches for messages in all chats except secret chats. Returns result in reverse chronological order, i. e. in order of decreasing (date, chat_id, message_id)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for messages in all chats except secret chats. Returns result in reverse chronological order, i. e. in order of decreasing (date, chat_id, message_id)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query|[string](../types/string.md) | Query to search for | Yes|
|offset\_date|[int](../types/int.md) | Date of the message to search from, you can use 0 or any date in the future to get results from the beginning | Yes|
|offset\_chat\_id|[int53](../types/int53.md) | Chat identifier of the last found message or 0 for the first request | Yes|
|offset\_message\_id|[int53](../types/int53.md) | Message identifier of the last found message or 0 for the first request | Yes|
|limit|[int](../types/int.md) | Maximum number of messages to be returned, at most 100 | Yes|


### Return type: [Messages](../types/Messages.md)


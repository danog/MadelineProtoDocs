---
title: searchChatMessages
description: Searches for messages with given words in the chat. Returns result in reverse chronological order, i. e. in order of decreasing message_id. Doesn't work in secret chats with non-empty query (searchSecretMessages should be used instead) or without enabled message database
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchChatMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for messages with given words in the chat. Returns result in reverse chronological order, i. e. in order of decreasing message_id. Doesn't work in secret chats with non-empty query (searchSecretMessages should be used instead) or without enabled message database

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier to search messages in | Yes|
|query|[string](../types/string.md) | Query to search for | Yes|
|sender\_user\_id|[int](../types/int.md) | If not 0, only messages sent by the specified user will be returned. Doesn't supported in secret chats | Yes|
|from\_message\_id|[int53](../types/int53.md) | Identifier of the message from which we need a history, you can use 0 to get results from the beginning | Yes|
|offset|[int](../types/int.md) | Specify 0 to get results exactly from from_message_id or negative offset to get specified message and some newer messages | Yes|
|limit|[int](../types/int.md) | Maximum number of messages to be returned, should be positive and can't be greater than 100. If offset is negative, limit must be greater than -offset. There may be less than limit messages returned even the end of the history is not reached | Yes|
|filter|[SearchMessagesFilter](../types/SearchMessagesFilter.md) | Filter for content of the searched messages | Optional|


### Return type: [Messages](../types/Messages.md)


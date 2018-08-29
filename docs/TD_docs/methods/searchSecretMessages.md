---
title: searchSecretMessages
description: Searches for messages in secret chats. Returns result in reverse chronological order
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchSecretMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for messages in secret chats. Returns result in reverse chronological order

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Identifier of a chat to search in. Specify 0 to search in all secret chats | Yes|
|query|[string](../types/string.md) | Query to search for. If empty, searchChatMessages should be used instead | Yes|
|from\_search\_id|[int64](../constructors/int64.md) | Identifier from the result of previous request, use 0 to get results from the beginning | Yes|
|limit|[int](../types/int.md) | Maximum number of messages to be returned, can't be greater than 100 | Yes|
|filter|[SearchMessagesFilter](../types/SearchMessagesFilter.md) | Filter for content of searched messages | Optional|


### Return type: [FoundMessages](../types/FoundMessages.md)


---
title: searchCallMessages
description: Searches for call messages. Returns result in reverse chronological order, i. e. in order of decreasing message_id
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: searchCallMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Searches for call messages. Returns result in reverse chronological order, i. e. in order of decreasing message_id

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|from\_message\_id|[int53](../types/int53.md) | Identifier of the message from which to search, you can use 0 to get results from beginning | Yes|
|limit|[int](../types/int.md) | Maximum number of messages to be returned, can't be greater than 100. There may be less than limit messages returned even the end of the history is not reached filter | Yes|
|only\_missed|[Bool](../types/Bool.md) | If true, return only messages with missed calls | Yes|


### Return type: [Messages](../types/Messages.md)


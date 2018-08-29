---
title: getChatHistory
description: Returns messages in a chat. Returns result in reverse chronological order, i.e. in order of decreasing message.message_id. Offline request if only_local is true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getChatHistory  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns messages in a chat. Returns result in reverse chronological order, i.e. in order of decreasing message.message_id. Offline request if only_local is true

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|from\_message\_id|[int53](../types/int53.md) | Identifier of the message near which we need a history, you can use 0 to get results from the beginning, i.e. from oldest to newest | Yes|
|offset|[int](../types/int.md) | Specify 0 to get results exactly from from_message_id or negative offset to get specified message and some newer messages | Yes|
|limit|[int](../types/int.md) | Maximum number of messages to be returned, should be positive and can't be greater than 100. If offset is negative, limit must be greater than -offset. There may be less than limit messages returned even the end of the history is not reached | Yes|
|only\_local|[Bool](../types/Bool.md) | Return only locally available messages without sending network requests | Yes|


### Return type: [Messages](../types/Messages.md)


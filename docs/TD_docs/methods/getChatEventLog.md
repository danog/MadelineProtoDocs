---
title: getChatEventLog
description: Returns list of service actions taken by chat members and administrators in the last 48 hours, available only in channels. Requires administrator rights. Returns result in reverse chronological order, i. e. in order of decreasing event_id
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getChatEventLog  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns list of service actions taken by chat members and administrators in the last 48 hours, available only in channels. Requires administrator rights. Returns result in reverse chronological order, i. e. in order of decreasing event_id

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|query|[string](../types/string.md) | Search query to filter events | Yes|
|from\_event\_id|[int64](../constructors/int64.md) | Identifier of an event from which to return result, you can use 0 to get results from the latest events | Yes|
|limit|[int](../types/int.md) | Maximum number of events to return, can't be greater than 100 | Yes|
|filters|[chatEventLogFilters](../constructors/chatEventLogFilters.md) | Types of events to return, defaults to all | Yes|
|user\_ids|Array of [int](../types/int.md) | User identifiers, which events to return, defaults to all users | Yes|


### Return type: [ChatEvents](../types/ChatEvents.md)


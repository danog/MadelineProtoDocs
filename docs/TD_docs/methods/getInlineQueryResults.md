---
title: getInlineQueryResults
description: Sends inline query to a bot and returns its results. Returns error with code 502 if bot fails to answer the query before query timeout expires. Unavailable for bots
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getInlineQueryResults  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sends inline query to a bot and returns its results. Returns error with code 502 if bot fails to answer the query before query timeout expires. Unavailable for bots

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_user\_id|[int](../types/int.md) | Identifier of the bot send query to | Yes|
|chat\_id|[int53](../types/int53.md) | Identifier of the chat, where the query is sent | Yes|
|user\_location|[location](../constructors/location.md) | User location, only if needed | Yes|
|query|[string](../types/string.md) | Text of the query | Yes|
|offset|[string](../types/string.md) | Offset of the first entry to return | Yes|


### Return type: [InlineQueryResults](../types/InlineQueryResults.md)


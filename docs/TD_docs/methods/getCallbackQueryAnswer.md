---
title: getCallbackQueryAnswer
description: Sends callback query to a bot and returns answer to it. Returns error with code 502 if bot fails to answer the query before query timeout expires. Unavailable for bots
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getCallbackQueryAnswer  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sends callback query to a bot and returns answer to it. Returns error with code 502 if bot fails to answer the query before query timeout expires. Unavailable for bots

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Identifier of the chat with a message | Yes|
|message\_id|[int53](../types/int53.md) | Identifier of the message, from which the query is originated | Yes|
|payload|[CallbackQueryPayload](../types/CallbackQueryPayload.md) | Query payload | Yes|


### Return type: [CallbackQueryAnswer](../types/CallbackQueryAnswer.md)


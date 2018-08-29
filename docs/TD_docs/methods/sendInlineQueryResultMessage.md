---
title: sendInlineQueryResultMessage
description: Sends result of the inline query as a message. Returns sent message. Always clears chat draft message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: sendInlineQueryResultMessage  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sends result of the inline query as a message. Returns sent message. Always clears chat draft message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat to send message | Yes|
|reply\_to\_message\_id|[int53](../types/int53.md) | Identifier of a message to reply to or 0 | Yes|
|disable\_notification|[Bool](../types/Bool.md) | Pass true, to disable notification about the message, doesn't works in secret chats | Yes|
|from\_background|[Bool](../types/Bool.md) | Pass true, if the message is sent from background | Yes|
|query\_id|[int64](../constructors/int64.md) | Identifier of the inline query | Yes|
|result\_id|[string](../types/string.md) | Identifier of the inline result | Yes|


### Return type: [Message](../types/Message.md)


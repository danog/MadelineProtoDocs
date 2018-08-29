---
title: sendMessage
description: Sends a message. Returns sent message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: sendMessage  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sends a message. Returns sent message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat to send message | Yes|
|reply\_to\_message\_id|[int53](../types/int53.md) | Identifier of a message to reply to or 0 | Yes|
|disable\_notification|[Bool](../types/Bool.md) | Pass true, to disable notification about the message, doesn't works in secret chats | Yes|
|from\_background|[Bool](../types/Bool.md) | Pass true, if the message is sent from background | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Bots only. Markup for replying to message | Yes|
|input\_message\_content|[InputMessageContent](../types/InputMessageContent.md) | Content of a message to send | Yes|


### Return type: [Message](../types/Message.md)


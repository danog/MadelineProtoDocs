---
title: forwardMessages
description: Forwards previously sent messages. Returns forwarded messages in the same order as message identifiers passed in message_ids. If message can't be forwarded, null will be returned instead of the message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: forwardMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Forwards previously sent messages. Returns forwarded messages in the same order as message identifiers passed in message_ids. If message can't be forwarded, null will be returned instead of the message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Identifier of a chat to forward messages | Yes|
|from\_chat\_id|[int53](../types/int53.md) | Identifier of a chat to forward from | Yes|
|message\_ids|Array of [int53](../types/int53.md) | Identifiers of messages to forward | Yes|
|disable\_notification|[Bool](../types/Bool.md) | Pass true, to disable notification about the message, doesn't works if messages are forwarded to secret chat | Yes|
|from\_background|[Bool](../types/Bool.md) | Pass true, if the message is sent from background | Yes|


### Return type: [Messages](../types/Messages.md)


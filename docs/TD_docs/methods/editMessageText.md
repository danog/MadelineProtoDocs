---
title: editMessageText
description: Edits text of text or game message. Non-bots can edit message in a limited period of time. Returns edited message after edit is complete server side
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: editMessageText  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Edits text of text or game message. Non-bots can edit message in a limited period of time. Returns edited message after edit is complete server side

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat the message belongs to | Yes|
|message\_id|[int53](../types/int53.md) | Identifier of the message | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Bots only. New message reply markup | Yes|
|input\_message\_content|[InputMessageContent](../types/InputMessageContent.md) | New text content of the message. Should be of type InputMessageText | Yes|


### Return type: [Message](../types/Message.md)


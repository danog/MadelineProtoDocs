---
title: editMessageCaption
description: Edits message content caption. Non-bots can edit message in a limited period of time. Returns edited message after edit is complete server side
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: editMessageCaption  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Edits message content caption. Non-bots can edit message in a limited period of time. Returns edited message after edit is complete server side

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat the message belongs to | Yes|
|message\_id|[int53](../types/int53.md) | Identifier of the message | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Bots only. New message reply markup | Yes|
|caption|[string](../types/string.md) | New message content caption, 0-200 characters | Yes|


### Return type: [Message](../types/Message.md)


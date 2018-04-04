---
title: replyMarkupRemoveKeyboard
description: Instruct clients to remove keyboard after receiving this message. This kind of keyboard can't be received. Instead UpdateChatReplyMarkup with message_id == 0 will be send
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: replyMarkupRemoveKeyboard  
[Back to constructors index](index.md)



Instruct clients to remove keyboard after receiving this message. This kind of keyboard can't be received. Instead UpdateChatReplyMarkup with message_id == 0 will be send

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|personal|[Bool](../types/Bool.md) | Yes|Keyboard is removed only for mentioned users or replied to user|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)



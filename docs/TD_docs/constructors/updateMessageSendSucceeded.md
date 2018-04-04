---
title: updateMessageSendSucceeded
description: Message is successfully sent
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageSendSucceeded  
[Back to constructors index](index.md)



Message is successfully sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[message](../constructors/message.md) | Yes|Information about sent message. Usually only message identifier, date and content are changed, but almost any other fields can also change|
|old\_message\_id|[int53](../types/int53.md) | Yes|Previous temporary message identifier|



### Type: [Update](../types/Update.md)



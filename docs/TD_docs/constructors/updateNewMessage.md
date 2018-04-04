---
title: updateNewMessage
description: New message received, maybe outcoming message sent from other device
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](index.md)



New message received, maybe outcoming message sent from other device

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[message](../constructors/message.md) | Yes|New message|
|disable\_notification|[Bool](../types/Bool.md) | Yes|If true, notification about the message should be disabled|
|contains\_mention|[Bool](../types/Bool.md) | Yes|True, if the message contains mention of the current user|



### Type: [Update](../types/Update.md)



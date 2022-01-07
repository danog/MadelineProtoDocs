---
title: "updateNewMessage"
description: "New message in a private chat or in a legacy group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](index.md)



New message in a private chat or in a [legacy group](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|pts|[int](../types/int.md) | Yes|New quantity of actions in a message box|
|pts\_count|[int](../types/int.md) | Yes|Number of generated events|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewMessage = ['_' => 'updateNewMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  

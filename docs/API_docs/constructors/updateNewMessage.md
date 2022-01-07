---
title: "updateNewMessage"
description: "New message in a private chat or in a legacy group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](/API_docs/constructors/index.md)



New message in a private chat or in a [legacy group](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.md) | Optional|Message|
|pts|[int](/API_docs/types/int.md) | Yes|New quantity of actions in a message box|
|pts\_count|[int](/API_docs/types/int.md) | Yes|Number of generated events|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateNewMessage = ['_' => 'updateNewMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  

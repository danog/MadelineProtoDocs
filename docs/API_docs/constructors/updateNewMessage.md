---
title: "updateNewMessage"
description: "New message in a private chat or in a basic group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](/API_docs/constructors/index.html)



New message in a private chat or in a [basic group](https://core.telegram.org/api/channel#basic-groups).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|Message|
|pts|[int](/API_docs/types/int.html) | Yes|New quantity of actions in a message box|
|pts\_count|[int](/API_docs/types/int.html) | Yes|Number of generated events|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewMessage = ['_' => 'updateNewMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  

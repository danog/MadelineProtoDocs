---
title: "updateServiceNotification"
description: "A service message for the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateServiceNotification  
[Back to constructors index](/API_docs/constructors/index.html)



A service message for the user.

The app must show the message to the user upon receiving this update. In case the **popup** parameter was passed, the text message must be displayed in a popup alert immediately upon receipt. It is recommended to handle the text as you would an ordinary message in terms of highlighting links, etc. The message must also be stored locally as part of the message history with the user id `777000` (Telegram Notifications).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|popup|[Bool](/API_docs/types/Bool.html) | Optional|(boolTrue) if the message must be displayed in a popup.|
|inbox\_date|[int](/API_docs/types/int.html) | Optional|When was the notification received<br>The message must also be stored locally as part of the message history with the user id `777000` (Telegram Notifications).|
|type|[string](/API_docs/types/string.html) | Yes|String, identical in format and contents to the [**type**](https://core.telegram.org/api/errors#error-type) field in API errors. Describes type of service message. It is acceptable to ignore repeated messages of the same **type** within a short period of time (15 minutes).|
|message|[string](/API_docs/types/string.html) | Yes|Message text|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|Media content (optional)|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateServiceNotification = ['_' => 'updateServiceNotification', 'popup' => Bool, 'inbox_date' => int, 'type' => 'string', 'message' => 'string', 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  

---
title: updateServiceNotification
description: A service message for the user.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateServiceNotification  
[Back to constructors index](index.md)



A service message for the user.

The app must show the message to the user upon receiving this update. In case the **popup** parameter was passed, the text message must be displayed in a popup alert immediately upon receipt. It is recommended to handle the text as you would an ordinary message in terms of highlighting links, etc. The message must also be stored locally as part of the message history with the user id `777000` (Telegram Notifications).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|String, identical in format and contents to the [**type**](https://core.telegram.org/api/errors#error-type) field in API errors. Describes type of service message. It is acceptable to ignore repeated messages of the same **type** within a short period of time (15 minutes).|
|message|[string](../types/string.md) | Yes|Message text|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media content (optional)|
|popup|[Bool](../types/Bool.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateServiceNotification = ['_' => 'updateServiceNotification', 'type' => 'string', 'message' => 'string', 'media' => MessageMedia, 'popup' => Bool];
```  


Or, if you're into Lua:

```lua
updateServiceNotification={_='updateServiceNotification', type='string', message='string', media=MessageMedia, popup=Bool}

```



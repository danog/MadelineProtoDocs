---
title: updateServiceNotification
description: Update service notification
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateServiceNotification  
[Back to constructors index](index.md)



Update service notification

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|popup|[Bool](../types/Bool.md) | Optional|Popup?|
|inbox\_date|[int](../types/int.md) | Optional|Inbox date|
|type|[string](../types/string.md) | Yes|Type|
|message|[string](../types/string.md) | Yes|Message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateServiceNotification = ['_' => 'updateServiceNotification', 'popup' => Bool, 'inbox_date' => int, 'type' => 'string', 'message' => 'string', 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
updateServiceNotification={_='updateServiceNotification', popup=Bool, inbox_date=int, type='string', message='string', media=MessageMedia, entities={MessageEntity}}

```



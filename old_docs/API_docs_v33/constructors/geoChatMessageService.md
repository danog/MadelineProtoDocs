---
title: geoChatMessageService
description: Geo chat message service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoChatMessageService  
[Back to constructors index](index.md)



Geo chat message service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Yes|From ID|
|date|[int](../types/int.md) | Yes|Date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Action|



### Type: [GeoChatMessage](../types/GeoChatMessage.md)


### Example:

```php
$geoChatMessageService = ['_' => 'geoChatMessageService', 'chat_id' => int, 'id' => int, 'from_id' => int, 'date' => int, 'action' => MessageAction];
```  


Or, if you're into Lua:

```lua
geoChatMessageService={_='geoChatMessageService', chat_id=int, id=int, from_id=int, date=int, action=MessageAction}

```



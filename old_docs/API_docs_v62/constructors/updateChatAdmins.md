---
title: updateChatAdmins
description: updateChatAdmins attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatAdmins  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|enabled|[Bool](../types/Bool.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatAdmins = ['_' => 'updateChatAdmins', 'chat_id' => int, 'enabled' => Bool, 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatAdmins", "chat_id": int, "enabled": Bool, "version": int}
```


Or, if you're into Lua:

```lua
updateChatAdmins={_='updateChatAdmins', chat_id=int, enabled=Bool, version=int}

```



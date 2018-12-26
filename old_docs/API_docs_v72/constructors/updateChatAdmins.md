---
title: updateChatAdmins
description: Update chat admins
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatAdmins  
[Back to constructors index](index.md)



Update chat admins

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|enabled|[Bool](../types/Bool.md) | Yes|Enabled?|
|version|[int](../types/int.md) | Yes|Version|



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



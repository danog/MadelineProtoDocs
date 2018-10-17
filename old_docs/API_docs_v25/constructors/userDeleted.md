---
title: userDeleted
description: userDeleted attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userDeleted  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|first\_name|[string](../types/string.md) | Yes|
|last\_name|[string](../types/string.md) | Yes|
|username|[string](../types/string.md) | Yes|



### Type: [User](../types/User.md)


### Example:

```php
$userDeleted = ['_' => 'userDeleted', 'id' => int, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userDeleted", "id": int, "first_name": "string", "last_name": "string", "username": "string"}
```


Or, if you're into Lua:

```lua
userDeleted={_='userDeleted', id=int, first_name='string', last_name='string', username='string'}

```



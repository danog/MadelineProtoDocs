---
title: userDeleted
description: User deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userDeleted  
[Back to constructors index](index.md)



User deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|username|[string](../types/string.md) | Yes|Username|



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



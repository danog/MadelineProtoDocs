---
title: help.userInfo
description: User info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.userInfo  
[Back to constructors index](index.md)



User info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|
|author|[string](../types/string.md) | Yes|Author|
|date|[int](../types/int.md) | Yes|Date|



### Type: [help\_UserInfo](../types/help_UserInfo.md)


### Example:

```php
$help_userInfo = ['_' => 'help.userInfo', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'author' => 'string', 'date' => int];
```  


Or, if you're into Lua:

```lua
help_userInfo={_='help.userInfo', message='string', entities={MessageEntity}, author='string', date=int}

```



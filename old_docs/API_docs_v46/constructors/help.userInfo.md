---
title: help.userInfo
description: Internal use
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_userInfo.html
---
# Constructor: help.userInfo  
[Back to constructors index](index.md)



Internal use

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Info|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|author|[string](../types/string.md) | Yes|Author|
|date|[int](../types/int.md) | Yes|Date|



### Type: [help.UserInfo](../types/help.UserInfo.md)


### Example:

```php
$help_userInfo = ['_' => 'help.userInfo', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'author' => 'string', 'date' => int];
```  


Or, if you're into Lua:

```lua
help_userInfo={_='help.userInfo', message='string', entities={MessageEntity}, author='string', date=int}

```



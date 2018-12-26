---
title: userStatusOffline
description: User status offline
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStatusOffline  
[Back to constructors index](index.md)



User status offline

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|was\_online|[int](../types/int.md) | Yes|Was online|



### Type: [UserStatus](../types/UserStatus.md)


### Example:

```php
$userStatusOffline = ['_' => 'userStatusOffline', 'was_online' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userStatusOffline", "was_online": int}
```


Or, if you're into Lua:

```lua
userStatusOffline={_='userStatusOffline', was_online=int}

```



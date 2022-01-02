---
title: "userStatusOffline"
description: "The user's offline status."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStatusOffline  
[Back to constructors index](index.md)



The user's offline status.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|was\_online|[int](../types/int.md) | Yes|Time the user was last seen online|



### Type: [UserStatus](../types/UserStatus.md)


### Example:

```php
$userStatusOffline = ['_' => 'userStatusOffline', 'was_online' => int];
```  


Or, if you're into Lua:

```lua
userStatusOffline={_='userStatusOffline', was_online=int}

```



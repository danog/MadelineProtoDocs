---
title: userStatusOffline
description: User is offline
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStatusOffline  
[Back to constructors index](index.md)



User is offline

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|was\_online|[int](../types/int.md) | Yes|Unix time user was online last time|



### Type: [UserStatus](../types/UserStatus.md)


### Example:

```
$userStatusOffline = ['_' => 'userStatusOffline', 'was_online' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userStatusOffline", "was_online": int}
```


Or, if you're into Lua:  


```
userStatusOffline={_='userStatusOffline', was_online=int}

```



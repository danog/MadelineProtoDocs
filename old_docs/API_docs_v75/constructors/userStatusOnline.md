---
title: userStatusOnline
description: userStatusOnline attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStatusOnline  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expires|[int](../types/int.md) | Yes|



### Type: [UserStatus](../types/UserStatus.md)


### Example:

```
$userStatusOnline = ['_' => 'userStatusOnline', 'expires' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userStatusOnline", "expires": int}
```


Or, if you're into Lua:  


```
userStatusOnline={_='userStatusOnline', expires=int}

```



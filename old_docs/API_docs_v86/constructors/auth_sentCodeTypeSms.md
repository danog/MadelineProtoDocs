---
title: auth.sentCodeTypeSms
description: Sent code type sms
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCodeTypeSms  
[Back to constructors index](index.md)



Sent code type sms

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](../types/int.md) | Yes|Length|



### Type: [auth\_SentCodeType](../types/auth_SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeSms = ['_' => 'auth.sentCodeTypeSms', 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.sentCodeTypeSms", "length": int}
```


Or, if you're into Lua:

```lua
auth_sentCodeTypeSms={_='auth.sentCodeTypeSms', length=int}

```



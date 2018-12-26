---
title: auth.sentCodeTypeApp
description: Sent code type app
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCodeTypeApp  
[Back to constructors index](index.md)



Sent code type app

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](../types/int.md) | Yes|Length|



### Type: [auth\_SentCodeType](../types/auth_SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeApp = ['_' => 'auth.sentCodeTypeApp', 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.sentCodeTypeApp", "length": int}
```


Or, if you're into Lua:

```lua
auth_sentCodeTypeApp={_='auth.sentCodeTypeApp', length=int}

```



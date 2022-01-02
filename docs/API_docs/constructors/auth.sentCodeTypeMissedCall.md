---
title: "auth.sentCodeTypeMissedCall"
description: "auth.sentCodeTypeMissedCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeMissedCall.html
---
# Constructor: auth.sentCodeTypeMissedCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prefix|[string](../types/string.md) | Yes|
|length|[int](../types/int.md) | Yes|



### Type: [auth.SentCodeType](../types/auth.SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeMissedCall = ['_' => 'auth.sentCodeTypeMissedCall', 'prefix' => 'string', 'length' => int];
```  


Or, if you're into Lua:

```lua
auth_sentCodeTypeMissedCall={_='auth.sentCodeTypeMissedCall', prefix='string', length=int}

```



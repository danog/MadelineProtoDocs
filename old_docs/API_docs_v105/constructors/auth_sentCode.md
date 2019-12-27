---
title: auth.sentCode
description: Contains info about a sent verification code.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCode  
[Back to constructors index](index.md)



Contains info about a sent verification code.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[auth\_SentCodeType](../types/auth_SentCodeType.md) | Yes|Phone code type|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash, to be stored and later re-used with [auth.signIn](../methods/auth.signIn.md)|
|next\_type|[auth\_CodeType](../types/auth_CodeType.md) | Optional|Phone code type that will be sent next, if the phone code is not received within `timeout` seconds: to send it use [auth.resendCode](../methods/auth.resendCode.md)|
|timeout|[int](../types/int.md) | Optional|Timeout for reception of the phone code|



### Type: [auth\_SentCode](../types/auth_SentCode.md)


### Example:

```php
$auth_sentCode = ['_' => 'auth.sentCode', 'type' => auth_SentCodeType, 'phone_code_hash' => 'string', 'next_type' => auth_CodeType, 'timeout' => int];
```  


Or, if you're into Lua:

```lua
auth_sentCode={_='auth.sentCode', type=auth_SentCodeType, phone_code_hash='string', next_type=auth_CodeType, timeout=int}

```


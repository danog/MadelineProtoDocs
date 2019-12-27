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
|phone\_registered|[Bool](../types/Bool.md) | Optional|Phone registered?|
|type|[auth.SentCodeType](../constructors/auth.SentCodeType.md) | Yes|Phone code type|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash, to be stored and later re-used with [auth.signIn](../methods/auth.signIn.md)|
|next\_type|[auth.CodeType](../constructors/auth.CodeType.md) | Optional|Phone code type that will be sent next, if the phone code is not received within `timeout` seconds: to send it use [auth.resendCode](../methods/auth.resendCode.md)|
|timeout|[int](../types/int.md) | Optional|Timeout for reception of the phone code|
|terms\_of\_service|[help.TermsOfService](../constructors/help.TermsOfService.md) | Optional|Terms of service|



### Type: [auth.SentCode](../types/auth.SentCode.md)


### Example:

```php
$auth.sentCode = ['_' => 'auth.sentCode', 'phone_registered' => Bool, 'type' => auth.SentCodeType, 'phone_code_hash' => 'string', 'next_type' => auth.CodeType, 'timeout' => int, 'terms_of_service' => help.TermsOfService];
```  


Or, if you're into Lua:

```lua
auth.sentCode={_='auth.sentCode', phone_registered=Bool, type=auth.SentCodeType, phone_code_hash='string', next_type=auth.CodeType, timeout=int, terms_of_service=help.TermsOfService}

```



---
title: auth.sentCode
description: Contains info about a sent verification code.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCode.html
---
# Constructor: auth.sentCode  
[Back to constructors index](index.md)



Contains info about a sent verification code.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_registered|[Bool](../types/Bool.md) | Yes|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash, to be stored and later re-used with [auth.signIn](../methods/auth.signIn.md)|
|send\_call\_timeout|[int](../types/int.md) | Yes|
|is\_password|[Bool](../types/Bool.md) | Yes|



### Type: [auth.SentCode](../types/auth.SentCode.md)


### Example:

```php
$auth.sentCode = ['_' => 'auth.sentCode', 'phone_registered' => Bool, 'phone_code_hash' => 'string', 'send_call_timeout' => int, 'is_password' => Bool];
```  


Or, if you're into Lua:

```lua
auth.sentCode={_='auth.sentCode', phone_registered=Bool, phone_code_hash='string', send_call_timeout=int, is_password=Bool}

```



---
title: auth.sentAppCode
description: Sent app code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentAppCode  
[Back to constructors index](index.md)



Sent app code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_registered|[Bool](../types/Bool.md) | Yes|Phone registered?|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash|
|send\_call\_timeout|[int](../types/int.md) | Yes|Send call timeout|
|is\_password|[Bool](../types/Bool.md) | Yes|Is password?|



### Type: [auth.SentCode](../types/auth.SentCode.md)


### Example:

```php
$auth.sentAppCode = ['_' => 'auth.sentAppCode', 'phone_registered' => Bool, 'phone_code_hash' => 'string', 'send_call_timeout' => int, 'is_password' => Bool];
```  


Or, if you're into Lua:

```lua
auth.sentAppCode={_='auth.sentAppCode', phone_registered=Bool, phone_code_hash='string', send_call_timeout=int, is_password=Bool}

```



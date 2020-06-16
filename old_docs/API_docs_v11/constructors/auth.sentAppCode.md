---
title: auth.sentAppCode
description: auth.sentAppCode attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentAppCode.html
---
# Constructor: auth.sentAppCode  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_registered|[Bool](../types/Bool.md) | Yes|
|phone\_code\_hash|[string](../types/string.md) | Yes|
|send\_call\_timeout|[int](../types/int.md) | Yes|
|is\_password|[Bool](../types/Bool.md) | Yes|



### Type: [auth.SentCode](../types/auth.SentCode.md)


### Example:

```php
$auth.sentAppCode = ['_' => 'auth.sentAppCode', 'phone_registered' => Bool, 'phone_code_hash' => 'string', 'send_call_timeout' => int, 'is_password' => Bool];
```  


Or, if you're into Lua:

```lua
auth.sentAppCode={_='auth.sentAppCode', phone_registered=Bool, phone_code_hash='string', send_call_timeout=int, is_password=Bool}

```



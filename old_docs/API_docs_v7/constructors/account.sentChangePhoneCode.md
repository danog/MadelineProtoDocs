---
title: account.sentChangePhoneCode
description: account.sentChangePhoneCode attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_sentChangePhoneCode.html
---
# Constructor: account.sentChangePhoneCode  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_code\_hash|[string](../types/string.md) | Yes|
|send\_call\_timeout|[int](../types/int.md) | Yes|



### Type: [account.SentChangePhoneCode](../types/account.SentChangePhoneCode.md)


### Example:

```php
$account_sentChangePhoneCode = ['_' => 'account.sentChangePhoneCode', 'phone_code_hash' => 'string', 'send_call_timeout' => int];
```  


Or, if you're into Lua:

```lua
account_sentChangePhoneCode={_='account.sentChangePhoneCode', phone_code_hash='string', send_call_timeout=int}

```



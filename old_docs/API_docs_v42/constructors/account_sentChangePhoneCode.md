---
title: account.sentChangePhoneCode
description: Sent change phone code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.sentChangePhoneCode  
[Back to constructors index](index.md)



Sent change phone code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash|
|send\_call\_timeout|[int](../types/int.md) | Yes|Send call timeout|



### Type: [account\_SentChangePhoneCode](../types/account_SentChangePhoneCode.md)


### Example:

```php
$account_sentChangePhoneCode = ['_' => 'account.sentChangePhoneCode', 'phone_code_hash' => 'string', 'send_call_timeout' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.sentChangePhoneCode", "phone_code_hash": "string", "send_call_timeout": int}
```


Or, if you're into Lua:

```lua
account_sentChangePhoneCode={_='account.sentChangePhoneCode', phone_code_hash='string', send_call_timeout=int}

```



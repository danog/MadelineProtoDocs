---
title: account.sentChangePhoneCode
description: Sent change phone code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_sentChangePhoneCode.html
---
# Constructor: account.sentChangePhoneCode  
[Back to constructors index](index.md)



Sent change phone code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash|
|send\_call\_timeout|[int](../types/int.md) | Yes|Send call timeout|



### Type: [account.SentChangePhoneCode](../types/account.SentChangePhoneCode.md)


### Example:

```php
$account.sentChangePhoneCode = ['_' => 'account.sentChangePhoneCode', 'phone_code_hash' => 'string', 'send_call_timeout' => int];
```  


Or, if you're into Lua:

```lua
account.sentChangePhoneCode={_='account.sentChangePhoneCode', phone_code_hash='string', send_call_timeout=int}

```



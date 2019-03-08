---
title: account.sentEmailCode
description: Sent email code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.sentEmailCode  
[Back to constructors index](index.md)



Sent email code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](../types/string.md) | Yes|Email pattern|
|length|[int](../types/int.md) | Yes|Length|



### Type: [account\_SentEmailCode](../types/account_SentEmailCode.md)


### Example:

```php
$account_sentEmailCode = ['_' => 'account.sentEmailCode', 'email_pattern' => 'string', 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.sentEmailCode", "email_pattern": "string", "length": int}
```


Or, if you're into Lua:

```lua
account_sentEmailCode={_='account.sentEmailCode', email_pattern='string', length=int}

```



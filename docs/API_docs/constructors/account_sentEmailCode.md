---
title: account.sentEmailCode
description: account_sentEmailCode attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.sentEmailCode  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|email\_pattern|[string](../types/string.md) | Yes|
|length|[int](../types/int.md) | Yes|



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



---
title: auth.sentCode
description: Sent code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCode  
[Back to constructors index](index.md)



Sent code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[auth\_SentCodeType](../types/auth_SentCodeType.md) | Yes|Type|
|phone\_code\_hash|[string](../types/string.md) | Yes|Phone code hash|
|next\_type|[auth\_CodeType](../types/auth_CodeType.md) | Optional|Next type|
|timeout|[int](../types/int.md) | Optional|Timeout|



### Type: [auth\_SentCode](../types/auth_SentCode.md)


### Example:

```php
$auth_sentCode = ['_' => 'auth.sentCode', 'type' => auth_SentCodeType, 'phone_code_hash' => 'string', 'next_type' => auth_CodeType, 'timeout' => int];
```  


Or, if you're into Lua:

```lua
auth_sentCode={_='auth.sentCode', type=auth_SentCodeType, phone_code_hash='string', next_type=auth_CodeType, timeout=int}

```



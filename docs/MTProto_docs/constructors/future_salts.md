---
title: future_salts
description: Future salts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: future\_salts  
[Back to constructors index](index.md)



Future salts

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|req\_msg\_id|[long](../types/long.md) | Yes|Req msg ID|
|now|[int](../types/int.md) | Yes|Now|
|salts|Array of [future\_salt](../constructors/future_salt.md) | Yes|Salts|



### Type: [FutureSalts](../types/FutureSalts.md)


### Example:

```php
$future_salts = ['_' => 'future_salts', 'req_msg_id' => long, 'now' => int, 'salts' => [future_salt, future_salt]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "future_salts", "req_msg_id": long, "now": int, "salts": [future_salt]}
```


Or, if you're into Lua:

```lua
future_salts={_='future_salts', req_msg_id=long, now=int, salts={future_salt}}

```



---
title: "future_salts"
description: "future_salts attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: future\_salts  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|req\_msg\_id|[long](../types/long.md) | Yes|
|now|[int](../types/int.md) | Yes|
|salts|Array of [future\_salt](../constructors/future_salt.md) | Yes|



### Type: [FutureSalts](../types/FutureSalts.md)


### Example:

```php
$future_salts = ['_' => 'future_salts', 'req_msg_id' => long, 'now' => int, 'salts' => [future_salt, future_salt]];
```  


Or, if you're into Lua:

```lua
future_salts={_='future_salts', req_msg_id=long, now=int, salts={future_salt}}

```



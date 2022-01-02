---
title: "messages.dhConfig"
description: "New set of configuring parameters."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dhConfig.html
---
# Constructor: messages.dhConfig  
[Back to constructors index](index.md)



New set of configuring parameters.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|g|[int](../types/int.md) | Yes|New value **prime**, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|
|p|[bytes](../types/bytes.md) | Yes|New value **primitive root**, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|
|version|[int](../types/int.md) | Yes|Vestion of set of parameters|
|random|[bytes](../types/bytes.md) | Yes|Random sequence of bytes of assigned length|



### Type: [messages.DhConfig](../types/messages.DhConfig.md)


### Example:

```php
$messages_dhConfig = ['_' => 'messages.dhConfig', 'g' => int, 'p' => 'bytes', 'version' => int, 'random' => 'bytes'];
```  


Or, if you're into Lua:

```lua
messages_dhConfig={_='messages.dhConfig', g=int, p='bytes', version=int, random='bytes'}

```



---
title: messages.dhConfig
description: Dh config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.dhConfig  
[Back to constructors index](index.md)



Dh config

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|g|[int](../types/int.md) | Yes|G|
|p|[bytes](../types/bytes.md) | Yes|P|
|version|[int](../types/int.md) | Yes|Version|
|random|[bytes](../types/bytes.md) | Yes|Random|



### Type: [messages\_DhConfig](../types/messages_DhConfig.md)


### Example:

```php
$messages_dhConfig = ['_' => 'messages.dhConfig', 'g' => int, 'p' => 'bytes', 'version' => int, 'random' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.dhConfig", "g": int, "p": {"_": "bytes", "bytes":"base64 encoded bytes"}, "version": int, "random": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
messages_dhConfig={_='messages.dhConfig', g=int, p='bytes', version=int, random='bytes'}

```



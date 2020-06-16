---
title: inputClientProxy
description: Info about an [MTProxy](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation) used to connect.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputClientProxy  
[Back to constructors index](index.md)



Info about an [MTProxy](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation) used to connect.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|address|[string](../types/string.md) | Yes|Proxy address|
|port|[int](../types/int.md) | Yes|Proxy port|



### Type: [InputClientProxy](../types/InputClientProxy.md)


### Example:

```php
$inputClientProxy = ['_' => 'inputClientProxy', 'address' => 'string', 'port' => int];
```  


Or, if you're into Lua:

```lua
inputClientProxy={_='inputClientProxy', address='string', port=int}

```



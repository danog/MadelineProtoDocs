---
title: inputClientProxy
description: Client proxy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputClientProxy  
[Back to constructors index](index.md)



Client proxy

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|address|[string](../types/string.md) | Yes|Address|
|port|[int](../types/int.md) | Yes|Port|



### Type: [InputClientProxy](../types/InputClientProxy.md)


### Example:

```php
$inputClientProxy = ['_' => 'inputClientProxy', 'address' => 'string', 'port' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputClientProxy", "address": "string", "port": int}
```


Or, if you're into Lua:

```lua
inputClientProxy={_='inputClientProxy', address='string', port=int}

```



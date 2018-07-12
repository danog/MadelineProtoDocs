---
title: inputClientProxy
description: inputClientProxy attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputClientProxy  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|address|[string](../types/string.md) | Yes|
|port|[int](../types/int.md) | Yes|



### Type: [InputClientProxy](../types/InputClientProxy.md)


### Example:

```
$inputClientProxy = ['_' => 'inputClientProxy', 'address' => 'string', 'port' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputClientProxy", "address": "string", "port": int}
```


Or, if you're into Lua:  


```
inputClientProxy={_='inputClientProxy', address='string', port=int}

```



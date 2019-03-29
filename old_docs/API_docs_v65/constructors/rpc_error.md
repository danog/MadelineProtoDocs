---
title: rpc_error
description: Rpc error
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: rpc\_error  
[Back to constructors index](index.md)



Rpc error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|error\_code|[int](../types/int.md) | Yes|Error code|
|error\_message|[string](../types/string.md) | Yes|Error message|



### Type: [RpcError](../types/RpcError.md)


### Example:

```php
$rpc_error = ['_' => 'rpc_error', 'error_code' => int, 'error_message' => 'string'];
```  


Or, if you're into Lua:

```lua
rpc_error={_='rpc_error', error_code=int, error_message='string'}

```



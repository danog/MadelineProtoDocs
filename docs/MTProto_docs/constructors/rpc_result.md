---
title: rpc_result
description: Rpc result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: rpc\_result  
[Back to constructors index](index.md)



Rpc result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|req\_msg\_id|[long](../types/long.md) | Yes|Req msg ID|
|result|[Object](../types/Object.md) | Yes|Result|



### Type: [RpcResult](../types/RpcResult.md)


### Example:

```php
$rpc_result = ['_' => 'rpc_result', 'req_msg_id' => long, 'result' => Object];
```  


Or, if you're into Lua:

```lua
rpc_result={_='rpc_result', req_msg_id=long, result=Object}

```



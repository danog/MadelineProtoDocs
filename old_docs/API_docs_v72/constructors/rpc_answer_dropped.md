---
title: rpc_answer_dropped
description: Rpc answer dropped
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: rpc\_answer\_dropped  
[Back to constructors index](index.md)



Rpc answer dropped

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[long](../types/long.md) | Yes|Msg ID|
|seq\_no|[int](../types/int.md) | Yes|Seq no|
|bytes|[int](../types/int.md) | Yes|Bytes|



### Type: [RpcDropAnswer](../types/RpcDropAnswer.md)


### Example:

```php
$rpc_answer_dropped = ['_' => 'rpc_answer_dropped', 'msg_id' => long, 'seq_no' => int, 'bytes' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "rpc_answer_dropped", "msg_id": long, "seq_no": int, "bytes": int}
```


Or, if you're into Lua:

```lua
rpc_answer_dropped={_='rpc_answer_dropped', msg_id=long, seq_no=int, bytes=int}

```



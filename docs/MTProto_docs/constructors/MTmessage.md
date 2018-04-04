---
title: MTmessage
description: MTmessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: MTmessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|[long](../types/long.md) | Yes|
|seqno|[int](../types/int.md) | Yes|
|bytes|[int](../types/int.md) | Yes|
|body|[Object](../types/Object.md) | Yes|



### Type: [MTMessage](../types/MTMessage.md)


### Example:

```
$MTmessage = ['_' => 'MTmessage', 'msg_id' => long, 'seqno' => int, 'bytes' => int, 'body' => Object];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "MTmessage", "msg_id": long, "seqno": int, "bytes": int, "body": Object}
```


Or, if you're into Lua:  


```
MTmessage={_='MTmessage', msg_id=long, seqno=int, bytes=int, body=Object}

```



---
title: MTmessage
description: MTProto message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: MTmessage  
[Back to constructors index](index.md)



MTProto message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[long](../types/long.md) | Yes|Message ID|
|seqno|[int](../types/int.md) | Yes|Seqno|
|bytes|[int](../types/int.md) | Yes|Message body|
|body|[Object](../types/Object.md) | Yes|Message body|



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



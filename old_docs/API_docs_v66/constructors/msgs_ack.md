---
title: msgs_ack
description: Msgs ack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msgs\_ack  
[Back to constructors index](index.md)



Msgs ack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_ids|Array of [long](../types/long.md) | Yes|Msg IDs|



### Type: [MsgsAck](../types/MsgsAck.md)


### Example:

```php
$msgs_ack = ['_' => 'msgs_ack', 'msg_ids' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msgs_ack", "msg_ids": [long]}
```


Or, if you're into Lua:

```lua
msgs_ack={_='msgs_ack', msg_ids={long}}

```



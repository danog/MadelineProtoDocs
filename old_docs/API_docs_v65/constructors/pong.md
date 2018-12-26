---
title: pong
description: Pong
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pong  
[Back to constructors index](index.md)



Pong

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[long](../types/long.md) | Yes|Msg ID|
|ping\_id|[long](../types/long.md) | Yes|Ping ID|



### Type: [Pong](../types/Pong.md)


### Example:

```php
$pong = ['_' => 'pong', 'msg_id' => long, 'ping_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pong", "msg_id": long, "ping_id": long}
```


Or, if you're into Lua:

```lua
pong={_='pong', msg_id=long, ping_id=long}

```



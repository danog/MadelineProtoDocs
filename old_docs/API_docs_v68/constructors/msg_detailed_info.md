---
title: msg_detailed_info
description: Msg detailed info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_detailed\_info  
[Back to constructors index](index.md)



Msg detailed info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[long](../types/long.md) | Yes|Msg ID|
|answer\_msg\_id|[long](../types/long.md) | Yes|Answer msg ID|
|bytes|[int](../types/int.md) | Yes|Bytes|
|status|[int](../types/int.md) | Yes|Status|



### Type: [MsgDetailedInfo](../types/MsgDetailedInfo.md)


### Example:

```php
$msg_detailed_info = ['_' => 'msg_detailed_info', 'msg_id' => long, 'answer_msg_id' => long, 'bytes' => int, 'status' => int];
```  


Or, if you're into Lua:

```lua
msg_detailed_info={_='msg_detailed_info', msg_id=long, answer_msg_id=long, bytes=int, status=int}

```



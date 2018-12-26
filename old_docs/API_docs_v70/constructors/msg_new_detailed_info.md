---
title: msg_new_detailed_info
description: Msg new detailed info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_new\_detailed\_info  
[Back to constructors index](index.md)



Msg new detailed info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|answer\_msg\_id|[long](../types/long.md) | Yes|Answer msg ID|
|bytes|[int](../types/int.md) | Yes|Bytes|
|status|[int](../types/int.md) | Yes|Status|



### Type: [MsgDetailedInfo](../types/MsgDetailedInfo.md)


### Example:

```php
$msg_new_detailed_info = ['_' => 'msg_new_detailed_info', 'answer_msg_id' => long, 'bytes' => int, 'status' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msg_new_detailed_info", "answer_msg_id": long, "bytes": int, "status": int}
```


Or, if you're into Lua:

```lua
msg_new_detailed_info={_='msg_new_detailed_info', answer_msg_id=long, bytes=int, status=int}

```



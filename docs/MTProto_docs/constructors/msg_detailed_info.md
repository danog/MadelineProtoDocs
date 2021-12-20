---
title: "msg_detailed_info"
description: "msg_detailed_info attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_detailed\_info  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|[long](../types/long.md) | Yes|
|answer\_msg\_id|[long](../types/long.md) | Yes|
|bytes|[int](../types/int.md) | Yes|
|status|[int](../types/int.md) | Yes|



### Type: [MsgDetailedInfo](../types/MsgDetailedInfo.md)


### Example:

```php
$msg_detailed_info = ['_' => 'msg_detailed_info', 'msg_id' => long, 'answer_msg_id' => long, 'bytes' => int, 'status' => int];
```  


Or, if you're into Lua:

```lua
msg_detailed_info={_='msg_detailed_info', msg_id=long, answer_msg_id=long, bytes=int, status=int}

```



---
title: msgs_state_info
description: Msgs state info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msgs\_state\_info  
[Back to constructors index](index.md)



Msgs state info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|req\_msg\_id|[long](../types/long.md) | Yes|Req msg ID|
|info|[bytes](../types/bytes.md) | Yes|Info|



### Type: [MsgsStateInfo](../types/MsgsStateInfo.md)


### Example:

```php
$msgs_state_info = ['_' => 'msgs_state_info', 'req_msg_id' => long, 'info' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msgs_state_info", "req_msg_id": long, "info": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
msgs_state_info={_='msgs_state_info', req_msg_id=long, info='bytes'}

```



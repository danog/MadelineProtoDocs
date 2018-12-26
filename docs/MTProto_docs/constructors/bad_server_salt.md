---
title: bad_server_salt
description: Bad server salt
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: bad\_server\_salt  
[Back to constructors index](index.md)



Bad server salt

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bad\_msg\_id|[long](../types/long.md) | Yes|Bad msg ID|
|bad\_msg\_seqno|[int](../types/int.md) | Yes|Bad msg seqno|
|error\_code|[int](../types/int.md) | Yes|Error code|
|new\_server\_salt|[long](../types/long.md) | Yes|New server salt|



### Type: [BadMsgNotification](../types/BadMsgNotification.md)


### Example:

```php
$bad_server_salt = ['_' => 'bad_server_salt', 'bad_msg_id' => long, 'bad_msg_seqno' => int, 'error_code' => int, 'new_server_salt' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "bad_server_salt", "bad_msg_id": long, "bad_msg_seqno": int, "error_code": int, "new_server_salt": long}
```


Or, if you're into Lua:

```lua
bad_server_salt={_='bad_server_salt', bad_msg_id=long, bad_msg_seqno=int, error_code=int, new_server_salt=long}

```



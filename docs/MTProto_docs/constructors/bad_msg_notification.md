---
title: "bad_msg_notification"
description: "bad_msg_notification attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: bad\_msg\_notification  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bad\_msg\_id|[long](../types/long.md) | Yes|
|bad\_msg\_seqno|[int](../types/int.md) | Yes|
|error\_code|[int](../types/int.md) | Yes|



### Type: [BadMsgNotification](../types/BadMsgNotification.md)


### Example:

```php
$bad_msg_notification = ['_' => 'bad_msg_notification', 'bad_msg_id' => long, 'bad_msg_seqno' => int, 'error_code' => int];
```  


Or, if you're into Lua:

```lua
bad_msg_notification={_='bad_msg_notification', bad_msg_id=long, bad_msg_seqno=int, error_code=int}

```



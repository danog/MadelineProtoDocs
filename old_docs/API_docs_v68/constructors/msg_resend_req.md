---
title: msg_resend_req
description: Msg resend req
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_resend\_req  
[Back to constructors index](index.md)



Msg resend req

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_ids|Array of [long](../types/long.md) | Yes|Msg IDs|



### Type: [MsgResendReq](../types/MsgResendReq.md)


### Example:

```php
$msg_resend_req = ['_' => 'msg_resend_req', 'msg_ids' => [long, long]];
```  


Or, if you're into Lua:

```lua
msg_resend_req={_='msg_resend_req', msg_ids={long}}

```



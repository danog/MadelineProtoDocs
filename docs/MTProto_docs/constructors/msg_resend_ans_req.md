---
title: "msg_resend_ans_req"
description: "msg_resend_ans_req attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_resend\_ans\_req  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_ids|Array of [long](../types/long.md) | Yes|



### Type: [MsgResendReq](../types/MsgResendReq.md)


### Example:

```php
$msg_resend_ans_req = ['_' => 'msg_resend_ans_req', 'msg_ids' => [long, long]];
```  


Or, if you're into Lua:

```lua
msg_resend_ans_req={_='msg_resend_ans_req', msg_ids={long}}

```



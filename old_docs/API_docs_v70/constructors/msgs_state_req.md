---
title: msgs_state_req
description: msgs_state_req attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msgs\_state\_req  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_ids|Array of [long](../types/long.md) | Yes|



### Type: [MsgsStateReq](../types/MsgsStateReq.md)


### Example:

```php
$msgs_state_req = ['_' => 'msgs_state_req', 'msg_ids' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msgs_state_req", "msg_ids": [long]}
```


Or, if you're into Lua:

```lua
msgs_state_req={_='msgs_state_req', msg_ids={long}}

```



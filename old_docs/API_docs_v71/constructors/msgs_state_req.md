---
title: msgs_state_req
description: Msgs state req
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msgs\_state\_req  
[Back to constructors index](index.md)



Msgs state req

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_ids|Array of [long](../types/long.md) | Yes|Msg IDs|



### Type: [MsgsStateReq](../types/MsgsStateReq.md)


### Example:

```php
$msgs_state_req = ['_' => 'msgs_state_req', 'msg_ids' => [long, long]];
```  


Or, if you're into Lua:

```lua
msgs_state_req={_='msgs_state_req', msg_ids={long}}

```



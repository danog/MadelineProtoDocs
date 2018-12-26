---
title: msgs_all_info
description: Msgs all info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msgs\_all\_info  
[Back to constructors index](index.md)



Msgs all info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_ids|Array of [long](../types/long.md) | Yes|Msg IDs|
|info|[string](../types/string.md) | Yes|Info|



### Type: [MsgsAllInfo](../types/MsgsAllInfo.md)


### Example:

```php
$msgs_all_info = ['_' => 'msgs_all_info', 'msg_ids' => [long, long], 'info' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msgs_all_info", "msg_ids": [long], "info": "string"}
```


Or, if you're into Lua:

```lua
msgs_all_info={_='msgs_all_info', msg_ids={long}, info='string'}

```



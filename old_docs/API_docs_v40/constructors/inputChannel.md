---
title: inputChannel
description: Channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChannel  
[Back to constructors index](index.md)



Channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputChat](../types/InputChat.md)


### Example:

```php
$inputChannel = ['_' => 'inputChannel', 'channel_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputChannel", "channel_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputChannel={_='inputChannel', channel_id=int, access_hash=long}

```



---
title: inputChannel
description: Represents a channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChannel  
[Back to constructors index](index.md)



Represents a channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash taken from the [channel](../constructors/channel.md) constructor|



### Type: [InputChat](../types/InputChat.md)


### Example:

```php
$inputChannel = ['_' => 'inputChannel', 'channel_id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputChannel={_='inputChannel', channel_id=int, access_hash=long}

```



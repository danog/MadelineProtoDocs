---
title: "inputPeerChannel"
description: "Defines a channel for further interaction."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannel  
[Back to constructors index](index.md)



Defines a channel for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** value from the [channel](../constructors/channel.md) constructor|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerChannel = ['_' => 'inputPeerChannel', 'channel_id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputPeerChannel={_='inputPeerChannel', channel_id=long, access_hash=long}

```



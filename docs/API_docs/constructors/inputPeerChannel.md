---
title: "inputPeerChannel"
description: "Defines a channel for further interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannel  
[Back to constructors index](/API_docs/constructors/index.md)



Defines a channel for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.md) | Yes|
|access\_hash|[long](/API_docs/types/long.md) | Yes|**access\_hash** value from the [channel](../constructors/channel.md) constructor|



### Type: [InputPeer](/API_docs/types/InputPeer.md)


### Example:

```php
$inputPeerChannel = ['_' => 'inputPeerChannel', 'channel_id' => long, 'access_hash' => long];
```  

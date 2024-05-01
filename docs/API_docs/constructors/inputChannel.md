---
title: "inputChannel"
description: "Represents a channel"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChannel  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash taken from the [channel](../constructors/channel.html) constructor|



### Type: [InputChannel](/API_docs/types/InputChannel.html)


### Example:

```
$inputChannel = ['_' => 'inputChannel', 'channel_id' => long, 'access_hash' => long];
```  

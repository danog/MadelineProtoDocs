---
title: inputVideo
description: Video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputVideo  
[Back to constructors index](index.md)



Video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputVideo](../types/InputVideo.md)


### Example:

```php
$inputVideo = ['_' => 'inputVideo', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputVideo", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputVideo={_='inputVideo', id=long, access_hash=long}

```



---
title: inputVideo
description: inputVideo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: inputVideo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputVideo](../types/InputVideo.md)


### Example:

```
$inputVideo = ['_' => 'inputVideo', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputVideo", "id": long, "access_hash": long}
```


Or, if you're into Lua:  


```
inputVideo={_='inputVideo', id=long, access_hash=long}

```



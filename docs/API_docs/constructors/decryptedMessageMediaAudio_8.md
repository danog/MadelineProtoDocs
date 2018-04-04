---
title: decryptedMessageMediaAudio
description: decryptedMessageMediaAudio attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: decryptedMessageMediaAudio\_8  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|duration|[int](../types/int.md) | Yes|
|size|[int](../types/int.md) | Yes|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```
$decryptedMessageMediaAudio_8 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaAudio", "duration": int, "size": int}
```


Or, if you're into Lua:  


```
decryptedMessageMediaAudio_8={_='decryptedMessageMediaAudio', duration=int, size=int}

```



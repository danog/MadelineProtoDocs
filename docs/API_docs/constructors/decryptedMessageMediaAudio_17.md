---
title: decryptedMessageMediaAudio
description: Decrypted message media audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaAudio\_17  
[Back to constructors index](index.md)



Decrypted message media audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Yes|Duration|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaAudio_17 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'mime_type' => 'string', 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaAudio", "duration": int, "mime_type": "string", "size": int}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaAudio_17={_='decryptedMessageMediaAudio', duration=int, mime_type='string', size=int}

```



---
title: "decryptedMessageMediaAudio"
description: "Audio file attached to a secret chat message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaAudio\_17  
[Back to constructors index](index.md)



Audio file attached to a secret chat message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Yes|Audio duration in seconds|
|mime\_type|[string](../types/string.md) | Yes|MIME-type of the audio file<br>Parameter added in [Layer 13](https://core.telegram.org/api/layers#layer-13).|
|size|[int](../types/int.md) | Yes|File size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaAudio_17 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'mime_type' => 'string', 'size' => int];
```  

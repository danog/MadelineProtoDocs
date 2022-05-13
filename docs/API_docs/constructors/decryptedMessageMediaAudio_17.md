---
title: "decryptedMessageMediaAudio"
description: "Audio file attached to a secret chat message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaAudio\_17  
[Back to constructors index](/API_docs/constructors/index.html)



Audio file attached to a secret chat message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](/API_docs/types/int.html) | Yes|Audio duration in seconds|
|mime\_type|[string](/API_docs/types/string.html) | Yes|MIME-type of the audio file<br>Parameter added in [Layer 13](https://core.telegram.org/api/layers#layer-13).|
|size|[int](/API_docs/types/int.html) | Yes|File size|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaAudio_17 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'mime_type' => 'string', 'size' => int];
```  

---
title: "decryptedMessageMediaAudio"
description: "Audio file attached to a secret chat message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaAudio\_8  
[Back to constructors index](/API_docs/constructors/index.html)



Audio file attached to a secret chat message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](/API_docs/types/int.html) | Yes|Audio duration in seconds|
|size|[int](/API_docs/types/int.html) | Yes|File size|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaAudio_8 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'size' => int];
```  

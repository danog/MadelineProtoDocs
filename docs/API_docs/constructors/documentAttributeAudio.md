---
title: "documentAttributeAudio"
description: "Represents an audio file"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio  
[Back to constructors index](/API_docs/constructors/index.md)



Represents an audio file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|voice|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a voice message|
|duration|[int](/API_docs/types/int.md) | Optional|Duration in seconds|
|title|[string](/API_docs/types/string.md) | Optional|Name of song|
|performer|[string](/API_docs/types/string.md) | Optional|Performer|
|waveform|[bytes](/API_docs/types/bytes.md) | Optional|Waveform|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio = ['_' => 'documentAttributeAudio', 'voice' => Bool, 'duration' => int, 'title' => 'string', 'performer' => 'string', 'waveform' => 'bytes'];
```  

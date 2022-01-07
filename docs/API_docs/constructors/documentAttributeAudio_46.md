---
title: "documentAttributeAudio"
description: "Represents an audio file"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio\_46  
[Back to constructors index](/API_docs/constructors/index.md)



Represents an audio file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](/API_docs/types/int.md) | Optional|Duration in seconds|
|title|[string](/API_docs/types/string.md) | Yes|Name of song|
|performer|[string](/API_docs/types/string.md) | Yes|Performer|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio_46 = ['_' => 'documentAttributeAudio', 'duration' => int, 'title' => 'string', 'performer' => 'string'];
```  

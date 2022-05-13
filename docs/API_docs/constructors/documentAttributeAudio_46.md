---
title: "documentAttributeAudio"
description: "Represents an audio file"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio\_46  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an audio file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](/API_docs/types/int.html) | Optional|Duration in seconds|
|title|[string](/API_docs/types/string.html) | Yes|Name of song|
|performer|[string](/API_docs/types/string.html) | Yes|Performer|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.html)


### Example:

```
$documentAttributeAudio_46 = ['_' => 'documentAttributeAudio', 'duration' => int, 'title' => 'string', 'performer' => 'string'];
```  

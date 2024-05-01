---
title: "textImage"
description: "Inline image"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textImage  
[Back to constructors index](/API_docs/constructors/index.html)



Inline image

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](/API_docs/types/long.html) | Yes|Document ID|
|w|[int](/API_docs/types/int.html) | Yes|Width|
|h|[int](/API_docs/types/int.html) | Yes|Height|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textImage = ['_' => 'textImage', 'document_id' => long, 'w' => int, 'h' => int];
```  

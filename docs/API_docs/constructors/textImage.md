---
title: "textImage"
description: "Inline image"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textImage  
[Back to constructors index](/API_docs/constructors/index.md)



Inline image

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](/API_docs/types/long.md) | Yes|Document ID|
|w|[int](/API_docs/types/int.md) | Yes|Width|
|h|[int](/API_docs/types/int.md) | Yes|Height|



### Type: [RichText](/API_docs/types/RichText.md)


### Example:

```php
$textImage = ['_' => 'textImage', 'document_id' => long, 'w' => int, 'h' => int];
```  

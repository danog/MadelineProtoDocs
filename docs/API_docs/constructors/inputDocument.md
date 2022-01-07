---
title: "inputDocument"
description: "Defines a video for subsequent interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocument  
[Back to constructors index](/API_docs/constructors/index.md)



Defines a video for subsequent interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|



### Type: [InputDocument](/API_docs/types/InputDocument.md)


### Example:

```php
$inputDocument = ['_' => 'inputDocument', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  

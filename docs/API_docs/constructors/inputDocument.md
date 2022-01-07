---
title: "inputDocument"
description: "Defines a video for subsequent interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocument  
[Back to constructors index](index.md)



Defines a video for subsequent interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|
|file\_reference|[bytes](../types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|



### Type: [InputDocument](../types/InputDocument.md)


### Example:

```php
$inputDocument = ['_' => 'inputDocument', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  

---
title: "inputPhoto"
description: "Defines a photo for further interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



Defines a photo for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Photo identifier|
|access\_hash|[long](/API_docs/types/long.md) | Yes|**access\_hash** value from the [photo](../constructors/photo.md) constructor|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|



### Type: [InputPhoto](/API_docs/types/InputPhoto.md)


### Example:

```php
$inputPhoto = ['_' => 'inputPhoto', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  

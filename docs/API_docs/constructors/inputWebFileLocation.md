---
title: "inputWebFileLocation"
description: "Location of a remote HTTP(s) file"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileLocation  
[Back to constructors index](/API_docs/constructors/index.md)



Location of a remote HTTP(s) file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|HTTP URL of file|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash|



### Type: [InputWebFileLocation](/API_docs/types/InputWebFileLocation.md)


### Example:

```php
$inputWebFileLocation = ['_' => 'inputWebFileLocation', 'url' => 'string', 'access_hash' => long];
```  

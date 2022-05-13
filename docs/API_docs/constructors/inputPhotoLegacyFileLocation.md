---
title: "inputPhotoLegacyFileLocation"
description: "DEPRECATED legacy photo file location"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoLegacyFileLocation  
[Back to constructors index](/API_docs/constructors/index.html)



DEPRECATED legacy photo file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Photo ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|File reference|
|volume\_id|[long](/API_docs/types/long.html) | Yes|Volume ID|
|local\_id|[int](/API_docs/types/int.html) | Yes|Local ID|
|secret|[long](/API_docs/types/long.html) | Yes|Secret|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputPhotoLegacyFileLocation = ['_' => 'inputPhotoLegacyFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  

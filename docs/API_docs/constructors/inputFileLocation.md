---
title: "inputFileLocation"
description: "DEPRECATED location of a photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileLocation  
[Back to constructors index](/API_docs/constructors/index.html)



DEPRECATED location of a photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|volume\_id|[long](/API_docs/types/long.html) | Yes|Server volume|
|local\_id|[int](/API_docs/types/int.html) | Yes|File identifier|
|secret|[long](/API_docs/types/long.html) | Yes|Check sum to access the file|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|[File reference](https://core.telegram.org/api/file_reference)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputFileLocation = ['_' => 'inputFileLocation', 'volume_id' => long, 'local_id' => int, 'secret' => long, 'file_reference' => 'bytes'];
```  

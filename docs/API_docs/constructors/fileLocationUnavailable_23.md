---
title: "fileLocationUnavailable"
description: "File is currently unavailable."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileLocationUnavailable\_23  
[Back to constructors index](/API_docs/constructors/index.html)



File is currently unavailable.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|volume\_id|[long](/API_docs/types/long.html) | Yes|
|local\_id|[int](/API_docs/types/int.html) | Yes|
|secret|[long](/API_docs/types/long.html) | Yes|



### Type: [FileLocation](/API_docs/types/FileLocation.html)


### Example:

```
$fileLocationUnavailable_23 = ['_' => 'fileLocationUnavailable', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  

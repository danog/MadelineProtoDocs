---
title: "inputGroupCallStream"
description: "inputGroupCallStream attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGroupCallStream  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.md) | Yes|
|time\_ms|[long](/API_docs/types/long.md) | Yes|
|scale|[int](/API_docs/types/int.md) | Yes|
|video\_channel|[int](/API_docs/types/int.md) | Optional|
|video\_quality|[int](/API_docs/types/int.md) | Optional|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.md)


### Example:

```php
$inputGroupCallStream = ['_' => 'inputGroupCallStream', 'call' => InputGroupCall, 'time_ms' => long, 'scale' => int, 'video_channel' => int, 'video_quality' => int];
```  

---
title: "inputGroupCallStream"
description: "Chunk of a livestream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGroupCallStream  
[Back to constructors index](/API_docs/constructors/index.html)



Chunk of a livestream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|Livestream info|
|time\_ms|[long](/API_docs/types/long.html) | Yes|Timestamp in milliseconds|
|scale|[int](/API_docs/types/int.html) | Yes|Specifies the duration of the video segment to fetch in milliseconds, by bitshifting `1000` to the right `scale` times: `duration_ms := 1000 >> scale`|
|video\_channel|[int](/API_docs/types/int.html) | Optional|Selected video channel|
|video\_quality|[int](/API_docs/types/int.html) | Optional|Selected video quality (0 = lowest, 1 = medium, 2 = best)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputGroupCallStream = ['_' => 'inputGroupCallStream', 'call' => InputGroupCall, 'time_ms' => long, 'scale' => int, 'video_channel' => int, 'video_quality' => int];
```  

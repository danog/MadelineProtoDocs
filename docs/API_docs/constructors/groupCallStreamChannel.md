---
title: "groupCallStreamChannel"
description: "Info about an RTMP stream in a group call or livestream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallStreamChannel  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an RTMP stream in a group call or livestream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[int](/API_docs/types/int.html) | Yes|Channel ID|
|scale|[int](/API_docs/types/int.html) | Yes|Specifies the duration of the video segment to fetch in milliseconds, by bitshifting `1000` to the right `scale` times: `duration_ms := 1000 >> scale`.|
|last\_timestamp\_ms|[long](/API_docs/types/long.html) | Yes|Last seen timestamp to easily start fetching livestream chunks using [inputGroupCallStream](../constructors/inputGroupCallStream.html)|



### Type: [GroupCallStreamChannel](/API_docs/types/GroupCallStreamChannel.html)


### Example:

```
$groupCallStreamChannel = ['_' => 'groupCallStreamChannel', 'channel' => int, 'scale' => int, 'last_timestamp_ms' => long];
```  

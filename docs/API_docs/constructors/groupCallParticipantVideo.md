---
title: "groupCallParticipantVideo"
description: "Info about a video stream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideo  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a video stream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|paused|[Bool](/API_docs/types/Bool.html) | Optional|Whether the stream is currently paused|
|endpoint|[string](/API_docs/types/string.html) | Yes|Endpoint|
|source\_groups|Array of [GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.html) | Yes|Source groups|
|audio\_source|[int](/API_docs/types/int.html) | Optional|Audio source ID|



### Type: [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html)


### Example:

```
$groupCallParticipantVideo = ['_' => 'groupCallParticipantVideo', 'paused' => Bool, 'endpoint' => 'string', 'source_groups' => [GroupCallParticipantVideoSourceGroup, GroupCallParticipantVideoSourceGroup], 'audio_source' => int];
```  

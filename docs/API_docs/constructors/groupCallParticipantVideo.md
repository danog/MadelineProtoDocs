---
title: "groupCallParticipantVideo"
description: "groupCallParticipantVideo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideo  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|paused|[Bool](/API_docs/types/Bool.md) | Optional|
|endpoint|[string](/API_docs/types/string.md) | Yes|
|source\_groups|Array of [GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.md) | Yes|
|audio\_source|[int](/API_docs/types/int.md) | Optional|



### Type: [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.md)


### Example:

```php
$groupCallParticipantVideo = ['_' => 'groupCallParticipantVideo', 'paused' => Bool, 'endpoint' => 'string', 'source_groups' => [GroupCallParticipantVideoSourceGroup, GroupCallParticipantVideoSourceGroup], 'audio_source' => int];
```  

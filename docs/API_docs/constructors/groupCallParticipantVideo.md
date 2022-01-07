---
title: "groupCallParticipantVideo"
description: "groupCallParticipantVideo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|paused|[Bool](/API_docs/types/Bool.html) | Optional|
|endpoint|[string](/API_docs/types/string.html) | Yes|
|source\_groups|Array of [GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.html) | Yes|
|audio\_source|[int](/API_docs/types/int.html) | Optional|



### Type: [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html)


### Example:

```php
$groupCallParticipantVideo = ['_' => 'groupCallParticipantVideo', 'paused' => Bool, 'endpoint' => 'string', 'source_groups' => [GroupCallParticipantVideoSourceGroup, GroupCallParticipantVideoSourceGroup], 'audio_source' => int];
```  

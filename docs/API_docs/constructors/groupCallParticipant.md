---
title: "groupCallParticipant"
description: "groupCallParticipant attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|muted|[Bool](/API_docs/types/Bool.html) | Optional|
|left|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_self\_unmute|[Bool](/API_docs/types/Bool.html) | Optional|
|just\_joined|[Bool](/API_docs/types/Bool.html) | Optional|
|versioned|[Bool](/API_docs/types/Bool.html) | Optional|
|min|[Bool](/API_docs/types/Bool.html) | Optional|
|muted\_by\_you|[Bool](/API_docs/types/Bool.html) | Optional|
|volume\_by\_admin|[Bool](/API_docs/types/Bool.html) | Optional|
|self|[Bool](/API_docs/types/Bool.html) | Optional|
|video\_joined|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|active\_date|[int](/API_docs/types/int.html) | Optional|
|source|[int](/API_docs/types/int.html) | Yes|
|volume|[int](/API_docs/types/int.html) | Optional|
|about|[string](/API_docs/types/string.html) | Optional|
|raise\_hand\_rating|[long](/API_docs/types/long.html) | Optional|
|video|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html) | Optional|
|presentation|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html) | Optional|



### Type: [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html)


### Example:

```php
$groupCallParticipant = ['_' => 'groupCallParticipant', 'muted' => Bool, 'left' => Bool, 'can_self_unmute' => Bool, 'just_joined' => Bool, 'versioned' => Bool, 'min' => Bool, 'muted_by_you' => Bool, 'volume_by_admin' => Bool, 'self' => Bool, 'video_joined' => Bool, 'peer' => Peer, 'date' => int, 'active_date' => int, 'source' => int, 'volume' => int, 'about' => 'string', 'raise_hand_rating' => long, 'video' => GroupCallParticipantVideo, 'presentation' => GroupCallParticipantVideo];
```  

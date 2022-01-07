---
title: "groupCallParticipant"
description: "groupCallParticipant attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipant  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|muted|[Bool](/API_docs/types/Bool.md) | Optional|
|left|[Bool](/API_docs/types/Bool.md) | Optional|
|can\_self\_unmute|[Bool](/API_docs/types/Bool.md) | Optional|
|just\_joined|[Bool](/API_docs/types/Bool.md) | Optional|
|versioned|[Bool](/API_docs/types/Bool.md) | Optional|
|min|[Bool](/API_docs/types/Bool.md) | Optional|
|muted\_by\_you|[Bool](/API_docs/types/Bool.md) | Optional|
|volume\_by\_admin|[Bool](/API_docs/types/Bool.md) | Optional|
|self|[Bool](/API_docs/types/Bool.md) | Optional|
|video\_joined|[Bool](/API_docs/types/Bool.md) | Optional|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|
|active\_date|[int](/API_docs/types/int.md) | Optional|
|source|[int](/API_docs/types/int.md) | Yes|
|volume|[int](/API_docs/types/int.md) | Optional|
|about|[string](/API_docs/types/string.md) | Optional|
|raise\_hand\_rating|[long](/API_docs/types/long.md) | Optional|
|video|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.md) | Optional|
|presentation|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.md) | Optional|



### Type: [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md)


### Example:

```php
$groupCallParticipant = ['_' => 'groupCallParticipant', 'muted' => Bool, 'left' => Bool, 'can_self_unmute' => Bool, 'just_joined' => Bool, 'versioned' => Bool, 'min' => Bool, 'muted_by_you' => Bool, 'volume_by_admin' => Bool, 'self' => Bool, 'video_joined' => Bool, 'peer' => Peer, 'date' => int, 'active_date' => int, 'source' => int, 'volume' => int, 'about' => 'string', 'raise_hand_rating' => long, 'video' => GroupCallParticipantVideo, 'presentation' => GroupCallParticipantVideo];
```  

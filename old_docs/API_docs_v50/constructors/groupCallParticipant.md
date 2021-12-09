---
title: groupCallParticipant
description: groupCallParticipant attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipant  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|muted|[Bool](../types/Bool.md) | Optional|
|left|[Bool](../types/Bool.md) | Optional|
|can\_self\_unmute|[Bool](../types/Bool.md) | Optional|
|just\_joined|[Bool](../types/Bool.md) | Optional|
|versioned|[Bool](../types/Bool.md) | Optional|
|min|[Bool](../types/Bool.md) | Optional|
|muted\_by\_you|[Bool](../types/Bool.md) | Optional|
|volume\_by\_admin|[Bool](../types/Bool.md) | Optional|
|self|[Bool](../types/Bool.md) | Optional|
|video\_joined|[Bool](../types/Bool.md) | Optional|
|peer|[Peer](../types/Peer.md) | Yes|
|date|[int](../types/int.md) | Yes|
|active\_date|[int](../types/int.md) | Optional|
|source|[int](../types/int.md) | Yes|
|volume|[int](../types/int.md) | Optional|
|about|[string](../types/string.md) | Optional|
|raise\_hand\_rating|[long](../types/long.md) | Optional|
|video|[GroupCallParticipantVideo](../types/GroupCallParticipantVideo.md) | Optional|
|presentation|[GroupCallParticipantVideo](../types/GroupCallParticipantVideo.md) | Optional|



### Type: [GroupCallParticipant](../types/GroupCallParticipant.md)


### Example:

```php
$groupCallParticipant = ['_' => 'groupCallParticipant', 'muted' => Bool, 'left' => Bool, 'can_self_unmute' => Bool, 'just_joined' => Bool, 'versioned' => Bool, 'min' => Bool, 'muted_by_you' => Bool, 'volume_by_admin' => Bool, 'self' => Bool, 'video_joined' => Bool, 'peer' => Peer, 'date' => int, 'active_date' => int, 'source' => int, 'volume' => int, 'about' => 'string', 'raise_hand_rating' => long, 'video' => GroupCallParticipantVideo, 'presentation' => GroupCallParticipantVideo];
```  


Or, if you're into Lua:

```lua
groupCallParticipant={_='groupCallParticipant', muted=Bool, left=Bool, can_self_unmute=Bool, just_joined=Bool, versioned=Bool, min=Bool, muted_by_you=Bool, volume_by_admin=Bool, self=Bool, video_joined=Bool, peer=Peer, date=int, active_date=int, source=int, volume=int, about='string', raise_hand_rating=long, video=GroupCallParticipantVideo, presentation=GroupCallParticipantVideo}

```



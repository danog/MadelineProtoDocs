---
title: "groupCallParticipant"
description: "Info about a group call participant"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a group call participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|muted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the participant is muted|
|left|[Bool](/API_docs/types/Bool.html) | Optional|Whether the participant has left|
|can\_self\_unmute|[Bool](/API_docs/types/Bool.html) | Optional|Whether the participant can unmute themselves|
|just\_joined|[Bool](/API_docs/types/Bool.html) | Optional|Whether the participant has just joined|
|versioned|[Bool](/API_docs/types/Bool.html) | Optional|If set, and [updateGroupCallParticipants](../constructors/updateGroupCallParticipants.html).version &lt; locally stored call.version, info about this participant should be ignored. If (...), and [updateGroupCallParticipants](../constructors/updateGroupCallParticipants.html).version &gt; call.version+1, the participant list should be refetched using [phone.getGroupParticipants](../methods/phone.getGroupParticipants.html).|
|min|[Bool](/API_docs/types/Bool.html) | Optional|If not set, the `volume` and `muted_by_you` fields can be safely used to overwrite locally cached information; otherwise, `volume` will contain valid information only if `volume_by_admin` is set both in the cache and in the received constructor.|
|muted\_by\_you|[Bool](/API_docs/types/Bool.html) | Optional|Whether this participant was muted by the current user|
|volume\_by\_admin|[Bool](/API_docs/types/Bool.html) | Optional|Whether our volume can only changed by an admin|
|self|[Bool](/API_docs/types/Bool.html) | Optional|Whether this participant is the current user|
|video\_joined|[Bool](/API_docs/types/Bool.html) | Optional|Whether this participant is currently broadcasting video|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer information|
|date|[int](/API_docs/types/int.html) | Yes|When did this participant join the group call|
|active\_date|[int](/API_docs/types/int.html) | Optional|When was this participant last active in the group call|
|source|[int](/API_docs/types/int.html) | Yes|Source ID|
|volume|[int](/API_docs/types/int.html) | Optional|Volume, if not set the volume is set to 100%.|
|about|[string](/API_docs/types/string.html) | Optional|Info about this participant|
|raise\_hand\_rating|[long](/API_docs/types/long.html) | Optional|Specifies the UI visualization order of peers with raised hands: peers with a higher rating should be showed first in the list.|
|video|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html) | Optional|Info about the video stream the participant is currently broadcasting|
|presentation|[GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html) | Optional|Info about the screen sharing stream the participant is currently broadcasting|



### Type: [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html)


### Example:

```
$groupCallParticipant = ['_' => 'groupCallParticipant', 'muted' => Bool, 'left' => Bool, 'can_self_unmute' => Bool, 'just_joined' => Bool, 'versioned' => Bool, 'min' => Bool, 'muted_by_you' => Bool, 'volume_by_admin' => Bool, 'self' => Bool, 'video_joined' => Bool, 'peer' => Peer, 'date' => int, 'active_date' => int, 'source' => int, 'volume' => int, 'about' => 'string', 'raise_hand_rating' => long, 'video' => GroupCallParticipantVideo, 'presentation' => GroupCallParticipantVideo];
```  

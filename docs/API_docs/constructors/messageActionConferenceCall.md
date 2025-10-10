---
title: "messageActionConferenceCall"
description: "Represents a conference call (or an invitation to a conference call, if neither the missed nor active flags are set)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionConferenceCall  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [conference call](https://core.telegram.org/api/end-to-end/group-calls) (or an invitation to a conference call, if neither the `missed` nor `active` flags are set).

If [call\_requests\_disabled](https://core.telegram.org/api/config#call-requests-disabled) is not set or false, an incoming [messageActionConferenceCall](../constructors/messageActionConferenceCall.html) with the `missed` and `active` flags **not** set should trigger ringing and an incoming call screen, just like for one-on-one calls.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|missed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the conference call has ended and the user hasn't joined.|
|active|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user is currently in the conference call.|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a video conference call.|
|call\_id|[long](/API_docs/types/long.html) | Yes|Call ID.|
|duration|[int](/API_docs/types/int.html) | Optional|Call duration, for left calls only.|
|other\_participants|Array of [Peer](/API_docs/types/Peer.html) | Optional|Identifiers of some other call participants.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionConferenceCall = ['_' => 'messageActionConferenceCall', 'missed' => Bool, 'active' => Bool, 'video' => Bool, 'call_id' => long, 'duration' => int, 'other_participants' => [Peer, Peer]];
```  

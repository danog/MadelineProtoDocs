---
title: "messageActionConferenceCall"
description: "messageActionConferenceCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionConferenceCall  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|missed|[Bool](/API_docs/types/Bool.html) | Optional|
|active|[Bool](/API_docs/types/Bool.html) | Optional|
|video|[Bool](/API_docs/types/Bool.html) | Optional|
|call\_id|[long](/API_docs/types/long.html) | Yes|
|duration|[int](/API_docs/types/int.html) | Optional|
|other\_participants|Array of [Peer](/API_docs/types/Peer.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionConferenceCall = ['_' => 'messageActionConferenceCall', 'missed' => Bool, 'active' => Bool, 'video' => Bool, 'call_id' => long, 'duration' => int, 'other_participants' => [Peer, Peer]];
```  

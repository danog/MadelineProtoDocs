---
title: "updateTranscribedAudio"
description: "updateTranscribedAudio attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateTranscribedAudio  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|
|text|[string](/API_docs/types/string.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateTranscribedAudio = ['_' => 'updateTranscribedAudio', 'pending' => Bool, 'peer' => Peer, 'msg_id' => int, 'transcription_id' => long, 'text' => 'string'];
```  

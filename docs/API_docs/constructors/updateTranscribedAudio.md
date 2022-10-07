---
title: "updateTranscribedAudio"
description: "A pending voice message transcription » initiated with messages.transcribeAudio was updated."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateTranscribedAudio  
[Back to constructors index](/API_docs/constructors/index.html)



A pending [voice message transcription »](https://core.telegram.org/api/transcribe) initiated with [messages.transcribeAudio](../methods/messages.transcribeAudio.html) was updated.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|Whether this transcription is still pending and further [updateTranscribedAudio](../constructors/updateTranscribedAudio.html) about it will be sent in the future.|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer of the transcribed message|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Transcribed message ID|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|Transcription ID|
|text|[string](/API_docs/types/string.html) | Yes|Transcribed text|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateTranscribedAudio = ['_' => 'updateTranscribedAudio', 'pending' => Bool, 'peer' => Peer, 'msg_id' => int, 'transcription_id' => long, 'text' => 'string'];
```  

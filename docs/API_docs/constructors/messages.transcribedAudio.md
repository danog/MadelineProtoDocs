---
title: "messages.transcribedAudio"
description: "Transcribed text from a voice message »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_transcribedAudio.html
---
# Constructor: messages.transcribedAudio  
[Back to constructors index](/API_docs/constructors/index.html)



[Transcribed text from a voice message »](https://core.telegram.org/api/transcribe)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|Whether the transcription is partial because audio transcription is still in progress, if set the user may receive further [updateTranscribedAudio](../constructors/updateTranscribedAudio.html) updates with the updated transcription.|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|Transcription ID|
|text|[string](/API_docs/types/string.html) | Yes|Transcripted text|
|trial\_remains\_num|[int](/API_docs/types/int.html) | Optional|
|trial\_remains\_until\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [messages.TranscribedAudio](/API_docs/types/messages.TranscribedAudio.html)


### Example:

```
$messages_transcribedAudio = ['_' => 'messages.transcribedAudio', 'pending' => Bool, 'transcription_id' => long, 'text' => 'string', 'trial_remains_num' => int, 'trial_remains_until_date' => int];
```  

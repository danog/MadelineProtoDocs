---
title: "messages.transcribedAudio"
description: "messages.transcribedAudio attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_transcribedAudio.html
---
# Constructor: messages.transcribedAudio  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|
|text|[string](/API_docs/types/string.html) | Yes|



### Type: [messages.TranscribedAudio](/API_docs/types/messages.TranscribedAudio.html)


### Example:

```
$messages_transcribedAudio = ['_' => 'messages.transcribedAudio', 'pending' => Bool, 'transcription_id' => long, 'text' => 'string'];
```  

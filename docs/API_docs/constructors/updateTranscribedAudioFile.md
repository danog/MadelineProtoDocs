---
title: "updateTranscribedAudioFile"
description: "updateTranscribedAudioFile attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateTranscribedAudioFile  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|transcription\_id|[long](/API_docs/types/long.html) | Yes|
|text|[string](/API_docs/types/string.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateTranscribedAudioFile = ['_' => 'updateTranscribedAudioFile', 'pending' => Bool, 'transcription_id' => long, 'text' => 'string'];
```  

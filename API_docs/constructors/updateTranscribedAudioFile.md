# updateTranscribedAudioFile

> updateTranscribedAudioFile attributes, type and example

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

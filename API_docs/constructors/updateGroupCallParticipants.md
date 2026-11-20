# updateGroupCallParticipants

> The participant list of a certain group call has changed

[Back to constructors index](/API_docs/constructors/index.html)



The participant list of a certain group call has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|Group call|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|New participant list|
|version|[int](/API_docs/types/int.html) | Yes|Version|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallParticipants = ['_' => 'updateGroupCallParticipants', 'call' => InputGroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'version' => int];
```

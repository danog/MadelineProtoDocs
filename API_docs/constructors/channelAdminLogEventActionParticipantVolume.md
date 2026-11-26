# channelAdminLogEventActionParticipantVolume

> channelAdminLogEvent.user_id has set the volume of participant.peer to participant.volume

[Back to constructors index](/API_docs/constructors/index.html)



channelAdminLogEvent.user\_id has set the volume of participant.peer to participant.volume

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|The participant whose volume was changed|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantVolume = ['_' => 'channelAdminLogEventActionParticipantVolume', 'participant' => GroupCallParticipant];
```

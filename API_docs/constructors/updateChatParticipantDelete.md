# updateChatParticipantDelete

> A member has left the group.

[Back to constructors index](/API_docs/constructors/index.html)



A member has left the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Group ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user|
|version|[int](/API_docs/types/int.html) | Yes|Used in basic groups to reorder updates and make sure that all of them was received.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChatParticipantDelete = ['_' => 'updateChatParticipantDelete', 'chat_id' => long, 'user_id' => long, 'version' => int];
```

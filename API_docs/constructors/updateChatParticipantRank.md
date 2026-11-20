# updateChatParticipantRank

> updateChatParticipantRank attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|rank|[string](/API_docs/types/string.html) | Yes|
|version|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChatParticipantRank = ['_' => 'updateChatParticipantRank', 'chat_id' => long, 'user_id' => long, 'rank' => 'string', 'version' => int];
```

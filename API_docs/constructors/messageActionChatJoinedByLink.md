# messageActionChatJoinedByLink

> A user joined the chat via an invite link

[Back to constructors index](/API_docs/constructors/index.html)



A user joined the chat via an invite link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inviter\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that created the invite link|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionChatJoinedByLink = ['_' => 'messageActionChatJoinedByLink', 'inviter_id' => long];
```

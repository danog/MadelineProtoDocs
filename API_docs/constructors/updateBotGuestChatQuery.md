# updateBotGuestChatQuery

> updateBotGuestChatQuery attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|message|[Message](/API_docs/types/Message.html) | Optional|
|reference\_messages|Array of [Message](/API_docs/types/Message.html) | Optional|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotGuestChatQuery = ['_' => 'updateBotGuestChatQuery', 'query_id' => long, 'message' => Message, 'reference_messages' => [Message, Message], 'qts' => int];
```

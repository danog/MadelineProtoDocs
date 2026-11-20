# messages.messageViews

> View, forward counter + info about replies

[Back to constructors index](/API_docs/constructors/index.html)



View, forward counter + info about replies

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|Array of [MessageViews](/API_docs/types/MessageViews.html) | Yes|View, forward counter + info about replies|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in constructor|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in constructor|



### Type: [messages.MessageViews](/API_docs/types/messages.MessageViews.html)


### Example:

```
$messages_messageViews = ['_' => 'messages.messageViews', 'views' => [MessageViews, MessageViews], 'chats' => [Chat, Chat], 'users' => [User, User]];
```

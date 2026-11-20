# messages.messages

> Full list of messages with auxiliary data.

[Back to constructors index](/API_docs/constructors/index.html)



Full list of messages with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|List of messages|
|topics|Array of [ForumTopic](/API_docs/types/ForumTopic.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List of chats mentioned in dialogs|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Messages](/API_docs/types/messages.Messages.html)


### Example:

```
$messages_messages = ['_' => 'messages.messages', 'messages' => [Message, Message], 'topics' => [ForumTopic, ForumTopic], 'chats' => [Chat, Chat], 'users' => [User, User]];
```

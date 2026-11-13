# messages.quickReplies

> Info about quick reply shortcuts ».

[Back to constructors index](/API_docs/constructors/index.html)



Info about [quick reply shortcuts »](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|quick\_replies|Array of [QuickReply](/API_docs/types/QuickReply.html) | Yes|Quick reply shortcuts.|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Messages mentioned in `quick_replies`.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.QuickReplies](/API_docs/types/messages.QuickReplies.html)


### Example:

```
$messages_quickReplies = ['_' => 'messages.quickReplies', 'quick_replies' => [QuickReply, QuickReply], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```

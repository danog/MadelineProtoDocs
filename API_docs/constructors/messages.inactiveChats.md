# messages.inactiveChats

> Inactive chat list

[Back to constructors index](/API_docs/constructors/index.html)



Inactive chat list

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dates|Array of [int](/API_docs/types/int.html) | Yes|When was the chat last active|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chat list|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the chat list|



### Type: [messages.InactiveChats](/API_docs/types/messages.InactiveChats.html)


### Example:

```
$messages_inactiveChats = ['_' => 'messages.inactiveChats', 'dates' => [int, int], 'chats' => [Chat, Chat], 'users' => [User, User]];
```

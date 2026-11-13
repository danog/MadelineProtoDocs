# users.userFull

> Full user information

[Back to constructors index](/API_docs/constructors/index.html)



Full user information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_user|[UserFull](/API_docs/types/UserFull.html) | Yes|Full user information|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [users.UserFull](/API_docs/types/users.UserFull.html)


### Example:

```
$users_userFull = ['_' => 'users.userFull', 'full_user' => UserFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```

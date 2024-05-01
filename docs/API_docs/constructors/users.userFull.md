---
title: "users.userFull"
description: "Full user information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_userFull.html
---
# Constructor: users.userFull  
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

---
title: "users.userFull"
description: "users.userFull attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_userFull.html
---
# Constructor: users.userFull  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|full\_user|[UserFull](../types/UserFull.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [users.UserFull](../types/users.UserFull.md)


### Example:

```php
$users_userFull = ['_' => 'users.userFull', 'full_user' => UserFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

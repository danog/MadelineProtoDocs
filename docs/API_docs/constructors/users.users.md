---
title: "users.users"
description: "Describes a list of users (or bots)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_users.html
---
# Constructor: users.users  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a list of users (or bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [users.Users](/API_docs/types/users.Users.html)


### Example:

```
$users_users = ['_' => 'users.users', 'users' => [User, User]];
```  

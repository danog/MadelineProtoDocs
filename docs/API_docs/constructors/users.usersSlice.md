---
title: "users.usersSlice"
description: "users.usersSlice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_usersSlice.html
---
# Constructor: users.usersSlice  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [users.Users](/API_docs/types/users.Users.html)


### Example:

```
$users_usersSlice = ['_' => 'users.usersSlice', 'count' => int, 'users' => [User, User]];
```  

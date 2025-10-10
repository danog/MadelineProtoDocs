---
title: "users.usersSlice"
description: "Describes a partial list of users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_usersSlice.html
---
# Constructor: users.usersSlice  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a partial list of users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of users (bigger than the users specified in `users`)|
|users|Array of [User](/API_docs/types/User.html) | Yes|Subset of users.|



### Type: [users.Users](/API_docs/types/users.Users.html)


### Example:

```
$users_usersSlice = ['_' => 'users.usersSlice', 'count' => int, 'users' => [User, User]];
```  

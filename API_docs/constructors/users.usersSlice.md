# users.usersSlice

> Describes a partial list of users.

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

# updateUserStatus

> Contact status update.

[Back to constructors index](/API_docs/constructors/index.html)



Contact status update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier|
|status|[UserStatus](/API_docs/types/UserStatus.html) | Optional|New status|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUserStatus = ['_' => 'updateUserStatus', 'user_id' => long, 'status' => UserStatus];
```

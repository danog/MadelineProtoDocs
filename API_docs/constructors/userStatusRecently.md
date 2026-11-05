# userStatusRecently

> Online status: last seen recently

[Back to constructors index](/API_docs/constructors/index.html)



Online status: last seen recently

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|by\_me|[Bool](/API_docs/types/Bool.html) | Optional|If set, the exact user status of this user is actually available to us, but to view it we must first purchase a [Premium](https://core.telegram.org/api/premium) subscription, or allow this user to see *our* exact last online status. See [here »](../constructors/privacyKeyStatusTimestamp.html) for more info.|



### Type: [UserStatus](/API_docs/types/UserStatus.html)


### Example:

```
$userStatusRecently = ['_' => 'userStatusRecently', 'by_me' => Bool];
```

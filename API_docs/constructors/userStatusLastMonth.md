# userStatusLastMonth

> Online status: last seen last month

[Back to constructors index](/API_docs/constructors/index.html)



Online status: last seen last month

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|by\_me|[Bool](/API_docs/types/Bool.html) | Optional|If set, the exact user status of this user is actually available to us, but to view it we must first purchase a [Premium](https://core.telegram.org/api/premium) subscription, or allow this user to see *our* exact last online status. See [here »](../constructors/privacyKeyStatusTimestamp.html) for more info.|



### Type: [UserStatus](/API_docs/types/UserStatus.html)


### Example:

```
$userStatusLastMonth = ['_' => 'userStatusLastMonth', 'by_me' => Bool];
```

# account.authorizations

> Logged-in sessions

[Back to constructors index](/API_docs/constructors/index.html)



Logged-in sessions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization\_ttl\_days|[int](/API_docs/types/int.html) | Yes|Time-to-live of session|
|authorizations|Array of [Authorization](/API_docs/types/Authorization.html) | Yes|Logged-in sessions|



### Type: [account.Authorizations](/API_docs/types/account.Authorizations.html)


### Example:

```
$account_authorizations = ['_' => 'account.authorizations', 'authorization_ttl_days' => int, 'authorizations' => [Authorization, Authorization]];
```

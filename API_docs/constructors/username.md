# username

> Contains information about a username.

[Back to constructors index](/API_docs/constructors/index.html)



Contains information about a username.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|editable|[Bool](/API_docs/types/Bool.html) | Optional|Whether the username is editable, meaning it wasn't bought on [fragment](https://fragment.com).|
|active|[Bool](/API_docs/types/Bool.html) | Optional|Whether the username is active.|
|deletable|[Bool](/API_docs/types/Bool.html) | Optional|
|expired|[Bool](/API_docs/types/Bool.html) | Optional|
|username|[string](/API_docs/types/string.html) | Yes|The username.|



### Type: [Username](/API_docs/types/Username.html)


### Example:

```
$username = ['_' => 'username', 'editable' => Bool, 'active' => Bool, 'deletable' => Bool, 'expired' => Bool, 'username' => 'string'];
```

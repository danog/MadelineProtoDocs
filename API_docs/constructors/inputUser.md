# inputUser

> Defines a user for further interaction.

[Back to constructors index](/API_docs/constructors/index.html)



Defines a user for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier|
|access\_hash|[long](/API_docs/types/long.html) | Yes|**access\_hash** value from the [user](../constructors/user.html) constructor|



### Type: [InputUser](/API_docs/types/InputUser.html)


### Example:

```
$inputUser = ['_' => 'inputUser', 'user_id' => long, 'access_hash' => long];
```

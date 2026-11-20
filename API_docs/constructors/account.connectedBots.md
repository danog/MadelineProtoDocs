# account.connectedBots

> Info about currently connected business bots.

[Back to constructors index](/API_docs/constructors/index.html)



Info about currently connected [business bots](https://core.telegram.org/api/bots/connected-business-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|connected\_bots|Array of [ConnectedBot](/API_docs/types/ConnectedBot.html) | Yes|Info about the connected bots|
|users|Array of [User](/API_docs/types/User.html) | Yes|Bot information|



### Type: [account.ConnectedBots](/API_docs/types/account.ConnectedBots.html)


### Example:

```
$account_connectedBots = ['_' => 'account.connectedBots', 'connected_bots' => [ConnectedBot, ConnectedBot], 'users' => [User, User]];
```

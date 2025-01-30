---
title: "account.connectedBots"
description: "Info about currently connected business bots."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_connectedBots.html
---
# Constructor: account.connectedBots  
[Back to constructors index](/API_docs/constructors/index.html)



Info about currently connected [business bots](https://core.telegram.org/api/business#connected-bots).

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

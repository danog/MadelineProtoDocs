---
title: "account.connectedBots"
description: "account.connectedBots attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_connectedBots.html
---
# Constructor: account.connectedBots  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|connected\_bots|Array of [ConnectedBot](/API_docs/types/ConnectedBot.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [account.ConnectedBots](/API_docs/types/account.ConnectedBots.html)


### Example:

```
$account_connectedBots = ['_' => 'account.connectedBots', 'connected_bots' => [ConnectedBot, ConnectedBot], 'users' => [User, User]];
```  

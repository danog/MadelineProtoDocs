---
title: "account.autoSaveSettings"
description: "account.autoSaveSettings attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_autoSaveSettings.html
---
# Constructor: account.autoSaveSettings  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|
|chats\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|
|broadcasts\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|
|exceptions|Array of [AutoSaveException](/API_docs/types/AutoSaveException.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [account.AutoSaveSettings](/API_docs/types/account.AutoSaveSettings.html)


### Example:

```
$account_autoSaveSettings = ['_' => 'account.autoSaveSettings', 'users_settings' => AutoSaveSettings, 'chats_settings' => AutoSaveSettings, 'broadcasts_settings' => AutoSaveSettings, 'exceptions' => [AutoSaveException, AutoSaveException], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

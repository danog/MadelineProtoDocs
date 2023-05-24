---
title: "account.autoSaveSettings"
description: "Contains media autosave settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_autoSaveSettings.html
---
# Constructor: account.autoSaveSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Contains media autosave settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|Default media autosave settings for private chats|
|chats\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|Default media autosave settings for [groups and supergroups](https://core.telegram.org/api/channel)|
|broadcasts\_settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|Default media autosave settings for [channels](https://core.telegram.org/api/channel)|
|exceptions|Array of [AutoSaveException](/API_docs/types/AutoSaveException.html) | Yes|Peer-specific granular autosave settings|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the peer-specific granular autosave settings|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the peer-specific granular autosave settings|



### Type: [account.AutoSaveSettings](/API_docs/types/account.AutoSaveSettings.html)


### Example:

```
$account_autoSaveSettings = ['_' => 'account.autoSaveSettings', 'users_settings' => AutoSaveSettings, 'chats_settings' => AutoSaveSettings, 'broadcasts_settings' => AutoSaveSettings, 'exceptions' => [AutoSaveException, AutoSaveException], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

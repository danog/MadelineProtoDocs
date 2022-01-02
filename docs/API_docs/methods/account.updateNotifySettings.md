---
title: "account.updateNotifySettings"
description: "Edits notification settings from a given user/group, from all users/all groups."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateNotifySettings.html
---
# Method: account.updateNotifySettings
[Back to methods index](index.md)



Edits notification settings from a given user/group, from all users/all groups.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](../types/InputNotifyPeer.md) | Notification source | Yes|
|settings|[InputPeerNotifySettings](../types/InputPeerNotifySettings.md) | Notification settings | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updateNotifySettings(['peer' => InputNotifyPeer, 'settings' => InputPeerNotifySettings, ]);
```

Or, if you're into Lua:

```lua
Bool = account.updateNotifySettings({peer=InputNotifyPeer, settings=InputPeerNotifySettings, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|SETTINGS_INVALID|Invalid settings were provided|



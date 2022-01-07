---
title: "account.getNotifySettings"
description: "Gets current notification settings for a given user/group, from all users/all groups."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getNotifySettings.html
---
# Method: account.getNotifySettings
[Back to methods index](index.md)



Gets current notification settings for a given user/group, from all users/all groups.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](../types/InputNotifyPeer.md) | Notification source | Yes|


### Return type: [PeerNotifySettings](../types/PeerNotifySettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$PeerNotifySettings = $MadelineProto->account->getNotifySettings(['peer' => InputNotifyPeer, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|



---
title: account.getNotifySettings
description: Get notification settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getNotifySettings  
[Back to methods index](index.md)


Get notification settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](../types/InputNotifyPeer.md) | Notification source  | Yes|


### Return type: [PeerNotifySettings](../types/PeerNotifySettings.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$PeerNotifySettings = $MadelineProto->account->getNotifySettings(['peer' => InputNotifyPeer, ]);
```

Or, if you're into Lua:

```lua
PeerNotifySettings = account.getNotifySettings({peer=InputNotifyPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|



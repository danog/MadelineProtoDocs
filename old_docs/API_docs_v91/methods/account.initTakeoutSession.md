---
title: account.initTakeoutSession
description: Intialize account takeout session
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.initTakeoutSession  
[Back to methods index](index.md)


Intialize account takeout session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|contacts|[Bool](../types/Bool.md) | Whether to export contacts | Optional|
|message\_users|[Bool](../types/Bool.md) | Whether to export messages in private chats | Optional|
|message\_chats|[Bool](../types/Bool.md) | Whether to export messages in [legacy groups](https://core.telegram.org/api/channel) | Optional|
|message\_megagroups|[Bool](../types/Bool.md) | Whether to export messages in [supergroups](https://core.telegram.org/api/channel) | Optional|
|message\_channels|[Bool](../types/Bool.md) | Whether to export messages in [channels](https://core.telegram.org/api/channel) | Optional|
|files|[Bool](../types/Bool.md) | Whether to export files | Optional|
|file\_max\_size|[int](../types/int.md) | Maximum size of files to export | Optional|


### Return type: [account.Takeout](../types/account.Takeout.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.Takeout = $MadelineProto->account->initTakeoutSession(['contacts' => Bool, 'message_users' => Bool, 'message_chats' => Bool, 'message_megagroups' => Bool, 'message_channels' => Bool, 'files' => Bool, 'file_max_size' => int, ]);
```

Or, if you're into Lua:

```lua
account.Takeout = account.initTakeoutSession({contacts=Bool, message_users=Bool, message_chats=Bool, message_megagroups=Bool, message_channels=Bool, files=Bool, file_max_size=int, })
```


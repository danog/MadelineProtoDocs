---
title: "account.initTakeoutSession"
description: "Initialize account takeout session"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_initTakeoutSession.html
---
# Method: account.initTakeoutSession
[Back to methods index](index.html)



Initialize account takeout session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|contacts|[Bool](/API_docs/types/Bool.html) | Whether to export contacts | Optional|
|message\_users|[Bool](/API_docs/types/Bool.html) | Whether to export messages in private chats | Optional|
|message\_chats|[Bool](/API_docs/types/Bool.html) | Whether to export messages in [basic groups](https://core.telegram.org/api/channel#basic-groups) | Optional|
|message\_megagroups|[Bool](/API_docs/types/Bool.html) | Whether to export messages in [supergroups](https://core.telegram.org/api/channel#supergroups) | Optional|
|message\_channels|[Bool](/API_docs/types/Bool.html) | Whether to export messages in [channels](https://core.telegram.org/api/channel#channels) | Optional|
|files|[Bool](/API_docs/types/Bool.html) | Whether to export files | Optional|
|file\_max\_size|[long](/API_docs/types/long.html) |  | Optional|


### Return type: [account.Takeout](/API_docs/types/account.Takeout.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$account_Takeout = $MadelineProto->account->initTakeoutSession(contacts: Bool, message_users: Bool, message_chats: Bool, message_megagroups: Bool, message_channels: Bool, files: Bool, file_max_size: long, );
```


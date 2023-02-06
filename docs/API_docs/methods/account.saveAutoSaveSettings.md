---
title: "account.saveAutoSaveSettings"
description: "account.saveAutoSaveSettings parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveAutoSaveSettings.html
---
# Method: account.saveAutoSaveSettings
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users|[Bool](/API_docs/types/Bool.html) | Optional|
|chats|[Bool](/API_docs/types/Bool.html) | Optional|
|broadcasts|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->account->saveAutoSaveSettings(users: Bool, chats: Bool, broadcasts: Bool, peer: InputPeer, settings: AutoSaveSettings, );
```


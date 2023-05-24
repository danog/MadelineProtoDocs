---
title: "account.saveAutoSaveSettings"
description: "Modify autosave settings"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveAutoSaveSettings.html
---
# Method: account.saveAutoSaveSettings
[Back to methods index](index.html)



Modify autosave settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|users|[Bool](/API_docs/types/Bool.html) | Whether the new settings should affect all private chats | Optional|
|chats|[Bool](/API_docs/types/Bool.html) | Whether the new settings should affect all groups | Optional|
|broadcasts|[Bool](/API_docs/types/Bool.html) | Whether the new settings should affect all [channels](https://core.telegram.org/api/channel) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Whether the new settings should affect a specific peer | Optional|
|settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | The new autosave settings | Yes|


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

$Bool = $MadelineProto->account->saveAutoSaveSettings(users: Bool, chats: Bool, broadcasts: Bool, peer: InputPeer, settings: AutoSaveSettings, );
```


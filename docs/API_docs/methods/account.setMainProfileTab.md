---
title: "account.setMainProfileTab"
description: "Changes the main profile tab of the current user, see [here »](https://core.telegram.org/api/profile#tabs) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setMainProfileTab.html
---
# Method: account.setMainProfileTab
[Back to methods index](index.html)



Changes the main profile tab of the current user, see [here »](https://core.telegram.org/api/profile#tabs) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|tab|[ProfileTab](/API_docs/types/ProfileTab.html) | The tab to set as main tab. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->setMainProfileTab(tab: $ProfileTab, );
```


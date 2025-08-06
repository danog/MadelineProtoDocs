---
title: "account.getBusinessChatLinks"
description: "List all created [business chat deep links »](https://core.telegram.org/api/business#business-chat-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getBusinessChatLinks.html
---
# Method: account.getBusinessChatLinks
[Back to methods index](index.html)



List all created [business chat deep links »](https://core.telegram.org/api/business#business-chat-links).



### Return type: [account.BusinessChatLinks](/API_docs/types/account.BusinessChatLinks.html)

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

$account_BusinessChatLinks = $MadelineProto->account->getBusinessChatLinks();
```


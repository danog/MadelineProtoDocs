---
title: "account.createBusinessChatLink"
description: "Create a [business chat deep link »](https://core.telegram.org/api/business#business-chat-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_createBusinessChatLink.html
---
# Method: account.createBusinessChatLink
[Back to methods index](index.html)



Create a [business chat deep link »](https://core.telegram.org/api/business#business-chat-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|link|[InputBusinessChatLink](/API_docs/types/InputBusinessChatLink.html) | Info about the link to create. | Yes|


### Return type: [BusinessChatLink](/API_docs/types/BusinessChatLink.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$BusinessChatLink = $MadelineProto->account->createBusinessChatLink(link: $InputBusinessChatLink, );
```


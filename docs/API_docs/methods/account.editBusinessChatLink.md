---
title: "account.editBusinessChatLink"
description: "Edit a created [business chat deep link »](https://core.telegram.org/api/business#business-chat-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_editBusinessChatLink.html
---
# Method: account.editBusinessChatLink
[Back to methods index](index.html)



Edit a created [business chat deep link »](https://core.telegram.org/api/business#business-chat-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | Slug of the link, obtained as specified [here »](https://core.telegram.org/api/links#business-chat-links). | Optional|
|link|[InputBusinessChatLink](/API_docs/types/InputBusinessChatLink.html) | New link information. | Yes|


### Return type: [BusinessChatLink](/API_docs/types/BusinessChatLink.html)

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

$BusinessChatLink = $MadelineProto->account->editBusinessChatLink(slug: 'string', link: $InputBusinessChatLink, );
```


---
title: "account.resolveBusinessChatLink"
description: "Resolve a [business chat deep link »](https://core.telegram.org/api/business#business-chat-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resolveBusinessChatLink.html
---
# Method: account.resolveBusinessChatLink
[Back to methods index](index.html)



Resolve a [business chat deep link »](https://core.telegram.org/api/business#business-chat-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | Slug of the link, obtained as specified [here »](https://core.telegram.org/api/links#business-chat-links). | Optional|


### Return type: [account.ResolvedBusinessChatLinks](/API_docs/types/account.ResolvedBusinessChatLinks.html)

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

$account_ResolvedBusinessChatLinks = $MadelineProto->account->resolveBusinessChatLink(slug: 'string', );
```


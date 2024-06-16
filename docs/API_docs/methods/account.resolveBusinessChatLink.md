---
title: "account.resolveBusinessChatLink"
description: "account.resolveBusinessChatLink parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resolveBusinessChatLink.html
---
# Method: account.resolveBusinessChatLink
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|slug|[string](/API_docs/types/string.html) | Optional|


### Return type: [account.ResolvedBusinessChatLinks](/API_docs/types/account.ResolvedBusinessChatLinks.html)

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


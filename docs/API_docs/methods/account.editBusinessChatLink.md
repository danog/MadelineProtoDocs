---
title: "account.editBusinessChatLink"
description: "account.editBusinessChatLink parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_editBusinessChatLink.html
---
# Method: account.editBusinessChatLink
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|slug|[string](/API_docs/types/string.html) | Optional|
|link|[InputBusinessChatLink](/API_docs/types/InputBusinessChatLink.html) | Yes|


### Return type: [BusinessChatLink](/API_docs/types/BusinessChatLink.html)

### Can bots use this method: **NO**


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


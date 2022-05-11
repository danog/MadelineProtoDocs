---
title: "help.getDeepLinkInfo"
description: "Get info about a `t.me` link"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getDeepLinkInfo.html
---
# Method: help.getDeepLinkInfo
[Back to methods index](index.html)



Get info about a `t.me` link

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|path|[string](/API_docs/types/string.html) | Path in `t.me/path` | Yes|


### Return type: [help.DeepLinkInfo](/API_docs/types/help.DeepLinkInfo.html)

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
$help_DeepLinkInfo = $MadelineProto->help->getDeepLinkInfo(path: 'string', );
```


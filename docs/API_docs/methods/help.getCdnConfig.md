---
title: "help.getCdnConfig"
description: "Get configuration for [CDN](https://core.telegram.org/cdn) file downloads."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getCdnConfig.html
---
# Method: help.getCdnConfig
[Back to methods index](index.html)



Get configuration for [CDN](https://core.telegram.org/cdn) file downloads.



### Return type: [CdnConfig](/API_docs/types/CdnConfig.html)

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
$CdnConfig = $MadelineProto->help->getCdnConfig();
```


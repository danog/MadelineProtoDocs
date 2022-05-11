---
title: "help.getAppUpdate"
description: "Returns information on update availability for the current application."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppUpdate.html
---
# Method: help.getAppUpdate
[Back to methods index](index.html)



Returns information on update availability for the current application.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|source|[string](/API_docs/types/string.html) | Source | Yes|


### Return type: [help.AppUpdate](/API_docs/types/help.AppUpdate.html)

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
$help_AppUpdate = $MadelineProto->help->getAppUpdate(source: 'string', );
```


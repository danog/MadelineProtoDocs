---
title: "help.getAppChangelog"
description: "Get changelog of current app.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppChangelog.html
---
# Method: help.getAppChangelog
[Back to methods index](index.html)



Get changelog of current app.  
Typically, an [updates](../constructors/updates.html) constructor will be returned, containing one or more [updateServiceNotification](../constructors/updateServiceNotification.html) updates with app-specific changelogs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|prev\_app\_version|[string](/API_docs/types/string.html) | Previous app version | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->help->getAppChangelog(prev_app_version: 'string', );
```


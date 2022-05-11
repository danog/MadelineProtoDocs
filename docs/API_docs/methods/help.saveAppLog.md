---
title: "help.saveAppLog"
description: "Saves logs of application on the server."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_saveAppLog.html
---
# Method: help.saveAppLog
[Back to methods index](index.html)



Saves logs of application on the server.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|events|Array of [InputAppEvent](/API_docs/types/InputAppEvent.html) | List of input events | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->help->saveAppLog(events: [InputAppEvent, InputAppEvent], );
```


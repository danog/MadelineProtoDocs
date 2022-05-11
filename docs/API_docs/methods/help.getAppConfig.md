---
title: "help.getAppConfig"
description: "Get app-specific configuration, see [client configuration](https://core.telegram.org/api/config#client-configuration) for more info on the result."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppConfig.html
---
# Method: help.getAppConfig
[Back to methods index](index.html)



Get app-specific configuration, see [client configuration](https://core.telegram.org/api/config#client-configuration) for more info on the result.



### Return type: [JSONValue](/API_docs/types/JSONValue.html)

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
$JSONValue = $MadelineProto->help->getAppConfig();
```


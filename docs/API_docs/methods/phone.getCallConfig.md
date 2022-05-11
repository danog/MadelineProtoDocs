---
title: "phone.getCallConfig"
description: "Get phone call configuration to be passed to libtgvoip's shared config"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getCallConfig.html
---
# Method: phone.getCallConfig
[Back to methods index](index.html)



Get phone call configuration to be passed to libtgvoip's shared config



### Return type: [DataJSON](/API_docs/types/DataJSON.html)

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
$DataJSON = $MadelineProto->phone->getCallConfig();
```


---
title: "help.getPeerColors"
description: "Get the set of [accent color palettes »](https://core.telegram.org/api/colors) that can be used for message accents."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPeerColors.html
---
# Method: help.getPeerColors
[Back to methods index](index.html)



Get the set of [accent color palettes »](https://core.telegram.org/api/colors) that can be used for message accents.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [help.PeerColors](/API_docs/types/help.PeerColors.html)

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

$help_PeerColors = $MadelineProto->help->getPeerColors(hash: [$long\|string, $long\|string], );
```


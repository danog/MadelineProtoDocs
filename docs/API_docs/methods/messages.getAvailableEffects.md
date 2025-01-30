---
title: "messages.getAvailableEffects"
description: "Fetch the full list of usable [animated message effects »](https://core.telegram.org/api/effects)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAvailableEffects.html
---
# Method: messages.getAvailableEffects
[Back to methods index](index.html)



Fetch the full list of usable [animated message effects »](https://core.telegram.org/api/effects).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [messages.AvailableEffects](/API_docs/types/messages.AvailableEffects.html)

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

$messages_AvailableEffects = $MadelineProto->messages->getAvailableEffects(hash: [$long\|string, $long\|string], );
```


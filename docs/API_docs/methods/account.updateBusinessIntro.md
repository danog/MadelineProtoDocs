---
title: "account.updateBusinessIntro"
description: "Set or remove the [Telegram Business introduction »](https://core.telegram.org/api/business#business-introduction)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateBusinessIntro.html
---
# Method: account.updateBusinessIntro
[Back to methods index](index.html)



Set or remove the [Telegram Business introduction »](https://core.telegram.org/api/business#business-introduction).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|intro|[InputBusinessIntro](/API_docs/types/InputBusinessIntro.html) | Telegram Business introduction, to remove it call the method without setting this flag. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->updateBusinessIntro(intro: $InputBusinessIntro, );
```


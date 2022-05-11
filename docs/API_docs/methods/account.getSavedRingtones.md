---
title: "account.getSavedRingtones"
description: "account.getSavedRingtones parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getSavedRingtones.html
---
# Method: account.getSavedRingtones
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|


### Return type: [account.SavedRingtones](/API_docs/types/account.SavedRingtones.html)

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
$account_SavedRingtones = $MadelineProto->account->getSavedRingtones(hash: long, );
```


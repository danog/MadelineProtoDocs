---
title: "account.getSavedMusicIds"
description: "account.getSavedMusicIds parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getSavedMusicIds.html
---
# Method: account.getSavedMusicIds
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [account.SavedMusicIds](/API_docs/types/account.SavedMusicIds.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_SavedMusicIds = $MadelineProto->account->getSavedMusicIds(hash: [$long\|string, $long\|string], );
```


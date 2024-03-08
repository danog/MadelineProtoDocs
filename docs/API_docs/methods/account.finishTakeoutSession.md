---
title: "account.finishTakeoutSession"
description: "Terminate a [takeout session, see here » for more info](https://core.telegram.org/api/takeout)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_finishTakeoutSession.html
---
# Method: account.finishTakeoutSession
[Back to methods index](index.html)



Terminate a [takeout session, see here » for more info](https://core.telegram.org/api/takeout).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|success|[Bool](/API_docs/types/Bool.html) | Data exported successfully | Optional|


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

$Bool = $MadelineProto->account->finishTakeoutSession(success: $Bool, );
```


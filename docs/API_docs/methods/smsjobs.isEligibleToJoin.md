---
title: "smsjobs.isEligibleToJoin"
description: "Check if we can process SMS jobs (official clients only)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/smsjobs_isEligibleToJoin.html
---
# Method: smsjobs.isEligibleToJoin
[Back to methods index](index.html)



Check if we can process SMS jobs (official clients only).



### Return type: [smsjobs.EligibilityToJoin](/API_docs/types/smsjobs.EligibilityToJoin.html)

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

$smsjobs_EligibilityToJoin = $MadelineProto->smsjobs->isEligibleToJoin();
```


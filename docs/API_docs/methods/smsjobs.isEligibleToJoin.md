---
title: "smsjobs.isEligibleToJoin"
description: "smsjobs.isEligibleToJoin parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/smsjobs_isEligibleToJoin.html
---
# Method: smsjobs.isEligibleToJoin
[Back to methods index](index.html)





### Return type: [smsjobs.EligibilityToJoin](/API_docs/types/smsjobs.EligibilityToJoin.html)

### Can bots use this method: **YES**


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


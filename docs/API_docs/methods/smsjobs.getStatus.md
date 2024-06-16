---
title: "smsjobs.getStatus"
description: "smsjobs.getStatus parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/smsjobs_getStatus.html
---
# Method: smsjobs.getStatus
[Back to methods index](index.html)





### Return type: [smsjobs.Status](/API_docs/types/smsjobs.Status.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$smsjobs_Status = $MadelineProto->smsjobs->getStatus();
```


---
title: "smsjobs.finishJob"
description: "Finish an SMS job (official clients only)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/smsjobs_finishJob.html
---
# Method: smsjobs.finishJob
[Back to methods index](index.html)



Finish an SMS job (official clients only).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|job\_id|[string](/API_docs/types/string.html) | Job ID. | Optional|
|error|[string](/API_docs/types/string.html) | If failed, the error. | Optional|


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

$Bool = $MadelineProto->smsjobs->finishJob(job_id: 'string', error: 'string', );
```


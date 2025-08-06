---
title: "smsjobs.getSmsJob"
description: "Get info about an SMS job (official clients only)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/smsjobs_getSmsJob.html
---
# Method: smsjobs.getSmsJob
[Back to methods index](index.html)



Get info about an SMS job (official clients only).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|job\_id|[string](/API_docs/types/string.html) | Job ID | Optional|


### Return type: [SmsJob](/API_docs/types/SmsJob.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$SmsJob = $MadelineProto->smsjobs->getSmsJob(job_id: 'string', );
```


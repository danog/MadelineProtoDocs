---
title: "phone.saveCallLog"
description: "Save phone call debug information"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_saveCallLog.html
---
# Method: phone.saveCallLog
[Back to methods index](index.html)



Save phone call debug information

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | Phone call | Yes|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Logs | Yes|


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

$Bool = $MadelineProto->phone->saveCallLog(peer: InputPhoneCall, file: InputFile, );
```


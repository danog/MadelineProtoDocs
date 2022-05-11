---
title: "account.uploadRingtone"
description: "account.uploadRingtone parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadRingtone.html
---
# Method: account.uploadRingtone
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Yes|
|file\_name|[string](/API_docs/types/string.html) | Yes|
|mime\_type|[string](/API_docs/types/string.html) | Yes|


### Return type: [Document](/API_docs/types/Document.html)

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
$Document = $MadelineProto->account->uploadRingtone(file: InputFile, file_name: 'string', mime_type: 'string', );
```


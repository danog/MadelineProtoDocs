---
title: "account.uploadRingtone"
description: "Upload notification sound, use [account.saveRingtone](../methods/account.saveRingtone.html) to convert it and add it to the list of saved notification sounds."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadRingtone.html
---
# Method: account.uploadRingtone
[Back to methods index](index.html)



Upload notification sound, use [account.saveRingtone](../methods/account.saveRingtone.html) to convert it and add it to the list of saved notification sounds.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Notification sound | Yes|
|file\_name|[string](/API_docs/types/string.html) | File name | Optional|
|mime\_type|[string](/API_docs/types/string.html) | MIME type of file | Optional|


### Return type: [Document](/API_docs/types/Document.html)

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

$Document = $MadelineProto->account->uploadRingtone(file: $InputFile, file_name: 'string', mime_type: 'string', );
```


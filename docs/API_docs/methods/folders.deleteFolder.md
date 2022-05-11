---
title: "folders.deleteFolder"
description: "Delete a [peer folder](https://core.telegram.org/api/folders#peer-folders)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/folders_deleteFolder.html
---
# Method: folders.deleteFolder
[Back to methods index](index.html)



Delete a [peer folder](https://core.telegram.org/api/folders#peer-folders)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](/API_docs/types/int.html) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->folders->deleteFolder(folder_id: int, );
```


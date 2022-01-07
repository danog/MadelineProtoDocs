---
title: "folders.deleteFolder"
description: "Delete a [peer folder](https://core.telegram.org/api/folders#peer-folders)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/folders_deleteFolder.html
---
# Method: folders.deleteFolder
[Back to methods index](index.md)



Delete a [peer folder](https://core.telegram.org/api/folders#peer-folders)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](../types/int.md) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->folders->deleteFolder(['folder_id' => int, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_EMPTY|An empty folder ID was specified|



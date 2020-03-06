---
title: folders.deleteFolder
description: Delete a folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/folders_deleteFolder.html
---
# Method: folders.deleteFolder  
[Back to methods index](index.md)


Delete a folder

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](../types/int.md) | Folder to delete | Yes|


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

Or, if you're into Lua:

```lua
Updates = folders.deleteFolder({folder_id=int, })
```


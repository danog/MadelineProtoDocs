---
title: folders.editPeerFolders
description: Edit peers in folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/folders_editPeerFolders.html
---
# Method: folders.editPeerFolders  
[Back to methods index](index.md)


Edit peers in folder

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_peers|Array of [InputFolderPeer](../types/InputFolderPeer.md) | New folder peers | Yes|


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

$Updates = $MadelineProto->folders->editPeerFolders(['folder_peers' => [InputFolderPeer, InputFolderPeer], ]);
```

Or, if you're into Lua:

```lua
Updates = folders.editPeerFolders({folder_peers={InputFolderPeer}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_INVALID|Invalid folder ID|



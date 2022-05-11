---
title: "folders.editPeerFolders"
description: "Edit peers in [peer folder](https://core.telegram.org/api/folders#peer-folders)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/folders_editPeerFolders.html
---
# Method: folders.editPeerFolders
[Back to methods index](index.html)



Edit peers in [peer folder](https://core.telegram.org/api/folders#peer-folders)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_peers|Array of [InputFolderPeer](/API_docs/types/InputFolderPeer.html) | New peer list | Yes|


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
$Updates = $MadelineProto->folders->editPeerFolders(folder_peers: [InputFolderPeer, InputFolderPeer], );
```


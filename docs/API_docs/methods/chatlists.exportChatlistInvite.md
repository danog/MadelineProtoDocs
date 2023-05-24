---
title: "chatlists.exportChatlistInvite"
description: "Export a [folder »](https://core.telegram.org/api/folders), creating a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_exportChatlistInvite.html
---
# Method: chatlists.exportChatlistInvite
[Back to methods index](index.html)



Export a [folder »](https://core.telegram.org/api/folders), creating a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | The folder to export | Yes|
|title|[string](/API_docs/types/string.html) | An optional name for the link | Yes|
|peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The list of channels, group and supergroups to share with the link. Basic groups will automatically be [converted to supergroups](https://core.telegram.org/api/channel#migration) when invoking the method. | Yes|


### Return type: [chatlists.ExportedChatlistInvite](/API_docs/types/chatlists.ExportedChatlistInvite.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$chatlists_ExportedChatlistInvite = $MadelineProto->chatlists->exportChatlistInvite(chatlist: InputChatlist, title: 'string', peers: [InputPeer, InputPeer], );
```


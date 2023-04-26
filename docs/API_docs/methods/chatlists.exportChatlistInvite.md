---
title: "chatlists.exportChatlistInvite"
description: "chatlists.exportChatlistInvite parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_exportChatlistInvite.html
---
# Method: chatlists.exportChatlistInvite
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Yes|


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


---
title: "chatlists.editExportedInvite"
description: "chatlists.editExportedInvite parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_editExportedInvite.html
---
# Method: chatlists.editExportedInvite
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | Yes|
|slug|[string](/API_docs/types/string.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|


### Return type: [ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedChatlistInvite = $MadelineProto->chatlists->editExportedInvite(chatlist: InputChatlist, slug: 'string', title: 'string', peers: [InputPeer, InputPeer], );
```


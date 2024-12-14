---
title: "chatlists.deleteExportedInvite"
description: "Delete a previously created [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_deleteExportedInvite.html
---
# Method: chatlists.deleteExportedInvite
[Back to methods index](index.html)



Delete a previously created [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | The related folder | Yes|
|slug|[string](/API_docs/types/string.html) | `slug` obtained from the [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links). | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->chatlists->deleteExportedInvite(chatlist: $InputChatlist, slug: 'string', );
```


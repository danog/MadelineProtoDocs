---
title: "messages.editExportedChatInvite"
description: "messages.editExportedChatInvite parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editExportedChatInvite.html
---
# Method: messages.editExportedChatInvite
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revoked|[Bool](/API_docs/types/Bool.md) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Optional|
|link|[string](/API_docs/types/string.md) | Yes|
|expire\_date|[int](/API_docs/types/int.md) | Optional|
|usage\_limit|[int](/API_docs/types/int.md) | Optional|
|request\_needed|[Bool](/API_docs/types/Bool.md) | Optional|
|title|[string](/API_docs/types/string.md) | Optional|


### Return type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ExportedChatInvite = $MadelineProto->messages->editExportedChatInvite(['revoked' => Bool, 'peer' => InputPeer, 'link' => 'string', 'expire_date' => int, 'usage_limit' => int, 'request_needed' => Bool, 'title' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|



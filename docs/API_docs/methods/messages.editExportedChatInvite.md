---
title: "messages.editExportedChatInvite"
description: "Edit an exported chat invite"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editExportedChatInvite.html
---
# Method: messages.editExportedChatInvite
[Back to methods index](index.html)



Edit an exported chat invite

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoked|[Bool](/API_docs/types/Bool.html) | Whether to revoke the chat invite | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Chat | Optional|
|link|[string](/API_docs/types/string.html) | Invite link | Yes|
|expire\_date|[int](/API_docs/types/int.html) | New expiration date | Optional|
|usage\_limit|[int](/API_docs/types/int.html) | Maximum number of users that can join using this link | Optional|
|request\_needed|[Bool](/API_docs/types/Bool.html) | Whether admin confirmation is required before admitting each separate user into the chat | Optional|
|title|[string](/API_docs/types/string.html) | Description of the invite link, visible only to administrators | Optional|


### Return type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_ExportedChatInvite = $MadelineProto->messages->editExportedChatInvite(revoked: Bool, peer: InputPeer, link: 'string', expire_date: int, usage_limit: int, request_needed: Bool, title: 'string', );
```


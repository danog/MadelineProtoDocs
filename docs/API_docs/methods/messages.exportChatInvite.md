---
title: "messages.exportChatInvite"
description: "Export an invite link for a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_exportChatInvite.html
---
# Method: messages.exportChatInvite
[Back to methods index](index.html)



Export an invite link for a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|legacy\_revoke\_permanent|[Bool](/API_docs/types/Bool.html) | Legacy flag, reproducing legacy behavior of this method: if set, revokes all previous links before creating a new one. Kept for bot API BC, should not be used by modern clients. | Optional|
|request\_needed|[Bool](/API_docs/types/Bool.html) | Whether admin confirmation is required before admitting each separate user into the chat | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Chat | Optional|
|expire\_date|[int](/API_docs/types/int.html) | Expiration date | Optional|
|usage\_limit|[int](/API_docs/types/int.html) | Maximum number of users that can join using this link | Optional|
|title|[string](/API_docs/types/string.html) | Description of the invite link, visible only to administrators | Optional|


### Return type: [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html)

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
$ExportedChatInvite = $MadelineProto->messages->exportChatInvite(legacy_revoke_permanent: Bool, request_needed: Bool, peer: InputPeer, expire_date: int, usage_limit: int, title: 'string', );
```


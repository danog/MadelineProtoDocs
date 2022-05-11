---
title: "messages.getExportedChatInvites"
description: "Get info about the chat invites of a specific chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getExportedChatInvites.html
---
# Method: messages.getExportedChatInvites
[Back to methods index](index.html)



Get info about the chat invites of a specific chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoked|[Bool](/API_docs/types/Bool.html) | Whether to fetch revoked chat invites | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Chat | Optional|
|admin\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Whether to only fetch chat invites from this admin | Optional|
|offset\_date|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_link|[string](/API_docs/types/string.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.html)

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
$messages_ExportedChatInvites = $MadelineProto->messages->getExportedChatInvites(revoked: Bool, peer: InputPeer, admin_id: InputUser, offset_date: int, offset_link: 'string', limit: int, );
```


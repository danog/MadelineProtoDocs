---
title: "messages.getChatInviteImporters"
description: "Get info about the users that joined the chat using a specific chat invite"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getChatInviteImporters.html
---
# Method: messages.getChatInviteImporters
[Back to methods index](index.html)



Get info about the users that joined the chat using a specific chat invite

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|requested|[Bool](/API_docs/types/Bool.html) | If set, only returns info about users with pending [join requests »](https://core.telegram.org/api/invites#join-requests) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Chat | Optional|
|link|[string](/API_docs/types/string.html) | Invite link | Optional|
|q|[string](/API_docs/types/string.html) | Search for a user in the pending [join requests »](https://core.telegram.org/api/invites#join-requests) list: only available when the `requested` flag is set, cannot be used together with a specific `link`. | Optional|
|offset\_date|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_user|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | User ID for [pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.ChatInviteImporters](/API_docs/types/messages.ChatInviteImporters.html)

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
$messages_ChatInviteImporters = $MadelineProto->messages->getChatInviteImporters(requested: Bool, peer: InputPeer, link: 'string', q: 'string', offset_date: int, offset_user: InputUser, limit: int, );
```


---
title: "messages.editChatDefaultBannedRights"
description: "Edit the default banned rights of a [channel/supergroup/group](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatDefaultBannedRights.html
---
# Method: messages.editChatDefaultBannedRights
[Back to methods index](index.html)



Edit the default banned rights of a [channel/supergroup/group](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer | Optional|
|banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | The new global rights | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->editChatDefaultBannedRights(peer: InputPeer, banned_rights: ChatBannedRights, );
```


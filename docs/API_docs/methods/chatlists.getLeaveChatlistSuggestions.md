---
title: "chatlists.getLeaveChatlistSuggestions"
description: "Returns identifiers of pinned or always included chats from a chat folder imported using a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links), which are suggested to be left when the chat folder is deleted."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_getLeaveChatlistSuggestions.html
---
# Method: chatlists.getLeaveChatlistSuggestions
[Back to methods index](index.html)



Returns identifiers of pinned or always included chats from a chat folder imported using a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links), which are suggested to be left when the chat folder is deleted.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | Folder ID | Yes|


### Return type: [Vector\_of\_Peer](/API_docs/types/Peer.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_Peer = $MadelineProto->chatlists->getLeaveChatlistSuggestions(chatlist: $InputChatlist, );
```


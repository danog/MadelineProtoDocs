---
title: "chatlists.joinChatlistUpdates"
description: "Join channels and supergroups recently added to a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_joinChatlistUpdates.html
---
# Method: chatlists.joinChatlistUpdates
[Back to methods index](index.html)



Join channels and supergroups recently added to a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chatlist|[InputChatlist](/API_docs/types/InputChatlist.html) | The folder | Yes|
|peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | List of new chats to join, fetched using [chatlists.getChatlistUpdates](../methods/chatlists.getChatlistUpdates.html) and filtered as specified in the [documentation »](https://core.telegram.org/api/folders#shared-folders). | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->chatlists->joinChatlistUpdates(chatlist: $InputChatlist, peers: [$InputPeer, $InputPeer], );
```


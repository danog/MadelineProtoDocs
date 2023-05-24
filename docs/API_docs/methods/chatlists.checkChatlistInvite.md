---
title: "chatlists.checkChatlistInvite"
description: "Obtain information about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/chatlists_checkChatlistInvite.html
---
# Method: chatlists.checkChatlistInvite
[Back to methods index](index.html)



Obtain information about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | `slug` obtained from the [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links) | Yes|


### Return type: [chatlists.ChatlistInvite](/API_docs/types/chatlists.ChatlistInvite.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$chatlists_ChatlistInvite = $MadelineProto->chatlists->checkChatlistInvite(slug: 'string', );
```


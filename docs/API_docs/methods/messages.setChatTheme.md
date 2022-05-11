---
title: "messages.setChatTheme"
description: "Change the chat theme of a certain chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setChatTheme.html
---
# Method: messages.setChatTheme
[Back to methods index](index.html)



Change the chat theme of a certain chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Private chat where to change theme | Optional|
|emoticon|[string](/API_docs/types/string.html) | Emoji, identifying a specific chat theme; a list of chat themes can be fetched using [account.getChatThemes](../methods/account.getChatThemes.html) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->setChatTheme(peer: InputPeer, emoticon: 'string', );
```


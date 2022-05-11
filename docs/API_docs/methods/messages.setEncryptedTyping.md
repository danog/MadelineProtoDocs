---
title: "messages.setEncryptedTyping"
description: "Send typing event by the current user to a secret chat."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setEncryptedTyping.html
---
# Method: messages.setEncryptedTyping
[Back to methods index](index.html)



Send typing event by the current user to a secret chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](/API_docs/types/InputEncryptedChat.html) | Secret chat ID | Yes|
|typing|[Bool](/API_docs/types/Bool.html) | Typing.<br>**Possible values**:<br>[(boolTrue)](../constructors/boolTrue.html), if the user started typing and more than **5 seconds** have passed since the last request<br>[(boolFalse)](../constructors/boolFalse.html), if the user stopped typing | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->setEncryptedTyping(peer: InputEncryptedChat, typing: Bool, );
```


---
title: "messages.translateText"
description: "Translate a given text"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_translateText.html
---
# Method: messages.translateText
[Back to methods index](index.html)



Translate a given text

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If the text is a chat message, the peer ID | Optional|
|msg\_id|[int](/API_docs/types/int.html) | If the text is a chat message, the message ID | Optional|
|text|[string](/API_docs/types/string.html) | The text to translate | Optional|
|from\_lang|[string](/API_docs/types/string.html) | Two-letter ISO 639-1 language code of the language from which the message is translated, if not set will be autodetected | Optional|
|to\_lang|[string](/API_docs/types/string.html) | Two-letter ISO 639-1 language code of the language to which the message is translated | Yes|


### Return type: [messages.TranslatedText](/API_docs/types/messages.TranslatedText.html)

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
$messages_TranslatedText = $MadelineProto->messages->translateText(peer: InputPeer, msg_id: int, text: 'string', from_lang: 'string', to_lang: 'string', );
```


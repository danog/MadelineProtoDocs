---
title: "messages.translateText"
description: "Translate a given text."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_translateText.html
---
# Method: messages.translateText
[Back to methods index](index.html)



Translate a given text.

[Styled text entities](https://core.telegram.org/api/entities) will only be preserved for [Telegram Premium](https://core.telegram.org/api/premium) users.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If the text is a chat message, the peer ID | Optional|
|id|Array of [int](/API_docs/types/int.html) | A list of message IDs to translate | Optional|
|text|Array of [TextWithEntities](/API_docs/types/TextWithEntities.html) | A list of styled messages to translate | Optional|
|to\_lang|[string](/API_docs/types/string.html) | Two-letter ISO 639-1 language code of the language to which the message is translated | Optional|


### Return type: [messages.TranslatedText](/API_docs/types/messages.TranslatedText.html)

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

$messages_TranslatedText = $MadelineProto->messages->translateText(peer: $InputPeer, id: [$int, $int], text: [$TextWithEntities, $TextWithEntities], to_lang: 'string', );
```


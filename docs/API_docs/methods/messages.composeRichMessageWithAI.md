---
title: "messages.composeRichMessageWithAI"
description: "messages.composeRichMessageWithAI parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_composeRichMessageWithAI.html
---
# Method: messages.composeRichMessageWithAI
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|proofread|[Bool](/API_docs/types/Bool.html) | Optional|
|emojify|[Bool](/API_docs/types/Bool.html) | Optional|
|text|[InputRichMessage](/API_docs/types/InputRichMessage.html) | Optional|
|translate\_to\_lang|[string](/API_docs/types/string.html) | Optional|
|tone|[InputAiComposeTone](/API_docs/types/InputAiComposeTone.html) | Optional|


### Return type: [messages.ComposedRichMessageWithAI](/API_docs/types/messages.ComposedRichMessageWithAI.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ComposedRichMessageWithAI = $MadelineProto->messages->composeRichMessageWithAI(proofread: $Bool, emojify: $Bool, text: $InputRichMessage, translate_to_lang: 'string', tone: $InputAiComposeTone, );
```


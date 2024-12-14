---
title: "messages.getEmojiKeywords"
description: "Get localized [emoji keywords »](https://core.telegram.org/api/custom-emoji#emoji-keywords)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiKeywords.html
---
# Method: messages.getEmojiKeywords
[Back to methods index](index.html)



Get localized [emoji keywords »](https://core.telegram.org/api/custom-emoji#emoji-keywords).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](/API_docs/types/string.html) | Language code | Optional|


### Return type: [EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.html)

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

$EmojiKeywordsDifference = $MadelineProto->messages->getEmojiKeywords(lang_code: 'string', );
```


---
title: "messages.getEmojiKeywordsLanguages"
description: "Obtain a list of related languages that must be used when fetching [emoji keyword lists »](https://core.telegram.org/api/custom-emoji#emoji-keywords)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiKeywordsLanguages.html
---
# Method: messages.getEmojiKeywordsLanguages
[Back to methods index](index.html)



Obtain a list of related languages that must be used when fetching [emoji keyword lists »](https://core.telegram.org/api/custom-emoji#emoji-keywords).

Usually the method will return the passed language codes (if localized) + `en` + some language codes for similar languages (if applicable).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_codes|Array of [string](/API_docs/types/string.html) | The user's language codes | Yes|


### Return type: [Vector\_of\_EmojiLanguage](/API_docs/types/EmojiLanguage.html)

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

$Vector_of_EmojiLanguage = $MadelineProto->messages->getEmojiKeywordsLanguages(lang_codes: ['string', 'string'], );
```


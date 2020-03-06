---
title: messages.getEmojiKeywordsLanguages
description: Get info about an emoji keyword localization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiKeywordsLanguages.html
---
# Method: messages.getEmojiKeywordsLanguages  
[Back to methods index](index.md)


Get info about an emoji keyword localization

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_codes|Array of [string](../types/string.md) | Language codes | Yes|


### Return type: [Vector\_of\_EmojiLanguage](../types/EmojiLanguage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_EmojiLanguage = $MadelineProto->messages->getEmojiKeywordsLanguages(['lang_codes' => ['string', 'string'], ]);
```

Or, if you're into Lua:

```lua
Vector_of_EmojiLanguage = messages.getEmojiKeywordsLanguages({lang_codes={'string'}, })
```


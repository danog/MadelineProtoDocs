---
title: messages.getEmojiKeywords
description: Get emoji keywords
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getEmojiKeywords  
[Back to methods index](index.md)


Get emoji keywords

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](../types/string.md) | Language code | Yes|


### Return type: [EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EmojiKeywordsDifference = $MadelineProto->messages->getEmojiKeywords(['lang_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
EmojiKeywordsDifference = messages.getEmojiKeywords({lang_code='string', })
```


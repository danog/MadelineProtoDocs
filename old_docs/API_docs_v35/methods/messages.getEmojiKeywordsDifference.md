---
title: messages.getEmojiKeywordsDifference
description: Get changed emoji keywords
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiKeywordsDifference.html
---
# Method: messages.getEmojiKeywordsDifference
[Back to methods index](index.md)



Get changed emoji keywords

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](../types/string.md) | Language code | Yes|
|from\_version|[int](../types/int.md) | Previous emoji keyword localization version | Yes|


### Return type: [EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EmojiKeywordsDifference = $MadelineProto->messages->getEmojiKeywordsDifference(['lang_code' => 'string', 'from_version' => int, ]);
```

Or, if you're into Lua:

```lua
EmojiKeywordsDifference = messages.getEmojiKeywordsDifference({lang_code='string', from_version=int, })
```


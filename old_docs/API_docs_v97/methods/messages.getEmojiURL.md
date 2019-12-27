---
title: messages.getEmojiURL
description: Returns an HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getEmojiURL  
[Back to methods index](index.md)


Returns an HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_code|[string](../types/string.md) | Language code for which the emoji replacements will be suggested | Yes|


### Return type: [EmojiURL](../types/EmojiURL.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EmojiURL = $MadelineProto->messages->getEmojiURL(['lang_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
EmojiURL = messages.getEmojiURL({lang_code='string', })
```


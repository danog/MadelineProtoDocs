---
title: langpack.getLanguages
description: Get available languages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: langpack.getLanguages  
[Back to methods index](index.md)


Get available languages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_pack|[string](../types/string.md) | Lang pack | Yes|


### Return type: [Vector\_of\_LangPackLanguage](../types/LangPackLanguage.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_LangPackLanguage = $MadelineProto->langpack->getLanguages(['lang_pack' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/langpack.getLanguages`

Parameters:

lang_pack - Json encoded string




Or, if you're into Lua:

```lua
Vector_of_LangPackLanguage = langpack.getLanguages({lang_pack='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|LANG_PACK_INVALID|The provided language pack is invalid|



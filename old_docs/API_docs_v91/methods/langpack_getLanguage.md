---
title: langpack.getLanguage
description: Get language
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: langpack.getLanguage  
[Back to methods index](index.md)


Get language

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_pack|[string](../types/string.md) | Lang pack | Yes|
|lang\_code|[string](../types/string.md) | Lang code | Yes|


### Return type: [LangPackLanguage](../types/LangPackLanguage.md)

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

$LangPackLanguage = $MadelineProto->langpack->getLanguage(['lang_pack' => 'string', 'lang_code' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - langpack.getLanguage
* params - `{"lang_pack": "string", "lang_code": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/langpack.getLanguage`

Parameters:

lang_pack - Json encoded string

lang_code - Json encoded string




Or, if you're into Lua:

```lua
LangPackLanguage = langpack.getLanguage({lang_pack='string', lang_code='string', })
```


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


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


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

Or, if you're into Lua:

```lua
LangPackLanguage = langpack.getLanguage({lang_pack='string', lang_code='string', })
```


---
title: langpack.getLanguages
description: Get information about all languages in a localization pack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/langpack_getLanguages.html
---
# Method: langpack.getLanguages  
[Back to methods index](index.md)


Get information about all languages in a localization pack



### Return type: [Vector\_of\_LangPackLanguage](../types/LangPackLanguage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_LangPackLanguage = $MadelineProto->langpack->getLanguages();
```

Or, if you're into Lua:

```lua
Vector_of_LangPackLanguage = langpack.getLanguages({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|LANG_PACK_INVALID|The provided language pack is invalid|



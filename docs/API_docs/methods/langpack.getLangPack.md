---
title: "langpack.getLangPack"
description: "Get localization pack strings"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/langpack_getLangPack.html
---
# Method: langpack.getLangPack
[Back to methods index](index.html)



Get localization pack strings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_pack|[string](/API_docs/types/string.html) | Language pack name, usually obtained from a [language pack link](https://core.telegram.org/api/links#language-pack-links) | Optional|
|lang\_code|[string](/API_docs/types/string.html) | Language code | Optional|


### Return type: [LangPackDifference](/API_docs/types/LangPackDifference.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$LangPackDifference = $MadelineProto->langpack->getLangPack(lang_pack: 'string', lang_code: 'string', );
```


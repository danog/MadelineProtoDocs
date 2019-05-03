---
title: langpack.getDifference
description: Get language pack updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: langpack.getDifference  
[Back to methods index](index.md)


Get language pack updates

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|lang\_pack|[string](../types/string.md) | Language pack | Yes|
|lang\_code|[string](../types/string.md) | Lang code | Yes|
|from\_version|[int](../types/int.md) | Previous version | Yes|


### Return type: [LangPackDifference](../types/LangPackDifference.md)

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

$LangPackDifference = $MadelineProto->langpack->getDifference(['lang_pack' => 'string', 'lang_code' => 'string', 'from_version' => int, ]);
```

Or, if you're into Lua:

```lua
LangPackDifference = langpack.getDifference({lang_pack='string', lang_code='string', from_version=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|LANG_PACK_INVALID|The provided language pack is invalid|



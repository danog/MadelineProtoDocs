---
title: help.getCdnConfig
description: Get CDN configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getCdnConfig  
[Back to methods index](index.md)


Get CDN configuration



### Return type: [CdnConfig](../types/CdnConfig.md)

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

$CdnConfig = $MadelineProto->help->getCdnConfig();
```

Or, if you're into Lua:

```lua
CdnConfig = help.getCdnConfig({})
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|Timeout|A timeout occurred while fetching data from the bot|



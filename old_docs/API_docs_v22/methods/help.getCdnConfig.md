---
title: help.getCdnConfig
description: Get configuration for [CDN](https://core.telegram.org/cdn) file downloads.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getCdnConfig.html
---
# Method: help.getCdnConfig
[Back to methods index](index.md)



Get configuration for [CDN](https://core.telegram.org/cdn) file downloads.



### Return type: [CdnConfig](../types/CdnConfig.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$CdnConfig = $MadelineProto->help->getCdnConfig();
```

Or, if you're into Lua:

```lua
CdnConfig = help.getCdnConfig({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|



---
title: help.getTermsOfServiceUpdate
description: Look for updates of telegram's terms of service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getTermsOfServiceUpdate.html
---
# Method: help.getTermsOfServiceUpdate  
[Back to methods index](index.md)


Look for updates of telegram's terms of service



### Return type: [help.TermsOfServiceUpdate](../types/help.TermsOfServiceUpdate.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.TermsOfServiceUpdate = $MadelineProto->help->getTermsOfServiceUpdate();
```

Or, if you're into Lua:

```lua
help.TermsOfServiceUpdate = help.getTermsOfServiceUpdate({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|



---
title: help.getTermsOfService
description: Get terms of service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getTermsOfService  
[Back to methods index](index.md)


Get terms of service



### Return type: [help.TermsOfService](../types/help.TermsOfService.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.TermsOfService = $MadelineProto->help->getTermsOfService();
```

Or, if you're into Lua:

```lua
help.TermsOfService = help.getTermsOfService({})
```


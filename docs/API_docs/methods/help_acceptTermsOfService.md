---
title: help.acceptTermsOfService
description: Accept telegram's TOS
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.acceptTermsOfService  
[Back to methods index](index.md)


Accept telegram's TOS

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[DataJSON](../types/DataJSON.md) | TOS | Yes|


### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->help->acceptTermsOfService(['id' => DataJSON, ]);
```

Or, if you're into Lua:

```lua
Bool = help.acceptTermsOfService({id=DataJSON, })
```


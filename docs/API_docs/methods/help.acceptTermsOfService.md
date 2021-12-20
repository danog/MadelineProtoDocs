---
title: "help.acceptTermsOfService"
description: "Accept the new terms of service"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_acceptTermsOfService.html
---
# Method: help.acceptTermsOfService
[Back to methods index](index.md)



Accept the new terms of service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[DataJSON](../types/DataJSON.md) | ID of terms of service | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->help->acceptTermsOfService(['id' => DataJSON, ]);
```

Or, if you're into Lua:

```lua
Bool = help.acceptTermsOfService({id=DataJSON, })
```


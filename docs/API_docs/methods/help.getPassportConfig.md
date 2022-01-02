---
title: "help.getPassportConfig"
description: "Get [passport](https://core.telegram.org/passport) configuration"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPassportConfig.html
---
# Method: help.getPassportConfig
[Back to methods index](index.md)



Get [passport](https://core.telegram.org/passport) configuration

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [help.PassportConfig](../types/help.PassportConfig.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_PassportConfig = $MadelineProto->help->getPassportConfig(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
help_PassportConfig = help.getPassportConfig({hash={int}, })
```


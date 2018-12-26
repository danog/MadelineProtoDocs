---
title: help.getPassportConfig
description: Get passport config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getPassportConfig  
[Back to methods index](index.md)


Get passport config

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | Hash | Optional|


### Return type: [help\_PassportConfig](../types/help_PassportConfig.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_PassportConfig = $MadelineProto->help->getPassportConfig(['hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getPassportConfig
* params - `{"hash": [int], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getPassportConfig`

Parameters:

hash - Json encoded  array of int




Or, if you're into Lua:

```lua
help_PassportConfig = help.getPassportConfig({hash={int}, })
```


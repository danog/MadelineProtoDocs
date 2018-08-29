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


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->help->acceptTermsOfService(['id' => DataJSON, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.acceptTermsOfService
* params - `{"id": DataJSON, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.acceptTermsOfService`

Parameters:

id - Json encoded DataJSON




Or, if you're into Lua:

```
Bool = help.acceptTermsOfService({id=DataJSON, })
```


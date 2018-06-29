---
title: account.deleteSecureValue
description: Delete secure telegram passport value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.deleteSecureValue  
[Back to methods index](index.md)


Delete secure telegram passport value

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|The values to delete|


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

$Bool = $MadelineProto->account->deleteSecureValue(['types' => [SecureValueType, SecureValueType], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.deleteSecureValue
* params - `{"types": [SecureValueType], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.deleteSecureValue`

Parameters:

types - Json encoded  array of SecureValueType




Or, if you're into Lua:

```
Bool = account.deleteSecureValue({types={SecureValueType}, })
```


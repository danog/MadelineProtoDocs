---
title: account.getSecureValue
description: Get secure value for telegram passport
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getSecureValue  
[Back to methods index](index.md)


Get secure value for telegram passport

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|Get telegram passport secure parameters|


### Return type: [Vector\_of\_SecureValue](../types/SecureValue.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_SecureValue = $MadelineProto->account->getSecureValue(['types' => [SecureValueType, SecureValueType], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.getSecureValue
* params - `{"types": [SecureValueType], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.getSecureValue`

Parameters:

types - Json encoded  array of SecureValueType




Or, if you're into Lua:

```
Vector_of_SecureValue = account.getSecureValue({types={SecureValueType}, })
```


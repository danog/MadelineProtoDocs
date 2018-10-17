---
title: auth.sendCall
description: Send verification phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.sendCall  
[Back to methods index](index.md)


Send verification phone call

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | The phone code hash | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->sendCall(['phone_number' => 'string', 'phone_code_hash' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - auth.sendCall
* params - `{"phone_number": "string", "phone_code_hash": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/auth.sendCall`

Parameters:

phone_number - Json encoded string

phone_code_hash - Json encoded string




Or, if you're into Lua:

```lua
Bool = auth.sendCall({phone_number='string', phone_code_hash='string', })
```


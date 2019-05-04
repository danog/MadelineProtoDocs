---
title: auth.cancelCode
description: Invalidate sent phone code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.cancelCode  
[Back to methods index](index.md)


Invalidate sent phone code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | Phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | Phone code hash | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->cancelCode(['phone_number' => 'string', 'phone_code_hash' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = auth.cancelCode({phone_number='string', phone_code_hash='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PHONE_NUMBER_INVALID|The phone number is invalid|



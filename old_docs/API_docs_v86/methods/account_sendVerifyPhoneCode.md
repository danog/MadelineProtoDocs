---
title: account.sendVerifyPhoneCode
description: Send phone verification code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyPhoneCode  
[Back to methods index](index.md)


Send phone verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|allow\_flashcall|[Bool](../types/Bool.md) | Allow phone calls? | Optional|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|current\_number|[Bool](../types/Bool.md) | Is this the current number? | Optional|


### Return type: [auth\_SentCode](../types/auth_SentCode.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendVerifyPhoneCode(['allow_flashcall' => Bool, 'phone_number' => 'string', 'current_number' => Bool, ]);
```

Or, if you're into Lua:

```lua
auth_SentCode = account.sendVerifyPhoneCode({allow_flashcall=Bool, phone_number='string', current_number=Bool, })
```


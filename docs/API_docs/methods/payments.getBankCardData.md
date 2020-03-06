---
title: payments.getBankCardData
description: payments.getBankCardData parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getBankCardData.html
---
# Method: payments.getBankCardData  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|number|[string](../types/string.md) | Yes|


### Return type: [payments.BankCardData](../types/payments.BankCardData.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments.BankCardData = $MadelineProto->payments->getBankCardData(['number' => 'string', ]);
```

Or, if you're into Lua:

```lua
payments.BankCardData = payments.getBankCardData({number='string', })
```


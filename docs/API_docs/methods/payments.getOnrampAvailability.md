---
title: "payments.getOnrampAvailability"
description: "payments.getOnrampAvailability parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getOnrampAvailability.html
---
# Method: payments.getOnrampAvailability
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|provider|[string](/API_docs/types/string.html) | Optional|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|
|base\_currency|[string](/API_docs/types/string.html) | Optional|


### Return type: [OnrampAvailability](/API_docs/types/OnrampAvailability.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$OnrampAvailability = $MadelineProto->payments->getOnrampAvailability(provider: 'string', crypto_currency: 'string', base_currency: 'string', );
```


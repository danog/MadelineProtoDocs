---
title: "payments.getOnrampLimits"
description: "payments.getOnrampLimits parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getOnrampLimits.html
---
# Method: payments.getOnrampLimits
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|provider|[string](/API_docs/types/string.html) | Optional|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|
|base\_currency|[string](/API_docs/types/string.html) | Optional|
|payment\_method|[string](/API_docs/types/string.html) | Optional|


### Return type: [OnrampLimits](/API_docs/types/OnrampLimits.html)

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

$OnrampLimits = $MadelineProto->payments->getOnrampLimits(provider: 'string', crypto_currency: 'string', base_currency: 'string', payment_method: 'string', );
```


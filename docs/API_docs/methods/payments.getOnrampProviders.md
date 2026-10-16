---
title: "payments.getOnrampProviders"
description: "payments.getOnrampProviders parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getOnrampProviders.html
---
# Method: payments.getOnrampProviders
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|


### Return type: [Vector\_of\_OnrampProviderInfo](/API_docs/types/OnrampProviderInfo.html)

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

$Vector_of_OnrampProviderInfo = $MadelineProto->payments->getOnrampProviders(crypto_currency: 'string', );
```


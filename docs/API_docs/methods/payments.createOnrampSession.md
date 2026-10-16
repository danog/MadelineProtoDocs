---
title: "payments.createOnrampSession"
description: "payments.createOnrampSession parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_createOnrampSession.html
---
# Method: payments.createOnrampSession
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|provider|[string](/API_docs/types/string.html) | Optional|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|
|address|[string](/API_docs/types/string.html) | Optional|
|payment\_method|[string](/API_docs/types/string.html) | Optional|
|base\_currency|[string](/API_docs/types/string.html) | Optional|
|base\_amount|[string](/API_docs/types/string.html) | Optional|
|memo|[string](/API_docs/types/string.html) | Optional|
|theme|[string](/API_docs/types/string.html) | Optional|
|success\_return\_url|[string](/API_docs/types/string.html) | Optional|
|fail\_return\_url|[string](/API_docs/types/string.html) | Optional|
|crypto\_amount|[string](/API_docs/types/string.html) | Optional|


### Return type: [OnrampSession](/API_docs/types/OnrampSession.html)

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

$OnrampSession = $MadelineProto->payments->createOnrampSession(provider: 'string', crypto_currency: 'string', address: 'string', payment_method: 'string', base_currency: 'string', base_amount: 'string', memo: 'string', theme: 'string', success_return_url: 'string', fail_return_url: 'string', crypto_amount: 'string', );
```


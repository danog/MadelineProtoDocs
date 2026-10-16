---
title: "payments.getOnrampQuote"
description: "payments.getOnrampQuote parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getOnrampQuote.html
---
# Method: payments.getOnrampQuote
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|provider|[string](/API_docs/types/string.html) | Optional|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|
|base\_currency|[string](/API_docs/types/string.html) | Optional|
|base\_amount|[string](/API_docs/types/string.html) | Optional|
|crypto\_amount|[string](/API_docs/types/string.html) | Optional|
|payment\_method|[string](/API_docs/types/string.html) | Optional|


### Return type: [OnrampQuote](/API_docs/types/OnrampQuote.html)

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

$OnrampQuote = $MadelineProto->payments->getOnrampQuote(provider: 'string', crypto_currency: 'string', base_currency: 'string', base_amount: 'string', crypto_amount: 'string', payment_method: 'string', );
```


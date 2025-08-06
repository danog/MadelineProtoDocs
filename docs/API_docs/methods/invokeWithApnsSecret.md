---
title: "invokeWithApnsSecret"
description: "Official clients only, invoke with Apple push verification."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithApnsSecret
[Back to methods index](index.html)



Official clients only, invoke with Apple push verification.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|nonce|[string](/API_docs/types/string.html) | Nonce. | Optional|
|secret|[string](/API_docs/types/string.html) | Secret. | Optional|
|query|[!X](/API_docs/types/!X.html) | Query. | Yes|


### Return type: [X](/API_docs/types/X.html)

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

$X = $MadelineProto->invokeWithApnsSecret(nonce: 'string', secret: 'string', query: $!X, );
```


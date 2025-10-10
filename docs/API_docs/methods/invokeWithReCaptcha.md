---
title: "invokeWithReCaptcha"
description: "Official clients only: re-execute a method call that required reCAPTCHA verification via a `RECAPTCHA_CHECK_%s__%s`, where the first placeholder is the `action`, and the second one is the reCAPTCHA key ID."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithReCaptcha
[Back to methods index](index.html)



Official clients only: re-execute a method call that required reCAPTCHA verification via a `RECAPTCHA_CHECK_%s__%s`, where the first placeholder is the `action`, and the second one is the reCAPTCHA key ID.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[string](/API_docs/types/string.html) | reCAPTCHA token received after verification. | Optional|
|query|[!X](/API_docs/types/!X.html) | The original method call. | Yes|


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

$X = $MadelineProto->invokeWithReCaptcha(token: 'string', query: $!X, );
```


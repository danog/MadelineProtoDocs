---
title: "auth.requestFirebaseSms"
description: "auth.requestFirebaseSms parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_requestFirebaseSms.html
---
# Method: auth.requestFirebaseSms
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|
|safety\_net\_token|[string](/API_docs/types/string.html) | Optional|
|ios\_push\_secret|[string](/API_docs/types/string.html) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->requestFirebaseSms(phone_number: 'string', phone_code_hash: 'string', safety_net_token: 'string', ios_push_secret: 'string', );
```


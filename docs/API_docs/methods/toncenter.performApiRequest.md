---
title: "toncenter.performApiRequest"
description: "toncenter.performApiRequest parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/toncenter_performApiRequest.html
---
# Method: toncenter.performApiRequest
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|post|[Bool](/API_docs/types/Bool.html) | Optional|
|endpoint|[string](/API_docs/types/string.html) | Optional|
|query|[string](/API_docs/types/string.html) | Optional|
|payload|[string](/API_docs/types/string.html) | Optional|


### Return type: [toncenter.ApiResponse](/API_docs/types/toncenter.ApiResponse.html)

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

$toncenter_ApiResponse = $MadelineProto->toncenter->performApiRequest(post: $Bool, endpoint: 'string', query: 'string', payload: 'string', );
```


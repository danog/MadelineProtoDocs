---
title: "phone.getGroupCallChainBlocks"
description: "phone.getGroupCallChainBlocks parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupCallChainBlocks.html
---
# Method: phone.getGroupCallChainBlocks
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|sub\_chain\_id|[int](/API_docs/types/int.html) | Optional|
|offset|[int](/API_docs/types/int.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->getGroupCallChainBlocks(call: $InputGroupCall, sub_chain_id: $int, offset: $int, limit: $int, );
```


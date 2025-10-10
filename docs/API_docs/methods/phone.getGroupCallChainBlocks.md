---
title: "phone.getGroupCallChainBlocks"
description: "Fetch the blocks of a [conference blockchain »](https://core.telegram.org/api/end-to-end/group-calls)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupCallChainBlocks.html
---
# Method: phone.getGroupCallChainBlocks
[Back to methods index](index.html)



Fetch the blocks of a [conference blockchain »](https://core.telegram.org/api/end-to-end/group-calls).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The conference. | Yes|
|sub\_chain\_id|[int](/API_docs/types/int.html) | Subchain ID. | Optional|
|offset|[int](/API_docs/types/int.html) | Offset for pagination. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of blocks to return in this call, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


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


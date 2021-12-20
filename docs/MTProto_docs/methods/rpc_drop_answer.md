---
title: "rpc_drop_answer"
description: "rpc_drop_answer parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: rpc\_drop\_answer
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|req\_msg\_id|[long](../types/long.md) | Yes|


### Return type: [RpcDropAnswer](../types/RpcDropAnswer.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$RpcDropAnswer = $MadelineProto->rpc_drop_answer(['req_msg_id' => long, ]);
```

Or, if you're into Lua:

```lua
RpcDropAnswer = rpc_drop_answer({req_msg_id=long, })
```


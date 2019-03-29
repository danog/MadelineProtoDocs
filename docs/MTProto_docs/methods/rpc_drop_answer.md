---
title: rpc_drop_answer
description: Do not send answer to provided request
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: rpc\_drop\_answer  
[Back to methods index](index.md)


Do not send answer to provided request

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|req\_msg\_id|[long](../types/long.md) | The message ID of the request | Yes|


### Return type: [RpcDropAnswer](../types/RpcDropAnswer.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$RpcDropAnswer = $MadelineProto->rpc_drop_answer(['req_msg_id' => long, ]);
```

Or, if you're into Lua:

```lua
RpcDropAnswer = rpc_drop_answer({req_msg_id=long, })
```


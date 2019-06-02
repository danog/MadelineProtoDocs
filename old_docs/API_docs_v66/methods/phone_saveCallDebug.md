---
title: phone.saveCallDebug
description: Save call debugging info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: phone.saveCallDebug  
[Back to methods index](index.md)


Save call debugging info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](../types/InputPhoneCall.md) | The call | Yes|
|debug|[DataJSON](../types/DataJSON.md) | Debugging info | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->phone->saveCallDebug(['peer' => InputPhoneCall, 'debug' => DataJSON, ]);
```

Or, if you're into Lua:

```lua
Bool = phone.saveCallDebug({peer=InputPhoneCall, debug=DataJSON, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CALL_PEER_INVALID|The provided call peer object is invalid|
|DATA_JSON_INVALID|The provided JSON data is invalid|



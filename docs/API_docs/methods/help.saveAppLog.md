---
title: "help.saveAppLog"
description: "Saves logs of application on the server."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_saveAppLog.html
---
# Method: help.saveAppLog
[Back to methods index](index.md)



Saves logs of application on the server.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|events|Array of [InputAppEvent](../types/InputAppEvent.md) | List of input events | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->help->saveAppLog(['events' => [InputAppEvent, InputAppEvent], ]);
```

Or, if you're into Lua:

```lua
Bool = help.saveAppLog({events={InputAppEvent}, })
```


---
title: bots.setBotCommands
description: Set bot command list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_setBotCommands.html
---
# Method: bots.setBotCommands
[Back to methods index](index.md)



Set bot command list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|commands|Array of [BotCommand](../types/BotCommand.md) | Bot commands | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->setBotCommands(['commands' => [BotCommand, BotCommand], ]);
```

Or, if you're into Lua:

```lua
Bool = bots.setBotCommands({commands={BotCommand}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_COMMAND_DESCRIPTION_INVALID|The specified command description is invalid|
|400|BOT_COMMAND_INVALID|The specified command is invalid|
|400|LANG_CODE_INVALID|The specified language code is invalid|



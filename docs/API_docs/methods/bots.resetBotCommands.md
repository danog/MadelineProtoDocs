---
title: "bots.resetBotCommands"
description: "bots.resetBotCommands parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_resetBotCommands.html
---
# Method: bots.resetBotCommands
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|scope|[BotCommandScope](../types/BotCommandScope.md) | Yes|
|lang\_code|[string](../types/string.md) | Yes|


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

$Bool = $MadelineProto->bots->resetBotCommands(['scope' => BotCommandScope, 'lang_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = bots.resetBotCommands({scope=BotCommandScope, lang_code='string', })
```


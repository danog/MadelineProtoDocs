---
title: "bots.resetBotCommands"
description: "Clear bot commands for the specified bot scope and language code"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_resetBotCommands.html
---
# Method: bots.resetBotCommands
[Back to methods index](index.html)



Clear bot commands for the specified bot scope and language code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|scope|[BotCommandScope](/API_docs/types/BotCommandScope.html) | Command scope | Yes|
|lang\_code|[string](/API_docs/types/string.html) | Language code | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->bots->resetBotCommands(scope: BotCommandScope, lang_code: 'string', );
```


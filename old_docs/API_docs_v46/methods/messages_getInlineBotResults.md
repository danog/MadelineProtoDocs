---
title: messages.getInlineBotResults
description: Call inline bot
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getInlineBotResults  
[Back to methods index](index.md)


Call inline bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The bot to call | Optional|
|query|[string](../types/string.md) | The query to send to the bot | Yes|
|offset|[string](../types/string.md) | The offset to send to the bot | Yes|


### Return type: [messages\_BotResults](../types/messages_BotResults.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => InputUser, 'query' => 'string', 'offset' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages_BotResults = messages.getInlineBotResults({bot=InputUser, query='string', offset='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|BOT_INLINE_DISABLED|This bot can't be used in inline mode|
|BOT_INVALID|This is not a valid bot|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|Timeout|Timeout while fetching data|



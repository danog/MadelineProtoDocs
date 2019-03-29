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
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where to call the bot | Optional|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | The current location | Optional|
|query|[string](../types/string.md) | The query to send to the bot | Yes|
|offset|[string](../types/string.md) | The offset to send to the bot | Yes|


### Return type: [messages\_BotResults](../types/messages_BotResults.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotResults = $MadelineProto->messages->getInlineBotResults(['bot' => InputUser, 'peer' => InputPeer, 'geo_point' => InputGeoPoint, 'query' => 'string', 'offset' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages_BotResults = messages.getInlineBotResults({bot=InputUser, peer=InputPeer, geo_point=InputGeoPoint, query='string', offset='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|BOT_INLINE_DISABLED|This bot can't be used in inline mode|
|BOT_INVALID|This is not a valid bot|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|Timeout|A timeout occurred while fetching data from the bot|



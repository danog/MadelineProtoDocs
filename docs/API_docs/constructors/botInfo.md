---
title: "botInfo"
description: "Info about bots (available bot commands, etc)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInfo  
[Back to constructors index](/API_docs/constructors/index.md)



Info about bots (available bot commands, etc)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|description|[string](/API_docs/types/string.md) | Yes|Description of the bot|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.md) | Yes|Bot commands that can be used in the chat|



### Type: [BotInfo](/API_docs/types/BotInfo.md)


### Example:

```php
$botInfo = ['_' => 'botInfo', 'user_id' => long, 'description' => 'string', 'commands' => [BotCommand, BotCommand]];
```  

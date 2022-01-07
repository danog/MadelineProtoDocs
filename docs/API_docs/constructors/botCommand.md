---
title: "botCommand"
description: "Describes a bot command that can be used in a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommand  
[Back to constructors index](/API_docs/constructors/index.md)



Describes a bot command that can be used in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|command|[string](/API_docs/types/string.md) | Yes|`/command` name|
|description|[string](/API_docs/types/string.md) | Yes|Description of the command|



### Type: [BotCommand](/API_docs/types/BotCommand.md)


### Example:

```php
$botCommand = ['_' => 'botCommand', 'command' => 'string', 'description' => 'string'];
```  

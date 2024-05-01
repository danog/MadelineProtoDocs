---
title: "botCommand"
description: "Describes a bot command that can be used in a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommand  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a bot command that can be used in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|command|[string](/API_docs/types/string.html) | Yes|`/command` name|
|description|[string](/API_docs/types/string.html) | Yes|Description of the command|



### Type: [BotCommand](/API_docs/types/BotCommand.html)


### Example:

```
$botCommand = ['_' => 'botCommand', 'command' => 'string', 'description' => 'string'];
```  

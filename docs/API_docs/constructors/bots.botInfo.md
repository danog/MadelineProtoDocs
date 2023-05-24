---
title: "bots.botInfo"
description: "Localized information about a bot."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/bots_botInfo.html
---
# Constructor: bots.botInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Localized information about a bot.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|Bot name|
|about|[string](/API_docs/types/string.html) | Yes|Bot about text|
|description|[string](/API_docs/types/string.html) | Yes|Bot description|



### Type: [bots.BotInfo](/API_docs/types/bots.BotInfo.html)


### Example:

```
$bots_botInfo = ['_' => 'bots.botInfo', 'name' => 'string', 'about' => 'string', 'description' => 'string'];
```  

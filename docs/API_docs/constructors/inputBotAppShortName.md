---
title: "inputBotAppShortName"
description: "Used to fetch information about a direct link Mini App by its short name"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotAppShortName  
[Back to constructors index](/API_docs/constructors/index.html)



Used to fetch information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps) by its short name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|ID of the bot that owns the bot mini app|
|short\_name|[string](/API_docs/types/string.html) | Yes|Short name, obtained from a [Direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links)|



### Type: [InputBotApp](/API_docs/types/InputBotApp.html)


### Example:

```
$inputBotAppShortName = ['_' => 'inputBotAppShortName', 'bot_id' => InputUser, 'short_name' => 'string'];
```  

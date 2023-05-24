---
title: "inputBotAppShortName"
description: "Used to fetch information about a named bot web app by its short name"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotAppShortName  
[Back to constructors index](/API_docs/constructors/index.html)



Used to fetch information about a [named bot web app](https://core.telegram.org/api/bots/webapps#named-bot-web-apps) by its short name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|ID of the bot that owns the bot web app|
|short\_name|[string](/API_docs/types/string.html) | Yes|Short name, obtained from a [named bot web app deep link](https://core.telegram.org/api/links#named-bot-web-app-links)|



### Type: [InputBotApp](/API_docs/types/InputBotApp.html)


### Example:

```
$inputBotAppShortName = ['_' => 'inputBotAppShortName', 'bot_id' => InputUser, 'short_name' => 'string'];
```  

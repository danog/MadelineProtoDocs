---
title: "inputBotAppID"
description: "Used to fetch information about a named bot web app by its ID"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotAppID  
[Back to constructors index](/API_docs/constructors/index.html)



Used to fetch information about a [named bot web app](https://core.telegram.org/api/bots/webapps#named-bot-web-apps) by its ID

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|[named bot web app](https://core.telegram.org/api/bots/webapps#named-bot-web-apps) ID.|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash, obtained from the [botApp](../constructors/botApp.html) constructor.|



### Type: [InputBotApp](/API_docs/types/InputBotApp.html)


### Example:

```
$inputBotAppID = ['_' => 'inputBotAppID', 'id' => long, 'access_hash' => long];
```  

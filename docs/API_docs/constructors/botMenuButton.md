---
title: "botMenuButton"
description: "Bot menu button that opens a web app when clicked."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botMenuButton  
[Back to constructors index](/API_docs/constructors/index.html)



[Bot menu button](https://core.telegram.org/api/bots/menu) that opens a [web app](https://core.telegram.org/api/bots/webapps) when clicked.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Title to be displayed on the menu button instead of 'Menu'|
|url|[string](/API_docs/types/string.html) | Yes|URL of a [web app](https://core.telegram.org/api/bots/webapps) to open when the user clicks on the button|



### Type: [BotMenuButton](/API_docs/types/BotMenuButton.html)


### Example:

```
$botMenuButton = ['_' => 'botMenuButton', 'text' => 'string', 'url' => 'string'];
```  

---
title: "botApp"
description: "Contains information about a named bot web app."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botApp  
[Back to constructors index](/API_docs/constructors/index.html)



Contains information about a [named bot web app](https://core.telegram.org/api/bots/webapps#named-bot-web-apps).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Bot web app ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Bot web app access hash|
|short\_name|[string](/API_docs/types/string.html) | Yes|Bot web app short name, used to generate [named bot web app deep links](https://core.telegram.org/api/links#named-bot-web-app-links).|
|title|[string](/API_docs/types/string.html) | Yes|Bot web app title.|
|description|[string](/API_docs/types/string.html) | Yes|Bot web app description.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Bot web app photo.|
|document|[Document](/API_docs/types/Document.html) | Optional|Bot web app animation.|
|hash|[long](/API_docs/types/long.html) | Yes|Hash to pass to [messages.getBotApp](../methods/messages.getBotApp.html), to avoid refetching bot app info if it hasn't changed.|



### Type: [BotApp](/API_docs/types/BotApp.html)


### Example:

```
$botApp = ['_' => 'botApp', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document, 'hash' => long];
```  

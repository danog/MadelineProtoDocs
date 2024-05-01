---
title: "botApp"
description: "Contains information about a direct link Mini App."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botApp  
[Back to constructors index](/API_docs/constructors/index.html)



Contains information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|bot mini app ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|bot mini app access hash|
|short\_name|[string](/API_docs/types/string.html) | Yes|bot mini app short name, used to generate [Direct Mini App deep links](https://core.telegram.org/api/links#direct-mini-app-links).|
|title|[string](/API_docs/types/string.html) | Yes|bot mini app title.|
|description|[string](/API_docs/types/string.html) | Yes|bot mini app description.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|bot mini app photo.|
|document|[Document](/API_docs/types/Document.html) | Optional|bot mini app animation.|
|hash|[long](/API_docs/types/long.html) | Yes|Hash to pass to [messages.getBotApp](../methods/messages.getBotApp.html), to avoid refetching bot app info if it hasn't changed.|



### Type: [BotApp](/API_docs/types/BotApp.html)


### Example:

```
$botApp = ['_' => 'botApp', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document, 'hash' => long];
```  

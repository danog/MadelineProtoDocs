---
title: "bots.popularAppBots"
description: "Popular Main Mini Apps, to be used in the apps tab of global search »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/bots_popularAppBots.html
---
# Constructor: bots.popularAppBots  
[Back to constructors index](/API_docs/constructors/index.html)



Popular [Main Mini Apps](https://core.telegram.org/api/bots/webapps#main-mini-apps), to be used in the [apps tab of global search »](https://core.telegram.org/api/search#apps-tab).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset for [pagination](https://core.telegram.org/api/offsets).|
|users|Array of [User](/API_docs/types/User.html) | Yes|The bots associated to each [Main Mini App, see here »](https://core.telegram.org/api/bots/webapps#main-mini-apps) for more info.|



### Type: [bots.PopularAppBots](/API_docs/types/bots.PopularAppBots.html)


### Example:

```
$bots_popularAppBots = ['_' => 'bots.popularAppBots', 'next_offset' => 'string', 'users' => [User, User]];
```  

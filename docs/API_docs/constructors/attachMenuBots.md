---
title: "attachMenuBots"
description: "Represents a list of bot mini apps that can be launched from the attachment menu »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBots  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a list of [bot mini apps that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|bots|Array of [AttachMenuBot](/API_docs/types/AttachMenuBot.html) | Yes|List of [bot mini apps that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about related users/bots|



### Type: [AttachMenuBots](/API_docs/types/AttachMenuBots.html)


### Example:

```
$attachMenuBots = ['_' => 'attachMenuBots', 'hash' => long, 'bots' => [AttachMenuBot, AttachMenuBot], 'users' => [User, User]];
```  

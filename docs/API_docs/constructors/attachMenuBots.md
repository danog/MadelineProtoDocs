---
title: "attachMenuBots"
description: "attachMenuBots attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBots  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|bots|Array of [AttachMenuBot](/API_docs/types/AttachMenuBot.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [AttachMenuBots](/API_docs/types/AttachMenuBots.html)


### Example:

```
$attachMenuBots = ['_' => 'attachMenuBots', 'hash' => long, 'bots' => [AttachMenuBot, AttachMenuBot], 'users' => [User, User]];
```  

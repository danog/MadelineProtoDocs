---
title: "attachMenuBotsBot"
description: "Represents a bot web app that can be launched from the attachment menu »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBotsBot  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [bot web app that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot|[AttachMenuBot](/API_docs/types/AttachMenuBot.html) | Yes|Represents a [bot web app that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)<br>|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about related users and bots|



### Type: [AttachMenuBotsBot](/API_docs/types/AttachMenuBotsBot.html)


### Example:

```
$attachMenuBotsBot = ['_' => 'attachMenuBotsBot', 'bot' => AttachMenuBot, 'users' => [User, User]];
```  

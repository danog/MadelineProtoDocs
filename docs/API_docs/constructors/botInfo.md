---
title: "botInfo"
description: "Info about bots (available bot commands, etc)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Info about bots (available bot commands, etc)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Optional|ID of the bot|
|description|[string](/API_docs/types/string.html) | Optional|Description of the bot|
|description\_photo|[Photo](/API_docs/types/Photo.html) | Optional|
|description\_document|[Document](/API_docs/types/Document.html) | Optional|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.html) | Optional|Bot commands that can be used in the chat|
|menu\_button|[BotMenuButton](/API_docs/types/BotMenuButton.html) | Optional|



### Type: [BotInfo](/API_docs/types/BotInfo.html)


### Example:

```
$botInfo = ['_' => 'botInfo', 'user_id' => long, 'description' => 'string', 'description_photo' => Photo, 'description_document' => Document, 'commands' => [BotCommand, BotCommand], 'menu_button' => BotMenuButton];
```  

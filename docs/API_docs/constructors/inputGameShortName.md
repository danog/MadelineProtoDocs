---
title: "inputGameShortName"
description: "Game by short name"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameShortName  
[Back to constructors index](/API_docs/constructors/index.md)



Game by short name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.md) | Optional|The bot that provides the game|
|short\_name|[string](/API_docs/types/string.md) | Yes|The game's short name|



### Type: [InputGame](/API_docs/types/InputGame.md)


### Example:

```php
$inputGameShortName = ['_' => 'inputGameShortName', 'bot_id' => InputUser, 'short_name' => 'string'];
```  

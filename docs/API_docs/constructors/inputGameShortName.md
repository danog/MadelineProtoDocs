---
title: "inputGameShortName"
description: "Game by short name"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameShortName  
[Back to constructors index](index.md)



Game by short name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Optional|The bot that provides the game|
|short\_name|[string](../types/string.md) | Yes|The game's short name|



### Type: [InputGame](../types/InputGame.md)


### Example:

```php
$inputGameShortName = ['_' => 'inputGameShortName', 'bot_id' => InputUser, 'short_name' => 'string'];
```  


Or, if you're into Lua:

```lua
inputGameShortName={_='inputGameShortName', bot_id=InputUser, short_name='string'}

```



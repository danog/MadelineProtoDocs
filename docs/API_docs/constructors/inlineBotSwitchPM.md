---
title: "inlineBotSwitchPM"
description: "The bot requested the user to message him in private"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inlineBotSwitchPM  
[Back to constructors index](index.md)



The bot requested the user to message him in private

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text for the button that switches the user to a private chat with the bot and sends the bot a start message with the parameter `start_parameter` (can be empty)|
|start\_param|[string](../types/string.md) | Yes|The parameter for the `/start parameter`|



### Type: [InlineBotSwitchPM](../types/InlineBotSwitchPM.md)


### Example:

```php
$inlineBotSwitchPM = ['_' => 'inlineBotSwitchPM', 'text' => 'string', 'start_param' => 'string'];
```  


Or, if you're into Lua:

```lua
inlineBotSwitchPM={_='inlineBotSwitchPM', text='string', start_param='string'}

```



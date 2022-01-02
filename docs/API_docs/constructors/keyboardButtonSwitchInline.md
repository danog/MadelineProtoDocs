---
title: "keyboardButtonSwitchInline"
description: "Button to force a user to switch to inline mode Pressing the button will prompt the user to select one of their chats, open that chat and insert the bot‘s username and the specified inline query in the input field."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonSwitchInline  
[Back to constructors index](index.md)



Button to force a user to switch to inline mode Pressing the button will prompt the user to select one of their chats, open that chat and insert the bot‘s username and the specified inline query in the input field.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|same\_peer|[Bool](../types/Bool.md) | Optional|If set, pressing the button will insert the bot‘s username and the specified inline `query` in the current chat's input field.|
|text|[string](../types/string.md) | Yes|Button label|
|query|[string](../types/string.md) | Yes|The inline query to use|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonSwitchInline = ['_' => 'keyboardButtonSwitchInline', 'same_peer' => Bool, 'text' => 'string', 'query' => 'string'];
```  


Or, if you're into Lua:

```lua
keyboardButtonSwitchInline={_='keyboardButtonSwitchInline', same_peer=Bool, text='string', query='string'}

```



---
title: "replyKeyboardMarkup"
description: "Bot keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardMarkup  
[Back to constructors index](index.md)



Bot keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|resize|[Bool](../types/Bool.md) | Optional|Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). If not set, the custom keyboard is always of the same height as the app's standard keyboard.|
|single\_use|[Bool](../types/Bool.md) | Optional|Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again.|
|selective|[Bool](../types/Bool.md) | Optional|Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply\_to\_message\_id), sender of the original message.<br><br>Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.|
|rows|Array of [KeyboardButtonRow](../types/KeyboardButtonRow.md) | Yes|Button row|
|placeholder|[string](../types/string.md) | Optional|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardMarkup = ['_' => 'replyKeyboardMarkup', 'resize' => Bool, 'single_use' => Bool, 'selective' => Bool, 'rows' => [KeyboardButtonRow, KeyboardButtonRow], 'placeholder' => 'string'];
```  


Or, if you're into Lua:

```lua
replyKeyboardMarkup={_='replyKeyboardMarkup', resize=Bool, single_use=Bool, selective=Bool, rows={KeyboardButtonRow}, placeholder='string'}

```



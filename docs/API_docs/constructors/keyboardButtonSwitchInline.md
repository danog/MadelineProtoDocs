---
title: "keyboardButtonSwitchInline"
description: "Button to force a user to switch to inline mode Pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonSwitchInline  
[Back to constructors index](/API_docs/constructors/index.html)



Button to force a user to switch to inline mode Pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|same\_peer|[Bool](/API_docs/types/Bool.html) | Optional|If set, pressing the button will insert the bot's username and the specified inline `query` in the current chat's input field.|
|text|[string](/API_docs/types/string.html) | Yes|Button label|
|query|[string](/API_docs/types/string.html) | Yes|The inline query to use|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonSwitchInline = ['_' => 'keyboardButtonSwitchInline', 'same_peer' => Bool, 'text' => 'string', 'query' => 'string'];
```  

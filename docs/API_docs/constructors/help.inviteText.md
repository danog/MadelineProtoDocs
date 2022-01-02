---
title: "help.inviteText"
description: "Text of a text message with an invitation to install Telegram."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_inviteText.html
---
# Constructor: help.inviteText  
[Back to constructors index](index.md)



Text of a text message with an invitation to install Telegram.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Text of the message|



### Type: [help.InviteText](../types/help.InviteText.md)


### Example:

```php
$help_inviteText = ['_' => 'help.inviteText', 'message' => 'string'];
```  


Or, if you're into Lua:

```lua
help_inviteText={_='help.inviteText', message='string'}

```



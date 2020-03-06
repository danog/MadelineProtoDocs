---
title: help.inviteText
description: Text of a text message with an invitation to install application.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_inviteText.html
---
# Constructor: help.inviteText  
[Back to constructors index](index.md)



Text of a text message with an invitation to install application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Text of a message|



### Type: [help.InviteText](../types/help.InviteText.md)


### Example:

```php
$help.inviteText = ['_' => 'help.inviteText', 'message' => 'string'];
```  


Or, if you're into Lua:

```lua
help.inviteText={_='help.inviteText', message='string'}

```



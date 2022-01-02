---
title: "inputKeyboardButtonUrlAuth"
description: "Button to request a user to authorize via URL using Seamless Telegram Login."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputKeyboardButtonUrlAuth  
[Back to constructors index](index.md)



Button to request a user to [authorize](../methods/messages.acceptUrlAuth.md) via URL using [Seamless Telegram Login](https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_write\_access|[Bool](../types/Bool.md) | Optional|Set this flag to request the permission for your bot to send messages to the user.|
|text|[string](../types/string.md) | Yes|Button text|
|fwd\_text|[string](../types/string.md) | Optional|New text of the button in forwarded messages.|
|url|[string](../types/string.md) | Yes|An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in [Receiving authorization data](https://core.telegram.org/widgets/login#receiving-authorization-data).<br>NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in [Checking authorization](https://core.telegram.org/widgets/login#checking-authorization).|
|bot|[InputUser](../types/InputUser.md) | Optional|Username of a bot, which will be used for user authorization. See [Setting up a bot](https://core.telegram.org/widgets/login#setting-up-a-bot) for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See [Linking your domain to the bot](https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot) for more details.|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$inputKeyboardButtonUrlAuth = ['_' => 'inputKeyboardButtonUrlAuth', 'request_write_access' => Bool, 'text' => 'string', 'fwd_text' => 'string', 'url' => 'string', 'bot' => InputUser];
```  


Or, if you're into Lua:

```lua
inputKeyboardButtonUrlAuth={_='inputKeyboardButtonUrlAuth', request_write_access=Bool, text='string', fwd_text='string', url='string', bot=InputUser}

```



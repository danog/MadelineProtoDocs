---
title: "inputKeyboardButtonUrlAuth"
description: "Button to request a user to authorize via URL using Seamless Telegram Login."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputKeyboardButtonUrlAuth  
[Back to constructors index](/API_docs/constructors/index.html)



Button to request a user to [authorize](../methods/messages.acceptUrlAuth.html) via URL using [Seamless Telegram Login](https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|Set this flag to request the permission for your bot to send messages to the user.|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|fwd\_text|[string](/API_docs/types/string.html) | Optional|New text of the button in forwarded messages.|
|url|[string](/API_docs/types/string.html) | Yes|An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in [Receiving authorization data](https://core.telegram.org/widgets/login#receiving-authorization-data).<br>NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in [Checking authorization](https://core.telegram.org/widgets/login#checking-authorization).|
|bot|[InputUser](/API_docs/types/InputUser.html) | Optional|Username of a bot, which will be used for user authorization. See [Setting up a bot](https://core.telegram.org/widgets/login#setting-up-a-bot) for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See [Linking your domain to the bot](https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot) for more details.|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$inputKeyboardButtonUrlAuth = ['_' => 'inputKeyboardButtonUrlAuth', 'request_write_access' => Bool, 'text' => 'string', 'fwd_text' => 'string', 'url' => 'string', 'bot' => InputUser];
```  

---
title: "keyboardButtonUrlAuth"
description: "Button to request a user to authorize via URL using Seamless Telegram Login. When the user clicks on such a button, messages.requestUrlAuth should be called, providing the button_id and the ID of the container message. The returned urlAuthResultRequest object will contain more details about the authorization request (request_write_access if the bot would like to send messages to the user along with the username of the bot which will be used for user authorization). Finally, the user can choose to call messages.acceptUrlAuth to get a urlAuthResultAccepted with the URL to open instead of the url of this constructor, or a urlAuthResultDefault, in which case the url of this constructor must be opened, instead. If the user refuses the authorization request but still wants to open the link, the url of this constructor must be used."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonUrlAuth  
[Back to constructors index](/API_docs/constructors/index.md)



Button to request a user to authorize via URL using [Seamless Telegram Login](https://telegram.org/blog/privacy-discussions-web-bots#meet-seamless-web-bots). When the user clicks on such a button, [messages.requestUrlAuth](../methods/messages.requestUrlAuth.md) should be called, providing the `button_id` and the ID of the container message. The returned [urlAuthResultRequest](../constructors/urlAuthResultRequest.md) object will contain more details about the authorization request (`request_write_access` if the bot would like to send messages to the user along with the username of the bot which will be used for user authorization). Finally, the user can choose to call [messages.acceptUrlAuth](../methods/messages.acceptUrlAuth.md) to get a [urlAuthResultAccepted](../constructors/urlAuthResultAccepted.md) with the URL to open instead of the `url` of this constructor, or a [urlAuthResultDefault](../constructors/urlAuthResultDefault.md), in which case the `url` of this constructor must be opened, instead. If the user refuses the authorization request but still wants to open the link, the `url` of this constructor must be used.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.md) | Yes|Button label|
|fwd\_text|[string](/API_docs/types/string.md) | Optional|New text of the button in forwarded messages.|
|url|[string](/API_docs/types/string.md) | Yes|An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in [Receiving authorization data](https://core.telegram.org/widgets/login#receiving-authorization-data).<br><br>**NOTE**: Services must **always** check the hash of the received data to verify the authentication and the integrity of the data as described in [Checking authorization](https://core.telegram.org/widgets/login#checking-authorization).|
|button\_id|[int](/API_docs/types/int.md) | Yes|ID of the button to pass to [messages.requestUrlAuth](../methods/messages.requestUrlAuth.md)|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.md)


### Example:

```php
$keyboardButtonUrlAuth = ['_' => 'keyboardButtonUrlAuth', 'text' => 'string', 'fwd_text' => 'string', 'url' => 'string', 'button_id' => int];
```  

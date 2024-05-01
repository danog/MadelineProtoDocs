---
title: "urlAuthResultRequest"
description: "Details about the authorization request, for more info click here »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: urlAuthResultRequest  
[Back to constructors index](/API_docs/constructors/index.html)



Details about the authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot would like to send messages to the user|
|bot|[User](/API_docs/types/User.html) | Optional|Username of a bot, which will be used for user authorization. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See [Linking your domain to the bot](https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot) for more details.|
|domain|[string](/API_docs/types/string.html) | Yes|The domain name of the website on which the user will log in.|



### Type: [UrlAuthResult](/API_docs/types/UrlAuthResult.html)


### Example:

```
$urlAuthResultRequest = ['_' => 'urlAuthResultRequest', 'request_write_access' => Bool, 'bot' => User, 'domain' => 'string'];
```  

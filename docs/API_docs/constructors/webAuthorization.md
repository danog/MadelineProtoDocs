---
title: "webAuthorization"
description: "Represents a bot logged in using the Telegram login widget"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webAuthorization  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a bot logged in using the [Telegram login widget](https://core.telegram.org/widgets/login)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|Authorization hash|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|domain|[string](/API_docs/types/string.html) | Yes|The domain name of the website on which the user has logged in.|
|browser|[string](/API_docs/types/string.html) | Yes|Browser user-agent|
|platform|[string](/API_docs/types/string.html) | Yes|Platform|
|date\_created|[int](/API_docs/types/int.html) | Yes|When was the web session created|
|date\_active|[int](/API_docs/types/int.html) | Yes|When was the web session last active|
|ip|[string](/API_docs/types/string.html) | Yes|IP address|
|region|[string](/API_docs/types/string.html) | Yes|Region, determined from IP address|



### Type: [WebAuthorization](/API_docs/types/WebAuthorization.html)


### Example:

```
$webAuthorization = ['_' => 'webAuthorization', 'hash' => long, 'bot_id' => long, 'domain' => 'string', 'browser' => 'string', 'platform' => 'string', 'date_created' => int, 'date_active' => int, 'ip' => 'string', 'region' => 'string'];
```  

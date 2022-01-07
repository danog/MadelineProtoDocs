---
title: "webAuthorization"
description: "Represents a bot logged in using the Telegram login widget"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webAuthorization  
[Back to constructors index](/API_docs/constructors/index.md)



Represents a bot logged in using the [Telegram login widget](https://core.telegram.org/widgets/login)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.md) | Yes|Authorization hash|
|bot\_id|[long](/API_docs/types/long.md) | Yes|
|domain|[string](/API_docs/types/string.md) | Yes|The domain name of the website on which the user has logged in.|
|browser|[string](/API_docs/types/string.md) | Yes|Browser user-agent|
|platform|[string](/API_docs/types/string.md) | Yes|Platform|
|date\_created|[int](/API_docs/types/int.md) | Yes|When was the web session created|
|date\_active|[int](/API_docs/types/int.md) | Yes|When was the web session last active|
|ip|[string](/API_docs/types/string.md) | Yes|IP address|
|region|[string](/API_docs/types/string.md) | Yes|Region, determined from IP address|



### Type: [WebAuthorization](/API_docs/types/WebAuthorization.md)


### Example:

```php
$webAuthorization = ['_' => 'webAuthorization', 'hash' => long, 'bot_id' => long, 'domain' => 'string', 'browser' => 'string', 'platform' => 'string', 'date_created' => int, 'date_active' => int, 'ip' => 'string', 'region' => 'string'];
```  

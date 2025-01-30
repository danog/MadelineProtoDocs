---
title: "updateNewAuthorization"
description: "A new session logged into the current user's account through an unknown device."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewAuthorization  
[Back to constructors index](/API_docs/constructors/index.html)



A new session logged into the current user's account through an unknown device.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unconfirmed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the session is [unconfirmed, see here »](https://core.telegram.org/api/auth#confirming-login) for more info.|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|date|[int](/API_docs/types/int.html) | Optional|Authorization date|
|device|[string](/API_docs/types/string.html) | Optional|Name of device, for example *Android*|
|location|[string](/API_docs/types/string.html) | Optional|Location, for example *USA, NY (IP=1.2.3.4)*|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewAuthorization = ['_' => 'updateNewAuthorization', 'unconfirmed' => Bool, 'hash' => long, 'date' => int, 'device' => 'string', 'location' => 'string'];
```  

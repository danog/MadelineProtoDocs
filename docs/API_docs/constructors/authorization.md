---
title: "authorization"
description: "Logged-in session"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: authorization  
[Back to constructors index](/API_docs/constructors/index.html)



Logged-in session

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|current|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the current session|
|official\_app|[Bool](/API_docs/types/Bool.html) | Optional|Whether the session is from an official app|
|password\_pending|[Bool](/API_docs/types/Bool.html) | Optional|Whether the session is still waiting for a 2FA password|
|encrypted\_requests\_disabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether this session will accept encrypted chats|
|call\_requests\_disabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether this session will accept phone calls|
|hash|[long](/API_docs/types/long.html) | Yes|Identifier|
|device\_model|[string](/API_docs/types/string.html) | Yes|Device model|
|platform|[string](/API_docs/types/string.html) | Yes|Platform|
|system\_version|[string](/API_docs/types/string.html) | Yes|System version|
|api\_id|[int](/API_docs/types/int.html) | Yes|[API ID](https://core.telegram.org/api/obtaining_api_id)|
|app\_name|[string](/API_docs/types/string.html) | Yes|App name|
|app\_version|[string](/API_docs/types/string.html) | Yes|App version|
|date\_created|[int](/API_docs/types/int.html) | Yes|When was the session created|
|date\_active|[int](/API_docs/types/int.html) | Yes|When was the session last active|
|ip|[string](/API_docs/types/string.html) | Yes|Last known IP|
|country|[string](/API_docs/types/string.html) | Yes|Country determined from IP|
|region|[string](/API_docs/types/string.html) | Yes|Region determined from IP|



### Type: [Authorization](/API_docs/types/Authorization.html)


### Example:

```
$authorization = ['_' => 'authorization', 'current' => Bool, 'official_app' => Bool, 'password_pending' => Bool, 'encrypted_requests_disabled' => Bool, 'call_requests_disabled' => Bool, 'hash' => long, 'device_model' => 'string', 'platform' => 'string', 'system_version' => 'string', 'api_id' => int, 'app_name' => 'string', 'app_version' => 'string', 'date_created' => int, 'date_active' => int, 'ip' => 'string', 'country' => 'string', 'region' => 'string'];
```  

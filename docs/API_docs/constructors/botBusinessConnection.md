---
title: "botBusinessConnection"
description: "botBusinessConnection attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botBusinessConnection  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|can\_reply|[Bool](/API_docs/types/Bool.html) | Optional|
|disabled|[Bool](/API_docs/types/Bool.html) | Optional|
|connection\_id|[string](/API_docs/types/string.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|dc\_id|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|



### Type: [BotBusinessConnection](/API_docs/types/BotBusinessConnection.html)


### Example:

```
$botBusinessConnection = ['_' => 'botBusinessConnection', 'can_reply' => Bool, 'disabled' => Bool, 'connection_id' => 'string', 'user_id' => long, 'dc_id' => int, 'date' => int];
```  

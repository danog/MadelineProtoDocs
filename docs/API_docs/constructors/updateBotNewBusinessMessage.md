---
title: "updateBotNewBusinessMessage"
description: "updateBotNewBusinessMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotNewBusinessMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|connection\_id|[string](/API_docs/types/string.html) | Yes|
|message|[Message](/API_docs/types/Message.html) | Optional|
|reply\_to\_message|[Message](/API_docs/types/Message.html) | Optional|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotNewBusinessMessage = ['_' => 'updateBotNewBusinessMessage', 'connection_id' => 'string', 'message' => Message, 'reply_to_message' => Message, 'qts' => int];
```  

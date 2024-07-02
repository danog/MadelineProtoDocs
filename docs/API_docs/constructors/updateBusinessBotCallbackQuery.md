---
title: "updateBusinessBotCallbackQuery"
description: "updateBusinessBotCallbackQuery attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBusinessBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|connection\_id|[string](/API_docs/types/string.html) | Yes|
|message|[Message](/API_docs/types/Message.html) | Optional|
|reply\_to\_message|[Message](/API_docs/types/Message.html) | Optional|
|chat\_instance|[long](/API_docs/types/long.html) | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBusinessBotCallbackQuery = ['_' => 'updateBusinessBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'connection_id' => 'string', 'message' => Message, 'reply_to_message' => Message, 'chat_instance' => long, 'data' => 'bytes'];
```  

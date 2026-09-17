---
title: "updateEphemeralBotCallbackQuery"
description: "updateEphemeralBotCallbackQuery attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEphemeralBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|peer|[long](/API_docs/types/long.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Yes|
|chat\_instance|[long](/API_docs/types/long.html) | Optional|
|message|[EphemeralMessage](/API_docs/types/EphemeralMessage.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEphemeralBotCallbackQuery = ['_' => 'updateEphemeralBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'peer' => long, 'msg_id' => int, 'data' => 'bytes', 'chat_instance' => long, 'message' => EphemeralMessage];
```  

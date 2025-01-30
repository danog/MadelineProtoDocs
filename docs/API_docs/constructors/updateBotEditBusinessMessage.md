---
title: "updateBotEditBusinessMessage"
description: "A message was edited in a connected business chat »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotEditBusinessMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was edited in a [connected business chat »](https://core.telegram.org/api/business#connected-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|connection\_id|[string](/API_docs/types/string.html) | Yes|Business connection ID|
|message|[Message](/API_docs/types/Message.html) | Optional|New message.|
|reply\_to\_message|[Message](/API_docs/types/Message.html) | Optional|The message that `message` is replying to.|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotEditBusinessMessage = ['_' => 'updateBotEditBusinessMessage', 'connection_id' => 'string', 'message' => Message, 'reply_to_message' => Message, 'qts' => int];
```  

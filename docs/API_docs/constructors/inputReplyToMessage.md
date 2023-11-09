---
title: "inputReplyToMessage"
description: "inputReplyToMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputReplyToMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Yes|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|reply\_to\_peer\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|quote\_text|[string](/API_docs/types/string.html) | Optional|
|quote\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToMessage = ['_' => 'inputReplyToMessage', 'reply_to_msg_id' => int, 'top_msg_id' => int, 'reply_to_peer_id' => InputPeer, 'quote_text' => 'string', 'quote_entities' => [MessageEntity, MessageEntity]];
```  

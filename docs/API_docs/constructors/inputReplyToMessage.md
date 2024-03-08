---
title: "inputReplyToMessage"
description: "Reply to a message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputReplyToMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Reply to a message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Yes|The message ID to reply to.|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|This field must contain the topic ID **only** when replying to messages in forum topics different from the "General" topic (i.e. `reply_to_msg_id` is set and `reply_to_msg_id != topicID` and `topicID != 1`).  <br>If the replied-to message is deleted before the method finishes execution, the value in this field will be used to send the message to the correct topic, instead of the "General" topic.|
|reply\_to\_peer\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Used to reply to messages sent to another chat (specified here), can only be used for non-`protected` chats and messages.|
|quote\_text|[string](/API_docs/types/string.html) | Optional|Used to quote-reply to only a certain section (specified here) of the original message. The maximum UTF-8 length for quotes is specified in the [quote\_length\_max](https://core.telegram.org/api/config#quote-length-max) config key.|
|quote\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities) from the `quote_text` field.|
|quote\_offset|[int](/API_docs/types/int.html) | Optional|Offset of the message `quote_text` within the original message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length)).|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToMessage = ['_' => 'inputReplyToMessage', 'reply_to_msg_id' => int, 'top_msg_id' => int, 'reply_to_peer_id' => InputPeer, 'quote_text' => 'string', 'quote_entities' => [MessageEntity, MessageEntity], 'quote_offset' => int];
```  

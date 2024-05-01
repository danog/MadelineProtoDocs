---
title: "sendMessageEmojiInteraction"
description: "User has clicked on an animated emoji triggering a reaction, click here for more info »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageEmojiInteraction  
[Back to constructors index](/API_docs/constructors/index.html)



User has clicked on an animated emoji triggering a [reaction, click here for more info »](https://core.telegram.org/api/animated-emojis#emoji-reactions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.html) | Yes|Emoji|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID of the animated emoji that was clicked|
|interaction|[DataJSON](/API_docs/types/DataJSON.html) | Yes|A JSON object with interaction info, [click here for more info »](https://core.telegram.org/api/animated-emojis#emoji-reactions)|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```
$sendMessageEmojiInteraction = ['_' => 'sendMessageEmojiInteraction', 'emoticon' => 'string', 'msg_id' => int, 'interaction' => DataJSON];
```  

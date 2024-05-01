---
title: "sendMessageEmojiInteractionSeen"
description: "User is watching an animated emoji reaction triggered by another user, click here for more info »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageEmojiInteractionSeen  
[Back to constructors index](/API_docs/constructors/index.html)



User is watching an animated emoji reaction triggered by another user, [click here for more info »](https://core.telegram.org/api/animated-emojis#emoji-reactions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.html) | Yes|Emoji|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```
$sendMessageEmojiInteractionSeen = ['_' => 'sendMessageEmojiInteractionSeen', 'emoticon' => 'string'];
```  

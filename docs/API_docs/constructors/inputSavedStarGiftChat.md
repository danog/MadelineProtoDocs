---
title: "inputSavedStarGiftChat"
description: "A gift received by a channel we own."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSavedStarGiftChat  
[Back to constructors index](/API_docs/constructors/index.html)



A gift received by a channel we own.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The channel.|
|saved\_id|[long](/API_docs/types/long.html) | Yes|ID of the gift, must be the `saved_id` of a [messageActionStarGift](../constructors/messageActionStarGift.html)/[messageActionStarGiftUnique](../constructors/messageActionStarGiftUnique.html) constructor.|



### Type: [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html)


### Example:

```
$inputSavedStarGiftChat = ['_' => 'inputSavedStarGiftChat', 'peer' => InputPeer, 'saved_id' => long];
```  

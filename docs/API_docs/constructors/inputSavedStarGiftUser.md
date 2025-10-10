---
title: "inputSavedStarGiftUser"
description: "A gift received in a private chat with another user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSavedStarGiftUser  
[Back to constructors index](/API_docs/constructors/index.html)



A gift received in a private chat with another user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the [messageService](../constructors/messageService.html) with the [messageActionStarGift](../constructors/messageActionStarGift.html) with the gift.|



### Type: [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html)


### Example:

```
$inputSavedStarGiftUser = ['_' => 'inputSavedStarGiftUser', 'msg_id' => int];
```  

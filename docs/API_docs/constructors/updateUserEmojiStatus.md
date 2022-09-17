---
title: "updateUserEmojiStatus"
description: "updateUserEmojiStatus attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserEmojiStatus  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUserEmojiStatus = ['_' => 'updateUserEmojiStatus', 'user_id' => long, 'emoji_status' => EmojiStatus];
```  

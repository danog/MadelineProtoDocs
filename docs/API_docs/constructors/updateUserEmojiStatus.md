---
title: "updateUserEmojiStatus"
description: "The emoji status of a certain user has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserEmojiStatus  
[Back to constructors index](/API_docs/constructors/index.html)



The [emoji status](https://core.telegram.org/api/emoji-status) of a certain user has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|New [emoji status](https://core.telegram.org/api/emoji-status)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUserEmojiStatus = ['_' => 'updateUserEmojiStatus', 'user_id' => long, 'emoji_status' => EmojiStatus];
```  

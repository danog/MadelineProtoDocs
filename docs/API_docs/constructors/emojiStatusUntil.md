---
title: "emojiStatusUntil"
description: "An emoji status valid until the specified date"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiStatusUntil  
[Back to constructors index](/API_docs/constructors/index.html)



An [emoji status](https://core.telegram.org/api/emoji-status) valid until the specified date

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](/API_docs/types/long.html) | Yes|[Custom emoji document ID](https://core.telegram.org/api/custom-emoji)|
|until|[int](/API_docs/types/int.html) | Yes|This status is valid until this date|



### Type: [EmojiStatus](/API_docs/types/EmojiStatus.html)


### Example:

```
$emojiStatusUntil = ['_' => 'emojiStatusUntil', 'document_id' => long, 'until' => int];
```  

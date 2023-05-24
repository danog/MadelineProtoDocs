---
title: "account.emojiStatuses"
description: "A list of emoji statuses"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_emojiStatuses.html
---
# Constructor: account.emojiStatuses  
[Back to constructors index](/API_docs/constructors/index.html)



A list of [emoji statuses](https://core.telegram.org/api/emoji-status)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|statuses|Array of [EmojiStatus](/API_docs/types/EmojiStatus.html) | Yes|[Emoji statuses](https://core.telegram.org/api/emoji-status)|



### Type: [account.EmojiStatuses](/API_docs/types/account.EmojiStatuses.html)


### Example:

```
$account_emojiStatuses = ['_' => 'account.emojiStatuses', 'hash' => long, 'statuses' => [EmojiStatus, EmojiStatus]];
```  

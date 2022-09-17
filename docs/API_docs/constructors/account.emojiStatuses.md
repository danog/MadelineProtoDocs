---
title: "account.emojiStatuses"
description: "account.emojiStatuses attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_emojiStatuses.html
---
# Constructor: account.emojiStatuses  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|statuses|Array of [EmojiStatus](/API_docs/types/EmojiStatus.html) | Yes|



### Type: [account.EmojiStatuses](/API_docs/types/account.EmojiStatuses.html)


### Example:

```
$account_emojiStatuses = ['_' => 'account.emojiStatuses', 'hash' => long, 'statuses' => [EmojiStatus, EmojiStatus]];
```  

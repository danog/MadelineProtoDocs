---
title: "emojiKeywordDeleted"
description: "Deleted emoji keyword"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiKeywordDeleted  
[Back to constructors index](/API_docs/constructors/index.md)



Deleted emoji keyword

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|keyword|[string](/API_docs/types/string.md) | Yes|Keyword|
|emoticons|Array of [string](/API_docs/types/string.md) | Yes|Emojis that were associated to keyword|



### Type: [EmojiKeyword](/API_docs/types/EmojiKeyword.md)


### Example:

```php
$emojiKeywordDeleted = ['_' => 'emojiKeywordDeleted', 'keyword' => 'string', 'emoticons' => ['string', 'string']];
```  

---
title: "emojiKeywordDeleted"
description: "Deleted emoji keyword"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiKeywordDeleted  
[Back to constructors index](index.md)



Deleted emoji keyword

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|keyword|[string](../types/string.md) | Yes|Keyword|
|emoticons|Array of [string](../types/string.md) | Yes|Emojis that were associated to keyword|



### Type: [EmojiKeyword](../types/EmojiKeyword.md)


### Example:

```php
$emojiKeywordDeleted = ['_' => 'emojiKeywordDeleted', 'keyword' => 'string', 'emoticons' => ['string', 'string']];
```  


Or, if you're into Lua:

```lua
emojiKeywordDeleted={_='emojiKeywordDeleted', keyword='string', emoticons={'string'}}

```



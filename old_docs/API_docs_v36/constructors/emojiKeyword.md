---
title: emojiKeyword
description: Emoji keyword
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiKeyword  
[Back to constructors index](index.md)



Emoji keyword

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|keyword|[string](../types/string.md) | Yes|Keyword|
|emoticons|Array of [string](../types/string.md) | Yes|Emojis associated to keyword|



### Type: [EmojiKeyword](../types/EmojiKeyword.md)


### Example:

```php
$emojiKeyword = ['_' => 'emojiKeyword', 'keyword' => 'string', 'emoticons' => ['string', 'string']];
```  


Or, if you're into Lua:

```lua
emojiKeyword={_='emojiKeyword', keyword='string', emoticons={'string'}}

```



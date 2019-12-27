---
title: emojiKeywordsDifference
description: Changes to emoji keywords
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiKeywordsDifference  
[Back to constructors index](index.md)



Changes to emoji keywords

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](../types/string.md) | Yes|Language code for keywords|
|from\_version|[int](../types/int.md) | Yes|Previous emoji keyword list version|
|version|[int](../types/int.md) | Yes|Current version of emoji keyword list|
|keywords|Array of [EmojiKeyword](../types/EmojiKeyword.md) | Yes|Keywords|



### Type: [EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)


### Example:

```php
$emojiKeywordsDifference = ['_' => 'emojiKeywordsDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'keywords' => [EmojiKeyword, EmojiKeyword]];
```  


Or, if you're into Lua:

```lua
emojiKeywordsDifference={_='emojiKeywordsDifference', lang_code='string', from_version=int, version=int, keywords={EmojiKeyword}}

```



---
title: "emojiKeywordsDifference"
description: "Changes to emoji keywords"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiKeywordsDifference  
[Back to constructors index](/API_docs/constructors/index.md)



Changes to emoji keywords

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](/API_docs/types/string.md) | Yes|Language code for keywords|
|from\_version|[int](/API_docs/types/int.md) | Yes|Previous emoji keyword list version|
|version|[int](/API_docs/types/int.md) | Yes|Current version of emoji keyword list|
|keywords|Array of [EmojiKeyword](/API_docs/types/EmojiKeyword.md) | Yes|Emojis associated to keywords|



### Type: [EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.md)


### Example:

```php
$emojiKeywordsDifference = ['_' => 'emojiKeywordsDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'keywords' => [EmojiKeyword, EmojiKeyword]];
```  

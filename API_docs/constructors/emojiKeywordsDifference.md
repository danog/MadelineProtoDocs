# emojiKeywordsDifference

> Changes to emoji keywords

[Back to constructors index](/API_docs/constructors/index.html)



Changes to emoji keywords

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](/API_docs/types/string.html) | Yes|Language code for keywords|
|from\_version|[int](/API_docs/types/int.html) | Yes|Previous emoji keyword list version|
|version|[int](/API_docs/types/int.html) | Yes|Current version of emoji keyword list|
|keywords|Array of [EmojiKeyword](/API_docs/types/EmojiKeyword.html) | Yes|Emojis associated to keywords|



### Type: [EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.html)


### Example:

```
$emojiKeywordsDifference = ['_' => 'emojiKeywordsDifference', 'lang_code' => 'string', 'from_version' => int, 'version' => int, 'keywords' => [EmojiKeyword, EmojiKeyword]];
```

---
title: "emojiURL"
description: "An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiURL  
[Back to constructors index](index.md)



An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation|



### Type: [EmojiURL](../types/EmojiURL.md)


### Example:

```php
$emojiURL = ['_' => 'emojiURL', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
emojiURL={_='emojiURL', url='string'}

```



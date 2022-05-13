---
title: "emojiURL"
description: "An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiURL  
[Back to constructors index](/API_docs/constructors/index.html)



An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|An HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation|



### Type: [EmojiURL](/API_docs/types/EmojiURL.html)


### Example:

```
$emojiURL = ['_' => 'emojiURL', 'url' => 'string'];
```  

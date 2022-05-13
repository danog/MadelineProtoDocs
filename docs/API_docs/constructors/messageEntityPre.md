---
title: "messageEntityPre"
description: "Message entity representing a preformatted codeblock, allowing the user to specify a programming language for the codeblock."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityPre  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a preformatted `codeblock`, allowing the user to specify a programming language for the codeblock.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|language|[string](/API_docs/types/string.html) | Yes|Programming language of the code|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityPre = ['_' => 'messageEntityPre', 'offset' => int, 'length' => int, 'language' => 'string'];
```  

---
title: "messageEntityBold"
description: "Message entity representing bold text."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBold  
[Back to constructors index](/API_docs/constructors/index.md)



Message entity representing **bold text**.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.md)


### Example:

```php
$messageEntityBold = ['_' => 'messageEntityBold', 'offset' => int, 'length' => int];
```  

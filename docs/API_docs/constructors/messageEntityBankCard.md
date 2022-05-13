---
title: "messageEntityBankCard"
description: "Indicates a credit card number"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBankCard  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a credit card number

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityBankCard = ['_' => 'messageEntityBankCard', 'offset' => int, 'length' => int];
```  

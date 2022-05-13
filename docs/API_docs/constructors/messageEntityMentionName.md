---
title: "messageEntityMentionName"
description: "Message entity representing a user mention: for creating a mention use inputMessageEntityMentionName."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityMentionName  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a [user mention](https://core.telegram.org/api/mentions): for *creating* a mention use [inputMessageEntityMentionName](../constructors/inputMessageEntityMentionName.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|user\_id|[long](/API_docs/types/long.html) | Yes|Identifier of the user that was mentioned|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityMentionName = ['_' => 'messageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => long];
```  

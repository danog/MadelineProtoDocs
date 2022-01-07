---
title: "inputMessageEntityMentionName"
description: "Message entity that can be used to create a user user mention: received mentions use the messageEntityMentionName constructor, instead."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageEntityMentionName  
[Back to constructors index](/API_docs/constructors/index.md)



Message entity that can be used to create a user [user mention](https://core.telegram.org/api/mentions): received mentions use the [messageEntityMentionName](../constructors/messageEntityMentionName.md) constructor, instead.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|user\_id|[InputUser](/API_docs/types/InputUser.md) | Optional|Identifier of the user that was mentioned|



### Type: [MessageEntity](/API_docs/types/MessageEntity.md)


### Example:

```php
$inputMessageEntityMentionName = ['_' => 'inputMessageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => InputUser];
```  

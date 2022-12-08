---
title: "messageActionTopicCreate"
description: "messageActionTopicCreate attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionTopicCreate  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|icon\_color|[int](/API_docs/types/int.html) | Yes|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTopicCreate = ['_' => 'messageActionTopicCreate', 'title' => 'string', 'icon_color' => int, 'icon_emoji_id' => long];
```  

---
title: "updateEditForumTopic"
description: "updateEditForumTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditForumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|topic\_id|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEditForumTopic = ['_' => 'updateEditForumTopic', 'peer' => long, 'topic_id' => int, 'title' => 'string', 'icon_emoji_id' => long, 'closed' => Bool, 'hidden' => Bool];
```  

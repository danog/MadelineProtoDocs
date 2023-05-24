---
title: "messageActionTopicEdit"
description: "Forum topic information was edited."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionTopicEdit  
[Back to constructors index](/API_docs/constructors/index.html)



[Forum topic](https://core.telegram.org/api/forum#forum-topics) information was edited.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Optional|Topic title.|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|ID of the [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon.|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was closed.|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was hidden (only valid for the "General" topic, `id=1`).|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTopicEdit = ['_' => 'messageActionTopicEdit', 'title' => 'string', 'icon_emoji_id' => long, 'closed' => Bool, 'hidden' => Bool];
```  

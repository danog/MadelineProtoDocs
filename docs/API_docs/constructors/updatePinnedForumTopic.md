---
title: "updatePinnedForumTopic"
description: "updatePinnedForumTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedForumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Yes|
|topic\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePinnedForumTopic = ['_' => 'updatePinnedForumTopic', 'pinned' => Bool, 'peer' => long, 'topic_id' => int];
```  

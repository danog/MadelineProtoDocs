---
title: "updatePinnedForumTopics"
description: "updatePinnedForumTopics attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedForumTopics  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|order|Array of [int](/API_docs/types/int.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePinnedForumTopics = ['_' => 'updatePinnedForumTopics', 'peer' => long, 'order' => [int, int]];
```  

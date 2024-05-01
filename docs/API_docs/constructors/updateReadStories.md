---
title: "updateReadStories"
description: "Stories of a specific peer were marked as read."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadStories  
[Back to constructors index](/API_docs/constructors/index.html)



Stories of a specific peer were marked as read.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer|
|max\_id|[int](/API_docs/types/int.html) | Yes|ID of the last story that was marked as read|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadStories = ['_' => 'updateReadStories', 'peer' => long, 'max_id' => int];
```  

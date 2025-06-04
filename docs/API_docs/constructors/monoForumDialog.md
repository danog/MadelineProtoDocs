---
title: "monoForumDialog"
description: "monoForumDialog attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: monoForumDialog  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|unread\_mark|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Yes|
|top\_message|[int](/API_docs/types/int.html) | Yes|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|
|unread\_count|[int](/API_docs/types/int.html) | Yes|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|



### Type: [SavedDialog](/API_docs/types/SavedDialog.html)


### Example:

```
$monoForumDialog = ['_' => 'monoForumDialog', 'unread_mark' => Bool, 'peer' => long, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_reactions_count' => int, 'draft' => DraftMessage];
```  

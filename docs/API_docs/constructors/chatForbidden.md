---
title: "chatForbidden"
description: "A group to which the user has no access. E.g., because the user was kicked from the group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatForbidden  
[Back to constructors index](/API_docs/constructors/index.html)



A group to which the user has no access. E.g., because the user was kicked from the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|User identifier|
|title|[string](/API_docs/types/string.html) | Yes|Group name|



### Type: [Chat](/API_docs/types/Chat.html)


### Example:

```
$chatForbidden = ['_' => 'chatForbidden', 'id' => long, 'title' => 'string'];
```  

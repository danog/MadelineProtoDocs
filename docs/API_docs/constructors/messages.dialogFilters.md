---
title: "messages.dialogFilters"
description: "messages.dialogFilters attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogFilters.html
---
# Constructor: messages.dialogFilters  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|tags\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|
|filters|Array of [DialogFilter](/API_docs/types/DialogFilter.html) | Yes|



### Type: [messages.DialogFilters](/API_docs/types/messages.DialogFilters.html)


### Example:

```
$messages_dialogFilters = ['_' => 'messages.dialogFilters', 'tags_enabled' => Bool, 'filters' => [DialogFilter, DialogFilter]];
```  

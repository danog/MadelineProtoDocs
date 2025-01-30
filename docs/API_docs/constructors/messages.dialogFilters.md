---
title: "messages.dialogFilters"
description: "Folder and folder tags information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogFilters.html
---
# Constructor: messages.dialogFilters  
[Back to constructors index](/API_docs/constructors/index.html)



[Folder and folder tags](https://core.telegram.org/api/folders) information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tags\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether [folder tags](https://core.telegram.org/api/folders#folder-tags) are enabled.|
|filters|Array of [DialogFilter](/API_docs/types/DialogFilter.html) | Yes|Folders.|



### Type: [messages.DialogFilters](/API_docs/types/messages.DialogFilters.html)


### Example:

```
$messages_dialogFilters = ['_' => 'messages.dialogFilters', 'tags_enabled' => Bool, 'filters' => [DialogFilter, DialogFilter]];
```  

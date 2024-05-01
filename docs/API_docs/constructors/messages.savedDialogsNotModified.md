---
title: "messages.savedDialogsNotModified"
description: "The saved dialogs haven't changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedDialogsNotModified.html
---
# Constructor: messages.savedDialogsNotModified  
[Back to constructors index](/API_docs/constructors/index.html)



The saved dialogs haven't changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of [saved dialogs](https://core.telegram.org/api/saved-messages) found server-side by the query|



### Type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)


### Example:

```
$messages_savedDialogsNotModified = ['_' => 'messages.savedDialogsNotModified', 'count' => int];
```  

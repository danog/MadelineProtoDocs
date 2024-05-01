---
title: "messages.dialogsNotModified"
description: "Dialogs haven't changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogsNotModified.html
---
# Constructor: messages.dialogsNotModified  
[Back to constructors index](/API_docs/constructors/index.html)



Dialogs haven't changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of dialogs found server-side by the query|



### Type: [messages.Dialogs](/API_docs/types/messages.Dialogs.html)


### Example:

```
$messages_dialogsNotModified = ['_' => 'messages.dialogsNotModified', 'count' => int];
```  

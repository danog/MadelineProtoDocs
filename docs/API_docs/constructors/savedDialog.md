---
title: "savedDialog"
description: "Represents a saved dialog »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedDialog  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [saved dialog »](https://core.telegram.org/api/saved-messages).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Is the dialog pinned|
|peer|[long](/API_docs/types/long.html) | Yes|The dialog|
|top\_message|[int](/API_docs/types/int.html) | Yes|The latest message ID|



### Type: [SavedDialog](/API_docs/types/SavedDialog.html)


### Example:

```
$savedDialog = ['_' => 'savedDialog', 'pinned' => Bool, 'peer' => long, 'top_message' => int];
```  

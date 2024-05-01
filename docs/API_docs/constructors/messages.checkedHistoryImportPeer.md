---
title: "messages.checkedHistoryImportPeer"
description: "Contains a confirmation text to be shown to the user, upon importing chat history, click here for more info »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_checkedHistoryImportPeer.html
---
# Constructor: messages.checkedHistoryImportPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Contains a confirmation text to be shown to the user, upon [importing chat history, click here for more info »](https://core.telegram.org/api/import).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|confirm\_text|[string](/API_docs/types/string.html) | Yes|A confirmation text to be shown to the user, upon [importing chat history »](https://core.telegram.org/api/import).|



### Type: [messages.CheckedHistoryImportPeer](/API_docs/types/messages.CheckedHistoryImportPeer.html)


### Example:

```
$messages_checkedHistoryImportPeer = ['_' => 'messages.checkedHistoryImportPeer', 'confirm_text' => 'string'];
```  

---
title: "autoSaveException"
description: "Peer-specific media autosave settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: autoSaveException  
[Back to constructors index](/API_docs/constructors/index.html)



Peer-specific media autosave settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer|
|settings|[AutoSaveSettings](/API_docs/types/AutoSaveSettings.html) | Yes|Media autosave settings|



### Type: [AutoSaveException](/API_docs/types/AutoSaveException.html)


### Example:

```
$autoSaveException = ['_' => 'autoSaveException', 'peer' => long, 'settings' => AutoSaveSettings];
```  

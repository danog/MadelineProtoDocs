---
title: "updateGroupCallConnection"
description: "New WebRTC parameters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallConnection  
[Back to constructors index](/API_docs/constructors/index.html)



New WebRTC parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|presentation|[Bool](/API_docs/types/Bool.html) | Optional|Are these parameters related to the screen capture session currently in progress?|
|params|[DataJSON](/API_docs/types/DataJSON.html) | Yes|WebRTC parameters|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallConnection = ['_' => 'updateGroupCallConnection', 'presentation' => Bool, 'params' => DataJSON];
```  

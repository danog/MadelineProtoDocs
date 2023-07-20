---
title: "documentAttributeVideo"
description: "Defines a video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo\_66  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a round video|
|duration|[int](/API_docs/types/int.html) | Optional|
|w|[int](/API_docs/types/int.html) | Optional|Video width|
|h|[int](/API_docs/types/int.html) | Optional|Video height|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.html)


### Example:

```
$documentAttributeVideo_66 = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  

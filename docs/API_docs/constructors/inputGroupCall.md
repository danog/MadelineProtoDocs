---
title: "inputGroupCall"
description: "Points to a specific group call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



Points to a specific group call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Group call ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Group call access hash|



### Type: [InputGroupCall](/API_docs/types/InputGroupCall.html)


### Example:

```
$inputGroupCall = ['_' => 'inputGroupCall', 'id' => long, 'access_hash' => long];
```  

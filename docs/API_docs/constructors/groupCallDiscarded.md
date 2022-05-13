---
title: "groupCallDiscarded"
description: "An ended group call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallDiscarded  
[Back to constructors index](/API_docs/constructors/index.html)



An ended group call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Group call ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Group call access hash|
|duration|[int](/API_docs/types/int.html) | Yes|Group call duration|



### Type: [GroupCall](/API_docs/types/GroupCall.html)


### Example:

```
$groupCallDiscarded = ['_' => 'groupCallDiscarded', 'id' => long, 'access_hash' => long, 'duration' => int];
```  

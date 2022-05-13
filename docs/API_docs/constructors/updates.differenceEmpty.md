---
title: "updates.differenceEmpty"
description: "No events."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_differenceEmpty.html
---
# Constructor: updates.differenceEmpty  
[Back to constructors index](/API_docs/constructors/index.html)



No events.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|Current date|
|seq|[int](/API_docs/types/int.html) | Yes|Number of sent updates|



### Type: [updates.Difference](/API_docs/types/updates.Difference.html)


### Example:

```
$updates_differenceEmpty = ['_' => 'updates.differenceEmpty', 'date' => int, 'seq' => int];
```  

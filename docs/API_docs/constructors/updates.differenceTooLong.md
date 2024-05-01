---
title: "updates.differenceTooLong"
description: "The difference is too long, and the specified state must be used to refetch updates."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_differenceTooLong.html
---
# Constructor: updates.differenceTooLong  
[Back to constructors index](/API_docs/constructors/index.html)



The difference is [too long](https://core.telegram.org/api/updates#recovering-gaps), and the specified state must be used to refetch updates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](/API_docs/types/int.html) | Yes|The new state to use.|



### Type: [updates.Difference](/API_docs/types/updates.Difference.html)


### Example:

```
$updates_differenceTooLong = ['_' => 'updates.differenceTooLong', 'pts' => int];
```  

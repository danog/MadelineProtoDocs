---
title: "defaultHistoryTTL"
description: "Contains info about the default value of the Time-To-Live setting, applied to all new chats."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: defaultHistoryTTL  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about the default value of the Time-To-Live setting, applied to all new chats.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[int](/API_docs/types/int.html) | Yes|Time-To-Live setting applied to all new chats.|



### Type: [DefaultHistoryTTL](/API_docs/types/DefaultHistoryTTL.html)


### Example:

```
$defaultHistoryTTL = ['_' => 'defaultHistoryTTL', 'period' => int];
```  

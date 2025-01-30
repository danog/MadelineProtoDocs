---
title: "outboxReadDate"
description: "Exact read date of a private message we sent to another user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: outboxReadDate  
[Back to constructors index](/API_docs/constructors/index.html)



Exact read date of a private message we sent to another user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|UNIX timestamp with the read date.|



### Type: [OutboxReadDate](/API_docs/types/OutboxReadDate.html)


### Example:

```
$outboxReadDate = ['_' => 'outboxReadDate', 'date' => int];
```  

---
title: "updateMessageID"
description: "Sent message with random_id client identifier was assigned an identifier."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageID  
[Back to constructors index](/API_docs/constructors/index.html)



Sent message with **random\_id** client identifier was assigned an identifier.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|**id** identifier of a respective [Message](../types/Message.html)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageID = ['_' => 'updateMessageID', 'id' => int];
```  

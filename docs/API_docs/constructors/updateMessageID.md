---
title: "updateMessageID"
description: "Sent message with random_id client identifier was assigned an identifier."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageID  
[Back to constructors index](/API_docs/constructors/index.md)



Sent message with **random\_id** client identifier was assigned an identifier.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.md) | Yes|**id** identifier of a respective [Message](../types/Message.md)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateMessageID = ['_' => 'updateMessageID', 'id' => int];
```  

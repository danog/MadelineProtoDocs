---
title: "updateBotDeleteBusinessMessage"
description: "updateBotDeleteBusinessMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotDeleteBusinessMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|connection\_id|[string](/API_docs/types/string.html) | Yes|
|peer|[long](/API_docs/types/long.html) | Yes|
|messages|Array of [int](/API_docs/types/int.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotDeleteBusinessMessage = ['_' => 'updateBotDeleteBusinessMessage', 'connection_id' => 'string', 'peer' => long, 'messages' => [int, int], 'qts' => int];
```  

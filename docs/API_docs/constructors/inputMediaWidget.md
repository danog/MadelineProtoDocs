---
title: "inputMediaWidget"
description: "inputMediaWidget attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaWidget  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|allow\_queries|[Bool](/API_docs/types/Bool.html) | Optional|
|shared\_widget|[Bool](/API_docs/types/Bool.html) | Optional|
|width|[int](/API_docs/types/int.html) | Yes|
|height|[int](/API_docs/types/int.html) | Yes|
|html|[string](/API_docs/types/string.html) | Yes|
|public\_data|[string](/API_docs/types/string.html) | Optional|
|chat\_data|[string](/API_docs/types/string.html) | Optional|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaWidget = ['_' => 'inputMediaWidget', 'allow_queries' => Bool, 'shared_widget' => Bool, 'width' => int, 'height' => int, 'html' => 'string', 'public_data' => 'string', 'chat_data' => 'string'];
```  

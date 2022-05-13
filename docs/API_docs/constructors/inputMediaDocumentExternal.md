---
title: "inputMediaDocumentExternal"
description: "Document that will be downloaded by the telegram servers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocumentExternal  
[Back to constructors index](/API_docs/constructors/index.html)



Document that will be downloaded by the telegram servers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|URL of the document|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Self-destruct time to live of document|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaDocumentExternal = ['_' => 'inputMediaDocumentExternal', 'url' => 'string', 'ttl_seconds' => int];
```  

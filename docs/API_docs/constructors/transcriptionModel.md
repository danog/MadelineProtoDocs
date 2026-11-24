---
title: "transcriptionModel"
description: "transcriptionModel attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: transcriptionModel  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|document|[Document](/API_docs/types/Document.html) | Optional|
|languages|Array of [string](/API_docs/types/string.html) | Yes|
|version|[int](/API_docs/types/int.html) | Yes|



### Type: [TranscriptionModel](/API_docs/types/TranscriptionModel.html)


### Example:

```
$transcriptionModel = ['_' => 'transcriptionModel', 'document' => Document, 'languages' => ['string', 'string'], 'version' => int];
```  

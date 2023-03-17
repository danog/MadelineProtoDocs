---
title: "botApp"
description: "botApp attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botApp  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](/API_docs/types/long.html) | Yes|
|access\_hash|[long](/API_docs/types/long.html) | Yes|
|short\_name|[string](/API_docs/types/string.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|
|document|[Document](/API_docs/types/Document.html) | Optional|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [BotApp](/API_docs/types/BotApp.html)


### Example:

```
$botApp = ['_' => 'botApp', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document, 'hash' => long];
```  

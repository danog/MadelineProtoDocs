---
title: "users.savedMusic"
description: "users.savedMusic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_savedMusic.html
---
# Constructor: users.savedMusic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [users.SavedMusic](/API_docs/types/users.SavedMusic.html)


### Example:

```
$users_savedMusic = ['_' => 'users.savedMusic', 'count' => int, 'documents' => [Document, Document]];
```  

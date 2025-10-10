---
title: "users.savedMusic"
description: "List of songs currently pinned on a user's profile, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_savedMusic.html
---
# Constructor: users.savedMusic  
[Back to constructors index](/API_docs/constructors/index.html)



List of songs currently pinned on a user's profile, see [here »](https://core.telegram.org/api/profile#music) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of songs (can be bigger than `documents` depending on the passed `limit`, and the default maximum `limit` in which case pagination is required).|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|Songs.|



### Type: [users.SavedMusic](/API_docs/types/users.SavedMusic.html)


### Example:

```
$users_savedMusic = ['_' => 'users.savedMusic', 'count' => int, 'documents' => [Document, Document]];
```  

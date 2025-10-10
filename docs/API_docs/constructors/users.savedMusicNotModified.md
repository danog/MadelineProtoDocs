---
title: "users.savedMusicNotModified"
description: "This subset of the songs currently pinned on a user's profile hasn't changed, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/users_savedMusicNotModified.html
---
# Constructor: users.savedMusicNotModified  
[Back to constructors index](/API_docs/constructors/index.html)



This subset of the songs currently pinned on a user's profile hasn't changed, see [here »](https://core.telegram.org/api/profile#music) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of songs on the user's profile.|



### Type: [users.SavedMusic](/API_docs/types/users.SavedMusic.html)


### Example:

```
$users_savedMusicNotModified = ['_' => 'users.savedMusicNotModified', 'count' => int];
```  

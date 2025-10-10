---
title: "account.savedMusicIds"
description: "List of IDs of songs (document.ids) currently pinned on our profile, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_savedMusicIds.html
---
# Constructor: account.savedMusicIds  
[Back to constructors index](/API_docs/constructors/index.html)



List of IDs of songs ([document](../constructors/document.html).`id`s) currently pinned on our profile, see [here »](https://core.telegram.org/api/profile#music) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ids|Array of [long](/API_docs/types/long.html) | Yes|Full list of [document](../constructors/document.html).`id`s|



### Type: [account.SavedMusicIds](/API_docs/types/account.SavedMusicIds.html)


### Example:

```
$account_savedMusicIds = ['_' => 'account.savedMusicIds', 'ids' => [long, long]];
```  

---
title: "shareThemeEmojiBackdrop"
description: "shareThemeEmojiBackdrop attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: shareThemeEmojiBackdrop  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|backdrop\_id|[int](/API_docs/types/int.html) | Optional|
|emojis|Array of [Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [ShareTheme](/API_docs/types/ShareTheme.html)


### Example:

```
$shareThemeEmojiBackdrop = ['_' => 'shareThemeEmojiBackdrop', 'backdrop_id' => int, 'emojis' => [Reaction, Reaction]];
```  

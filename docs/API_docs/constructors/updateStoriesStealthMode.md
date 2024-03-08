---
title: "updateStoriesStealthMode"
description: "Indicates that stories stealth mode was activated."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStoriesStealthMode  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates that [stories stealth mode](https://core.telegram.org/api/stories#stealth-mode) was activated.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stealth\_mode|[StoriesStealthMode](/API_docs/types/StoriesStealthMode.html) | Yes|Information about the current [stealth mode](https://core.telegram.org/api/stories#stealth-mode) session.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStoriesStealthMode = ['_' => 'updateStoriesStealthMode', 'stealth_mode' => StoriesStealthMode];
```  

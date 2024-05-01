---
title: "updateStoryID"
description: "A story was successfully uploaded."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStoryID  
[Back to constructors index](/API_docs/constructors/index.html)



A story was successfully uploaded.

Once a story is successfully uploaded, an [updateStoryID](../constructors/updateStoryID.html) will be returned, indicating the story ID (`id`) that was attributed to the story (like for messages, `random_id` indicates the `random_id` that was passed to [stories.sendStory](../methods/stories.sendStory.html): this way, you can tell which story was assigned a specific `id` by checking which [stories.sendStory](../methods/stories.sendStory.html) call has the returned `random_id`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|The `id` that was attributed to the story.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStoryID = ['_' => 'updateStoryID', 'id' => int];
```  

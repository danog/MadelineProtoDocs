---
title: "webPageAttributeStory"
description: "Webpage preview of a Telegram story"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeStory  
[Back to constructors index](/API_docs/constructors/index.html)



Webpage preview of a Telegram story

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer that posted the story|
|id|[int](/API_docs/types/int.html) | Yes|[Story ID](https://core.telegram.org/api/stories#watching-stories)|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Optional|May contain the story, if not the story should be fetched when and if needed using [stories.getStoriesByID](../methods/stories.getStoriesByID.html) with the above `id` and `peer`.|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeStory = ['_' => 'webPageAttributeStory', 'peer' => long, 'id' => int, 'story' => StoryItem];
```  

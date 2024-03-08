---
title: "stories.allStories"
description: "Full list of active (or active and hidden) stories."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_allStories.html
---
# Constructor: stories.allStories  
[Back to constructors index](/API_docs/constructors/index.html)



Full list of active (or active and hidden) [stories](https://core.telegram.org/api/stories#watching-stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_more|[Bool](/API_docs/types/Bool.html) | Optional|Whether more results can be fetched as [described here »](https://core.telegram.org/api/stories#watching-stories).|
|count|[int](/API_docs/types/int.html) | Yes|Total number of active (or active and hidden) stories|
|state|[string](/API_docs/types/string.html) | Yes|State to use for pagination|
|peer\_stories|Array of [PeerStories](/API_docs/types/PeerStories.html) | Yes|Stories|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|
|stealth\_mode|[StoriesStealthMode](/API_docs/types/StoriesStealthMode.html) | Yes|Current [stealth mode](https://core.telegram.org/api/stories#stealth-mode) information|



### Type: [stories.AllStories](/API_docs/types/stories.AllStories.html)


### Example:

```
$stories_allStories = ['_' => 'stories.allStories', 'has_more' => Bool, 'count' => int, 'state' => 'string', 'peer_stories' => [PeerStories, PeerStories], 'chats' => [Chat, Chat], 'users' => [User, User], 'stealth_mode' => StoriesStealthMode];
```  

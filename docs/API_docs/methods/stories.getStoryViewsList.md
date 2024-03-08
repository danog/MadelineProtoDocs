---
title: "stories.getStoryViewsList"
description: "Obtain the list of users that have viewed a specific [story we posted](https://core.telegram.org/api/stories)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_getStoryViewsList.html
---
# Method: stories.getStoryViewsList
[Back to methods index](index.html)



Obtain the list of users that have viewed a specific [story we posted](https://core.telegram.org/api/stories)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|just\_contacts|[Bool](/API_docs/types/Bool.html) | Whether to only fetch view reaction/views made by our [contacts](https://core.telegram.org/api/contacts) | Optional|
|reactions\_first|[Bool](/API_docs/types/Bool.html) | Whether to return [storyView](../constructors/storyView.html) info about users that reacted to the story (i.e. if set, the server will first sort results by view date as usual, and then also additionally sort the list by putting [storyView](../constructors/storyView.html)s with an associated reaction first in the list). Ignored if `forwards_first` is set. | Optional|
|forwards\_first|[Bool](/API_docs/types/Bool.html) | If set, returns forwards and reposts first, then reactions, then other views; otherwise returns interactions sorted just by interaction date. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the story was posted | Optional|
|q|[string](/API_docs/types/string.html) | Search for specific peers | Optional|
|id|[int](/API_docs/types/int.html) | Story ID | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination, obtained from [stories.storyViewsList](../constructors/stories.storyViewsList.html).`next_offset` | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stories.StoryViewsList](/API_docs/types/stories.StoryViewsList.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stories_StoryViewsList = $MadelineProto->stories->getStoryViewsList(just_contacts: $Bool, reactions_first: $Bool, forwards_first: $Bool, peer: $InputPeer, q: 'string', id: $int, offset: 'string', limit: $int, );
```


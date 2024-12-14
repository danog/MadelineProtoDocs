---
title: "stories.exportStoryLink"
description: "Generate a [story deep link](https://core.telegram.org/api/links#story-links) for a specific story"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_exportStoryLink.html
---
# Method: stories.exportStoryLink
[Back to methods index](index.html)



Generate a [story deep link](https://core.telegram.org/api/links#story-links) for a specific story

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the story was posted | Optional|
|id|[int](/API_docs/types/int.html) | Story ID | Optional|


### Return type: [ExportedStoryLink](/API_docs/types/ExportedStoryLink.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedStoryLink = $MadelineProto->stories->exportStoryLink(peer: $InputPeer, id: $int, );
```


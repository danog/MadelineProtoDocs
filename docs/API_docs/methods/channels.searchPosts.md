---
title: "channels.searchPosts"
description: "Globally search for posts from public [channels »](https://core.telegram.org/api/channel) (*including* those we aren't a member of) containing a specific hashtag."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_searchPosts.html
---
# Method: channels.searchPosts
[Back to methods index](index.html)



Globally search for posts from public [channels »](https://core.telegram.org/api/channel) (*including* those we aren't a member of) containing a specific hashtag.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hashtag|[string](/API_docs/types/string.html) | The hashtag to search, without the `#` character. | Optional|
|query|[string](/API_docs/types/string.html) |  | Optional|
|offset\_rate|[int](/API_docs/types/int.html) | Initially 0, then set to the [`next_rate` parameter of messages.messagesSlice](../constructors/messages.messagesSlice.html) | Optional|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|
|allow\_paid\_stars|[long](/API_docs/types/long.html) |  | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

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

$messages_Messages = $MadelineProto->channels->searchPosts(hashtag: 'string', query: 'string', offset_rate: $int, offset_peer: $InputPeer, offset_id: $int, limit: $int, allow_paid_stars: $long, );
```


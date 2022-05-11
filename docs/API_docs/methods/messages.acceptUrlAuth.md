---
title: "messages.acceptUrlAuth"
description: "Use this to accept a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_acceptUrlAuth.html
---
# Method: messages.acceptUrlAuth
[Back to methods index](index.html)



Use this to accept a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|write\_allowed|[Bool](/API_docs/types/Bool.html) | Set this flag to allow the bot to send messages to you (if requested) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The location of the message | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID of the message with the login button | Optional|
|button\_id|[int](/API_docs/types/int.html) | ID of the login button | Optional|
|url|[string](/API_docs/types/string.html) | URL used for [link URL authorization, click here for more info »](https://core.telegram.org/api/url-authorization#link-url-authorization) | Optional|


### Return type: [UrlAuthResult](/API_docs/types/UrlAuthResult.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$UrlAuthResult = $MadelineProto->messages->acceptUrlAuth(write_allowed: Bool, peer: InputPeer, msg_id: int, button_id: int, url: 'string', );
```


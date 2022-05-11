---
title: "messages.requestUrlAuth"
description: "Get more info about a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestUrlAuth.html
---
# Method: messages.requestUrlAuth
[Back to methods index](index.html)



Get more info about a Seamless Telegram Login authorization request, for more info [click here »](https://core.telegram.org/api/url-authorization)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the message is located | Optional|
|msg\_id|[int](/API_docs/types/int.html) | The message | Optional|
|button\_id|[int](/API_docs/types/int.html) | The ID of the button with the authorization request | Optional|
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
$UrlAuthResult = $MadelineProto->messages->requestUrlAuth(peer: InputPeer, msg_id: int, button_id: int, url: 'string', );
```


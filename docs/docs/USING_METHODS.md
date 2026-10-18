---
title: "Using methods"
description: "There are simplifications for many, if not all of, these methods."
nav_order: 31
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Using methods

There are simplifications for many, if not all of, these methods.

A list of all of the methods that can be called with MadelineProto can be found here: [here (layer 230)](https://docs.madelineproto.xyz/API_docs/).

 [Now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)

* [Named arguments](#named-arguments)
* [Peers](#peers)
* [Files](https://docs.madelineproto.xyz/docs/FILES.html)
* [Secret chats](#secret-chats)
* [Entities (Markdown & HTML)](#entities)
* [Rich messages](#rich-messages)
* [reply_markup (keyboards & inline keyboards)](#reply_markup)
* [bot API objects](#bot-api-objects)
* [No result](#no-result)
* [Multiple method calls](#multiple-method-calls)
* [Cancellation](#cancellation)
* [FULL API Documentation with descriptions](https://docs.madelineproto.xyz/API_docs/methods/)

## Named arguments

You must use named arguments instead of arrays to provide method arguments, which allows for much cleaner syntax:

```php
$MadelineProto->messages->sendMessage(peer: '@danogentili', message: 'Testing MadelineProto...');
```

## Peers
[Full example](https://github.com/danog/MadelineProto/blob/v8/bot.php)

If an object of type User, InputUser, Chat, InputChannel, Peer or InputPeer must be provided as a parameter to a method, you can substitute it with the user/group/channel's username (`@username`), bot API id (`-1029449`, `1249421`, `-100412412901`), or update.  

```php
$MadelineProto->messages->sendMessage(peer: '@danogentili', message: 'Testing MadelineProto...');
```


## Secret chats
[Full example](https://github.com/danog/MadelineProto/blob/v8/examples/secret_bot.php)
If an object of type InputSecretChat must be provided as a parameter to a method, you can substitute it with the secret chat's id, the updateNewEncrypted message or the decryptedMessage:

```php
$MadelineProto->messages->sendEncrypted(peer: $update, message: ['_' => 'decryptedMessage', 'ttl' => 0, 'message' => 'Hi']);
```


## Entities
[Full example](https://github.com/danog/MadelineProto/blob/v8/tests/testing.php)
Methods that allow sending message entities ([messages.sendMessage](http://docs.madelineproto.xyz/API_docs/methods/messages_sendMessage.html) for example) also have an additional `parse_mode` parameter that enables or disables html/markdown parsing of the message to be sent.

```php
$MadelineProto->messages->sendMessage(peer: '@danogentili', message: '[Testing Markdown in MadelineProto](https://docs.madelineproto.xyz)', parse_mode:  'Markdown');
$MadelineProto->messages->sendMessage(peer: '@danogentili', message: '<a href="https://docs.madelineproto.xyz">Testing HTML in MadelineProto</a>', parse_mode:  'HTML');
```



## Rich messages

[Rich messages](https://core.telegram.org/bots/api#sendrichmessage) are messages made of structured blocks: headings, paragraphs, lists, tables, quotes, collapsible details, maths, maps, media and buttons.

Send them with `sendRichMessage`, passing Markdown or HTML (parsed by Telegram), or a list of blocks in the format of the Bot API's [InputRichBlock](https://core.telegram.org/bots/api#inputrichblock) type:

```php
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\ParseMode;

// Markdown (the default) or HTML
$MadelineProto->sendRichMessage(
    peer: '@danogentili',
    message: "# Shopping list\n\n- [x] Milk\n- [ ] Eggs\n\n| Item | Price |\n|---|---|\n| Milk | 1€ |\n\n![A cat](tg://photo?id=cat)",
    media: ['cat' => $MadelineProto->uploadPhoto(file: new LocalFile('cat.jpg'), peer: '@danogentili')],
);
$MadelineProto->sendRichMessage(peer: '@danogentili', message: '<h1>Title</h1><p>Some <b>HTML</b></p>', parseMode: ParseMode::HTML);

// Blocks
$MadelineProto->sendRichMessage(peer: '@danogentili', message: [
    ['type' => 'heading', 'size' => 1, 'text' => 'Title'],
    ['type' => 'paragraph', 'text' => ['Some ', ['type' => 'bold', 'text' => 'bold'], ' text']],
    ['type' => 'list', 'items' => [
        ['blocks' => [['type' => 'paragraph', 'text' => 'First']], 'type' => '1', 'value' => 1],
        ['blocks' => [['type' => 'paragraph', 'text' => 'Second']], 'type' => '1', 'value' => 2],
    ]],
    ['type' => 'photo', 'photo' => ['type' => 'photo', 'media' => new LocalFile('cat.jpg')], 'caption' => ['text' => 'A cat']],
    ['type' => 'buttons', 'buttons' => [['text' => 'Docs', 'url' => 'https://docs.madelineproto.xyz', 'style' => 'primary']]],
]);
```

Media (in blocks, or referenced by ID in Markdown with `![alt](tg://photo?id=ID)` and `![alt](tg://document?id=ID)`) can be `Media` or `Message` objects, bot API file IDs, or files to upload (`LocalFile`, `RemoteUrl`, `ReadableStream`), optionally wrapped in a bot API InputMedia-like array to specify the type (`['type' => 'video', 'media' => new LocalFile('video.mp4')]`).

Rich messages can also be:

* Streamed while they're being generated (e.g. by an AI), with `sendRichMessageDraft` (call it again with the returned draft ID to update the draft, then send the final message with `sendRichMessage`).
* Sent from the event handler with `$message->replyRich(...)`, `$message->sendRich(...)`, `$message->editRich(...)`, `$message->replyOrEditRich(...)`, `$query->editRich(...)` for callback queries, `$story->replyRich(...)` and `sendRichMessageToAdmins(...)`.
* Passed to raw methods (`messages.sendMessage`, `messages.editMessage`, `inputBotInlineMessageRichMessage`, ...) as a bot API [InputRichMessage](https://core.telegram.org/bots/api#inputrichmessage) in the `rich_message` parameter, as an array or JSON string.

Received rich messages are available in `$message->richMessage`, which has the same API as messages for their text and media:

```php
$rich = $message->richMessage;
$rich->message;   // Plain text version
$rich->entities;  // Entities of the styled text (headings are bold, quotes are block quotes, ...)
$rich->getHTML(); // HTML version
$rich->media;     // Media of the media blocks
$rich->blocks;    // Blocks, in the bot API RichBlock format (with MadelineProto Media objects)

$message->replyRich($rich); // Rich messages can be sent again as-is
```

`MTProtoToBotAPI` converts the `rich_message` of messages to bot API objects.

## reply_markup
reply_markup accepts bot API reply markup objects as well as MTProto ones.

```php
$bot_API_markup = ['inline_keyboard' => 
    [
        [
            ['text' => 'MadelineProto docs', 'url' => 'https://docs.madelineproto.xyz'],
            ['text' => 'MadelineProto channel', 'url' => 'https://t.me/MadelineProto']
        ]
    ]
];
$MadelineProto->messages->sendMessage(peer: '@danogentili', message: 'lel', reply_markup: $bot_API_markup);
```


## Bot API objects
To convert the results of methods to bot API objects you can use the MTProtoToBotAPI method.

```php
$bot_API_object = $MadelineProto->MTProtoToBotAPI($MadelineProto->messages->sendMessage(peer: '@danogentili', message: 'lel'));
```

MadelineProto also [supports bot API file IDs when working with files](FILES.html)


## No result

See [ignored async](https://docs.madelineproto.xyz/docs/ASYNC.html#ignored-async).  

## Multiple method calls

See [multiple async](https://docs.madelineproto.xyz/docs/ASYNC.html#multiple-async).  

## Cancellation

See [cancellation &raquo;](https://docs.madelineproto.xyz/docs/ASYNC.html#cancellation).  

<a href="https://docs.madelineproto.xyz/docs/CONTRIB.html">Next section</a>
---
title: "Uploading and downloading files"
description: "MadelineProto provides fully parallelized wrapper methods to upload and download files that support bot API file ids, direct upload by URL and file renaming."
nav_order: 17
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Uploading and downloading files

MadelineProto provides **fully parallelized** wrapper methods to upload and download files that support bot API file ids, direct upload by URL and file renaming.

Maximum file size is of 2 GB.

Example bot: [`downloadRenameBot.php`](https://github.com/danog/MadelineProto/blob/master/examples/downloadRenameBot.php) - download files by URL and rename Telegram files using this async parallelized bot!


* [Bot API file IDs](#bot-api-file-ids)
* [Uploading & sending files](#sending-files)
  * [Security notice](#security-notice)
  * [Photos](#inputmediauploadedphoto)
  * [Documents](#inputmediauploadeddocument)
    * [Documents](#documentattributefilename-to-send-a-document)
    * [Photos as documents](#documentattributeimagesize-to-send-a-photo-as-document)
    * [GIFs](#documentattributeanimated-to-send-a-gif)
    * [Videos](#documentattributevideo-to-send-a-video)
    * [Audio & Voice](#documentattributeaudio-to-send-an-audio-file)
* [Uploading files](#uploading-files)
* [Reusing uploaded files](#reusing-uploaded-files)
* [Renaming files](#renaming-files)
* [Downloading files](#downloading-files)
  * [Extracting download info](#extracting-download-info)
  * [Downloading profile pictures](#downloading-profile-pictures)
  * [Download to directory](#download-to-directory)
  * [Download to file](#download-to-file)
  * [Download to stream](#download-to-stream)
  * [Download to callback](#download-to-callback)
  * [Download to http-server](#download-to-http-server)
  * [Download to browser](#download-to-browser)
* [Getting progress](#getting-progress)

## Sending files

To send photos and documents to someone, use the [$MadelineProto->messages->sendMedia](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMedia.html) method, click on the link for more info.

All files will be uploaded **asynchronously and in parallel**, 20 chunks at a time for maximum performance (this value can be tweaked in the [settings](https://docs.madelineproto.xyz/docs/SETTINGS.html)).

The required `message` parameter is the caption: it can contain URLs, mentions, bold and italic text, thanks to the `parse_mode` parameter, that enables markdown or HTML parsing.

The `media` parameter contains the file path and other info about the file.

It can contain [lots of various objects](https://docs.madelineproto.xyz/API_docs/types/InputMedia.html), here are the most important:

### Security notice

Be careful when calling methods with user-provided parameters: the upload function may be used to access and send any file.  
To disable automatic uploads by file name (disabled by default), [use the appropriate setting](../PHP/danog/MadelineProto/Settings/Files.html#setallowautomaticuploadbool-allowautomaticupload-self) OR upload files [manually](#reusing-uploaded-files).


### [inputMediaUploadedPhoto](https://docs.madelineproto.xyz/API_docs/constructors/inputMediaUploadedPhoto.html)
```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedPhoto',
        'file' => 'faust.jpg'
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

Can be used to upload photos: simply provide the photo's file path in the `file` field, and optionally provide a `ttl_seconds` field to set the self-destruction period of the photo, even for normal chats.
You can also provide a URL to the `file` field.

### [inputMediaUploadedDocument](https://docs.madelineproto.xyz/API_docs/constructors/inputMediaUploadedDocument.html)
```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'video.mp4',
        'attributes' => [
            ['_' => 'documentAttributeVideo', 'round_message' => false, 'supports_streaming' => true]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

Can be used to upload documents, videos, gifs, voice messages, round videos, round voice messages: simply provide the file's file path in the `file` field, and optionally provide a `ttl_seconds` field to set the self-destruction period of the photo, even for normal chats.  
You can also provide a URL to the `file` field.  
To rename files, provide an Update or another already-uploaded Telegram file object to the `file` field.
You can also (optionally) provide the file's mime type in the `mime_type` field, generate it using `mime_content_type($file_path);` (tip: try using an unexpected mime type to make official clients crash ;).  
Use the `nosound_video` field if the video does not have sound (gifs).  
To actually set the document type, provide one or more [DocumentAttribute](https://docs.madelineproto.xyz/API_docs/types/DocumentAttribute.html) objects to the `attributes` field:  

### [documentAttributeFilename](https://docs.madelineproto.xyz/API_docs/constructors/documentAttributeFilename.html) to send a document

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'file.txt',
        'attributes' => [
            ['_' => 'documentAttributeFilename', 'file_name' => 'document.txt']
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

### [documentAttributeImageSize](https://docs.madelineproto.xyz/API_docs/constructors/documentAttributeImageSize.html) to send a photo as document

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'file.jpg',
        'attributes' => [
            ['_' => 'documentAttributeImageSize'],
            ['_' => 'documentAttributeFilename', 'file_name' => 'image.jpg']
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

### [documentAttributeAnimated](https://docs.madelineproto.xyz/API_docs/constructors/documentAttributeAnimated.html) to send a gif
```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'file.mp4',
        'attributes' => [
            ['_' => 'documentAttributeAnimated']
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

### [documentAttributeVideo](https://docs.madelineproto.xyz/API_docs/constructors/documentAttributeVideo.html) to send a video
```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'video.mp4',
        'attributes' => [
            ['_' => 'documentAttributeVideo', 'round_message' => false, 'supports_streaming' => true]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

Set `round_message` to true to send a round message.  
You might want to manually provide square `w` (width) and `h` (height) parameters to send round videos.


### [documentAttributeAudio](https://docs.madelineproto.xyz/API_docs/constructors/documentAttributeAudio.html) to send an audio file

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => 'song.mp3',
        'attributes' => [
            ['_' => 'documentAttributeAudio', 'voice' => false, 'title' => 'This is magic', 'performer' => 'Daniil Gentili']
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

Set the `voice` parameter to true to send a voice message.


## Uploading files

```php
$MessageMedia = yield $MadelineProto->messages->uploadMedia([
    'media' => [
        '_' => 'inputMediaUploadedPhoto',
        'file' => 'faust.jpg'
    ],
]);
```

The `file` can be a file name, a URL, or a file uploaded by someone else (can be used to rename files).

You can also only upload a file, without actually sending it to anyone, storing only the file ID for later usage.

All files will be uploaded **asynchronously and in parallel**, 20 chunks at a time for maximum performance (this value can be tweaked in the [settings](https://docs.madelineproto.xyz/docs/SETTINGS.html)).

The [$MadelineProto->messages->uploadMedia](https://docs.madelineproto.xyz/API_docs/methods/messages_uploadMedia.html) function is a reduced version of the [$MadelineProto->messages->sendMedia](https://docs.madelineproto.xyz/API_docs/methods/messages_sendMedia.html), that requires only a `media` parameter, with the media to upload (on normal users, the `peer` field should be populated with `@me` or another value).  

The returned [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object can then be reused to resend the document using sendMedia.

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => $MessageMedia,
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

`$MessageMedia` can also be a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html) (the media contained in the message will be sent), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) (the media contained in the message contained in the update will be sent).

## Reusing uploaded files

`$MadelineProto->messages->uploadMedia` and bot API file IDs do not allow you to modify the type of the file to send: however, MadelineProto provides methods that can generate a file object that can be resent with multiple file types.

```php
$inputFile = yield $MadelineProto->upload('filename.mp4');
```

The file name can also be a URL.  
More optional parameters are available, check the PHPDOC of the method in your IDE.  
You can also upload a file from a stream (this is especially useful, for example, when downloading YouTube videos using `youtube-dl` with `ffmpeg` and [async AMPHP CLI streams](https://github.com/amphp/process)):  

```php
$inputFile = yield $MadelineProto->uploadFromStream($stream, $size, $mime);
```

`$stream` - PHP resource or [async AMPHP stream](https://github.com/amphp/byte-stream).  
`$size`   - Size of file to upload  
`$mime`   - MIME type of file to upload  

More optional parameters are available, check the PHPDOC of the method in your IDE.  
You can also upload files from a callable:

```php
$inputFile = yield $MadelineProto->uploadFromCallable($callable, $size, $mime);
```

`$callable`:  
The callable must accept two parameters: `int $offset, int $size`  
The callable must return a string with the contest of the file at the specified offset and size.  
`$size`   - Size of file to upload  
`$mime`   - MIME type of file to upload 

More optional parameters are available, check the PHPDOC of the method in your IDE.  

---

The generated `$inputFile` can later be reused thusly:

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => $inputFile,
        'attributes' => [
            ['_' => 'documentAttributeFilename', 'file_name' => 'video.mp4']
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
$sentMessageVideo = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => $inputFile,
        'attributes' => [
            ['_' => 'documentAttributeVideo', 'round_message' => false, 'supports_streaming' => true]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

In this case, we're reusing the same InputFile to send both a document and a video, without uploading the file twice.

The concept is easy: where you would usually provide a file path, simply provide `$inputFile`.

## Renaming files

Files can be renamed by simply providing the `$Update` with the file to the sendMedia method thusly:  

```php
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => '@danogentili',
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => $Update,
        'attributes' => [
            ['_' => 'documentAttributeFilename', 'file_name' => $newName]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);
```

## Downloading files

There are multiple download methods that allow you to download a file to a directory, to a file or to a stream.  

### Extracting download info
```php
$info = yield $MadelineProto->getDownloadInfo($MessageMedia);
```

`$MessageMedia` can be a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object or a bot API file ID.

* `$info['ext']` - The file extension
* `$info['name']` - The file name, without the extension
* `$info['mime']` - The file mime type
* `$info['size']` - The file size

### Downloading profile pictures
```php
$info = yield $MadelineProto->getPropicInfo($Update);
```

`$Update` can be a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html) object, an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), or any value supported by [getInfo](https://docs.madelineproto.xyz/getInfo.html).  
The result (which is in the same format as `getDownloadInfo`) should the be passed to the download functions in order to download the profile picture.  

* `$info['ext']` - The file extension
* `$info['name']` - The file name, without the extension
* `$info['mime']` - The file mime type
* `$info['size']` - The file size

### Download to directory
```php
$output_file_name = yield $MadelineProto->downloadToDir($MessageMedia, '/tmp/');
```

This downloads the given file to `/tmp`, and returns the full generated file path.

`$MessageMedia` can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.

### Download to file
```php
$output_file_name = yield $MadelineProto->downloadToFile($MessageMedia, '/tmp/myname.mp4');
```

This downloads the given file to `/tmp/myname.mp4`, and returns the full file path.

`$MessageMedia`can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.

### Download to stream
```php
yield $MadelineProto->downloadToStream($MessageMedia, $stream);
```

This downloads the given file to the given resource or [async AMPHP stream](https://github.com/amphp/byte-stream), the latter is especially useful for building an async HTTP file server with [http-server](https://github.com/amphp/http-server).

`$MessageMedia`can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.

### Download to callback
```php
yield $MadelineProto->downloadToCallable($MessageMedia, $callable);
```

This downloads the given file to the callable.
The callable must accept two parameters: `string $payload, int $offset`
The callable will be called (possibly out of order, depending on the value of the `$seekable` (see PHPDOC)).
The callable should return the number of written bytes.  

`$MessageMedia`can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.


### Download to http-server
```php
yield $MadelineProto->downloadToResponse($MessageMedia, $request, $cb);
```

This downloads the given file, replying to the specified [async http-server](https://amphp.org/http-server) request.  
Automatically supports HEAD requests and content-ranges for parallel and resumed downloads.  

`$MessageMedia` can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.

`$request` is the [Request](https://amphp.org/http-server/classes/request) object returned by [http-server](https://amphp.org/http-server).

`$cb` is an optional parameter can be a callback for download progress, but it shouldn't be used, the new [FileCallback](#getting-progress) should be used instead



### Download to browser
```php
yield $MadelineProto->downloadToBrowser($MessageMedia, $cb);
```

This downloads the given file to the browser, sending also information about the file's type and size.
Automatically supports HEAD requests and content-ranges for parallel and resumed downloads.  

`$MessageMedia` can be either a [Message](https://docs.madelineproto.xyz/API_docs/types/Message.html), an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), a [MessageMedia](https://docs.madelineproto.xyz/API_docs/types/MessageMedia.html) object, or a bot API file ID.

`$cb` is an optional parameter can be a callback for download progress, but it shouldn't be used, the new [FileCallback](#getting-progress) should be used instead


## Getting progress

To get the upload/download progress in real-time, use the `\danog\MadelineProto\FileCallback` class:

```php
$peer = '@danogentili';
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => $peer,
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => new \danog\MadelineProto\FileCallback(
            'video.mp4',
            function ($progress, $speed, $time) use ($MadelineProto, $peer) {
                try {
                    yield $MadelineProto->messages->sendMessage(['peer' => $peer, 'message' => "Upload progress: $progress%\nSpeed: $speed mbps\nTime elapsed since start: $time"]);
                } catch (\Throwable $e) {}
            }
        ),
        'attributes' => [
            ['_' => 'documentAttributeVideo', 'round_message' => false, 'supports_streaming' => true]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);

$output_file_name = yield $MadelineProto->downloadToFile(
    $sentMessage,
    new \danog\MadelineProto\FileCallback(
        '/tmp/myname.mp4',
        function ($progress, $speed, $time) use ($MadelineProto, $peer) {
            try {
                yield $MadelineProto->messages->sendMessage(['peer' => $peer, 'message' => "Download progress: $progress%\nSpeed: $speed mbps\nTime elapsed since start: $time"]);
            } catch (\Throwable $e) {}
        }
    )
);
```

This will send the file `video.mp4` to [@danogentili](https://t.me/danogentili): while uploading, he will receive progress messages `Upload progress: 24%` until the upload is complete; while downloading, he will receive progress messages `Download progress: 34%` until the download is complete.

You can also add two more parameters `$speed, $time` to the signature of the method to get a partial upload speed in mbps, along with the time elapsed since the start of the download.

A FileCallback object can be provided to `uploadMedia`, `sendMedia`, `uploadProfilePicture`, `upload`, `upload_encrypted`, `download_to_*`: the first parameter to its constructor must be the file path/object that is usually accepted by the function, the second must be a callable function or object.

You can also write your own callback class, just implement `\danog\MadelineProto\FileCallbackInterface`:  
```php
class MyCallback implements \danog\MadelineProto\FileCallbackInterface
{
    private $file;
    private $peer;
    private $MadelineProto;
    public function __construct($file, $peer, $MadelineProto)
    {
        $this->file = $file;
        $this->peer = $peer;
        $this->MadelineProto = $MadelineProto;
    }
    public function getFile()
    {
        return $this->file;
    }
    public function __invoke($progress, $speed, $time)
    {
        yield $this->MadelineProto->messages->sendMessage(['peer' => $this->peer, 'message' => 'Progress: '.$progress.'%']);
    }
}
$peer = '@danogentili';
$sentMessage = yield $MadelineProto->messages->sendMedia([
    'peer' => $peer,
    'media' => [
        '_' => 'inputMediaUploadedDocument',
        'file' => new MyCallback('video.mp4', $peer, $MadelineProto),
        'attributes' => [
            ['_' => 'documentAttributeVideo', 'round_message' => false, 'supports_streaming' => true]
        ]
    ],
    'message' => '[This is the caption](https://t.me/MadelineProto)',
    'parse_mode' => 'Markdown'
]);

$output_file_name = yield $MadelineProto->downloadToFile(
    $sentMessage,
    new MyCallback('/tmp/myname.mp4', $peer, $MadelineProto)
);
```


## Bot API file IDs

`$MessageMedia` can even be a bot API file ID, generated by the bot API, or by MadelineProto:

Actual MessageMedia objects can also be converted to bot API file IDs like this:

```php
$botAPI_file = yield $MadelineProto->MTProtoToBotAPI($MessageMedia);
```

`$botAPI_file` now contains a [bot API message](https://core.telegram.org/bots/api#message), to extract the file ID from it use the following code:

```php
foreach (['audio', 'document', 'photo', 'sticker', 'video', 'voice', 'video_note'] as $type) {
    if (isset($botAPI_file[$type]) && is_array($botAPI_file[$type])) {
        $method = $type;
    }
}
$result['file_type'] = $method;
if ($result['file_type'] == 'photo') {
    $result['file_size'] = $botAPI_file[$method][0]['file_size'];
    if (isset($botAPI_file[$method][0]['file_name'])) {
        $result['file_name'] = $botAPI_file[$method][0]['file_name'];
        $result['file_id'] = $botAPI_file[$method][0]['file_id'];
    }
} else {
    if (isset($botAPI_file[$method]['file_name'])) {
        $result['file_name'] = $botAPI_file[$method]['file_name'];
    }
    if (isset($botAPI_file[$method]['file_size'])) {
        $result['file_size'] = $botAPI_file[$method]['file_size'];
    }
    if (isset($botAPI_file[$method]['mime_type'])) {
        $result['mime_type'] = $botAPI_file[$method]['mime_type'];
    }
    $result['file_id'] = $botAPI_file[$method]['file_id'];
}
if (!isset($result['mime_type'])) {
    $result['mime_type'] = 'application/octet-stream';
}
if (!isset($result['file_name'])) {
    $result['file_name'] = $result['file_id'].($method === 'sticker' ? '.webp' : '');
}
```

* `$result['file_id']` - Bot API file ID
* `$result['mime_type']` - Mime type
* `$result['file_type']` - File type: voice, video, video_note (round video), music, video, photo, sticker or document
* `$result['file_size']` - File size
* `$result['file_name']` - File name

<a href="https://docs.madelineproto.xyz/docs/CHAT_INFO.html">Next section</a>
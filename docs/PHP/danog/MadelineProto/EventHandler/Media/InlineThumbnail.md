---
title: "danog\\MadelineProto\\EventHandler\\Media\\InlineThumbnail: Represents a thumbnail inlined in a media (like the stripped preview of a photo, or the thumbnail of a secret chat media)."
description: "\nIt behaves like any other thumbnail, but it's downloaded from memory, without contacting Telegram:\nits file ID carries the thumbnail itself, authenticated by the session that generated it: it's accepted by\nevery method of that session (not by the bot API, nor by other sessions).\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Media\InlineThumbnail`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a thumbnail inlined in a media (like the stripped preview of a photo, or the thumbnail of a secret chat media).  


It behaves like any other thumbnail, but it's downloaded from memory, without contacting Telegram:
its file ID carries the thumbnail itself, authenticated by the session that generated it: it's accepted by
every method of that session (not by the bot API, nor by other sessions).



## Constants
* `danog\MadelineProto\EventHandler\Media\InlineThumbnail::SECRET_CHAT_TYPE`: 

## Properties
* `$type`: `string` Thumbnail type, see https://core.telegram.org/api/files#image-thumbnail-types
* `$width`: `int` Thumbnail width
* `$height`: `int` Thumbnail height
* `$size`: `int` Media filesize
* `$fileName`: `string` Media file name
* `$fileExt`: `string` Media file extension
* `$creationDate`: `int` Media creation date
* `$mimeType`: `string` Media MIME type
* `$ttl`: `?int` Time-to-live of media
* `$thumbs`: `list<(Thumbnail | InlineThumbnail)>` Thumbnails, from the smallest to the biggest: for photos, the smaller sizes of the photo.

Includes the thumbnails inlined in the media (always the only thumbnail of secret chat media),
which are downloaded from memory, without contacting Telegram.
* `$videoThumbs`: `list<VideoThumbnail>` Animated thumbnails (MPEG4 videos), from the smallest to the biggest.
* `$spoiler`: `bool` Whether the media should be hidden behind a spoiler
* `$botApiFileId`: `string` File ID in bot API format (always present even for users)
* `$botApiFileUniqueId`: `string` Unique file ID in bot API format (always present even for users)
* `$encrypted`: `bool` Whether this media originates from a secret chat.
* `$protected`: `bool` Whether this media is protected

## Method list:
* [`getDownloadInfo(): array`](#getDownloadInfo)
* [`getDownloadLink((string|null) $scriptUrl = NULL): string`](#getDownloadLink)
* [`getStream((callable(float, float, float): voi)|null) $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): \Amp\ByteStream\ReadableStream&danog\MadelineProto\ResumableStream`](#getStream)
* [`downloadToDir(string $dir = NULL, (callable(float, float, float): voi)|null) $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): string`](#downloadToDir)
* [`downloadToFile(string $file, (callable(float, float, float): voi)|null) $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): string`](#downloadToFile)

## Methods:
### <a name="getDownloadInfo"></a> `getDownloadInfo(): array`





### <a name="getDownloadLink"></a> `getDownloadLink((string|null) $scriptUrl = NULL): string`

Gets a download link for any file up to 4GB.


Parameters:

* `$scriptUrl`: `(string|null)` Optional path to custom download script (not needed when running via web)  



### <a name="getStream"></a> `getStream((callable(float, float, float): voi)|null) $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): \Amp\ByteStream\ReadableStream&danog\MadelineProto\ResumableStream`

Get a readable amp stream with the file contents.
  
The returned stream is resumable: it can be serialized, and once unserialized,  
reading continues from the end of the last chunk read before serialization.  


Parameters:

* `$cb`: `(callable(float, float, float): voi)|null)` Progress callback  
* `$offset`: `int`   
* `$end`: `int`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`
* `\Amp\ByteStream\ReadableStream&danog\MadelineProto\ResumableStream`




### <a name="downloadToDir"></a> `downloadToDir(string $dir = NULL, (callable(float, float, float): voi)|null) $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): string`

Download the media to working directory or passed path.


Parameters:

* `$dir`: `string` Directory where to download the file  
* `$cb`: `(callable(float, float, float): voi)|null)` Progress callback  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="downloadToFile"></a> `downloadToFile(string $file, (callable(float, float, float): voi)|null) $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): string`

Download the media to file.


Parameters:

* `$file`: `string` Downloaded file path  
* `$cb`: `(callable(float, float, float): voi)|null)` Progress callback  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

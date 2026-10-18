---
title: "danog\\MadelineProto\\Settings\\Files: File management settings."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Files`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

File management settings.  




## Method list:
* [`getAllowAutomaticUpload(): bool`](#getAllowAutomaticUpload)
* [`setAllowAutomaticUpload(bool $allowAutomaticUpload): \danog\MadelineProto\Settings\Files`](#setAllowAutomaticUpload)
* [`getUploadParallelChunks(): int`](#getUploadParallelChunks)
* [`setUploadParallelChunks(int $uploadParallelChunks): \danog\MadelineProto\Settings\Files`](#setUploadParallelChunks)
* [`getDownloadParallelChunks(): int`](#getDownloadParallelChunks)
* [`setDownloadParallelChunks(int $downloadParallelChunks): \danog\MadelineProto\Settings\Files`](#setDownloadParallelChunks)
* [`getResumeInterruptedCalls(): bool`](#getResumeInterruptedCalls)
* [`setResumeInterruptedCalls(bool $resumeInterruptedCalls): \danog\MadelineProto\Settings\Files`](#setResumeInterruptedCalls)
* [`getSandboxDownloads(): bool`](#getSandboxDownloads)
* [`setSandboxDownloads(bool $sandboxDownloads): \danog\MadelineProto\Settings\Files`](#setSandboxDownloads)
* [`getReportBrokenMedia(): bool`](#getReportBrokenMedia)
* [`setReportBrokenMedia(bool $reportBrokenMedia): \danog\MadelineProto\Settings\Files`](#setReportBrokenMedia)
* [`getDownloadLink(): ?string`](#getDownloadLink)
* [`setDownloadLink(?string $downloadLink): \danog\MadelineProto\Settings\Files`](#setDownloadLink)

## Methods:
### <a name="getAllowAutomaticUpload"></a> `getAllowAutomaticUpload(): bool`

Get allow automatic upload of files from file paths present in constructors?



### <a name="setAllowAutomaticUpload"></a> `setAllowAutomaticUpload(bool $allowAutomaticUpload): \danog\MadelineProto\Settings\Files`

Set allow automatic upload of files from file paths present in constructors?


Parameters:

* `$allowAutomaticUpload`: `bool` Allow automatic upload of files from file paths present in constructors?  



### <a name="getUploadParallelChunks"></a> `getUploadParallelChunks(): int`

Get upload parallel chunk count.



### <a name="setUploadParallelChunks"></a> `setUploadParallelChunks(int $uploadParallelChunks): \danog\MadelineProto\Settings\Files`

Set upload parallel chunk count.


Parameters:

* `$uploadParallelChunks`: `int` Upload parallel chunk count  



### <a name="getDownloadParallelChunks"></a> `getDownloadParallelChunks(): int`

Get download parallel chunk count.



### <a name="setDownloadParallelChunks"></a> `setDownloadParallelChunks(int $downloadParallelChunks): \danog\MadelineProto\Settings\Files`

Set download parallel chunk count.


Parameters:

* `$downloadParallelChunks`: `int` Download parallel chunk count  



### <a name="getResumeInterruptedCalls"></a> `getResumeInterruptedCalls(): bool`

Get whether to resume interrupted calls that upload files after a restart.



### <a name="setResumeInterruptedCalls"></a> `setResumeInterruptedCalls(bool $resumeInterruptedCalls): \danog\MadelineProto\Settings\Files`

Set whether to resume interrupted calls that upload files after a restart.
  
If enabled, method calls and sendMedia calls (sendDocument, sendPhoto, ...) uploading a file that survives a restart  
(a local file, a URL, a Telegram file or a resumable stream) are saved in the session until they complete:  
if the session is restarted in the meantime, the call is made again once the session starts, resuming the interrupted upload.  
  
Disable it if your code already makes interrupted calls again after a restart, to avoid sending files twice.  


Parameters:

* `$resumeInterruptedCalls`: `bool` Whether to resume interrupted calls that upload files after a restart  



### <a name="getSandboxDownloads"></a> `getSandboxDownloads(): bool`

Get whether files served to browsers can't run as pages of the website serving them.



### <a name="setSandboxDownloads"></a> `setSandboxDownloads(bool $sandboxDownloads): \danog\MadelineProto\Settings\Files`

Set whether files served to browsers can't run as pages of the website serving them.
  
Applies to the files served by the download script (getDownloadLink, downloadToBrowser) and by downloadToResponse:  
their MIME type and name come from whoever sent them on Telegram, or from the query string of the download script.  
If enabled, they're served with a sandboxing Content-Security-Policy and X-Content-Type-Options: nosniff, with  
their MIME type normalized, and only media and plain text are shown inline (everything else is downloaded).  
  
Disable it only if the files served are trusted, and must be shown as pages of the website (HTML, SVG, PDF...).  


Parameters:

* `$sandboxDownloads`: `bool` Whether files served to browsers can't run as pages of the website serving them  



### <a name="getReportBrokenMedia"></a> `getReportBrokenMedia(): bool`

Get whether to report undownloadable media to TSF.



### <a name="setReportBrokenMedia"></a> `setReportBrokenMedia(bool $reportBrokenMedia): \danog\MadelineProto\Settings\Files`

Set whether to report undownloadable media to TSF.


Parameters:

* `$reportBrokenMedia`: `bool` Whether to report undownloadable media to TSF  



### <a name="getDownloadLink"></a> `getDownloadLink(): ?string`

Get custom download link URL for CLI bots, used by `getDownloadLink`.



### <a name="setDownloadLink"></a> `setDownloadLink(?string $downloadLink): \danog\MadelineProto\Settings\Files`

Only needed for CLI bots, not bots started via web.
  
Sets custom download link URL for CLI bots, used by `getDownloadLink`.  
  
Can be null, in which case MadelineProto will automatically generate a download link.  


Parameters:

* `$downloadLink`: `?string` Custom download link URL for CLI bots, used by `getDownloadLink`.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

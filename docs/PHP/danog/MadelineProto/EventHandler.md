---
title: "danog\\MadelineProto\\EventHandler: Event handler."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Event handler.  



## Properties
* `$auth`: `\danog\MadelineProto\Namespace\Auth` 
* `$account`: `\danog\MadelineProto\Namespace\Account` 
* `$users`: `\danog\MadelineProto\Namespace\Users` 
* `$contacts`: `\danog\MadelineProto\Namespace\Contacts` 
* `$messages`: `\danog\MadelineProto\Namespace\Messages` 
* `$updates`: `\danog\MadelineProto\Namespace\Updates` 
* `$photos`: `\danog\MadelineProto\Namespace\Photos` 
* `$upload`: `\danog\MadelineProto\Namespace\Upload` 
* `$help`: `\danog\MadelineProto\Namespace\Help` 
* `$channels`: `\danog\MadelineProto\Namespace\Channels` 
* `$bots`: `\danog\MadelineProto\Namespace\Bots` 
* `$payments`: `\danog\MadelineProto\Namespace\Payments` 
* `$stickers`: `\danog\MadelineProto\Namespace\Stickers` 
* `$phone`: `\danog\MadelineProto\Namespace\Phone` 
* `$langpack`: `\danog\MadelineProto\Namespace\Langpack` 
* `$folders`: `\danog\MadelineProto\Namespace\Folders` 
* `$stats`: `\danog\MadelineProto\Namespace\Stats` 
* `$chatlists`: `\danog\MadelineProto\Namespace\Chatlists` 
* `$stories`: `\danog\MadelineProto\Namespace\Stories` 

## Method list:
* [`startAndLoop(string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`](#startandloop-string-session-danog-madelineproto-settingsabstract-settings-null-void)
* [`startAndLoopBot(string $session, string $token, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`](#startandloopbot-string-session-string-token-danog-madelineproto-settingsabstract-settings-null-void)
* [`getPeriodicLoop(string $name): \danog\Loop\PeriodicLoop`](#getperiodicloop-string-name-danog-loop-periodicloop)
* [`getPeriodicLoops(): array<string, \danog\Loop\PeriodicLoop>`](#getperiodicloops-array-string-danog-loop-periodicloop)
* [`getReportPeers(): string|int|(string|int)[]`](#getreportpeers-string-int-string-int)
* [`getPluginPaths(): \non-empty-string|\non-empty-list<\non-empty-string>|null`](#getpluginpaths-non-empty-string-non-empty-list-non-empty-string-null)
* [`getPlugins(): class-string<\danog\MadelineProto\EventHandler>[]`](#getplugins-class-string-danog-madelineproto-eventhandler)
* [`MTProtoToBotAPI(array $data): array`](#mtprototobotapi-array-data-array)
* [`MTProtoToTd(mixed $params): mixed`](#mtprotototd-mixed-params-mixed)
* [`MTProtoToTdcli(mixed $params): mixed`](#mtprotototdcli-mixed-params-mixed)
* [`acceptCall(int $id): void`](#acceptcall-int-id-void)
* [`acceptSecretChat(array $params): void`](#acceptsecretchat-array-params-void)
* [`arr(mixed ...$params): array`](#arr-mixed-params-array)
* [`base64urlDecode(string $data): string`](#base64urldecode-string-data-string)
* [`base64urlEncode(string $data): string`](#base64urlencode-string-data-string)
* [`botAPIToMTProto(array $arguments): array`](#botapitomtproto-array-arguments-array)
* [`botLogin(string $token): ?array`](#botlogin-string-token-array)
* [`broadcastCustom(\danog\MadelineProto\Broadcast\Action $action, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL): int`](#broadcastcustom-danog-madelineproto-broadcast-action-action-danog-madelineproto-broadcast-filter-filter-null-int)
* [`broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author = false, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false): int`](#broadcastforwardmessages-mixed-from_peer-list-int-message_ids-bool-drop_author-false-danog-madelineproto-broadcast-filter-filter-null-bool-pin-false-int)
* [`broadcastMessages(array $messages, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false): int`](#broadcastmessages-array-messages-danog-madelineproto-broadcast-filter-filter-null-bool-pin-false-int)
* [`callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<\T>`](#callfork-generator-amp-future-callable-callable-mixed-args-amp-future-t)
* [`callGetCurrent(int $id): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#callgetcurrent-int-id-danog-madelineproto-remoteurl-danog-madelineproto-localfile-string-null)
* [`callPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): void`](#callplay-int-id-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-file-void)
* [`callPlayOnHold(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`](#callplayonhold-int-id-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-files-void)
* [`canConvertOgg(): bool`](#canconvertogg-bool)
* [`cancelBroadcast(int $id): void`](#cancelbroadcast-int-id-void)
* [`closeConnection(string $message): void`](#closeconnection-string-message-void)
* [`complete2faLogin(string $password): array`](#complete2falogin-string-password-array)
* [`completePhoneLogin(string $code): mixed`](#completephonelogin-string-code-mixed)
* [`completeSignup(string $first_name, string $last_name = ''): array`](#completesignup-string-first_name-string-last_name-array)
* [`discardCall(int $id, \danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<\1, \5> $rating = NULL, string $comment = NULL): void`](#discardcall-int-id-danog-madelineproto-voip-discardreason-reason-danog-madelineproto-voip-discardreason-hangup-int-1-5-rating-null-string-comment-null-void)
* [`discardSecretChat(int $chat): void`](#discardsecretchat-int-chat-void)
* [`downloadServer(string $session): void`](#downloadserver-string-session-void)
* [`downloadToBrowser(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message $messageMedia, null|callable $cb = NULL, null|int $size = NULL, null|string $name = NULL, null|string $mime = NULL): void`](#downloadtobrowser-array-string-danog-madelineproto-filecallbackinterface-danog-madelineproto-eventhandler-message-messagemedia-null-callable-cb-null-null-int-size-null-null-string-name-null-null-string-mime-null-void)
* [`downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb = NULL, bool $seekable = true, int $offset = 0, int $end = -1, int $part_size = NULL): mixed`](#downloadtocallable-mixed-messagemedia-callable-danog-madelineproto-filecallbackinterface-callable-callable-cb-null-bool-seekable-true-int-offset-0-int-end-1-int-part_size-null-mixed)
* [`downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb = NULL): mixed`](#downloadtodir-mixed-messagemedia-string-danog-madelineproto-filecallbackinterface-dir-callable-cb-null-mixed)
* [`downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb = NULL): string|false`](#downloadtofile-mixed-messagemedia-string-danog-madelineproto-filecallbackinterface-file-callable-cb-null-string-false)
* [`downloadToResponse(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message $messageMedia, \Amp\Http\Server\Request $request, callable $cb = NULL, null|int $size = NULL, null|string $mime = NULL, null|string $name = NULL): \Amp\Http\Server\Response`](#downloadtoresponse-array-string-danog-madelineproto-filecallbackinterface-danog-madelineproto-eventhandler-message-messagemedia-amp-http-server-request-request-callable-cb-null-null-int-size-null-null-string-mime-null-null-string-name-null-amp-http-server-response)
* [`downloadToReturnedStream(mixed $messageMedia, callable $cb = NULL, int $offset = 0, int $end = -1): \Amp\ByteStream\ReadableStream`](#downloadtoreturnedstream-mixed-messagemedia-callable-cb-null-int-offset-0-int-end-1-amp-bytestream-readablestream)
* [`downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream $stream, callable $cb = NULL, int $offset = 0, int $end = -1): mixed`](#downloadtostream-mixed-messagemedia-mixed-danog-madelineproto-filecallbackinterface-resource-amp-bytestream-writablestream-stream-callable-cb-null-int-offset-0-int-end-1-mixed)
* [`echo(string $string): void`](#echo-string-string-void)
* [`end(array $what): mixed`](#end-array-what-mixed)
* [`entitiesToHtml(string $message, list<array{_: string, offset: int, length: int}> $entities, bool $allowTelegramTags = false): string`](#entitiestohtml-string-message-list-array-_-string-offset-int-length-int-entities-bool-allowtelegramtags-false-string)
* [`exportAuthorization(): array{0: int|string, 1: string}`](#exportauthorization-array-0-int-string-1-string)
* [`extractBotAPIFile(array $info): ?array`](#extractbotapifile-array-info-array)
* [`extractMessage(array $updates): array`](#extractmessage-array-updates-array)
* [`extractMessageId(array $updates): int`](#extractmessageid-array-updates-int)
* [`extractMessageUpdate(array $updates): array`](#extractmessageupdate-array-updates-array)
* [`extractUpdates(array $updates): array[]`](#extractupdates-array-updates-array)
* [`fileGetContents(string $url): string`](#filegetcontents-string-url-string)
* [`flock(string $file, int $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): mixed`](#flock-string-file-int-operation-float-polling-0-1-amp-cancellation-token-null-closure-failurecb-null-mixed)
* [`fromSupergroup(int $id): int`](#fromsupergroup-int-id-int)
* [`fullChatLastUpdated(mixed $id): int`](#fullchatlastupdated-mixed-id-int)
* [`fullGetSelf(): array|false`](#fullgetself-array-false)
* [`genVectorHash(array $longs): string`](#genvectorhash-array-longs-string)
* [`getAdminIds(): array`](#getadminids-array)
* [`getAllCalls(): array<int, \danog\MadelineProto\VoIP>`](#getallcalls-array-int-danog-madelineproto-voip)
* [`getAllMethods(): array`](#getallmethods-array)
* [`getAuthorization(): \danog\MadelineProto\API::NOT_LOGGED_IN|\danog\MadelineProto\API::WAITING_CODE|\danog\MadelineProto\API::WAITING_SIGNUP|\danog\MadelineProto\API::WAITING_PASSWORD|\danog\MadelineProto\API::LOGGED_IN|\API::LOGGED_OUT`](#getauthorization-danog-madelineproto-api-not_logged_in-danog-madelineproto-api-waiting_code-danog-madelineproto-api-waiting_signup-danog-madelineproto-api-waiting_password-danog-madelineproto-api-logged_in-api-logged_out)
* [`getBroadcastProgress(int $id): ?\danog\MadelineProto\Broadcast\Progress`](#getbroadcastprogress-int-id-danog-madelineproto-broadcast-progress)
* [`getCachedConfig(): array`](#getcachedconfig-array)
* [`getCall(int $id): ?\danog\MadelineProto\VoIP`](#getcall-int-id-danog-madelineproto-voip)
* [`getCallByPeer(int $userId): ?\danog\MadelineProto\VoIP`](#getcallbypeer-int-userid-danog-madelineproto-voip)
* [`getCallState(int $id): ?\danog\MadelineProto\VoIP\CallState`](#getcallstate-int-id-danog-madelineproto-voip-callstate)
* [`getCdnConfig(): void`](#getcdnconfig-void)
* [`getConfig(array $config = []): array`](#getconfig-array-config-array)
* [`getDNSClient(): \Amp\Dns\DnsResolver`](#getdnsclient-amp-dns-dnsresolver)
* [`getDhConfig(): array`](#getdhconfig-array)
* [`getDialogIds(): list<int>`](#getdialogids-list-int)
* [`getDialogs(): list<array>`](#getdialogs-list-array)
* [`getDownloadInfo(mixed $messageMedia): array{ext: string, name: string, mime: string, size: int, InputFileLocation: array, key_fingerprint?: string, key?: string, iv?: string, thumb_size?: string}`](#getdownloadinfo-mixed-messagemedia-array-ext-string-name-string-mime-string-size-int-inputfilelocation-array-key_fingerprint-string-key-string-iv-string-thumb_size-string)
* [`getDownloadLink(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|array|string $media, ?string $scriptUrl = NULL, ?int $size = NULL, ?string $name = NULL, ?string $mime = NULL): string`](#getdownloadlink-danog-madelineproto-eventhandler-message-danog-madelineproto-eventhandler-media-array-string-media-string-scripturl-null-int-size-null-string-name-null-string-mime-null-string)
* [`getEventHandler(class-string<\T>|null $class = NULL): \T|\danog\MadelineProto\Ipc\EventHandlerProxy|\__PHP_Incomplete_Class|null`](#geteventhandler-class-string-t-null-class-null-t-danog-madelineproto-ipc-eventhandlerproxy-__php_incomplete_class-null)
* [`getExtensionFromLocation(mixed $location, string $default): string`](#getextensionfromlocation-mixed-location-string-default-string)
* [`getExtensionFromMime(string $mime): string`](#getextensionfrommime-string-mime-string)
* [`getFileInfo(mixed $constructor): array`](#getfileinfo-mixed-constructor-array)
* [`getFolderId(mixed $id): ?int`](#getfolderid-mixed-id-int)
* [`getFullDialogs(): array<int, array>`](#getfulldialogs-array-int-array)
* [`getFullInfo(mixed $id): array`](#getfullinfo-mixed-id-array)
* [`getHTTPClient(): \Amp\Http\Client\HttpClient`](#gethttpclient-amp-http-client-httpclient)
* [`getHint(): string`](#gethint-string)
* [`getId(mixed $id): int`](#getid-mixed-id-int)
* [`getInfo(mixed $id, \danog\MadelineProto\API::INFO_TYPE_* $type = \danog\MadelineProto\API::INFO_TYPE_ALL): mixed`](#getinfo-mixed-id-danog-madelineproto-api-info_type_-type-danog-madelineproto-api-info_type_all-mixed)
* [`getLogger(): \danog\MadelineProto\Logger`](#getlogger-danog-madelineproto-logger)
* [`getMaps(): ?int`](#getmaps-int)
* [`getMaxMaps(): ?int`](#getmaxmaps-int)
* [`getMethodNamespaces(): array`](#getmethodnamespaces-array)
* [`getMethodsNamespaced(): array`](#getmethodsnamespaced-array)
* [`getMimeFromBuffer(string $buffer): string`](#getmimefrombuffer-string-buffer-string)
* [`getMimeFromExtension(string $extension, string $default): string`](#getmimefromextension-string-extension-string-default-string)
* [`getMimeFromFile(string $file): string`](#getmimefromfile-string-file-string)
* [`getPlugin(class-string<\T> $class): \danog\MadelineProto\PluginEventHandler|\danog\MadelineProto\Ipc\EventHandlerProxy|null`](#getplugin-class-string-t-class-danog-madelineproto-plugineventhandler-danog-madelineproto-ipc-eventhandlerproxy-null)
* [`getPropicInfo(mixed $data): array`](#getpropicinfo-mixed-data-array)
* [`getPsrLogger(): \Psr\Log\LoggerInterface`](#getpsrlogger-psr-log-loggerinterface)
* [`getPwrChat(mixed $id, bool $fullfetch = true): array`](#getpwrchat-mixed-id-bool-fullfetch-true-array)
* [`getSecretChat(array|int $chat): array`](#getsecretchat-array-int-chat-array)
* [`getSelf(): array|false`](#getself-array-false)
* [`getSessionName(): string`](#getsessionname-string)
* [`getSettings(): \danog\MadelineProto\Settings`](#getsettings-danog-madelineproto-settings)
* [`getSponsoredMessages(int|string|array $peer): ?array`](#getsponsoredmessages-int-string-array-peer-array)
* [`getStreamPipe(): \Amp\ByteStream\Pipe`](#getstreampipe-amp-bytestream-pipe)
* [`getTL(): \danog\MadelineProto\TL\TLInterface`](#gettl-danog-madelineproto-tl-tlinterface)
* [`getType(mixed $id): \danog\MadelineProto\API::PEER_TYPE_*`](#gettype-mixed-id-danog-madelineproto-api-peer_type_)
* [`getUpdates(array{offset?: int, limit?: int, timeout?: float} $params = []): list<array{update_id: mixed, update: mixed}>`](#getupdates-array-offset-int-limit-int-timeout-float-params-list-array-update_id-mixed-update-mixed)
* [`getWebMessage(string $message): string`](#getwebmessage-string-message-string)
* [`getWebWarnings(): string`](#getwebwarnings-string)
* [`hasAdmins(): bool`](#hasadmins-bool)
* [`hasEventHandler(): bool`](#haseventhandler-bool)
* [`hasPlugin(class-string<\danog\MadelineProto\EventHandler> $class): bool`](#hasplugin-class-string-danog-madelineproto-eventhandler-class-bool)
* [`hasReportPeers(): bool`](#hasreportpeers-bool)
* [`hasSecretChat(array|int $chat): bool`](#hassecretchat-array-int-chat-bool)
* [`htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities Object containing message and entities`](#htmltomessageentities-string-html-danog-madelineproto-tl-conversion-domentities-object-containing-message-and-entities)
* [`importAuthorization(array<int, string> $authorization, int $mainDcID): array`](#importauthorization-array-int-string-authorization-int-maindcid-array)
* [`inflateStripped(string $stripped): string`](#inflatestripped-string-stripped-string)
* [`initSelfRestart(): void`](#initselfrestart-void)
* [`isAltervista(): bool`](#isaltervista-bool)
* [`isArrayOrAlike(mixed $var): bool`](#isarrayoralike-mixed-var-bool)
* [`isForum(mixed $peer): bool`](#isforum-mixed-peer-bool)
* [`isIpc(): bool`](#isipc-bool)
* [`isIpcWorker(): bool`](#isipcworker-bool)
* [`isPlayPaused(int $id): bool`](#isplaypaused-int-id-bool)
* [`isPremium(): bool`](#ispremium-bool)
* [`isSelfBot(): bool`](#isselfbot-bool)
* [`isSelfUser(): bool`](#isselfuser-bool)
* [`isSupergroup(int $id): bool`](#issupergroup-int-id-bool)
* [`isTestMode(): bool`](#istestmode-bool)
* [`logger(mixed $param, int $level = \danog\MadelineProto\Logger::NOTICE, string $file = ''): void`](#logger-mixed-param-int-level-danog-madelineproto-logger-notice-string-file-void)
* [`logout(): void`](#logout-void)
* [`markdownCodeblockEscape(string $what): string`](#markdowncodeblockescape-string-what-string)
* [`markdownEscape(string $what): string`](#markdownescape-string-what-string)
* [`markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities Object containing message and entities`](#markdowntomessageentities-string-markdown-danog-madelineproto-tl-conversion-markdownentities-object-containing-message-and-entities)
* [`markdownUrlEscape(string $what): string`](#markdownurlescape-string-what-string)
* [`mbStrSplit(string $text, int $length): string[]`](#mbstrsplit-string-text-int-length-string)
* [`mbStrlen(string $text): int`](#mbstrlen-string-text-int)
* [`mbSubstr(string $text, int $offset, null|int $length = NULL): string`](#mbsubstr-string-text-int-offset-null-int-length-null-string)
* [`openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): callable`](#openbuffered-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-stream-amp-cancellation-cancellation-null-callable)
* [`openFileAppendOnly(string $path): \Amp\File\File`](#openfileappendonly-string-path-amp-file-file)
* [`packDouble(float $value): string`](#packdouble-float-value-string)
* [`packSignedInt(int $value): string`](#packsignedint-int-value-string)
* [`packSignedLong(int $value): string`](#packsignedlong-int-value-string)
* [`packUnsignedInt(int $value): string`](#packunsignedint-int-value-string)
* [`pausePlay(int $id): void`](#pauseplay-int-id-void)
* [`peerIsset(mixed $id): bool`](#peerisset-mixed-id-bool)
* [`phoneLogin(string $number, int $sms_type = 5): mixed`](#phonelogin-string-number-int-sms_type-5-mixed)
* [`posmod(int $a, int $b): int`](#posmod-int-a-int-b-int)
* [`processDownloadServerPing(string $path, string $payload): void`](#processdownloadserverping-string-path-string-payload-void)
* [`qrLogin(): ?\danog\MadelineProto\TL\Types\LoginQrCode`](#qrlogin-danog-madelineproto-tl-types-loginqrcode)
* [`random(int $length): string`](#random-int-length-string)
* [`randomInt(int $modulus = 0): int`](#randomint-int-modulus-0-int)
* [`readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`](#readline-string-prompt-amp-cancellation-cancel-null-string)
* [`refreshFullPeerCache(mixed $id): void`](#refreshfullpeercache-mixed-id-void)
* [`refreshPeerCache(mixed ...$ids): void`](#refreshpeercache-mixed-ids-void)
* [`rekey(int $chat): ?string`](#rekey-int-chat-string)
* [`report(string $message, string $parseMode = ''): void`](#report-string-message-string-parsemode-void)
* [`reportMemoryProfile(): void`](#reportmemoryprofile-void)
* [`requestCall(mixed $user): \danog\MadelineProto\VoIP`](#requestcall-mixed-user-danog-madelineproto-voip)
* [`requestSecretChat(mixed $user): mixed`](#requestsecretchat-mixed-user-mixed)
* [`resetUpdateState(): void`](#resetupdatestate-void)
* [`restart(): void`](#restart-void)
* [`resumePlay(int $id): void`](#resumeplay-int-id-void)
* [`rethrow(\Throwable $e): void`](#rethrow-throwable-e-void)
* [`rleDecode(string $string): string`](#rledecode-string-string-string)
* [`rleEncode(string $string): string`](#rleencode-string-string-string)
* [`secretChatStatus(int $chat): \int One of \danog\MadelineProto\API::SECRET_EMPTY, \danog\MadelineProto\API::SECRET_REQUESTED, \danog\MadelineProto\API::SECRET_READY`](#secretchatstatus-int-chat-int-one-of-danog-madelineproto-api-secret_empty-danog-madelineproto-api-secret_requested-danog-madelineproto-api-secret_ready)
* [`sendCustomEvent(mixed $payload): void`](#sendcustomevent-mixed-payload-void)
* [`sendDocument(int|string $peer, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, ?int $ttl = NULL, bool $spoiler = false, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#senddocument-int-string-peer-danog-madelineproto-eventhandler-message-danog-madelineproto-eventhandler-media-danog-madelineproto-localfile-danog-madelineproto-remoteurl-danog-madelineproto-botapifileid-amp-bytestream-readablestream-file-danog-madelineproto-eventhandler-message-danog-madelineproto-eventhandler-media-danog-madelineproto-localfile-danog-madelineproto-remoteurl-danog-madelineproto-botapifileid-amp-bytestream-readablestream-null-thumb-null-string-caption-danog-madelineproto-parsemode-parsemode-danog-madelineproto-parsemode-text-callable-callback-null-string-filename-null-string-mimetype-null-int-ttl-null-bool-spoiler-false-int-null-replytomsgid-null-int-null-topmsgid-null-array-null-replymarkup-null-int-null-sendas-null-int-null-scheduledate-null-bool-silent-false-bool-noforwards-false-bool-background-false-bool-cleardraft-false-bool-updatestickersetsorder-false-danog-madelineproto-eventhandler-message)
* [`sendMessage(int|string $peer, string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#sendmessage-int-string-peer-string-message-danog-madelineproto-parsemode-parsemode-danog-madelineproto-parsemode-text-int-null-replytomsgid-null-int-null-topmsgid-null-array-null-replymarkup-null-int-null-sendas-null-int-null-scheduledate-null-bool-silent-false-bool-noforwards-false-bool-background-false-bool-cleardraft-false-bool-nowebpage-false-bool-updatestickersetsorder-false-danog-madelineproto-eventhandler-message)
* [`sendMessageToAdmins(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false): list<\danog\MadelineProto\EventHandler\Message>`](#sendmessagetoadmins-string-message-danog-madelineproto-parsemode-parsemode-danog-madelineproto-parsemode-text-array-null-replymarkup-null-int-null-scheduledate-null-bool-silent-false-bool-noforwards-false-bool-background-false-bool-cleardraft-false-bool-nowebpage-false-list-danog-madelineproto-eventhandler-message)
* [`sendPhoto(int|string $peer, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#sendphoto-int-string-peer-danog-madelineproto-eventhandler-message-danog-madelineproto-eventhandler-media-danog-madelineproto-localfile-danog-madelineproto-remoteurl-danog-madelineproto-botapifileid-amp-bytestream-readablestream-file-string-caption-danog-madelineproto-parsemode-parsemode-danog-madelineproto-parsemode-text-callable-callback-null-string-filename-null-int-ttl-null-bool-spoiler-false-int-null-replytomsgid-null-int-null-topmsgid-null-array-null-replymarkup-null-int-null-sendas-null-int-null-scheduledate-null-bool-silent-false-bool-noforwards-false-bool-background-false-bool-cleardraft-false-bool-updatestickersetsorder-false-danog-madelineproto-eventhandler-message)
* [`setNoop(): void`](#setnoop-void)
* [`setReportPeers(int|string|(int|string)[] $userOrId): void`](#setreportpeers-int-string-int-string-userorid-void)
* [`setWebhook(string $webhookUrl): void`](#setwebhook-string-webhookurl-void)
* [`skipPlay(int $id): void`](#skipplay-int-id-void)
* [`sleep(float $time): void`](#sleep-float-time-void)
* [`start(): mixed`](#start-mixed)
* [`stop(): void`](#stop-void)
* [`stopPlay(int $id): void`](#stopplay-int-id-void)
* [`stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`](#stringtostream-string-str-amp-bytestream-readablebuffer)
* [`subscribeToUpdates(mixed $channel): \bool False if we were already subscribed`](#subscribetoupdates-mixed-channel-bool-false-if-we-were-already-subscribed)
* [`tdToMTProto(array $params): array`](#tdtomtproto-array-params-array)
* [`tdToTdcli(mixed $params): mixed`](#tdtotdcli-mixed-params-mixed)
* [`tdcliToTd(mixed $params, array $key = NULL): array`](#tdclitotd-mixed-params-array-key-null-array)
* [`testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`](#testfibers-int-fibercount-100000-array-maxfibers-int-realmemorymb-int-maps-int-maxmaps-int)
* [`toCamelCase(string $input): string`](#tocamelcase-string-input-string)
* [`toSnakeCase(string $input): string`](#tosnakecase-string-input-string)
* [`toSupergroup(int $id): int`](#tosupergroup-int-id-int)
* [`unpackDouble(string $value): float`](#unpackdouble-string-value-float)
* [`unpackFileId(string $fileId): \array Unpacked file ID`](#unpackfileid-string-fileid-array-unpacked-file-id)
* [`unpackSignedInt(string $value): int`](#unpacksignedint-string-value-int)
* [`unpackSignedLong(string $value): int`](#unpacksignedlong-string-value-int)
* [`unpackSignedLongString(string|int|array $value): string`](#unpacksignedlongstring-string-int-array-value-string)
* [`unsetEventHandler(): void`](#unseteventhandler-void)
* [`update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params): void`](#update2fa-array-password-string-new_password-string-email-string-hint-string-params-void)
* [`updateSettings(\danog\MadelineProto\SettingsAbstract $settings): void`](#updatesettings-danog-madelineproto-settingsabstract-settings-void)
* [`upload(\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|\resource $file, string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`](#upload-danog-madelineproto-filecallbackinterface-danog-madelineproto-localfile-danog-madelineproto-remoteurl-danog-madelineproto-botapifileid-string-array-resource-file-string-filename-callable-cb-null-bool-encrypted-false-mixed)
* [`uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName = '', callable $cb = NULL): mixed`](#uploadencrypted-danog-madelineproto-filecallbackinterface-string-array-file-string-filename-callable-cb-null-mixed)
* [`uploadFromCallable(mixed $callable, int $size = 0, string $mime = 'application/octet-stream', string $fileName = '', callable $cb = NULL, bool $seekable = true, bool $encrypted = false): mixed`](#uploadfromcallable-mixed-callable-int-size-0-string-mime-application-octet-stream-string-filename-callable-cb-null-bool-seekable-true-bool-encrypted-false-mixed)
* [`uploadFromStream(mixed $stream, int $size = 0, string $mime = 'application/octet-stream', string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`](#uploadfromstream-mixed-stream-int-size-0-string-mime-application-octet-stream-string-filename-callable-cb-null-bool-encrypted-false-mixed)
* [`uploadFromTgfile(mixed $media, callable $cb = NULL, bool $encrypted = false): mixed`](#uploadfromtgfile-mixed-media-callable-cb-null-bool-encrypted-false-mixed)
* [`uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size = 0, string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`](#uploadfromurl-string-danog-madelineproto-filecallbackinterface-url-int-size-0-string-filename-callable-cb-null-bool-encrypted-false-mixed)
* [`validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`](#validateeventhandlerclass-class-string-danog-madelineproto-eventhandler-class-list-danog-madelineproto-eventhandlerissue)
* [`viewSponsoredMessage(int|array $peer, string|array{random_id: string} $message): bool`](#viewsponsoredmessage-int-array-peer-string-array-random_id-string-message-bool)
* [`wrapMedia(array $media, bool $protected = false): ?\danog\MadelineProto\EventHandler\Media`](#wrapmedia-array-media-bool-protected-false-danog-madelineproto-eventhandler-media)
* [`wrapMessage(array $message): ?\danog\MadelineProto\EventHandler\AbstractMessage`](#wrapmessage-array-message-danog-madelineproto-eventhandler-abstractmessage)
* [`wrapUpdate(array $update): ?\danog\MadelineProto\EventHandler\Update`](#wrapupdate-array-update-danog-madelineproto-eventhandler-update)

## Methods:
### `startAndLoop(string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`

Start MadelineProto and the event handler.
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.

Parameters:

* `$session`: `string` Session name  
* `$settings`: `?\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `startAndLoopBot(string $session, string $token, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`

Start MadelineProto as a bot and the event handler.
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.

Parameters:

* `$session`: `string` Session name  
* `$token`: `string` Bot token  
* `$settings`: `?\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `getPeriodicLoop(string $name): \danog\Loop\PeriodicLoop`

Obtain a PeriodicLoop instance created by the Cron attribute.


Parameters:

* `$name`: `string` Method name  


#### See also: 
* `\danog\Loop\PeriodicLoop`




### `getPeriodicLoops(): array<string, \danog\Loop\PeriodicLoop>`

Obtain all PeriodicLoop instances created by the Cron attribute.


#### See also: 
* `\danog\Loop\PeriodicLoop`




### `getReportPeers(): string|int|(string|int)[]`

Get peers where to send error reports.



### `getPluginPaths(): \non-empty-string|\non-empty-list<\non-empty-string>|null`

Obtain a path or a list of paths that will be recursively searched for plugins.
Plugin filenames end with Plugin.php, and will be included automatically.


### `getPlugins(): class-string<\danog\MadelineProto\EventHandler>[]`

Obtain a list of plugin event handlers to use, in addition with those found by getPluginPath.



### `MTProtoToBotAPI(array $data): array`

Convert MTProto parameters to bot API parameters.


Parameters:

* `$data`: `array` Data  



### `MTProtoToTd(mixed $params): mixed`

MTProto to TD params.


Parameters:

* `$params`: `mixed` Params  



### `MTProtoToTdcli(mixed $params): mixed`

MTProto to TDCLI params.


Parameters:

* `$params`: `mixed` Params  



### `acceptCall(int $id): void`

Accept call.


Parameters:

* `$id`: `int`   



### `acceptSecretChat(array $params): void`

Accept secret chat.


Parameters:

* `$params`: `array` Secret chat ID  



### `arr(mixed ...$params): array`

Create array.


Parameters:

* `...$params`: `mixed` Params  



### `base64urlDecode(string $data): string`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### `base64urlEncode(string $data): string`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### `botAPIToMTProto(array $arguments): array`

Convert bot API parameters to MTProto parameters.


Parameters:

* `$arguments`: `array` Arguments  



### `botLogin(string $token): ?array`

Login as bot.


Parameters:

* `$token`: `string` Bot token  



### `broadcastCustom(\danog\MadelineProto\Broadcast\Action $action, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL): int`

Executes a custom broadcast action with all peers (users, chats, channels) of the bot.
Will return an integer ID that can be used to:  
  
- Get the current broadcast progress with getBroadcastProgress  
- Cancel the broadcast using cancelBroadcast  
  
Note that to avoid manually polling the progress,  
MadelineProto will also periodically emit updateBroadcastProgress updates,  
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$action`: `\danog\MadelineProto\Broadcast\Action` A custom, serializable Action class that will be called once for every peer.  
* `$filter`: `?\danog\MadelineProto\Broadcast\Filter`   


#### See also: 
* [`\danog\MadelineProto\Broadcast\Action`: Interface that represents a broadcast action.](../../danog/MadelineProto/Broadcast/Action.html)
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### `broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author = false, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false): int`

Forwards a list of messages to all peers (users, chats, channels) of the bot.
Will return an integer ID that can be used to:  
  
- Get the current broadcast progress with getBroadcastProgress  
- Cancel the broadcast using cancelBroadcast  
  
Note that to avoid manually polling the progress,  
MadelineProto will also periodically emit updateBroadcastProgress updates,  
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$from_peer`: `mixed` Bot API ID or Update, from where to forward the messages.  
* `$message_ids`: `list<int>` IDs of the messages to forward.  
* `$drop_author`: `bool` If true, will forward messages without quoting the original author.  
* `$filter`: `?\danog\MadelineProto\Broadcast\Filter`   
* `$pin`: `bool` Whether to also pin the last sent message.  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### `broadcastMessages(array $messages, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false): int`

Sends a list of messages to all peers (users, chats, channels) of the bot.
A simplified version of this method is also available: broadcastForwardMessages can work with pre-prepared messages.  
  
Will return an integer ID that can be used to:  
  
- Get the current broadcast progress with getBroadcastProgress  
- Cancel the broadcast using cancelBroadcast  
  
Note that to avoid manually polling the progress,  
MadelineProto will also periodically emit updateBroadcastProgress updates,  
containing a Progress object for all broadcasts currently in-progress.

Parameters:

* `$messages`: `array` The messages to send: an array of arrays, containing parameters to pass to messages.sendMessage.  
* `$filter`: `?\danog\MadelineProto\Broadcast\Filter`   
* `$pin`: `bool` Whether to also pin the last sent message.  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### `callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<\T>`

Fork a new green thread and execute the passed function in the background.


Parameters:

* `$callable`: `\Generator|\Amp\Future|callable`   
* `...$args`: `mixed` Arguments forwarded to the function when forking the thread.  


#### See also: 
* `\Generator`
* `\Amp\Future`
* `\T`




### `callGetCurrent(int $id): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
Will return a string with the object ID of the stream if we're currently playing a stream, otherwise returns the related LocalFile or RemoteUrl.

Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### `callPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): void`

Play file in call.


Parameters:

* `$id`: `int`   
* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `callPlayOnHold(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`

Play files on hold in call.


Parameters:

* `$id`: `int`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `canConvertOgg(): bool`

Whether we can convert any audio/video file to a VoIP OGG OPUS file, or the files must be preconverted using @libtgvoipbot.



### `cancelBroadcast(int $id): void`

Cancel a running broadcast.


Parameters:

* `$id`: `int` Broadcast ID  



### `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `complete2faLogin(string $password): array`

Complete 2FA login.


Parameters:

* `$password`: `string` Password  



### `completePhoneLogin(string $code): mixed`

Complet user login using login code.


Parameters:

* `$code`: `string` Login code  



### `completeSignup(string $first_name, string $last_name = ''): array`

Complete signup to Telegram.


Parameters:

* `$first_name`: `string` First name  
* `$last_name`: `string` Last name  



### `discardCall(int $id, \danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<\1, \5> $rating = NULL, string $comment = NULL): void`

Discard call.


Parameters:

* `$id`: `int`   
* `$reason`: `\danog\MadelineProto\VoIP\DiscardReason`   
* `$rating`: `int<\1, \5>` Call rating in stars  
* `$comment`: `string` Additional comment on call quality.  


#### See also: 
* [`\danog\MadelineProto\VoIP\DiscardReason`: Why was the call discarded?](../../danog/MadelineProto/VoIP/DiscardReason.html)




### `discardSecretChat(int $chat): void`

Discard secret chat.


Parameters:

* `$chat`: `int` Secret chat ID  



### `downloadServer(string $session): void`

Downloads a file to the browser using the specified session file.


Parameters:

* `$session`: `string`   



### `downloadToBrowser(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message $messageMedia, null|callable $cb = NULL, null|int $size = NULL, null|string $name = NULL, null|string $mime = NULL): void`

Download file to browser.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message` File to download  
* `$cb`: `null|callable` Status callback (can also use FileCallback)  
* `$size`: `null|int` Size of file to download, required for bot API file IDs.  
* `$name`: `null|string` Name of file to download, required for bot API file IDs.  
* `$mime`: `null|string` MIME type of file to download, required for bot API file IDs.  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)




### `downloadToCallable(mixed $messageMedia, callable|\danog\MadelineProto\FileCallbackInterface $callable, callable $cb = NULL, bool $seekable = true, int $offset = 0, int $end = -1, int $part_size = NULL): mixed`

Download file to callable.
The callable must accept two parameters: string $payload, int $offset  
The callable will be called (possibly out of order, depending on the value of $seekable).

Parameters:

* `$messageMedia`: `mixed` File to download  
* `$callable`: `callable|\danog\MadelineProto\FileCallbackInterface` Chunk callback  
* `$cb`: `callable` Status callback  
* `$seekable`: `bool` Whether the callable can be called out of order  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to stop downloading (inclusive)  
* `$part_size`: `int` Size of each chunk  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToDir(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $dir, callable $cb = NULL): mixed`

Download file to directory.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$dir`: `string|\danog\MadelineProto\FileCallbackInterface` Directory where to download the file  
* `$cb`: `callable` Callback  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToFile(mixed $messageMedia, string|\danog\MadelineProto\FileCallbackInterface $file, callable $cb = NULL): string|false`

Download file.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$file`: `string|\danog\MadelineProto\FileCallbackInterface` Downloaded file path  
* `$cb`: `callable` Callback  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `downloadToResponse(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message $messageMedia, \Amp\Http\Server\Request $request, callable $cb = NULL, null|int $size = NULL, null|string $mime = NULL, null|string $name = NULL): \Amp\Http\Server\Response`

Download file to amphp/http-server response.
Supports HEAD requests and content-ranges for parallel and resumed downloads.

Parameters:

* `$messageMedia`: `array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message` File to download  
* `$request`: `\Amp\Http\Server\Request` Request  
* `$cb`: `callable` Status callback (can also use FileCallback)  
* `$size`: `null|int` Size of file to download, required for bot API file IDs.  
* `$mime`: `null|string` MIME type of file to download, required for bot API file IDs.  
* `$name`: `null|string` Name of file to download, required for bot API file IDs.  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* `\Amp\Http\Server\Request`
* `\Amp\Http\Server\Response`




### `downloadToReturnedStream(mixed $messageMedia, callable $cb = NULL, int $offset = 0, int $end = -1): \Amp\ByteStream\ReadableStream`

Download file to an amphp stream, returning it.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$cb`: `callable` Callback  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  


#### See also: 
* `\Amp\ByteStream\ReadableStream`




### `downloadToStream(mixed $messageMedia, mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream $stream, callable $cb = NULL, int $offset = 0, int $end = -1): mixed`

Download file to stream.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$stream`: `mixed|\danog\MadelineProto\FileCallbackInterface|\resource|\Amp\ByteStream\WritableStream` Stream where to download file  
* `$cb`: `callable` Callback  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\resource`
* `\Amp\ByteStream\WritableStream`




### `echo(string $string): void`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `end(array $what): mixed`

Get final element of array.


Parameters:

* `$what`: `array` Array  



### `entitiesToHtml(string $message, list<array{_: string, offset: int, length: int}> $entities, bool $allowTelegramTags = false): string`

Convert a message and a set of entities to HTML.


Parameters:

* `$message`: `string`   
* `$entities`: `list<array{_: string, offset: int, length: int}>`   
* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  



### `exportAuthorization(): array{0: int|string, 1: string}`

Export authorization.



### `extractBotAPIFile(array $info): ?array`

Extract file info from bot API message.


Parameters:

* `$info`: `array` Bot API message object  



### `extractMessage(array $updates): array`

Extract a message constructor from an Updates constructor.


Parameters:

* `$updates`: `array`   



### `extractMessageId(array $updates): int`

Extract a message ID from an Updates constructor.


Parameters:

* `$updates`: `array`   



### `extractMessageUpdate(array $updates): array`

Extract an update message constructor from an Updates constructor.


Parameters:

* `$updates`: `array`   



### `extractUpdates(array $updates): array[]`

Extract Update constructors from an Updates constructor.


Parameters:

* `$updates`: `array`   



### `fileGetContents(string $url): string`

Get contents of remote file asynchronously.


Parameters:

* `$url`: `string` URL  



### `flock(string $file, int $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): mixed`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `int` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Cancellation` Cancellation token  
* `$failureCb`: `?\Closure` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Cancellation`
* `\Closure`




### `fromSupergroup(int $id): int`

Convert bot API channel ID to MTProto channel ID.


Parameters:

* `$id`: `int` Bot API channel ID  



### `fullChatLastUpdated(mixed $id): int`

When was full info for this chat last cached.


Parameters:

* `$id`: `mixed` Chat ID  



### `fullGetSelf(): array|false`

Get info about the logged-in user, not cached.



### `genVectorHash(array $longs): string`

Generate MTProto vector hash.
Returns a vector hash.

Parameters:

* `$longs`: `array` IDs  



### `getAdminIds(): array`

Get admin IDs (equal to all user report peers).



### `getAllCalls(): array<int, \danog\MadelineProto\VoIP>`

Get all pending and running calls, indexed by user ID.


#### See also: 
* [`\danog\MadelineProto\VoIP`: This update represents a VoIP Telegram call.](../../danog/MadelineProto/VoIP.html)




### `getAllMethods(): array`

Get full list of MTProto and API methods.



### `getAuthorization(): \danog\MadelineProto\API::NOT_LOGGED_IN|\danog\MadelineProto\API::WAITING_CODE|\danog\MadelineProto\API::WAITING_SIGNUP|\danog\MadelineProto\API::WAITING_PASSWORD|\danog\MadelineProto\API::LOGGED_IN|\API::LOGGED_OUT`

Get authorization info.


#### See also: 
* `\danog\MadelineProto\API::NOT_LOGGED_IN`
* `\danog\MadelineProto\API::WAITING_CODE`
* `\danog\MadelineProto\API::WAITING_SIGNUP`
* `\danog\MadelineProto\API::WAITING_PASSWORD`
* `\danog\MadelineProto\API::LOGGED_IN`
* `\API::LOGGED_OUT`




### `getBroadcastProgress(int $id): ?\danog\MadelineProto\Broadcast\Progress`

Get the progress of a currently running broadcast.
Will return null if the broadcast doesn't exist, has already completed or was cancelled.  
  
Use updateBroadcastProgress updates to get real-time progress status without polling.

Parameters:

* `$id`: `int` Broadcast ID  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Progress`: Broadcast progress.](../../danog/MadelineProto/Broadcast/Progress.html)




### `getCachedConfig(): array`

Get cached server-side config.



### `getCall(int $id): ?\danog\MadelineProto\VoIP`

Get phone call information.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\VoIP`: This update represents a VoIP Telegram call.](../../danog/MadelineProto/VoIP.html)




### `getCallByPeer(int $userId): ?\danog\MadelineProto\VoIP`

Get the phone call with the specified user ID.


Parameters:

* `$userId`: `int`   


#### See also: 
* [`\danog\MadelineProto\VoIP`: This update represents a VoIP Telegram call.](../../danog/MadelineProto/VoIP.html)




### `getCallState(int $id): ?\danog\MadelineProto\VoIP\CallState`

Get call state.


Parameters:

* `$id`: `int`   


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../danog/MadelineProto/VoIP/CallState.html)




### `getCdnConfig(): void`

Store RSA keys for CDN datacenters.



### `getConfig(array $config = []): array`

Get cached (or eventually re-fetch) server-side config.


Parameters:

* `$config`: `array` Current config  



### `getDNSClient(): \Amp\Dns\DnsResolver`

Get async DNS client.


#### See also: 
* `\Amp\Dns\DnsResolver`




### `getDhConfig(): array`

Get diffie-hellman configuration.



### `getDialogIds(): list<int>`

Get dialog IDs.



### `getDialogs(): list<array>`

Get dialog peers.



### `getDownloadInfo(mixed $messageMedia): array{ext: string, name: string, mime: string, size: int, InputFileLocation: array, key_fingerprint?: string, key?: string, iv?: string, thumb_size?: string}`

Get download info of file
Returns an array with the following structure:.
`$info['ext']` - The file extension  
`$info['name']` - The file name, without the extension  
`$info['mime']` - The file mime type  
`$info['size']` - The file size

Parameters:

* `$messageMedia`: `mixed` File ID  



### `getDownloadLink(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|array|string $media, ?string $scriptUrl = NULL, ?int $size = NULL, ?string $name = NULL, ?string $mime = NULL): string`

Get download link of media file.


Parameters:

* `$media`: `\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|array|string`   
* `$scriptUrl`: `?string`   
* `$size`: `?int`   
* `$name`: `?string`   
* `$mime`: `?string`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)




### `getEventHandler(class-string<\T>|null $class = NULL): \T|\danog\MadelineProto\Ipc\EventHandlerProxy|\__PHP_Incomplete_Class|null`

Get event handler (or plugin instance).


Parameters:

* `$class`: `class-string<\T>|null`   


#### See also: 
* `\T`
* `\danog\MadelineProto\Ipc\EventHandlerProxy`
* `\__PHP_Incomplete_Class`




### `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getFileInfo(mixed $constructor): array`

Get info about file.


Parameters:

* `$constructor`: `mixed` File ID  



### `getFolderId(mixed $id): ?int`

Get folder ID from object.


Parameters:

* `$id`: `mixed` Object  



### `getFullDialogs(): array<int, array>`

Get full info of all dialogs.
Bots should use getDialogs or getDialogIds, instead.


### `getFullInfo(mixed $id): array`

Get full info about peer, returns an FullInfo object.


Parameters:

* `$id`: `mixed` Peer  


#### See also: 
* [https://docs.madelineproto.xyz/FullInfo.html](https://docs.madelineproto.xyz/FullInfo.html)




### `getHTTPClient(): \Amp\Http\Client\HttpClient`

Get async HTTP client.


#### See also: 
* `\Amp\Http\Client\HttpClient`




### `getHint(): string`

Get current password hint.



### `getId(mixed $id): int`

Get the bot API ID of a peer.


Parameters:

* `$id`: `mixed` Peer  



### `getInfo(mixed $id, \danog\MadelineProto\API::INFO_TYPE_* $type = \danog\MadelineProto\API::INFO_TYPE_ALL): mixed`

Get info about peer, returns an Info object.


Parameters:

* `$id`: `mixed` Peer  
* `$type`: `\danog\MadelineProto\API::INFO_TYPE_*` Whether to generate an Input*, an InputPeer or the full set of constructors  


#### See also: 
* [https://docs.madelineproto.xyz/Info.html](https://docs.madelineproto.xyz/Info.html)




### `getLogger(): \danog\MadelineProto\Logger`

Get logger.


#### See also: 
* [`\danog\MadelineProto\Logger`: Logger class.](../../danog/MadelineProto/Logger.html)




### `getMaps(): ?int`

Get current number of memory-mapped regions, UNIX only.



### `getMaxMaps(): ?int`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.


### `getMethodNamespaces(): array`

Get TL namespaces.



### `getMethodsNamespaced(): array`

Get namespaced methods (method => namespace).



### `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



### `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getPlugin(class-string<\T> $class): \danog\MadelineProto\PluginEventHandler|\danog\MadelineProto\Ipc\EventHandlerProxy|null`

Obtain a certain event handler plugin instance.


Parameters:

* `$class`: `class-string<\T>`   


#### See also: 
* `\T`
* [`\danog\MadelineProto\PluginEventHandler`: Plugin event handler class.](../../danog/MadelineProto/PluginEventHandler.html)
* `\danog\MadelineProto\Ipc\EventHandlerProxy`




### `getPropicInfo(mixed $data): array`

Get download info of the propic of a user
Returns an array with the following structure:.
`$info['ext']` - The file extension  
`$info['name']` - The file name, without the extension  
`$info['mime']` - The file mime type  
`$info['size']` - The file size

Parameters:

* `$data`: `mixed`   



### `getPsrLogger(): \Psr\Log\LoggerInterface`

Get PSR logger.


#### See also: 
* `\Psr\Log\LoggerInterface`




### `getPwrChat(mixed $id, bool $fullfetch = true): array`

Get full info about peer (including full list of channel members), returns a Chat object.


Parameters:

* `$id`: `mixed` Peer  
* `$fullfetch`: `bool`   


#### See also: 
* [https://docs.madelineproto.xyz/Chat.html](https://docs.madelineproto.xyz/Chat.html)




### `getSecretChat(array|int $chat): array`

Get secret chat.


Parameters:

* `$chat`: `array|int` Secret chat ID  



### `getSelf(): array|false`

Get info about the logged-in user, cached.
Use fullGetSelf to bypass the cache.


### `getSessionName(): string`

Returns the session name.



### `getSettings(): \danog\MadelineProto\Settings`

Return current settings.


#### See also: 
* [`\danog\MadelineProto\Settings`: Settings class used for configuring MadelineProto.](../../danog/MadelineProto/Settings.html)




### `getSponsoredMessages(int|string|array $peer): ?array`

Get sponsored messages for channel.
This method will return an array of [sponsored message objects](https://docs.madelineproto.xyz/API_docs/constructors/sponsoredMessage.html).  
  
See [the API documentation](https://core.telegram.org/api/sponsored-messages) for more info on how to handle sponsored messages.

Parameters:

* `$peer`: `int|string|array` Channel ID, or Update, or Message, or Peer.  



### `getStreamPipe(): \Amp\ByteStream\Pipe`

Obtains a pipe that can be used to upload a file from a stream.


#### See also: 
* `\Amp\ByteStream\Pipe`




### `getTL(): \danog\MadelineProto\TL\TLInterface`

Get TL serializer.


#### See also: 
* [\danog\MadelineProto\TL\TLInterface](../../danog/MadelineProto/TL/TLInterface.html)




### `getType(mixed $id): \danog\MadelineProto\API::PEER_TYPE_*`

Get type of peer.


Parameters:

* `$id`: `mixed` Peer  



### `getUpdates(array{offset?: int, limit?: int, timeout?: float} $params = []): list<array{update_id: mixed, update: mixed}>`

Only useful when consuming MadelineProto updates through an API in another language (like Javascript), **absolutely not recommended when directly writing MadelineProto bots**.
`getUpdates` will **greatly slow down your bot** if used directly inside of PHP code.  
  
**Only use the [event handler](#async-event-driven) when writing a MadelineProto bot**, because update handling in the **event handler** is completely parallelized and non-blocking.

Parameters:

* `$params`: `array{offset?: int, limit?: int, timeout?: float}` Params  



### `getWebMessage(string $message): string`

Get a message to show to the user when starting the bot.


Parameters:

* `$message`: `string`   



### `getWebWarnings(): string`

Get various warnings to show to the user in the web UI.



### `hasAdmins(): bool`

Check if has admins.



### `hasEventHandler(): bool`

Check if an event handler instance is present.



### `hasPlugin(class-string<\danog\MadelineProto\EventHandler> $class): bool`

Check if a certain event handler plugin is installed.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>`   


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)




### `hasReportPeers(): bool`

Check if has report peers.



### `hasSecretChat(array|int $chat): bool`

Check whether secret chat exists.


Parameters:

* `$chat`: `array|int` Secret chat ID  



### `htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities Object containing message and entities`

Manually convert HTML to a message and a set of entities.
NOTE: You don't have to use this method to send HTML messages.  
  
This method is already called automatically by using parse_mode: "HTML" in messages.sendMessage, messages.sendMedia, et cetera...

Parameters:

* `$html`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)




### `importAuthorization(array<int, string> $authorization, int $mainDcID): array`

Import authorization.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$mainDcID`: `int` Main DC ID  



### `inflateStripped(string $stripped): string`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  



### `initSelfRestart(): void`

Initialize self-restart hack.



### `isAltervista(): bool`

Whether this is altervista.



### `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `isForum(mixed $peer): bool`

Check if the specified peer is a forum.


Parameters:

* `$peer`: `mixed`   



### `isIpc(): bool`

Whether we're an IPC client instance.



### `isIpcWorker(): bool`

Whether we're an IPC server process (as opposed to an event handler).



### `isPlayPaused(int $id): bool`

Whether the currently playing audio file is paused.


Parameters:

* `$id`: `int`   



### `isPremium(): bool`

Returns whether the current user is a premium user, cached.



### `isSelfBot(): bool`

Returns whether the current user is a bot.



### `isSelfUser(): bool`

Returns whether the current user is a user.



### `isSupergroup(int $id): bool`

Check whether provided bot API ID is a channel or supergroup.


Parameters:

* `$id`: `int` Bot API ID  



### `isTestMode(): bool`

Whether we're currently connected to the test DCs.



### `logger(mixed $param, int $level = \danog\MadelineProto\Logger::NOTICE, string $file = ''): void`

Logger.


Parameters:

* `$param`: `mixed` Parameter  
* `$level`: `int` Logging level  
* `$file`: `string` File where the message originated  



### `logout(): void`

Logout the session.



### `markdownCodeblockEscape(string $what): string`

Escape string for markdown codeblock.


Parameters:

* `$what`: `string` String to escape  



### `markdownEscape(string $what): string`

Escape string for markdown.


Parameters:

* `$what`: `string` String to escape  



### `markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities Object containing message and entities`

Manually convert markdown to a message and a set of entities.
NOTE: You don't have to use this method to send Markdown messages.  
  
This method is already called automatically by using parse_mode: "Markdown" in messages.sendMessage, messages.sendMedia, et cetera...

Parameters:

* `$markdown`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)




### `markdownUrlEscape(string $what): string`

Escape string for URL.


Parameters:

* `$what`: `string` String to escape  



### `mbStrSplit(string $text, int $length): string[]`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



### `mbStrlen(string $text): int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, null|int $length = NULL): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `int` Offset  
* `$length`: `null|int` Length  



### `openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): callable`

Provide a buffered reader for a file, URL or amp stream.


Parameters:

* `$stream`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### `openFileAppendOnly(string $path): \Amp\File\File`

Opens a file in append-only mode.


Parameters:

* `$path`: `string` File path.  


#### See also: 
* `\Amp\File\File`




### `packDouble(float $value): string`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### `packSignedInt(int $value): string`

Convert integer to base256 signed int.


Parameters:

* `$value`: `int` Value to convert  



### `packSignedLong(int $value): string`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### `packUnsignedInt(int $value): string`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### `pausePlay(int $id): void`

Pauses playback of the current audio file in the call.


Parameters:

* `$id`: `int`   



### `peerIsset(mixed $id): bool`

Check if peer is present in internal peer database.


Parameters:

* `$id`: `mixed` Peer  



### `phoneLogin(string $number, int $sms_type = 5): mixed`

Login as user.


Parameters:

* `$number`: `string` Phone number  
* `$sms_type`: `int` SMS type  



### `posmod(int $a, int $b): int`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  



### `processDownloadServerPing(string $path, string $payload): void`

Internal endpoint used by the download server.


Parameters:

* `$path`: `string`   
* `$payload`: `string`   



### `qrLogin(): ?\danog\MadelineProto\TL\Types\LoginQrCode`

Initiates QR code login.
Returns a QR code login helper object, that can be used to render the QR code, display the link directly, wait for login, QR code expiration and much more.  
  
Returns null if we're already logged in, or if we're waiting for a password (use getAuthorization to distinguish between the two cases).

#### See also: 
* [`\danog\MadelineProto\TL\Types\LoginQrCode`: Represents a login QR code.](../../danog/MadelineProto/TL/Types/LoginQrCode.html)




### `random(int $length): string`

Get secure random string of specified length.


Parameters:

* `$length`: `int` Length  



### `randomInt(int $modulus = 0): int`

Get random integer.


Parameters:

* `$modulus`: `int` Modulus  



### `readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  
* `$cancel`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### `refreshFullPeerCache(mixed $id): void`

Refresh full peer cache for a certain peer.


Parameters:

* `$id`: `mixed` The peer to refresh  



### `refreshPeerCache(mixed ...$ids): void`

Refresh peer cache for a certain peer.


Parameters:

* `...$ids`: `mixed`   



### `rekey(int $chat): ?string`

Rekey secret chat.


Parameters:

* `$chat`: `int` Secret chat to rekey  



### `report(string $message, string $parseMode = ''): void`

Report an error to the previously set peer.


Parameters:

* `$message`: `string` Error to report  
* `$parseMode`: `string` Parse mode  



### `reportMemoryProfile(): void`

Report memory profile with memprof.



### `requestCall(mixed $user): \danog\MadelineProto\VoIP`

Request VoIP call.


Parameters:

* `$user`: `mixed` User  


#### See also: 
* [`\danog\MadelineProto\VoIP`: This update represents a VoIP Telegram call.](../../danog/MadelineProto/VoIP.html)




### `requestSecretChat(mixed $user): mixed`

Request secret chat.


Parameters:

* `$user`: `mixed` User to start secret chat with  



### `resetUpdateState(): void`

Reset the update state and fetch all updates from the beginning.



### `restart(): void`

Restart update loop.



### `resumePlay(int $id): void`

Resumes playback of the current audio file in the call.


Parameters:

* `$id`: `int`   



### `rethrow(\Throwable $e): void`

Rethrow exception into event loop.


Parameters:

* `$e`: `\Throwable`   


#### See also: 
* `\Throwable`




### `rleDecode(string $string): string`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string): string`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `secretChatStatus(int $chat): \int One of \danog\MadelineProto\API::SECRET_EMPTY, \danog\MadelineProto\API::SECRET_REQUESTED, \danog\MadelineProto\API::SECRET_READY`

Get secret chat status.


Parameters:

* `$chat`: `int` Chat ID  


Return value: One of \danog\MadelineProto\API::SECRET_EMPTY, \danog\MadelineProto\API::SECRET_REQUESTED, \danog\MadelineProto\API::SECRET_READY


### `sendCustomEvent(mixed $payload): void`

Sends an updateCustomEvent update to the event handler.


Parameters:

* `$payload`: `mixed`   



### `sendDocument(int|string $peer, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, ?int $ttl = NULL, bool $spoiler = false, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Sends a document.
Please use named arguments to call this method.

Parameters:

* `$peer`: `int|string` Destination peer or username.  
* `$file`: `\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null` Optional: Thumbnail to upload  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `?string`   
* `$ttl`: `?int`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `int|null` ID of message to reply to.  
* `$topMsgId`: `int|null` ID of thread where to send the message.  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$sendAs`: `int|null` Peer to send the message as.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$updateStickersetsOrder`: `bool` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc.](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)




### `sendMessage(int|string $peer, string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Sends a message.


Parameters:

* `$peer`: `int|string` Destination peer or username.  
* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyToMsgId`: `int|null` ID of message to reply to.  
* `$topMsgId`: `int|null` ID of thread where to send the message.  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$sendAs`: `int|null` Peer to send the message as.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$noWebpage`: `bool` Set this flag to disable generation of the webpage preview  
* `$updateStickersetsOrder`: `bool` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)




### `sendMessageToAdmins(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false): list<\danog\MadelineProto\EventHandler\Message>`

Sends a message to all report peers (admins of the bot).


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$noWebpage`: `bool` Set this flag to disable generation of the webpage preview  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)




### `sendPhoto(int|string $peer, \danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, int|null $replyToMsgId = NULL, int|null $topMsgId = NULL, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Sends a photo.
Please use named arguments to call this method.

Parameters:

* `$peer`: `int|string` Destination peer or username.  
* `$file`: `\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream` File to upload: can be a message to reuse media present in a message.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `?int`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `int|null` ID of message to reply to.  
* `$topMsgId`: `int|null` ID of thread where to send the message.  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$sendAs`: `int|null` Peer to send the message as.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$updateStickersetsOrder`: `bool` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc.](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)




### `setNoop(): void`

Set NOOP update handler, ignoring all updates.



### `setReportPeers(int|string|(int|string)[] $userOrId): void`

Set peer(s) where to send errors occurred in the event loop.


Parameters:

* `$userOrId`: `int|string|(int|string)[]` Username(s) or peer ID(s)  



### `setWebhook(string $webhookUrl): void`

Set webhook update handler.


Parameters:

* `$webhookUrl`: `string` Webhook URL  



### `skipPlay(int $id): void`

When called, skips to the next file in the playlist.


Parameters:

* `$id`: `int`   



### `sleep(float $time): void`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### `start(): mixed`

Log in to telegram (via CLI or web).



### `stop(): void`

Stop update loop.



### `stopPlay(int $id): void`

Stops playing all files in the call, clears the main and the hold playlist.


Parameters:

* `$id`: `int`   



### `stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`

Converts a string into an async amphp stream.


Parameters:

* `$str`: `string`   


#### See also: 
* `\Amp\ByteStream\ReadableBuffer`




### `subscribeToUpdates(mixed $channel): \bool False if we were already subscribed`

Subscribe to event handler updates for a channel/supergroup we're not a member of.


Parameters:

* `$channel`: `mixed` Channel/supergroup to subscribe to  


Return value: False if we were already subscribed


### `tdToMTProto(array $params): array`

Convert TD to MTProto parameters.


Parameters:

* `$params`: `array` Parameters  



### `tdToTdcli(mixed $params): mixed`

Convert TD parameters to tdcli.


Parameters:

* `$params`: `mixed` Parameters  



### `tdcliToTd(mixed $params, array $key = NULL): array`

Convert tdcli parameters to tdcli.


Parameters:

* `$params`: `mixed` Params  
* `$key`: `array` Key  



### `testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.


Parameters:

* `$fiberCount`: `int`   



### `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `toSupergroup(int $id): int`

Convert MTProto channel ID to bot API channel ID.


Parameters:

* `$id`: `int` MTProto channel ID  



### `unpackDouble(string $value): float`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### `unpackFileId(string $fileId): \array Unpacked file ID`

Unpack bot API file ID.


Parameters:

* `$fileId`: `string` Bot API file ID  


Return value: Unpacked file ID


### `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### `unpackSignedLongString(string|int|array $value): string`

Unpack base256 signed long to string.


Parameters:

* `$value`: `string|int|array` base256 long  



### `unsetEventHandler(): void`

Unset event handler.



### `update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params): void`

Update the 2FA password.
The params array can contain password, new_password, email and hint params.

Parameters:

* `$params`: `array{password?: string, new_password?: string, email?: string, hint?: string}` The params  



### `updateSettings(\danog\MadelineProto\SettingsAbstract $settings): void`

Parse, update and store settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `upload(\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|\resource $file, string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`

Upload file.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|\resource` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc.](../../danog/MadelineProto/BotApiFileId.html)
* `\resource`




### `uploadEncrypted(\danog\MadelineProto\FileCallbackInterface|string|array $file, string $fileName = '', callable $cb = NULL): mixed`

Upload file to secret chat.


Parameters:

* `$file`: `\danog\MadelineProto\FileCallbackInterface|string|array` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `uploadFromCallable(mixed $callable, int $size = 0, string $mime = 'application/octet-stream', string $fileName = '', callable $cb = NULL, bool $seekable = true, bool $encrypted = false): mixed`

Upload file from callable.
The callable must accept two parameters: int $offset, int $size  
The callable must return a string with the contest of the file at the specified offset and size.

Parameters:

* `$callable`: `mixed` Callable  
* `$size`: `int` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$seekable`: `bool` Whether chunks can be fetched out of order  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  



### `uploadFromStream(mixed $stream, int $size = 0, string $mime = 'application/octet-stream', string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`

Upload file from stream.


Parameters:

* `$stream`: `mixed` PHP resource or AMPHP async stream  
* `$size`: `int` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  



### `uploadFromTgfile(mixed $media, callable $cb = NULL, bool $encrypted = false): mixed`

Reupload telegram file.


Parameters:

* `$media`: `mixed` Telegram file  
* `$cb`: `callable` Callback  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  



### `uploadFromUrl(string|\danog\MadelineProto\FileCallbackInterface $url, int $size = 0, string $fileName = '', callable $cb = NULL, bool $encrypted = false): mixed`

Upload file from URL.


Parameters:

* `$url`: `string|\danog\MadelineProto\FileCallbackInterface` URL of file  
* `$size`: `int` Size of file  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `bool` Whether to encrypt file for secret chats  


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)




### `validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`

Perform static analysis on a certain event handler class, to make sure it satisfies some performance requirements.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>` Class name  


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)
* [`\danog\MadelineProto\EventHandlerIssue`: Represents an event handler issue.](../../danog/MadelineProto/EventHandlerIssue.html)




### `viewSponsoredMessage(int|array $peer, string|array{random_id: string} $message): bool`

Mark sponsored message as read.


Parameters:

* `$peer`: `int|array` Channel ID, or Update, or Message, or Peer.  
* `$message`: `string|array{random_id: string}` Random ID or sponsored message to mark as read.  



### `wrapMedia(array $media, bool $protected = false): ?\danog\MadelineProto\EventHandler\Media`

Wrap a media constructor into an abstract Media object.


Parameters:

* `$media`: `array`   
* `$protected`: `bool`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)




### `wrapMessage(array $message): ?\danog\MadelineProto\EventHandler\AbstractMessage`

Wrap a Message constructor into an abstract Message object.


Parameters:

* `$message`: `array`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\AbstractMessage`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/AbstractMessage.html)




### `wrapUpdate(array $update): ?\danog\MadelineProto\EventHandler\Update`

Wrap an Update constructor into an abstract Update object.


Parameters:

* `$update`: `array`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Update`: Represents a generic update.](../../danog/MadelineProto/EventHandler/Update.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

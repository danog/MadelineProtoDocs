---
title: "danog\\MadelineProto\\PluginEventHandler: Plugin event handler class."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\PluginEventHandler`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Plugin event handler class.  



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
* `$premium`: `\danog\MadelineProto\Namespace\Premium` 
* `$smsjobs`: `\danog\MadelineProto\Namespace\Smsjobs` 
* `$fragment`: `\danog\MadelineProto\Namespace\Fragment` 
* `$aicompose`: `\danog\MadelineProto\Namespace\Aicompose` 
* `$communities`: `\danog\MadelineProto\Namespace\Communities` 
* `$ephemeral`: `\danog\MadelineProto\Namespace\Ephemeral` 

## Method list:
* [`getPluginPaths(): array|string|null`](#getPluginPaths)
* [`isPluginEnabled(): bool`](#isPluginEnabled)
* [`startAndLoop(string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`](#startAndLoop)
* [`startAndLoopBot(string $session, string $token, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`](#startAndLoopBot)
* [`getPeriodicLoop(string $name): ?\danog\Loop\PeriodicLoop`](#getPeriodicLoop)
* [`getPeriodicLoops(): array<string, \danog\Loop\PeriodicLoop>`](#getPeriodicLoops)
* [`getReportPeers(): (string|int|array<(string|int)>)`](#getReportPeers)
* [`getPlugins(): array<class-string<\danog\MadelineProto\EventHandler>>`](#getPlugins)
* [`initDbProperties(\danog\AsyncOrm\Settings $settings, string $tablePrefix): void`](#initDbProperties)
* [`saveDbProperties(): void`](#saveDbProperties)
* [`MTProtoToBotAPI(array $data): array`](#MTProtoToBotAPI)
* [`MTProtoToTd(mixed $params): array`](#MTProtoToTd)
* [`MTProtoToTdcli(mixed $params): array`](#MTProtoToTdcli)
* [`acceptCall(int $id, ?\Amp\Cancellation $cancellation = NULL): void`](#acceptCall)
* [`acceptSecretChat(array $params): void`](#acceptSecretChat)
* [`arr(mixed ...$params): array`](#arr)
* [`base64urlDecode(string $data): string`](#base64urlDecode)
* [`base64urlEncode(string $data): string`](#base64urlEncode)
* [`botAPIToMTProto(array $arguments): array`](#botAPIToMTProto)
* [`botLogin(string $token): ?array`](#botLogin)
* [`broadcastCustom(\danog\MadelineProto\Broadcast\Action $action, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, (float|null) $delay = NULL): int`](#broadcastCustom)
* [`broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author = false, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false, (float|null) $delay = NULL): int`](#broadcastForwardMessages)
* [`broadcastMessages(array $messages, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false, (float|null) $delay = NULL): int`](#broadcastMessages)
* [`callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<T>`](#callFork)
* [`callGetCurrent(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#callGetCurrent)
* [`callPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#callPlay)
* [`callPlayOnHold(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`](#callPlayOnHold)
* [`callSetOutput(int $id, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`](#callSetOutput)
* [`callSetOutputFolder(int $id, \danog\MadelineProto\LocalDirectory $dir, ?\danog\MadelineProto\RecordingFormat $format = NULL): void`](#callSetOutputFolder)
* [`canConvertOgg(): bool`](#canConvertOgg)
* [`canUseFFmpeg(?\Amp\Cancellation $cancellation = NULL): bool`](#canUseFFmpeg)
* [`cancelBroadcast(integer $id): void`](#cancelBroadcast)
* [`closeConnection(string $message): void`](#closeConnection)
* [`complete2faLogin(string $password): array`](#complete2faLogin)
* [`completePhoneLogin(string $code): array`](#completePhoneLogin)
* [`completeSignup(string $first_name, string $last_name = ''): array`](#completeSignup)
* [`createConferenceCall(bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#createConferenceCall)
* [`createGroupCall(mixed $peer, (string|null) $title = NULL, (int|null) $scheduleDate = NULL, bool $rtmpStream = false): \danog\MadelineProto\EventHandler\Calls\GroupCall`](#createGroupCall)
* [`declineConferenceCallInvite(int $msgId): void`](#declineConferenceCallInvite)
* [`discardCall(int $id, \danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): void`](#discardCall)
* [`discardGroupCall(int $id): void`](#discardGroupCall)
* [`discardSecretChat(int $chat, bool $deleteHistory = false): void`](#discardSecretChat)
* [`downloadServer(string $session): void`](#downloadServer)
* [`downloadToBrowser((array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message) $messageMedia, (null|callable) $cb = NULL, (null|int) $size = NULL, (null|string) $name = NULL, (null|string) $mime = NULL, ?\Amp\Cancellation $cancellation = NULL): void`](#downloadToBrowser)
* [`downloadToCallable(mixed $messageMedia, (callable|\danog\MadelineProto\FileCallbackInterface) $callable, callable $cb = NULL, bool $seekable = true, int $offset = 0, int $end = -1, int $part_size = NULL, ?\Amp\Cancellation $cancellation = NULL): void`](#downloadToCallable)
* [`downloadToDir(mixed $messageMedia, (string|\danog\MadelineProto\FileCallbackInterface) $dir, callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): non-empty-string`](#downloadToDir)
* [`downloadToFile(mixed $messageMedia, (string|\danog\MadelineProto\FileCallbackInterface) $file, callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): non-empty-string`](#downloadToFile)
* [`downloadToResponse((array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message) $messageMedia, \Amp\Http\Server\Request $request, callable $cb = NULL, (null|int) $size = NULL, (null|string) $mime = NULL, (null|string) $name = NULL, ?\Amp\Cancellation $cancellation = NULL): \Amp\Http\Server\Response`](#downloadToResponse)
* [`downloadToReturnedStream(mixed $messageMedia, callable $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): \Amp\ByteStream\ReadableStream`](#downloadToReturnedStream)
* [`downloadToStream(mixed $messageMedia, (mixed|\danog\MadelineProto\FileCallbackInterface|resource|\Amp\ByteStream\WritableStream) $stream, callable $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): void`](#downloadToStream)
* [`echo(string $string): void`](#echo)
* [`end(array<T> $what): T`](#end)
* [`entitiesToHtml(string $message, list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})> $entities, bool $allowTelegramTags = false): string`](#entitiesToHtml)
* [`exportAuthorization(): array{0: int, 1: string}`](#exportAuthorization)
* [`exportGroupCallInvite(int $id, bool $canSelfUnmute = false): string`](#exportGroupCallInvite)
* [`extractBotAPIFile(array $info): ?array`](#extractBotAPIFile)
* [`extractMessage(array $updates): array`](#extractMessage)
* [`extractMessageId(array $updates): int`](#extractMessageId)
* [`extractMessageUpdate(array $updates): array`](#extractMessageUpdate)
* [`extractUpdates(array $updates): array<array>`](#extractUpdates)
* [`fileGetContents(string $url, ?\Amp\Cancellation $cancellation = NULL): string`](#fileGetContents)
* [`flock(string $file, integer $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): ($token is null ? Closure(): void : (Closure(): void | null))`](#flock)
* [`fullChatLastUpdated(mixed $id): int`](#fullChatLastUpdated)
* [`fullGetSelf(): array|false`](#fullGetSelf)
* [`genVectorHash(array<(string|int)> $longs): string`](#genVectorHash)
* [`getAdminIds(): array`](#getAdminIds)
* [`getAllCalls(): array<int, \danog\MadelineProto\EventHandler\Calls\PrivateCall>`](#getAllCalls)
* [`getAllGroupCalls(): array<int, \danog\MadelineProto\EventHandler\Calls\AbstractGroupCall>`](#getAllGroupCalls)
* [`getAllMethods(): array`](#getAllMethods)
* [`getAuthorization(): (\danog\MadelineProto\API::NOT_LOGGED_IN|\danog\MadelineProto\API::WAITING_CODE|\danog\MadelineProto\API::WAITING_SIGNUP|\danog\MadelineProto\API::WAITING_PASSWORD|\danog\MadelineProto\API::LOGGED_IN|API::LOGGED_OUT)`](#getAuthorization)
* [`getBroadcastProgress(integer $id): ?\danog\MadelineProto\Broadcast\Progress`](#getBroadcastProgress)
* [`getCachedConfig(): array`](#getCachedConfig)
* [`getCall(int $id): ?\danog\MadelineProto\EventHandler\Calls\PrivateCall`](#getCall)
* [`getCallByPeer(int $userId): ?\danog\MadelineProto\EventHandler\Calls\PrivateCall`](#getCallByPeer)
* [`getCallRemoteMediaState(int $id): ?\danog\MadelineProto\VoIP\MediaState`](#getCallRemoteMediaState)
* [`getCallState(int $id): ?\danog\MadelineProto\VoIP\CallState`](#getCallState)
* [`getCdnConfig(): void`](#getCdnConfig)
* [`getConferenceCall(int $id): ?\danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#getConferenceCall)
* [`getConferenceCallBySlug(string $slug): ?\danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#getConferenceCallBySlug)
* [`getConfig(array $config = []): array`](#getConfig)
* [`getDNSClient(): \Amp\Dns\DnsResolver`](#getDNSClient)
* [`getDhConfig(?\Amp\Cancellation $cancellation = NULL): array`](#getDhConfig)
* [`getDialogIds(): list<int>`](#getDialogIds)
* [`getDownloadInfo(mixed $messageMedia): array{ext: string, name: string, mime: string, size: int, InputFileLocation: array, key_fingerprint?: string, key?: string, iv?: string, thumb_size?: string}`](#getDownloadInfo)
* [`getDownloadLink(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|array|string $media, ?string $scriptUrl = NULL, ?int $size = NULL, ?string $name = NULL, ?string $mime = NULL): string`](#getDownloadLink)
* [`getEventHandler((class-string<T>|null) $class = NULL): (T|\danog\MadelineProto\Ipc\EventHandlerProxy|\__PHP_Incomplete_Class|null)`](#getEventHandler)
* [`getExtensionFromLocation(mixed $location, string $default): string`](#getExtensionFromLocation)
* [`getExtensionFromMime(string $mime): string`](#getExtensionFromMime)
* [`getFileInfo(mixed $constructor): array`](#getFileInfo)
* [`getFullDialogs(): array<int, array>`](#getFullDialogs)
* [`getFullInfo(mixed $id): array`](#getFullInfo)
* [`getGroupCall(mixed $peer): ?\danog\MadelineProto\EventHandler\Calls\GroupCall`](#getGroupCall)
* [`getGroupCallBySlug(string $slug): ?\danog\MadelineProto\EventHandler\Calls\GroupCall`](#getGroupCallBySlug)
* [`getGroupCallJoinAs(mixed $peer): list<int>`](#getGroupCallJoinAs)
* [`getGroupCallParticipants(int $id): array<int, \danog\MadelineProto\EventHandler\Participant>`](#getGroupCallParticipants)
* [`getGroupCallState(int $id): \danog\MadelineProto\GroupCall\GroupCallState`](#getGroupCallState)
* [`getGroupCallStreamRtmpUrl(mixed $peer, bool $revoke = false, bool $liveStory = false): array{url: string, key: string}`](#getGroupCallStreamRtmpUrl)
* [`getHTTPClient(): \Amp\Http\Client\HttpClient`](#getHTTPClient)
* [`getHint(): string`](#getHint)
* [`getId(mixed $id): int`](#getId)
* [`getInfo(mixed $id, \danog\MadelineProto\API::INFO_TYPE_* $type = \danog\MadelineProto\API::INFO_TYPE_ALL): (\$type is \danog\MadelineProto\API::INFO_TYPE_ALL ? array{User?: array, Chat?: array, bot_api_id: int, user_id?: int, chat_id?: int, channel_id?: int, type: string} : ($type is API::INFO_TYPE_TYPE ? string : ($type is \danog\MadelineProto\API::INFO_TYPE_ID ? int : (array{_: string, user_id?: int, access_hash?: int, min?: bool, chat_id?: int, channel_id?: int} | array{_: string, user_id?: int, access_hash?: int, min?: bool} | array{_: string, channel_id: int, access_hash: int, min: bool}))))`](#getInfo)
* [`getLogger(): \danog\MadelineProto\Logger`](#getLogger)
* [`getMaps(): ?int`](#getMaps)
* [`getMaxMaps(): ?int`](#getMaxMaps)
* [`getMemoryProfile(): string`](#getMemoryProfile)
* [`getMethodNamespaces(): array`](#getMethodNamespaces)
* [`getMethodsNamespaced(): array`](#getMethodsNamespaced)
* [`getMimeFromBuffer(string $buffer): string`](#getMimeFromBuffer)
* [`getMimeFromExtension(string $extension, string $default): string`](#getMimeFromExtension)
* [`getMimeFromFile(string $file): string`](#getMimeFromFile)
* [`getPlugin(class-string<T> $class): \danog\MadelineProto\PluginEventHandler|\danog\MadelineProto\Ipc\EventHandlerProxy|null`](#getPlugin)
* [`getPromCounter(string $namespace, string $name, string $help, array<string, string> $labels = []): ?\danog\BetterPrometheus\BetterCounter`](#getPromCounter)
* [`getPromGauge(string $namespace, string $name, string $help, array<string, string> $labels = []): ?\danog\BetterPrometheus\BetterGauge`](#getPromGauge)
* [`getPromHistogram(string $namespace, string $name, string $help, array<string, string> $labels = [], ?non-empty-list<float> $buckets = NULL): ?\danog\BetterPrometheus\BetterHistogram`](#getPromHistogram)
* [`getPromSummary(string $namespace, string $name, string $help, array<string, string> $labels = [], int $maxAgeSeconds = 600, ?non-empty-list<float> $quantiles = NULL): ?\danog\BetterPrometheus\BetterSummary`](#getPromSummary)
* [`getPropicInfo(mixed $data): ?\danog\MadelineProto\EventHandler\Media\Photo`](#getPropicInfo)
* [`getPsrLogger(): \Psr\Log\LoggerInterface`](#getPsrLogger)
* [`getPwrChat(mixed $id, bool $fullfetch = true): array`](#getPwrChat)
* [`getSecretChat((array|int) $chat): \danog\MadelineProto\SecretChats\SecretChat`](#getSecretChat)
* [`getSecretMessage(integer $chatId, integer $randomId): \danog\MadelineProto\EventHandler\Message\SecretMessage`](#getSecretMessage)
* [`getSelf(): array|false`](#getSelf)
* [`getSessionName(): string`](#getSessionName)
* [`getSettings(): \danog\MadelineProto\Settings`](#getSettings)
* [`getSponsoredMessages((int|string|array) $peer): ?array`](#getSponsoredMessages)
* [`getStream(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL, ?int $size = NULL): \Amp\ByteStream\ReadableStream`](#getStream)
* [`getStreamPipe(): \Amp\ByteStream\Pipe`](#getStreamPipe)
* [`getType(mixed $id): \danog\MadelineProto\API::PEER_TYPE_*`](#getType)
* [`getUpdates(array{offset?: int, limit?: int, timeout?: float} $params = []): list<array{update_id: mixed, update: mixed}>`](#getUpdates)
* [`getWebMessage(string $message): string`](#getWebMessage)
* [`getWebWarnings(): string`](#getWebWarnings)
* [`groupCallGetCurrent(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#groupCallGetCurrent)
* [`groupCallPausePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#groupCallPausePlay)
* [`groupCallPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#groupCallPlay)
* [`groupCallPlayOnHold(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`](#groupCallPlayOnHold)
* [`groupCallResumePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#groupCallResumePlay)
* [`groupCallSetOutput(int $id, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`](#groupCallSetOutput)
* [`groupCallSetOutputFolder(int $id, \danog\MadelineProto\LocalDirectory $dir, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): void`](#groupCallSetOutputFolder)
* [`groupCallSkipPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#groupCallSkipPlay)
* [`groupCallStopPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#groupCallStopPlay)
* [`hasAdmins(): bool`](#hasAdmins)
* [`hasEventHandler(): bool`](#hasEventHandler)
* [`hasPlugin(class-string<\danog\MadelineProto\EventHandler> $class): bool`](#hasPlugin)
* [`hasReportPeers(): bool`](#hasReportPeers)
* [`hasSecretChat((array|int) $chat): bool`](#hasSecretChat)
* [`htmlEscape(string $what): string`](#htmlEscape)
* [`htmlToMessageEntities(string $html): \danog\MadelineProto\TextEntities`](#htmlToMessageEntities)
* [`importAuthorization(array<int, string> $authorization, int $mainDcID): array`](#importAuthorization)
* [`inflateStripped(string $stripped): string`](#inflateStripped)
* [`initSelfRestart(): void`](#initSelfRestart)
* [`inviteToGroupCall(int $id, mixed ...$users): void`](#inviteToGroupCall)
* [`isAltervista(): bool`](#isAltervista)
* [`isArrayOrAlike(mixed $var): bool`](#isArrayOrAlike)
* [`isBot(mixed $peer): bool`](#isBot)
* [`isCallMuted(int $id): bool`](#isCallMuted)
* [`isForum(mixed $peer): bool`](#isForum)
* [`isGroupCallMuted(int $id): bool`](#isGroupCallMuted)
* [`isGroupCallPlayPaused(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isGroupCallPlayPaused)
* [`isIpc(): bool`](#isIpc)
* [`isIpcWorker(): bool`](#isIpcWorker)
* [`isPlayPaused(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPlayPaused)
* [`isPremium(): bool`](#isPremium)
* [`isSelfBot(): bool`](#isSelfBot)
* [`isSelfUser(): bool`](#isSelfUser)
* [`isTestMode(): boolean`](#isTestMode)
* [`joinConferenceCall(array $call, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#joinConferenceCall)
* [`joinConferenceCallByInviteMessage(int $msgId, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#joinConferenceCallByInviteMessage)
* [`joinConferenceCallBySlug(string $slug, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#joinConferenceCallBySlug)
* [`joinGroupCall(mixed $peer, bool $muted = false, mixed $joinAs = NULL, (string|null) $inviteHash = NULL): \danog\MadelineProto\EventHandler\Calls\GroupCall`](#joinGroupCall)
* [`leaveGroupCall(int $id): void`](#leaveGroupCall)
* [`logger(mixed $param, int $level = \danog\MadelineProto\Logger::NOTICE, string $file = ''): void`](#logger)
* [`logout(): void`](#logout)
* [`markdownCodeEscape(string $what): string`](#markdownCodeEscape)
* [`markdownCodeblockEscape(string $what): string`](#markdownCodeblockEscape)
* [`markdownEscape(string $what): string`](#markdownEscape)
* [`markdownToMessageEntities(string $markdown): \danog\MadelineProto\TextEntities`](#markdownToMessageEntities)
* [`markdownUrlEscape(string $what): string`](#markdownUrlEscape)
* [`mbStrSplit(string $text, integer $length): array<string>`](#mbStrSplit)
* [`mbStrlen(string $text): int`](#mbStrlen)
* [`mbSubstr(string $text, integer $offset, (null|int) $length = NULL): string`](#mbSubstr)
* [`migrateCallToConference(int $id, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#migrateCallToConference)
* [`openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL, int $offset = 0): Closure(int): ?string`](#openBuffered)
* [`openFileAppendOnly(string $path): \Amp\File\File`](#openFileAppendOnly)
* [`packDouble(float $value): string`](#packDouble)
* [`packSignedInt(integer $value): string`](#packSignedInt)
* [`packSignedLong(int $value): string`](#packSignedLong)
* [`packUnsignedInt(int $value): string`](#packUnsignedInt)
* [`pausePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#pausePlay)
* [`peerIsset(mixed $id): bool`](#peerIsset)
* [`phoneLogin(string $number, integer $sms_type = 5): array`](#phoneLogin)
* [`posmod(int $a, int $b): int`](#posmod)
* [`processDownloadServerPing(string $path, string $payload): void`](#processDownloadServerPing)
* [`qrLogin(): ?\danog\MadelineProto\TL\Types\LoginQrCode`](#qrLogin)
* [`random(integer $length): string`](#random)
* [`randomInt(integer $modulus = 0): int`](#randomInt)
* [`readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`](#readLine)
* [`refreshFullPeerCache(mixed $id): void`](#refreshFullPeerCache)
* [`refreshPeerCache(mixed ...$ids): void`](#refreshPeerCache)
* [`renderPromStats(?\Prometheus\RendererInterface $renderer = NULL): string`](#renderPromStats)
* [`report(string $message, string $parseMode = ''): void`](#report)
* [`reportMemoryProfile(): void`](#reportMemoryProfile)
* [`requestCall(mixed $user, bool $video = false): \danog\MadelineProto\EventHandler\Calls\PrivateCall`](#requestCall)
* [`requestSecretChat(mixed $user): int`](#requestSecretChat)
* [`resetUpdateState(): void`](#resetUpdateState)
* [`restart(): void`](#restart)
* [`resumePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#resumePlay)
* [`rethrow(Throwable $e): void`](#rethrow)
* [`rleDecode(string $string): string`](#rleDecode)
* [`rleEncode(string $string): string`](#rleEncode)
* [`saveDefaultGroupCallJoinAs(mixed $peer, mixed $joinAs): void`](#saveDefaultGroupCallJoinAs)
* [`sendAudio((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, (integer|null) $duration = NULL, (string|null) $title = NULL, (string|null) $performer = NULL, ?int $ttl = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendAudio)
* [`sendCustomEvent(mixed $payload): void`](#sendCustomEvent)
* [`sendDocument((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendDocument)
* [`sendDocumentPhoto((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendDocumentPhoto)
* [`sendGif((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $ttl = NULL, boolean $spoiler = false, ?int $duration = NULL, ?int $width = NULL, ?int $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendGif)
* [`sendMessage((integer|string) $peer, string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendMessage)
* [`sendMessageToAdmins(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, ?\Amp\Cancellation $cancellation = NULL): list<\danog\MadelineProto\EventHandler\Message>`](#sendMessageToAdmins)
* [`sendPhoto((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendPhoto)
* [`sendSticker((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $mimeType, string $emoji = '', array $stickerSet = [  '_' => 'inputStickerSetEmpty',], ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendSticker)
* [`sendVideo((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, string $mimeType = 'video/mp4', (integer|null) $ttl = NULL, boolean $spoiler = false, boolean $roundMessage = false, boolean $supportsStreaming = true, boolean $noSound = false, (integer|null) $duration = NULL, (integer|null) $width = NULL, (integer|null) $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, bool $updateStickersetsOrder = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendVideo)
* [`sendVoice((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $ttl = NULL, (integer|null) $duration = NULL, (array|null) $waveform = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendVoice)
* [`setCallMuted(int $id, bool $muted = true): void`](#setCallMuted)
* [`setGroupCallMuted(int $id, bool $muted = true): void`](#setGroupCallMuted)
* [`setGroupCallTitle(int $id, string $title): void`](#setGroupCallTitle)
* [`setNoop(): void`](#setNoop)
* [`setReportPeers((int|string|array<(int|string)>) $userOrId): void`](#setReportPeers)
* [`setWebhook(string $webhookUrl): void`](#setWebhook)
* [`skipPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#skipPlay)
* [`sleep(float $time): void`](#sleep)
* [`start(): array`](#start)
* [`startLive(mixed $peer, (string|null) $caption = NULL, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, list<array<string, mixed>> $privacyRules = [  0 =>   [    '_' => 'inputPrivacyValueAllowAll',  ],], bool $pinned = false, bool $noForwards = false, bool $rtmpStream = false, (bool|null) $messagesEnabled = NULL, (int|null) $sendPaidMessagesStars = NULL): \danog\MadelineProto\EventHandler\Calls\LiveStory`](#startLive)
* [`stop(): void`](#stop)
* [`stopPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`](#stopPlay)
* [`stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`](#stringToStream)
* [`subscribeToUpdates(mixed $channel): bool`](#subscribeToUpdates)
* [`tdToMTProto(array $params): array`](#tdToMTProto)
* [`tdToTdcli(mixed $params): array`](#tdToTdcli)
* [`tdcliToTd(mixed $params, array $key = NULL): array`](#tdcliToTd)
* [`testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`](#testFibers)
* [`toCamelCase(string $input): string`](#toCamelCase)
* [`toSnakeCase(string $input): string`](#toSnakeCase)
* [`unpackDouble(string $value): float`](#unpackDouble)
* [`unpackFileId(string $fileId): array`](#unpackFileId)
* [`unpackSignedInt(string $value): int`](#unpackSignedInt)
* [`unpackSignedLong(string $value): int`](#unpackSignedLong)
* [`unpackSignedLongString((string|int|array) $value): string`](#unpackSignedLongString)
* [`unsetEventHandler(): void`](#unsetEventHandler)
* [`update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params): void`](#update2fa)
* [`updateSettings(\danog\MadelineProto\SettingsAbstract $settings): void`](#updateSettings)
* [`upload((\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|string|array|resource) $file, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`](#upload)
* [`uploadAudio((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, (integer|null) $duration = NULL, (string|null) $title = NULL, (string|null) $performer = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadAudio)
* [`uploadDocument((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadDocument)
* [`uploadDocumentPhoto((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadDocumentPhoto)
* [`uploadEncrypted((\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|resource) $file, string $fileName = '', callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): array`](#uploadEncrypted)
* [`uploadFromCallable(callable(int, int, ?Cancellation): strin) $callable, integer $size = 0, ?string $mime = NULL, string $fileName = '', callable(float, float, float): voi) $cb = NULL, boolean $seekable = true, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`](#uploadFromCallable)
* [`uploadFromStream(mixed $stream, integer $size = 0, string $mime = NULL, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`](#uploadFromStream)
* [`uploadFromTgfile(mixed $media, callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`](#uploadFromTgfile)
* [`uploadFromUrl((string|\danog\MadelineProto\FileCallbackInterface) $url, integer $size = 0, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`](#uploadFromUrl)
* [`uploadGif((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, boolean $spoiler = false, ?int $duration = NULL, ?int $width = NULL, ?int $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadGif)
* [`uploadPhoto((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadPhoto)
* [`uploadSticker((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $mimeType, (integer|string|null) $peer = NULL, string $emoji = '', array $stickerSet = [  '_' => 'inputStickerSetEmpty',], ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadSticker)
* [`uploadVideo((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, string $mimeType = 'video/mp4', boolean $spoiler = false, boolean $roundMessage = false, boolean $supportsStreaming = true, boolean $noSound = false, (integer|null) $duration = NULL, (integer|null) $width = NULL, (integer|null) $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, bool $updateStickersetsOrder = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadVideo)
* [`uploadVoice((integer|string|null) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $duration = NULL, (array|null) $waveform = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`](#uploadVoice)
* [`validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`](#validateEventHandlerClass)
* [`viewSponsoredMessage((int|array) $peer, (string|array{random_id: string}) $message): bool`](#viewSponsoredMessage)
* [`wrapMedia(array $media, bool $protected = false): ?\danog\MadelineProto\EventHandler\Media`](#wrapMedia)
* [`wrapMessage(array $message, bool $scheduled = false): ?\danog\MadelineProto\EventHandler\AbstractMessage`](#wrapMessage)
* [`wrapPin(array $message): ?\danog\MadelineProto\EventHandler\Pinned`](#wrapPin)
* [`wrapUpdate(array $update): ?\danog\MadelineProto\EventHandler\Update`](#wrapUpdate)

## Methods:
### <a name="getPluginPaths"></a> `getPluginPaths(): array|string|null`

Plugins can require other plugins ONLY with the getPlugins() method.



### <a name="isPluginEnabled"></a> `isPluginEnabled(): bool`

Whether the plugin is enabled.



### <a name="startAndLoop"></a> `startAndLoop(string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`

Start MadelineProto and the event handler.
  
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.  


Parameters:

* `$session`: `string` Session name  
* `$settings`: `?\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### <a name="startAndLoopBot"></a> `startAndLoopBot(string $session, string $token, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): void`

Start MadelineProto as a bot and the event handler.
  
Also initializes error reporting, catching and reporting all errors surfacing from the event loop.  


Parameters:

* `$session`: `string` Session name  
* `$token`: `string` Bot token  
* `$settings`: `?\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### <a name="getPeriodicLoop"></a> `getPeriodicLoop(string $name): ?\danog\Loop\PeriodicLoop`

Obtain a PeriodicLoop instance created by the Cron attribute.


Parameters:

* `$name`: `string` Method name  


#### See also: 
* `\danog\Loop\PeriodicLoop`




### <a name="getPeriodicLoops"></a> `getPeriodicLoops(): array<string, \danog\Loop\PeriodicLoop>`

Obtain all PeriodicLoop instances created by the Cron attribute.


#### See also: 
* `\danog\Loop\PeriodicLoop`




### <a name="getReportPeers"></a> `getReportPeers(): (string|int|array<(string|int)>)`

Get peers where to send error reports.



### <a name="getPlugins"></a> `getPlugins(): array<class-string<\danog\MadelineProto\EventHandler>>`

Obtain a list of plugin event handlers to use, in addition with those found by getPluginPath.



### <a name="initDbProperties"></a> `initDbProperties(\danog\AsyncOrm\Settings $settings, string $tablePrefix): void`

Initialize database properties.


Parameters:

* `$settings`: `\danog\AsyncOrm\Settings`   
* `$tablePrefix`: `string`   


#### See also: 
* `\danog\AsyncOrm\Settings`




### <a name="saveDbProperties"></a> `saveDbProperties(): void`

Save all properties.



### <a name="MTProtoToBotAPI"></a> `MTProtoToBotAPI(array $data): array`

Convert MTProto parameters to bot API parameters.


Parameters:

* `$data`: `array` Data  



### <a name="MTProtoToTd"></a> `MTProtoToTd(mixed $params): array`

MTProto to TD params.


Parameters:

* `$params`: `mixed` Params  



### <a name="MTProtoToTdcli"></a> `MTProtoToTdcli(mixed $params): array`

MTProto to TDCLI params.


Parameters:

* `$params`: `mixed` Params  



### <a name="acceptCall"></a> `acceptCall(int $id, ?\Amp\Cancellation $cancellation = NULL): void`

Accept call.


Parameters:

* `$id`: `int`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="acceptSecretChat"></a> `acceptSecretChat(array $params): void`

Accept secret chat.


Parameters:

* `$params`: `array` Secret chat ID  



### <a name="arr"></a> `arr(mixed ...$params): array`

Create array.


Parameters:

* `...$params`: `mixed` Params  



### <a name="base64urlDecode"></a> `base64urlDecode(string $data): string`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### <a name="base64urlEncode"></a> `base64urlEncode(string $data): string`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### <a name="botAPIToMTProto"></a> `botAPIToMTProto(array $arguments): array`

Convert bot API parameters to MTProto parameters.


Parameters:

* `$arguments`: `array` Arguments  



### <a name="botLogin"></a> `botLogin(string $token): ?array`

Login as bot.


Parameters:

* `$token`: `string` Bot token  



### <a name="broadcastCustom"></a> `broadcastCustom(\danog\MadelineProto\Broadcast\Action $action, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, (float|null) $delay = NULL): int`

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
* `$delay`: `(float|null)` Number of seconds to wait between each peer.  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Action`: Interface that represents a broadcast action.](../../danog/MadelineProto/Broadcast/Action.html)
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### <a name="broadcastForwardMessages"></a> `broadcastForwardMessages(mixed $from_peer, list<int> $message_ids, bool $drop_author = false, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false, (float|null) $delay = NULL): int`

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
* `$delay`: `(float|null)` Number of seconds to wait between each peer.  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### <a name="broadcastMessages"></a> `broadcastMessages(array $messages, ?\danog\MadelineProto\Broadcast\Filter $filter = NULL, bool $pin = false, (float|null) $delay = NULL): int`

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
* `$delay`: `(float|null)` Number of seconds to wait between each peer.  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Filter`: Broadcast filter.](../../danog/MadelineProto/Broadcast/Filter.html)




### <a name="callFork"></a> `callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<T>`

Fork a new green thread and execute the passed function in the background.


Parameters:

* `$callable`: `\Generator|\Amp\Future|callable`   
* `...$args`: `mixed` Arguments forwarded to the function when forking the thread.  


#### See also: 
* `\Generator`
* `\Amp\Future`




### <a name="callGetCurrent"></a> `callGetCurrent(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
  
Will return a string with the object ID of the stream if we're currently playing a stream, otherwise returns the related LocalFile or RemoteUrl.  


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### <a name="callPlay"></a> `callPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Play file in call.


Parameters:

* `$id`: `int`   
* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="callPlayOnHold"></a> `callPlayOnHold(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`

Play files on hold in call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="callSetOutput"></a> `callSetOutput(int $id, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`

Record the incoming media of a call into one file (or stream) with a fixed set of tracks, see
{@see \danog\MadelineProto\EventHandler\Calls\PrivateCall::setOutput()}.  


Parameters:

* `$id`: `int`   
* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `?int` The streams to record, as a bitmask of {@see CallStream} flags, or null for every available one.  


Return value: The streams the other party currently sends, as a bitmask of {@see CallStream} flags (0 while unknown).

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../danog/MadelineProto/RecordingFormat.html)




### <a name="callSetOutputFolder"></a> `callSetOutputFolder(int $id, \danog\MadelineProto\LocalDirectory $dir, ?\danog\MadelineProto\RecordingFormat $format = NULL): void`

Record the incoming media of a call into a directory, one numbered file per combination of
streams the other party sends, see {@see \danog\MadelineProto\EventHandler\Calls\PrivateCall::setOutputFolder()}.  


Parameters:

* `$id`: `int`   
* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../danog/MadelineProto/RecordingFormat.html)




### <a name="canConvertOgg"></a> `canConvertOgg(): bool`

Whether we can convert any audio/video file to a VoIP OGG OPUS file, or the files must be preconverted using @libtgvoipbot.



### <a name="canUseFFmpeg"></a> `canUseFFmpeg(?\Amp\Cancellation $cancellation = NULL): bool`

Whether we can convert any audio/video file using ffmpeg.


Parameters:

* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="cancelBroadcast"></a> `cancelBroadcast(integer $id): void`

Cancel a running broadcast.


Parameters:

* `$id`: `integer` Broadcast ID  



### <a name="closeConnection"></a> `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### <a name="complete2faLogin"></a> `complete2faLogin(string $password): array`

Complete 2FA login.


Parameters:

* `$password`: `string` Password  



### <a name="completePhoneLogin"></a> `completePhoneLogin(string $code): array`

Complet user login using login code.


Parameters:

* `$code`: `string` Login code  



### <a name="completeSignup"></a> `completeSignup(string $first_name, string $last_name = ''): array`

Complete signup to Telegram.


Parameters:

* `$first_name`: `string` First name  
* `$last_name`: `string` Last name  



### <a name="createConferenceCall"></a> `createConferenceCall(bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Create and join a new end-to-end encrypted conference call, with ourselves as the only
participant. Others join it with {@see self::joinConferenceCall()} using the returned call id.  
  
See [end-to-end encrypted group calls »](https://core.telegram.org/api/end-to-end/group-calls).  
Requires the `sodium` and `openssl` PHP extensions.  


Parameters:

* `$muted`: `bool` Whether to join muted.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="createGroupCall"></a> `createGroupCall(mixed $peer, (string|null) $title = NULL, (int|null) $scheduleDate = NULL, bool $rtmpStream = false): \danog\MadelineProto\EventHandler\Calls\GroupCall`

Create a group call (video chat or livestream) in the specified group or channel.
  
Requires the `manage_call` admin right, see  
[video chats/livestreams »](https://core.telegram.org/api/group-calls#video-chats-livestreams).  


Parameters:

* `$peer`: `mixed` The group or channel where the call should be created.  
* `$title`: `(string|null)` Custom title, defaults to the group/channel name.  
* `$scheduleDate`: `(int|null)` If set, creates a scheduled call for the specified UNIX timestamp.  
* `$rtmpStream`: `bool` Whether the call's media is published by an external RTMP application.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\GroupCall`: This update represents a Telegram [video chat or livestream »](https://core.telegram.org/api/group-calls#video-chats-livestreams):](../../danog/MadelineProto/EventHandler/Calls/GroupCall.html)




### <a name="declineConferenceCallInvite"></a> `declineConferenceCallInvite(int $msgId): void`

Decline an invitation to a conference call.


Parameters:

* `$msgId`: `int` ID of the invitation message (a `messageActionConferenceCall`).  



### <a name="discardCall"></a> `discardCall(int $id, \danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): void`

Discard call.


Parameters:

* `$id`: `int`   
* `$reason`: `\danog\MadelineProto\VoIP\DiscardReason`   
* `$rating`: `int<1, 5>` Call rating in stars  
* `$comment`: `string` Additional comment on call quality.  


#### See also: 
* [`\danog\MadelineProto\VoIP\DiscardReason`: Why was the call discarded?](../../danog/MadelineProto/VoIP/DiscardReason.html)




### <a name="discardGroupCall"></a> `discardGroupCall(int $id): void`

End a group call for all participants.


Parameters:

* `$id`: `int`   



### <a name="discardSecretChat"></a> `discardSecretChat(int $chat, bool $deleteHistory = false): void`

Discard secret chat.


Parameters:

* `$chat`: `int` Secret chat ID  
* `$deleteHistory`: `bool` If true, deletes the entire chat history for the other user as well.  



### <a name="downloadServer"></a> `downloadServer(string $session): void`

Downloads a file to the browser using the specified session file.


Parameters:

* `$session`: `string`   



### <a name="downloadToBrowser"></a> `downloadToBrowser((array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message) $messageMedia, (null|callable) $cb = NULL, (null|int) $size = NULL, (null|string) $name = NULL, (null|string) $mime = NULL, ?\Amp\Cancellation $cancellation = NULL): void`

Download file to browser.
  
Supports HEAD requests and content-ranges for parallel and resumed downloads.  


Parameters:

* `$messageMedia`: `(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message)` File to download  
* `$cb`: `(null|callable)` Status callback (can also use FileCallback)  
* `$size`: `(null|int)` Size of file to download, required for bot API file IDs.  
* `$name`: `(null|string)` Name of file to download, required for bot API file IDs.  
* `$mime`: `(null|string)` MIME type of file to download, required for bot API file IDs.  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* `\Amp\Cancellation`




### <a name="downloadToCallable"></a> `downloadToCallable(mixed $messageMedia, (callable|\danog\MadelineProto\FileCallbackInterface) $callable, callable $cb = NULL, bool $seekable = true, int $offset = 0, int $end = -1, int $part_size = NULL, ?\Amp\Cancellation $cancellation = NULL): void`

Download file to callable.
The callable must accept two parameters: string $payload, int $offset  
The callable will be called (possibly out of order, depending on the value of $seekable).  


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$callable`: `(callable|\danog\MadelineProto\FileCallbackInterface)` Chunk callback  
* `$cb`: `callable` Status callback  
* `$seekable`: `bool` Whether the callable can be called out of order  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to stop downloading (inclusive)  
* `$part_size`: `int` Size of each chunk  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\Amp\Cancellation`




### <a name="downloadToDir"></a> `downloadToDir(mixed $messageMedia, (string|\danog\MadelineProto\FileCallbackInterface) $dir, callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): non-empty-string`

Download file to directory.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$dir`: `(string|\danog\MadelineProto\FileCallbackInterface)` Directory where to download the file  
* `$cb`: `callable` Callback  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: Downloaded file name

#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\Amp\Cancellation`
* `non-empty-string`




### <a name="downloadToFile"></a> `downloadToFile(mixed $messageMedia, (string|\danog\MadelineProto\FileCallbackInterface) $file, callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): non-empty-string`

Download file.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$file`: `(string|\danog\MadelineProto\FileCallbackInterface)` Downloaded file path  
* `$cb`: `callable` Callback  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: Downloaded file name

#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\Amp\Cancellation`
* `non-empty-string`




### <a name="downloadToResponse"></a> `downloadToResponse((array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message) $messageMedia, \Amp\Http\Server\Request $request, callable $cb = NULL, (null|int) $size = NULL, (null|string) $mime = NULL, (null|string) $name = NULL, ?\Amp\Cancellation $cancellation = NULL): \Amp\Http\Server\Response`

Download file to amphp/http-server response.
  
Supports HEAD requests and content-ranges for parallel and resumed downloads.  


Parameters:

* `$messageMedia`: `(array|string|\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\EventHandler\Message)` File to download  
* `$request`: `\Amp\Http\Server\Request` Request  
* `$cb`: `callable` Status callback (can also use FileCallback)  
* `$size`: `(null|int)` Size of file to download, required for bot API file IDs.  
* `$mime`: `(null|string)` MIME type of file to download, required for bot API file IDs.  
* `$name`: `(null|string)` Name of file to download, required for bot API file IDs.  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* `\Amp\Http\Server\Request`
* `\Amp\Cancellation`
* `\Amp\Http\Server\Response`




### <a name="downloadToReturnedStream"></a> `downloadToReturnedStream(mixed $messageMedia, callable $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): \Amp\ByteStream\ReadableStream`

Download file to an amphp stream, returning it.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$cb`: `callable` Callback  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`
* `\Amp\ByteStream\ReadableStream`




### <a name="downloadToStream"></a> `downloadToStream(mixed $messageMedia, (mixed|\danog\MadelineProto\FileCallbackInterface|resource|\Amp\ByteStream\WritableStream) $stream, callable $cb = NULL, int $offset = 0, int $end = -1, ?\Amp\Cancellation $cancellation = NULL): void`

Download file to stream.


Parameters:

* `$messageMedia`: `mixed` File to download  
* `$stream`: `(mixed|\danog\MadelineProto\FileCallbackInterface|resource|\Amp\ByteStream\WritableStream)` Stream where to download file  
* `$cb`: `callable` Callback  
* `$offset`: `int` Offset where to start downloading  
* `$end`: `int` Offset where to end download  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `resource`
* `\Amp\ByteStream\WritableStream`
* `\Amp\Cancellation`




### <a name="echo"></a> `echo(string $string): void`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### <a name="end"></a> `end(array<T> $what): T`

Get final element of array.


Parameters:

* `$what`: `array<T>` Array  



### <a name="entitiesToHtml"></a> `entitiesToHtml(string $message, list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})> $entities, bool $allowTelegramTags = false): string`

Convert a message and a set of entities to HTML.


Parameters:

* `$message`: `string`   
* `$entities`: `list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})>`   
* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity`: Master class for message entities.](../../danog/MadelineProto/EventHandler/Message/Entities/MessageEntity.html)




### <a name="exportAuthorization"></a> `exportAuthorization(): array{0: int, 1: string}`

Export authorization.



### <a name="exportGroupCallInvite"></a> `exportGroupCallInvite(int $id, bool $canSelfUnmute = false): string`

Export an invite link for a group call.


Parameters:

* `$id`: `int`   
* `$canSelfUnmute`: `bool` Whether users joining with this link may speak without asking; admins only.  



### <a name="extractBotAPIFile"></a> `extractBotAPIFile(array $info): ?array`

Extract file info from bot API message.


Parameters:

* `$info`: `array` Bot API message object  



### <a name="extractMessage"></a> `extractMessage(array $updates): array`

Extract a message constructor from an Updates constructor.


Parameters:

* `$updates`: `array`   



### <a name="extractMessageId"></a> `extractMessageId(array $updates): int`

Extract a message ID from an Updates constructor.


Parameters:

* `$updates`: `array`   



### <a name="extractMessageUpdate"></a> `extractMessageUpdate(array $updates): array`

Extract an update message constructor from an Updates constructor.


Parameters:

* `$updates`: `array`   



### <a name="extractUpdates"></a> `extractUpdates(array $updates): array<array>`

Extract Update constructors from an Updates constructor.


Parameters:

* `$updates`: `array`   



### <a name="fileGetContents"></a> `fileGetContents(string $url, ?\Amp\Cancellation $cancellation = NULL): string`

Get contents of remote file asynchronously.


Parameters:

* `$url`: `string` URL  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="flock"></a> `flock(string $file, integer $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): ($token is null ? Closure(): void : (Closure(): void | null))`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.  


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `integer` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Cancellation` Cancellation token  
* `$failureCb`: `?\Closure` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Cancellation`
* `\Closure`




### <a name="fullChatLastUpdated"></a> `fullChatLastUpdated(mixed $id): int`

When was full info for this chat last cached.


Parameters:

* `$id`: `mixed` Chat ID  



### <a name="fullGetSelf"></a> `fullGetSelf(): array|false`

Get info about the logged-in user, not cached.



### <a name="genVectorHash"></a> `genVectorHash(array<(string|int)> $longs): string`

Generate MTProto vector hash.
  
Returns a vector hash.  


Parameters:

* `$longs`: `array<(string|int)>` IDs  



### <a name="getAdminIds"></a> `getAdminIds(): array`

Get admin IDs (equal to all user report peers).



### <a name="getAllCalls"></a> `getAllCalls(): array<int, \danog\MadelineProto\EventHandler\Calls\PrivateCall>`

Get all pending and running calls, indexed by user ID.


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\PrivateCall`: This update represents a private (one-to-one) VoIP Telegram call.](../../danog/MadelineProto/EventHandler/Calls/PrivateCall.html)




### <a name="getAllGroupCalls"></a> `getAllGroupCalls(): array<int, \danog\MadelineProto\EventHandler\Calls\AbstractGroupCall>`

Get all group calls (video chats, livestreams and live stories) we're currently tracking, indexed by their ID.


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\AbstractGroupCall`: What a [video chat/livestream »](https://core.telegram.org/api/group-calls#video-chats-livestreams)](../../danog/MadelineProto/EventHandler/Calls/AbstractGroupCall.html)




### <a name="getAllMethods"></a> `getAllMethods(): array`

Get full list of MTProto and API methods.



### <a name="getAuthorization"></a> `getAuthorization(): (\danog\MadelineProto\API::NOT_LOGGED_IN|\danog\MadelineProto\API::WAITING_CODE|\danog\MadelineProto\API::WAITING_SIGNUP|\danog\MadelineProto\API::WAITING_PASSWORD|\danog\MadelineProto\API::LOGGED_IN|API::LOGGED_OUT)`

Get authorization info.


#### See also: 
* `\danog\MadelineProto\API::NOT_LOGGED_IN`
* `\danog\MadelineProto\API::WAITING_CODE`
* `\danog\MadelineProto\API::WAITING_SIGNUP`
* `\danog\MadelineProto\API::WAITING_PASSWORD`
* `\danog\MadelineProto\API::LOGGED_IN`
* `API::LOGGED_OUT`




### <a name="getBroadcastProgress"></a> `getBroadcastProgress(integer $id): ?\danog\MadelineProto\Broadcast\Progress`

Get the progress of a currently running broadcast.
  
Will return null if the broadcast doesn't exist, has already completed or was cancelled.  
  
Use updateBroadcastProgress updates to get real-time progress status without polling.  


Parameters:

* `$id`: `integer` Broadcast ID  


#### See also: 
* [`\danog\MadelineProto\Broadcast\Progress`: Broadcast progress.](../../danog/MadelineProto/Broadcast/Progress.html)




### <a name="getCachedConfig"></a> `getCachedConfig(): array`

Get cached server-side config.



### <a name="getCall"></a> `getCall(int $id): ?\danog\MadelineProto\EventHandler\Calls\PrivateCall`

Get phone call information.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\PrivateCall`: This update represents a private (one-to-one) VoIP Telegram call.](../../danog/MadelineProto/EventHandler/Calls/PrivateCall.html)




### <a name="getCallByPeer"></a> `getCallByPeer(int $userId): ?\danog\MadelineProto\EventHandler\Calls\PrivateCall`

Get the phone call with the specified user ID.


Parameters:

* `$userId`: `int`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\PrivateCall`: This update represents a private (one-to-one) VoIP Telegram call.](../../danog/MadelineProto/EventHandler/Calls/PrivateCall.html)




### <a name="getCallRemoteMediaState"></a> `getCallRemoteMediaState(int $id): ?\danog\MadelineProto\VoIP\MediaState`

Get the media state of the other party of a call, as reported by their client.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\VoIP\MediaState`: The media state of the other party of a one-to-one call, as reported by its `MediaState`](../../danog/MadelineProto/VoIP/MediaState.html)




### <a name="getCallState"></a> `getCallState(int $id): ?\danog\MadelineProto\VoIP\CallState`

Get call state.


Parameters:

* `$id`: `int`   


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../danog/MadelineProto/VoIP/CallState.html)




### <a name="getCdnConfig"></a> `getCdnConfig(): void`

Store RSA keys for CDN datacenters.



### <a name="getConferenceCall"></a> `getConferenceCall(int $id): ?\danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Get a live end-to-end encrypted conference call this session is in, by its call id.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="getConferenceCallBySlug"></a> `getConferenceCallBySlug(string $slug): ?\danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Get an [end-to-end encrypted conference call »](https://core.telegram.org/api/group-calls#conference-calls)
from its [conference link »](https://core.telegram.org/api/links#conference-links) slug, or null if  
the link is not valid any more.  


Parameters:

* `$slug`: `string`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="getConfig"></a> `getConfig(array $config = []): array`

Get cached (or eventually re-fetch) server-side config.


Parameters:

* `$config`: `array` Current config  



### <a name="getDNSClient"></a> `getDNSClient(): \Amp\Dns\DnsResolver`

Get async DNS client.


#### See also: 
* `\Amp\Dns\DnsResolver`




### <a name="getDhConfig"></a> `getDhConfig(?\Amp\Cancellation $cancellation = NULL): array`

Get diffie-hellman configuration.


Parameters:

* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="getDialogIds"></a> `getDialogIds(): list<int>`

Get dialog IDs.



### <a name="getDownloadInfo"></a> `getDownloadInfo(mixed $messageMedia): array{ext: string, name: string, mime: string, size: int, InputFileLocation: array, key_fingerprint?: string, key?: string, iv?: string, thumb_size?: string}`

Get download info of file
Returns an array with the following structure:.  
  
`$info['ext']` - The file extension  
`$info['name']` - The file name, without the extension  
`$info['mime']` - The file mime type  
`$info['size']` - The file size  


Parameters:

* `$messageMedia`: `mixed` File ID  



### <a name="getDownloadLink"></a> `getDownloadLink(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|array|string $media, ?string $scriptUrl = NULL, ?int $size = NULL, ?string $name = NULL, ?string $mime = NULL): string`

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




### <a name="getEventHandler"></a> `getEventHandler((class-string<T>|null) $class = NULL): (T|\danog\MadelineProto\Ipc\EventHandlerProxy|\__PHP_Incomplete_Class|null)`

Get event handler (or plugin instance).


Parameters:

* `$class`: `(class-string<T>|null)`   


#### See also: 
* `\danog\MadelineProto\Ipc\EventHandlerProxy`
* `\__PHP_Incomplete_Class`




### <a name="getExtensionFromLocation"></a> `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### <a name="getExtensionFromMime"></a> `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### <a name="getFileInfo"></a> `getFileInfo(mixed $constructor): array`

Get info about file.


Parameters:

* `$constructor`: `mixed` File ID  



### <a name="getFullDialogs"></a> `getFullDialogs(): array<int, array>`

Get full info of all dialogs.
  
Bots should use getDialogIds, instead.  



### <a name="getFullInfo"></a> `getFullInfo(mixed $id): array`

Get full info about peer, returns an FullInfo object.


Parameters:

* `$id`: `mixed` Peer  


#### See also: 
* [https://docs.madelineproto.xyz/FullInfo.html](https://docs.madelineproto.xyz/FullInfo.html)




### <a name="getGroupCall"></a> `getGroupCall(mixed $peer): ?\danog\MadelineProto\EventHandler\Calls\GroupCall`

Get the group call (video chat or livestream) currently active in a group or channel.


Parameters:

* `$peer`: `mixed`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\GroupCall`: This update represents a Telegram [video chat or livestream »](https://core.telegram.org/api/group-calls#video-chats-livestreams):](../../danog/MadelineProto/EventHandler/Calls/GroupCall.html)




### <a name="getGroupCallBySlug"></a> `getGroupCallBySlug(string $slug): ?\danog\MadelineProto\EventHandler\Calls\GroupCall`

Get a group call from its
[conference deep link »](https://core.telegram.org/api/links#conference-links) slug.  


Parameters:

* `$slug`: `string`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\GroupCall`: This update represents a Telegram [video chat or livestream »](https://core.telegram.org/api/group-calls#video-chats-livestreams):](../../danog/MadelineProto/EventHandler/Calls/GroupCall.html)




### <a name="getGroupCallJoinAs"></a> `getGroupCallJoinAs(mixed $peer): list<int>`

The peers we may join the video chats and livestreams of a group or channel as: ourselves, the
channels we own, and (for anonymous admins) the group itself. Bot API IDs.  
  
See [joining a group call on behalf of owned channels »](https://core.telegram.org/api/group-calls#joining-a-group-call-on-behalf-of-owned-channels).  


Parameters:

* `$peer`: `mixed`   



### <a name="getGroupCallParticipants"></a> `getGroupCallParticipants(int $id): array<int, \danog\MadelineProto\EventHandler\Participant>`

Get the participants of a group call, indexed by their bot API peer ID.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Participant`: Info about a channel participant.](../../danog/MadelineProto/EventHandler/Participant.html)




### <a name="getGroupCallState"></a> `getGroupCallState(int $id): \danog\MadelineProto\GroupCall\GroupCallState`

Get the state of a group call.


Parameters:

* `$id`: `int`   


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallState`: State of a group call we are interacting with.](../../danog/MadelineProto/GroupCall/GroupCallState.html)




### <a name="getGroupCallStreamRtmpUrl"></a> `getGroupCallStreamRtmpUrl(mixed $peer, bool $revoke = false, bool $liveStory = false): array{url: string, key: string}`

Get the RTMP URL and stream key to publish an [RTMP livestream »](https://core.telegram.org/api/group-calls#creating-and-publishing-an-rtmp-livestream)
to, in a group or channel (create the call with `rtmpStream` afterwards, see {@see self::createGroupCall()}),  
or as a live story (see {@see self::startLive()}).  


Parameters:

* `$peer`: `mixed` The group or channel (or, for a live story, the user, group or channel it is posted as).  
* `$revoke`: `bool` Whether to generate a new stream key, invalidating the previous one.  
* `$liveStory`: `bool` Whether the key is for a live story rather than a video chat/livestream.  



### <a name="getHTTPClient"></a> `getHTTPClient(): \Amp\Http\Client\HttpClient`

Get async HTTP client.


#### See also: 
* `\Amp\Http\Client\HttpClient`




### <a name="getHint"></a> `getHint(): string`

Get current password hint.



### <a name="getId"></a> `getId(mixed $id): int`

Get the bot API ID of a peer.


Parameters:

* `$id`: `mixed` Peer  



### <a name="getInfo"></a> `getInfo(mixed $id, \danog\MadelineProto\API::INFO_TYPE_* $type = \danog\MadelineProto\API::INFO_TYPE_ALL): (\$type is \danog\MadelineProto\API::INFO_TYPE_ALL ? array{User?: array, Chat?: array, bot_api_id: int, user_id?: int, chat_id?: int, channel_id?: int, type: string} : ($type is API::INFO_TYPE_TYPE ? string : ($type is \danog\MadelineProto\API::INFO_TYPE_ID ? int : (array{_: string, user_id?: int, access_hash?: int, min?: bool, chat_id?: int, channel_id?: int} | array{_: string, user_id?: int, access_hash?: int, min?: bool} | array{_: string, channel_id: int, access_hash: int, min: bool}))))`

Get info about peer, returns an Info object.
  
If passed a secret chat ID, returns information about the user, not about the secret chat.  
Use getSecretChat to return information about the secret chat.  


Parameters:

* `$id`: `mixed` Peer  
* `$type`: `\danog\MadelineProto\API::INFO_TYPE_*` Whether to generate an Input*, an InputPeer or the full set of constructors  


#### See also: 
* [https://docs.madelineproto.xyz/Info.html](https://docs.madelineproto.xyz/Info.html)
* `\danog\MadelineProto\API::INFO_TYPE_*`




### <a name="getLogger"></a> `getLogger(): \danog\MadelineProto\Logger`

Get logger.


#### See also: 
* [`\danog\MadelineProto\Logger`: Logger class.](../../danog/MadelineProto/Logger.html)




### <a name="getMaps"></a> `getMaps(): ?int`

Get current number of memory-mapped regions, UNIX only.



### <a name="getMaxMaps"></a> `getMaxMaps(): ?int`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.  



### <a name="getMemoryProfile"></a> `getMemoryProfile(): string`

Get memory profile with memprof.



### <a name="getMethodNamespaces"></a> `getMethodNamespaces(): array`

Get TL namespaces.



### <a name="getMethodsNamespaced"></a> `getMethodsNamespaced(): array`

Get namespaced methods (method => namespace).



### <a name="getMimeFromBuffer"></a> `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



### <a name="getMimeFromExtension"></a> `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### <a name="getMimeFromFile"></a> `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### <a name="getPlugin"></a> `getPlugin(class-string<T> $class): \danog\MadelineProto\PluginEventHandler|\danog\MadelineProto\Ipc\EventHandlerProxy|null`

Obtain a certain event handler plugin instance.


Parameters:

* `$class`: `class-string<T>` 

return T|null  


#### See also: 
* [`\danog\MadelineProto\PluginEventHandler`: Plugin event handler class.](../../danog/MadelineProto/PluginEventHandler.html)
* `\danog\MadelineProto\Ipc\EventHandlerProxy`




### <a name="getPromCounter"></a> `getPromCounter(string $namespace, string $name, string $help, array<string, string> $labels = []): ?\danog\BetterPrometheus\BetterCounter`

Creates and returns a prometheus counter.
  
Returns null if prometheus stats are disabled.  


Parameters:

* `$namespace`: `string`   
* `$name`: `string`   
* `$help`: `string`   
* `$labels`: `array<string, string>`   


#### See also: 
* `\danog\BetterPrometheus\BetterCounter`




### <a name="getPromGauge"></a> `getPromGauge(string $namespace, string $name, string $help, array<string, string> $labels = []): ?\danog\BetterPrometheus\BetterGauge`

Creates and returns a prometheus gauge.
  
Returns null if prometheus stats are disabled.  


Parameters:

* `$namespace`: `string`   
* `$name`: `string`   
* `$help`: `string`   
* `$labels`: `array<string, string>`   


#### See also: 
* `\danog\BetterPrometheus\BetterGauge`




### <a name="getPromHistogram"></a> `getPromHistogram(string $namespace, string $name, string $help, array<string, string> $labels = [], ?non-empty-list<float> $buckets = NULL): ?\danog\BetterPrometheus\BetterHistogram`

Creates and returns a prometheus histogram.
  
Returns null if prometheus stats are disabled.  


Parameters:

* `$namespace`: `string`   
* `$name`: `string`   
* `$help`: `string`   
* `$labels`: `array<string, string>`   
* `$buckets`: `?non-empty-list<float>`   


#### See also: 
* `non-empty-list`
* `\danog\BetterPrometheus\BetterHistogram`




### <a name="getPromSummary"></a> `getPromSummary(string $namespace, string $name, string $help, array<string, string> $labels = [], int $maxAgeSeconds = 600, ?non-empty-list<float> $quantiles = NULL): ?\danog\BetterPrometheus\BetterSummary`

Creates and returns a prometheus summary.
  
Returns null if prometheus stats are disabled.  


Parameters:

* `$namespace`: `string`   
* `$name`: `string`   
* `$help`: `string`   
* `$labels`: `array<string, string>`   
* `$maxAgeSeconds`: `int`   
* `$quantiles`: `?non-empty-list<float>`   


#### See also: 
* `non-empty-list`
* `\danog\BetterPrometheus\BetterSummary`




### <a name="getPropicInfo"></a> `getPropicInfo(mixed $data): ?\danog\MadelineProto\EventHandler\Media\Photo`

Gets info of the propic of a user.


Parameters:

* `$data`: `mixed`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Media\Photo`: Represents a photo.](../../danog/MadelineProto/EventHandler/Media/Photo.html)




### <a name="getPsrLogger"></a> `getPsrLogger(): \Psr\Log\LoggerInterface`

Get PSR logger.


#### See also: 
* `\Psr\Log\LoggerInterface`




### <a name="getPwrChat"></a> `getPwrChat(mixed $id, bool $fullfetch = true): array`

Get full info about peer (including full list of channel members), returns a Chat object.


Parameters:

* `$id`: `mixed` Peer  
* `$fullfetch`: `bool`   


#### See also: 
* [https://docs.madelineproto.xyz/Chat.html](https://docs.madelineproto.xyz/Chat.html)




### <a name="getSecretChat"></a> `getSecretChat((array|int) $chat): \danog\MadelineProto\SecretChats\SecretChat`

Get secret chat.


Parameters:

* `$chat`: `(array|int)` Secret chat ID  


#### See also: 
* [`\danog\MadelineProto\SecretChats\SecretChat`: Represents a secret chat.](../../danog/MadelineProto/SecretChats/SecretChat.html)




### <a name="getSecretMessage"></a> `getSecretMessage(integer $chatId, integer $randomId): \danog\MadelineProto\EventHandler\Message\SecretMessage`

Gets a secret chat message.


Parameters:

* `$chatId`: `integer` Secret chat ID.  
* `$randomId`: `integer` Secret chat message ID.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\SecretMessage`: Represents New encrypted message.](../../danog/MadelineProto/EventHandler/Message/SecretMessage.html)




### <a name="getSelf"></a> `getSelf(): array|false`

Get info about the logged-in user, cached.
  
Use fullGetSelf to bypass the cache.  



### <a name="getSessionName"></a> `getSessionName(): string`

Returns the session name.



### <a name="getSettings"></a> `getSettings(): \danog\MadelineProto\Settings`

Return current settings.


#### See also: 
* [`\danog\MadelineProto\Settings`: Settings class used for configuring MadelineProto.](../../danog/MadelineProto/Settings.html)




### <a name="getSponsoredMessages"></a> `getSponsoredMessages((int|string|array) $peer): ?array`

Get sponsored messages for channel.
This method will return an array of [sponsored message objects](https://docs.madelineproto.xyz/API_docs/constructors/sponsoredMessage.html).  
  
See [the API documentation](https://core.telegram.org/api/sponsored-messages) for more info on how to handle sponsored messages.  


Parameters:

* `$peer`: `(int|string|array)` Channel ID, or Update, or Message, or Peer.  



### <a name="getStream"></a> `getStream(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL, ?int $size = NULL): \Amp\ByteStream\ReadableStream`

Provide a stream for a file, URL or amp stream.


Parameters:

* `$stream`: `\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   
* `$size`: `?int`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### <a name="getStreamPipe"></a> `getStreamPipe(): \Amp\ByteStream\Pipe`

Obtains a pipe that can be used to upload a file from a stream.


#### See also: 
* `\Amp\ByteStream\Pipe`




### <a name="getType"></a> `getType(mixed $id): \danog\MadelineProto\API::PEER_TYPE_*`

Get type of peer.


Parameters:

* `$id`: `mixed` Peer  


#### See also: 
* `\danog\MadelineProto\API::PEER_TYPE_*`




### <a name="getUpdates"></a> `getUpdates(array{offset?: int, limit?: int, timeout?: float} $params = []): list<array{update_id: mixed, update: mixed}>`

Only useful when consuming MadelineProto updates through an API in another language (like Javascript), **absolutely not recommended when directly writing MadelineProto bots**.
  
`getUpdates` will **greatly slow down your bot** if used directly inside of PHP code.  
  
**Only use the [event handler](#async-event-driven) when writing a MadelineProto bot**, because update handling in the **event handler** is completely parallelized and non-blocking.  


Parameters:

* `$params`: `array{offset?: int, limit?: int, timeout?: float}` Params  



### <a name="getWebMessage"></a> `getWebMessage(string $message): string`

Get a message to show to the user when starting the bot.


Parameters:

* `$message`: `string`   



### <a name="getWebWarnings"></a> `getWebWarnings(): string`

Get various warnings to show to the user in the web UI.



### <a name="groupCallGetCurrent"></a> `groupCallGetCurrent(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played in a group call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### <a name="groupCallPausePlay"></a> `groupCallPausePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Pause playback of the current audio file in a group call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="groupCallPlay"></a> `groupCallPlay(int $id, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Play a file in a group call.


Parameters:

* `$id`: `int`   
* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="groupCallPlayOnHold"></a> `groupCallPlayOnHold(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): void`

Files to play on hold in a group call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="groupCallResumePlay"></a> `groupCallResumePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Resume playback of the current audio file in a group call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="groupCallSetOutput"></a> `groupCallSetOutput(int $id, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`

Record one participant of a group call (or, in stream mode, its mixed stream) into a single file
(or stream) with a fixed set of tracks, see {@see \danog\MadelineProto\EventHandler\Calls\AbstractGroupCall::setOutput()}.  


Parameters:

* `$id`: `int`   
* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `?int` The streams to record, as a bitmask of {@see CallStream} flags, or null for every available one.  


Return value: The streams the participant currently sends, as a bitmask of {@see CallStream} flags.

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../danog/MadelineProto/RecordingFormat.html)




### <a name="groupCallSetOutputFolder"></a> `groupCallSetOutputFolder(int $id, \danog\MadelineProto\LocalDirectory $dir, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): void`

Record group call media into a directory: every transmitting participant (or only the given
one) as its own numbered series of files, see  
{@see \danog\MadelineProto\EventHandler\Calls\AbstractGroupCall::setOutputFolder()}.  


Parameters:

* `$id`: `int`   
* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../danog/MadelineProto/RecordingFormat.html)




### <a name="groupCallSkipPlay"></a> `groupCallSkipPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Skip to the next file in the playlist of a group call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="groupCallStopPlay"></a> `groupCallStopPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Stop playing all files in a group call, clearing the main and the hold playlist.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="hasAdmins"></a> `hasAdmins(): bool`

Check if has admins.



### <a name="hasEventHandler"></a> `hasEventHandler(): bool`

Check if an event handler instance is present.



### <a name="hasPlugin"></a> `hasPlugin(class-string<\danog\MadelineProto\EventHandler> $class): bool`

Check if a certain event handler plugin is installed.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>`   


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)




### <a name="hasReportPeers"></a> `hasReportPeers(): bool`

Check if has report peers.



### <a name="hasSecretChat"></a> `hasSecretChat((array|int) $chat): bool`

Check whether secret chat exists.


Parameters:

* `$chat`: `(array|int)` Secret chat ID  



### <a name="htmlEscape"></a> `htmlEscape(string $what): string`

Escape string for MadelineProto's HTML entity converter.


Parameters:

* `$what`: `string` String to escape  



### <a name="htmlToMessageEntities"></a> `htmlToMessageEntities(string $html): \danog\MadelineProto\TextEntities`

Manually convert HTML to a message and a set of entities.
  
NOTE: You don't have to use this method to send HTML messages.  
  
This method is already called automatically by using parse_mode: "HTML" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$html`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TextEntities`: Class that converts HTML or markdown to a message + set of entities.](../../danog/MadelineProto/TextEntities.html)




### <a name="importAuthorization"></a> `importAuthorization(array<int, string> $authorization, int $mainDcID): array`

Import authorization.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$mainDcID`: `int` Main DC ID  



### <a name="inflateStripped"></a> `inflateStripped(string $stripped): string`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  



### <a name="initSelfRestart"></a> `initSelfRestart(): void`

Initialize self-restart hack.



### <a name="inviteToGroupCall"></a> `inviteToGroupCall(int $id, mixed ...$users): void`

Invite users to a group call.


Parameters:

* `$id`: `int`   
* `...$users`: `mixed`   



### <a name="isAltervista"></a> `isAltervista(): bool`

Whether this is altervista.



### <a name="isArrayOrAlike"></a> `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### <a name="isBot"></a> `isBot(mixed $peer): bool`

Check if the specified peer is a bot.


Parameters:

* `$peer`: `mixed`   



### <a name="isCallMuted"></a> `isCallMuted(int $id): bool`

Whether our own audio stream is muted in a call.


Parameters:

* `$id`: `int`   



### <a name="isForum"></a> `isForum(mixed $peer): bool`

Check if the specified peer is a forum.


Parameters:

* `$peer`: `mixed`   



### <a name="isGroupCallMuted"></a> `isGroupCallMuted(int $id): bool`

Whether our own audio stream is muted in a group call.


Parameters:

* `$id`: `int`   



### <a name="isGroupCallPlayPaused"></a> `isGroupCallPlayPaused(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether the currently playing audio file of a group call is paused.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="isIpc"></a> `isIpc(): bool`

Whether we're an IPC client instance.



### <a name="isIpcWorker"></a> `isIpcWorker(): bool`

Whether we're an IPC server process (as opposed to an event handler).



### <a name="isPlayPaused"></a> `isPlayPaused(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether the currently playing audio file is paused.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="isPremium"></a> `isPremium(): bool`

Returns whether the current user is a premium user, cached.



### <a name="isSelfBot"></a> `isSelfBot(): bool`

Returns whether the current user is a bot.



### <a name="isSelfUser"></a> `isSelfUser(): bool`

Returns whether the current user is a user.



### <a name="isTestMode"></a> `isTestMode(): boolean`

Whether we're currently connected to the test DCs.



### <a name="joinConferenceCall"></a> `joinConferenceCall(array $call, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Join an existing end-to-end encrypted conference call.
  
See [end-to-end encrypted group calls »](https://core.telegram.org/api/end-to-end/group-calls).  
Requires the `sodium` and `openssl` PHP extensions.  


Parameters:

* `$call`: `array` The `groupCall` (or `inputGroupCall`) of the conference to join.  
* `$muted`: `bool` Whether to join muted.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="joinConferenceCallByInviteMessage"></a> `joinConferenceCallByInviteMessage(int $msgId, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Join an end-to-end encrypted conference call from the service message that invited us to it
(a `messageActionConferenceCall`, see {@see \danog\MadelineProto\EventHandler\Message\Service\DialogConferenceCall}).  


Parameters:

* `$msgId`: `int` ID of the invitation message.  
* `$muted`: `bool` Whether to join muted.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="joinConferenceCallBySlug"></a> `joinConferenceCallBySlug(string $slug, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Join an end-to-end encrypted conference call from its conference link slug.


Parameters:

* `$slug`: `string`   
* `$muted`: `bool` Whether to join muted.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="joinGroupCall"></a> `joinGroupCall(mixed $peer, bool $muted = false, mixed $joinAs = NULL, (string|null) $inviteHash = NULL): \danog\MadelineProto\EventHandler\Calls\GroupCall`

Join the group call currently active in a group or channel.


Parameters:

* `$peer`: `mixed` The group or channel whose call should be joined.  
* `$muted`: `bool` Whether to join muted.  
* `$joinAs`: `mixed` Peer to join as, defaults to ourselves.  
* `$inviteHash`: `(string|null)` Invite hash from a video chat invite link, if any.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\GroupCall`: This update represents a Telegram [video chat or livestream »](https://core.telegram.org/api/group-calls#video-chats-livestreams):](../../danog/MadelineProto/EventHandler/Calls/GroupCall.html)




### <a name="leaveGroupCall"></a> `leaveGroupCall(int $id): void`

Leave a group call, without ending it for the other participants.


Parameters:

* `$id`: `int`   



### <a name="logger"></a> `logger(mixed $param, int $level = \danog\MadelineProto\Logger::NOTICE, string $file = ''): void`

Logger.


Parameters:

* `$param`: `mixed` Parameter  
* `$level`: `int` Logging level  
* `$file`: `string` File where the message originated  



### <a name="logout"></a> `logout(): void`

Logout the session.



### <a name="markdownCodeEscape"></a> `markdownCodeEscape(string $what): string`

Escape string for markdown code section.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownCodeblockEscape"></a> `markdownCodeblockEscape(string $what): string`

Escape string for markdown codeblock.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownEscape"></a> `markdownEscape(string $what): string`

Escape string for markdown.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownToMessageEntities"></a> `markdownToMessageEntities(string $markdown): \danog\MadelineProto\TextEntities`

Manually convert markdown to a message and a set of entities.
  
NOTE: You don't have to use this method to send Markdown messages.  
  
This method is already called automatically by using parse_mode: "Markdown" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$markdown`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TextEntities`: Class that converts HTML or markdown to a message + set of entities.](../../danog/MadelineProto/TextEntities.html)




### <a name="markdownUrlEscape"></a> `markdownUrlEscape(string $what): string`

Escape string for URL.


Parameters:

* `$what`: `string` String to escape  



### <a name="mbStrSplit"></a> `mbStrSplit(string $text, integer $length): array<string>`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `integer` Length  



### <a name="mbStrlen"></a> `mbStrlen(string $text): int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### <a name="mbSubstr"></a> `mbSubstr(string $text, integer $offset, (null|int) $length = NULL): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `integer` Offset  
* `$length`: `(null|int)` Length  



### <a name="migrateCallToConference"></a> `migrateCallToConference(int $id, bool $muted = false): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

Upgrade a one-to-one call to an [end-to-end encrypted conference call »](https://core.telegram.org/api/group-calls#conference-calls):
create a conference, invite the other party to it, and discard the one-to-one call pointing them  
to the conference (`phoneCallDiscardReasonMigrateConferenceCall`).  


Parameters:

* `$id`: `int` ID of the one-to-one call.  
* `$muted`: `bool` Whether to join the conference muted.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="openBuffered"></a> `openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL, int $offset = 0): Closure(int): ?string`

Provide a buffered reader for a file, URL or amp stream, optionally starting at a byte offset.
  
The `$offset` makes a demuxer resumable across a serialize/unserialize cycle: a `LocalFile` is  
seeked and a `RemoteUrl` is fetched with a `Range` request. A raw {@see ReadableStream} cannot  
be seeked, so a non-zero offset on one is rejected.  


Parameters:

* `$stream`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   
* `$offset`: `int`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### <a name="openFileAppendOnly"></a> `openFileAppendOnly(string $path): \Amp\File\File`

Opens a file in append-only mode.


Parameters:

* `$path`: `string` File path.  


#### See also: 
* `\Amp\File\File`




### <a name="packDouble"></a> `packDouble(float $value): string`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### <a name="packSignedInt"></a> `packSignedInt(integer $value): string`

Convert integer to base256 signed int.


Parameters:

* `$value`: `integer` Value to convert  



### <a name="packSignedLong"></a> `packSignedLong(int $value): string`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### <a name="packUnsignedInt"></a> `packUnsignedInt(int $value): string`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### <a name="pausePlay"></a> `pausePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Pauses playback of the current audio file in the call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="peerIsset"></a> `peerIsset(mixed $id): bool`

Check if peer is present in internal peer database.


Parameters:

* `$id`: `mixed` Peer  



### <a name="phoneLogin"></a> `phoneLogin(string $number, integer $sms_type = 5): array`

Login as user.


Parameters:

* `$number`: `string` Phone number  
* `$sms_type`: `integer` SMS type  



### <a name="posmod"></a> `posmod(int $a, int $b): int`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.  


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  



### <a name="processDownloadServerPing"></a> `processDownloadServerPing(string $path, string $payload): void`

Internal endpoint used by the download server.


Parameters:

* `$path`: `string`   
* `$payload`: `string`   



### <a name="qrLogin"></a> `qrLogin(): ?\danog\MadelineProto\TL\Types\LoginQrCode`

Initiates QR code login.
  
Returns a QR code login helper object, that can be used to render the QR code, display the link directly, wait for login, QR code expiration and much more.  
  
Returns null if we're already logged in, or if we're waiting for a password (use getAuthorization to distinguish between the two cases).  


#### See also: 
* [`\danog\MadelineProto\TL\Types\LoginQrCode`: Represents a login QR code.](../../danog/MadelineProto/TL/Types/LoginQrCode.html)




### <a name="random"></a> `random(integer $length): string`

Get secure random string of specified length.


Parameters:

* `$length`: `integer` Length  



### <a name="randomInt"></a> `randomInt(integer $modulus = 0): int`

Get random integer.


Parameters:

* `$modulus`: `integer` Modulus  



### <a name="readLine"></a> `readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  
* `$cancel`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="refreshFullPeerCache"></a> `refreshFullPeerCache(mixed $id): void`

Refresh full peer cache for a certain peer.


Parameters:

* `$id`: `mixed` The peer to refresh  



### <a name="refreshPeerCache"></a> `refreshPeerCache(mixed ...$ids): void`

Refresh peer cache for a certain peer.


Parameters:

* `...$ids`: `mixed`   



### <a name="renderPromStats"></a> `renderPromStats(?\Prometheus\RendererInterface $renderer = NULL): string`

Renders prometheus stats using the specified renderer.
  
By default uses the text renderer.  


Parameters:

* `$renderer`: `?\Prometheus\RendererInterface`   


#### See also: 
* `\Prometheus\RendererInterface`




### <a name="report"></a> `report(string $message, string $parseMode = ''): void`

Report an error to the previously set peer.


Parameters:

* `$message`: `string` Error to report  
* `$parseMode`: `string` Parse mode  



### <a name="reportMemoryProfile"></a> `reportMemoryProfile(): void`

Report memory profile with memprof.



### <a name="requestCall"></a> `requestCall(mixed $user, bool $video = false): \danog\MadelineProto\EventHandler\Calls\PrivateCall`

Request VoIP call.


Parameters:

* `$user`: `mixed` User  
* `$video`: `bool` Whether to start a video call.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\PrivateCall`: This update represents a private (one-to-one) VoIP Telegram call.](../../danog/MadelineProto/EventHandler/Calls/PrivateCall.html)




### <a name="requestSecretChat"></a> `requestSecretChat(mixed $user): int`

Request secret chat.


Parameters:

* `$user`: `mixed` User to start secret chat with  



### <a name="resetUpdateState"></a> `resetUpdateState(): void`

Reset the update state and fetch all updates from the beginning.



### <a name="restart"></a> `restart(): void`

Restart update loop.



### <a name="resumePlay"></a> `resumePlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Resumes playback of the current audio file in the call.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="rethrow"></a> `rethrow(Throwable $e): void`

Rethrow exception into event loop.


Parameters:

* `$e`: `Throwable`   


#### See also: 
* `Throwable`




### <a name="rleDecode"></a> `rleDecode(string $string): string`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### <a name="rleEncode"></a> `rleEncode(string $string): string`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### <a name="saveDefaultGroupCallJoinAs"></a> `saveDefaultGroupCallJoinAs(mixed $peer, mixed $joinAs): void`

Save the peer we join the video chats and livestreams of a group or channel as by default.


Parameters:

* `$peer`: `mixed` The group or channel.  
* `$joinAs`: `mixed` The peer to join as (one of {@see self::getGroupCallJoinAs()}).  



### <a name="sendAudio"></a> `sendAudio((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, (integer|null) $duration = NULL, (string|null) $title = NULL, (string|null) $performer = NULL, ?int $ttl = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends an audio.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `?string`   
* `$duration`: `(integer|null)` Duration of the audio  
* `$title`: `(string|null)` Title of the audio  
* `$performer`: `(string|null)` Performer of the audio  
* `$ttl`: `?int`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendCustomEvent"></a> `sendCustomEvent(mixed $payload): void`

Sends an updateCustomEvent update to the event handler.


Parameters:

* `$payload`: `mixed`   



### <a name="sendDocument"></a> `sendDocument((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a document.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `?string`   
* `$ttl`: `?int`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendDocumentPhoto"></a> `sendDocumentPhoto((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a photo.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `?int`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendGif"></a> `sendGif((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $ttl = NULL, boolean $spoiler = false, ?int $duration = NULL, ?int $width = NULL, ?int $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a gif.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `(integer|null)` Time to live  
* `$spoiler`: `boolean` Whether the message is a spoiler  
* `$duration`: `?int`   
* `$width`: `?int`   
* `$height`: `?int`   
* `$thumbSeek`: `string`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendMessage"></a> `sendMessage((integer|string) $peer, string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a message.


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$noWebpage`: `boolean` Set this flag to disable generation of the webpage preview  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$cancellation`: `?\Amp\Cancellation` Cancellation  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)




### <a name="sendMessageToAdmins"></a> `sendMessageToAdmins(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, ?\Amp\Cancellation $cancellation = NULL): list<\danog\MadelineProto\EventHandler\Message>`

Sends a message to all report peers (admins of the bot).


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$noWebpage`: `boolean` Set this flag to disable generation of the webpage preview  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)




### <a name="sendPhoto"></a> `sendPhoto((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a photo.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `?int`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendSticker"></a> `sendSticker((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $mimeType, string $emoji = '', array $stickerSet = [  '_' => 'inputStickerSetEmpty',], ?callable $callback = NULL, ?string $fileName = NULL, ?int $ttl = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a sticker.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$mimeType`: `string`   
* `$emoji`: `string`   
* `$stickerSet`: `array`   
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `?int`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### <a name="sendVideo"></a> `sendVideo((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, string $mimeType = 'video/mp4', (integer|null) $ttl = NULL, boolean $spoiler = false, boolean $roundMessage = false, boolean $supportsStreaming = true, boolean $noSound = false, (integer|null) $duration = NULL, (integer|null) $width = NULL, (integer|null) $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, bool $updateStickersetsOrder = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a video.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `string`   
* `$ttl`: `(integer|null)` Time to live  
* `$spoiler`: `boolean` Whether the message is a spoiler  
* `$roundMessage`: `boolean` Whether the message should be round  
* `$supportsStreaming`: `boolean` Whether the video supports streaming  
* `$noSound`: `boolean` Whether the video has no sound  
* `$duration`: `(integer|null)` Duration of the video  
* `$width`: `(integer|null)` Width of the video  
* `$height`: `(integer|null)` Height of the video  
* `$thumbSeek`: `string`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$updateStickersetsOrder`: `bool`   
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="sendVoice"></a> `sendVoice((integer|string) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $ttl = NULL, (integer|null) $duration = NULL, (array|null) $waveform = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Sends a voice.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string)` Destination peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$ttl`: `(integer|null)` Time to live  
* `$duration`: `(integer|null)` Duration of the voice  
* `$waveform`: `(array|null)` Waveform of the voice  
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="setCallMuted"></a> `setCallMuted(int $id, bool $muted = true): void`

Mute or unmute our own audio stream in a call.


Parameters:

* `$id`: `int`   
* `$muted`: `bool`   



### <a name="setGroupCallMuted"></a> `setGroupCallMuted(int $id, bool $muted = true): void`

Mute or unmute our own audio stream in a group call.


Parameters:

* `$id`: `int`   
* `$muted`: `bool`   



### <a name="setGroupCallTitle"></a> `setGroupCallTitle(int $id, string $title): void`

Change the title of a group call.


Parameters:

* `$id`: `int`   
* `$title`: `string`   



### <a name="setNoop"></a> `setNoop(): void`

Set NOOP update handler, ignoring all updates.



### <a name="setReportPeers"></a> `setReportPeers((int|string|array<(int|string)>) $userOrId): void`

Set peer(s) where to send errors occurred in the event loop.


Parameters:

* `$userOrId`: `(int|string|array<(int|string)>)` Username(s) or peer ID(s)  



### <a name="setWebhook"></a> `setWebhook(string $webhookUrl): void`

Set webhook update handler.


Parameters:

* `$webhookUrl`: `string` Webhook URL  



### <a name="skipPlay"></a> `skipPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

When called, skips to the next file in the playlist.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="sleep"></a> `sleep(float $time): void`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### <a name="start"></a> `start(): array`

Log in to telegram (via CLI or web).



### <a name="startLive"></a> `startLive(mixed $peer, (string|null) $caption = NULL, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, list<array<string, mixed>> $privacyRules = [  0 =>   [    '_' => 'inputPrivacyValueAllowAll',  ],], bool $pinned = false, bool $noForwards = false, bool $rtmpStream = false, (bool|null) $messagesEnabled = NULL, (int|null) $sendPaidMessagesStars = NULL): \danog\MadelineProto\EventHandler\Calls\LiveStory`

Start a [live story »](https://core.telegram.org/api/group-calls#live-stories): a livestream posted
as a story, of which we are the single publisher (everyone else joins as a listener).  


Parameters:

* `$peer`: `mixed` Who to post the live story as: ourselves, or a group or channel we administer.  
* `$caption`: `(string|null)` Caption of the story.  
* `$parseMode`: `(\danog\MadelineProto\ParseMode|null)` Whether to parse HTML or Markdown markup in the caption.  
* `$privacyRules`: `list<array<string, mixed>>` Who may see the story, as [InputPrivacyRule](https://core.telegram.org/type/InputPrivacyRule)s; everyone by default.  
* `$pinned`: `bool` Whether to pin the story to the profile.  
* `$noForwards`: `bool` Whether to forbid forwarding and screenshots.  
* `$rtmpStream`: `bool` Whether the media is published by an external RTMP application (see {@see self::getGroupCallStreamRtmpUrl()}) rather than by us.  
* `$messagesEnabled`: `(bool|null)` Whether viewers may comment with in-call messages.  
* `$sendPaidMessagesStars`: `(int|null)` The minimum Telegram Stars donation required to comment, if any.  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Calls\LiveStory`: This update represents a Telegram [live story »](https://core.telegram.org/api/group-calls#live-stories):](../../danog/MadelineProto/EventHandler/Calls/LiveStory.html)




### <a name="stop"></a> `stop(): void`

Stop update loop.



### <a name="stopPlay"></a> `stopPlay(int $id, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): void`

Stops playing all files in the call, clears the main and the hold playlist.


Parameters:

* `$id`: `int`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="stringToStream"></a> `stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`

Converts a string into an async amphp stream.


Parameters:

* `$str`: `string`   


#### See also: 
* `\Amp\ByteStream\ReadableBuffer`




### <a name="subscribeToUpdates"></a> `subscribeToUpdates(mixed $channel): bool`

Subscribe to event handler updates for a channel/supergroup we're not a member of.


Parameters:

* `$channel`: `mixed` Channel/supergroup to subscribe to  


Return value: False if we were already subscribed


### <a name="tdToMTProto"></a> `tdToMTProto(array $params): array`

Convert TD to MTProto parameters.


Parameters:

* `$params`: `array` Parameters  



### <a name="tdToTdcli"></a> `tdToTdcli(mixed $params): array`

Convert TD parameters to tdcli.


Parameters:

* `$params`: `mixed` Parameters  



### <a name="tdcliToTd"></a> `tdcliToTd(mixed $params, array $key = NULL): array`

Convert tdcli parameters to tdcli.


Parameters:

* `$params`: `mixed` Params  
* `$key`: `array` Key  



### <a name="testFibers"></a> `testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.


Parameters:

* `$fiberCount`: `int`   



### <a name="toCamelCase"></a> `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### <a name="toSnakeCase"></a> `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### <a name="unpackDouble"></a> `unpackDouble(string $value): float`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### <a name="unpackFileId"></a> `unpackFileId(string $fileId): array`

Unpack bot API file ID.


Parameters:

* `$fileId`: `string` Bot API file ID  


Return value: Unpacked file ID


### <a name="unpackSignedInt"></a> `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### <a name="unpackSignedLong"></a> `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### <a name="unpackSignedLongString"></a> `unpackSignedLongString((string|int|array) $value): string`

Unpack base256 signed long to string.


Parameters:

* `$value`: `(string|int|array)` base256 long  



### <a name="unsetEventHandler"></a> `unsetEventHandler(): void`

Unset event handler.



### <a name="update2fa"></a> `update2fa(array{password?: string, new_password?: string, email?: string, hint?: string} $params): void`

Update the 2FA password.
  
The params array can contain password, new_password, email and hint params.  


Parameters:

* `$params`: `array{password?: string, new_password?: string, email?: string, hint?: string}` The params  



### <a name="updateSettings"></a> `updateSettings(\danog\MadelineProto\SettingsAbstract $settings): void`

Parse, update and store settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### <a name="upload"></a> `upload((\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|string|array|resource) $file, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`

Upload file.


Parameters:

* `$file`: `(\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|string|array|resource)` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `boolean` Whether to encrypt file for secret chats  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* `resource`
* `\Amp\Cancellation`




### <a name="uploadAudio"></a> `uploadAudio((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, (integer|null) $duration = NULL, (string|null) $title = NULL, (string|null) $performer = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads an audio without actually sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$peer`: `(integer|string|null)` Optional: associate the audio to the specified peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `?string`   
* `$duration`: `(integer|null)` Duration of the audio  
* `$title`: `(string|null)` Title of the audio  
* `$performer`: `(string|null)` Performer of the audio  
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadDocument"></a> `uploadDocument((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, ?string $mimeType = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a document without sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$peer`: `(integer|string|null)` Optional: associate the media to the specified peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `?string`   
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadDocumentPhoto"></a> `uploadDocumentPhoto((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a photo without sending it to the chat.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$peer`: `(integer|string|null)` Optional: associate the file to the destination peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadEncrypted"></a> `uploadEncrypted((\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|resource) $file, string $fileName = '', callable $cb = NULL, ?\Amp\Cancellation $cancellation = NULL): array`

Upload file to secret chat.


Parameters:

* `$file`: `(\danog\MadelineProto\FileCallbackInterface|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|string|array|resource)` File, URL or Telegram file to upload  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `resource`
* `\Amp\Cancellation`




### <a name="uploadFromCallable"></a> `uploadFromCallable(callable(int, int, ?Cancellation): strin) $callable, integer $size = 0, ?string $mime = NULL, string $fileName = '', callable(float, float, float): voi) $cb = NULL, boolean $seekable = true, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`

Upload file from callable.
  
The callable must accept two parameters: int $offset, int $size  
The callable must return a string with the contest of the file at the specified offset and size.  


Parameters:

* `$callable`: `callable(int, int, ?Cancellation): strin)` Callable (offset, length) => data  
* `$size`: `integer` File size  
* `$mime`: `?string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable(float, float, float): voi)` Status callback  
* `$seekable`: `boolean` Whether chunks can be fetched out of order  
* `$encrypted`: `boolean` Whether to encrypt file for secret chats  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* `\Amp\Cancellation`




### <a name="uploadFromStream"></a> `uploadFromStream(mixed $stream, integer $size = 0, string $mime = NULL, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`

Upload file from stream.


Parameters:

* `$stream`: `mixed` PHP resource or AMPHP async stream  
* `$size`: `integer` File size  
* `$mime`: `string` Mime type  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `boolean` Whether to encrypt file for secret chats  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* `\Amp\Cancellation`




### <a name="uploadFromTgfile"></a> `uploadFromTgfile(mixed $media, callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`

Reupload telegram file.


Parameters:

* `$media`: `mixed` Telegram file  
* `$cb`: `callable` Callback  
* `$encrypted`: `boolean` Whether to encrypt file for secret chats  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* `\Amp\Cancellation`




### <a name="uploadFromUrl"></a> `uploadFromUrl((string|\danog\MadelineProto\FileCallbackInterface) $url, integer $size = 0, string $fileName = '', callable $cb = NULL, boolean $encrypted = false, ?\Amp\Cancellation $cancellation = NULL): array`

Upload file from URL.


Parameters:

* `$url`: `(string|\danog\MadelineProto\FileCallbackInterface)` URL of file  
* `$size`: `integer` Size of file  
* `$fileName`: `string` File name  
* `$cb`: `callable` Callback  
* `$encrypted`: `boolean` Whether to encrypt file for secret chats  
* `$cancellation`: `?\Amp\Cancellation`   


Return value: InputFile constructor

#### See also: 
* [`\danog\MadelineProto\FileCallbackInterface`: File callback interface.](../../danog/MadelineProto/FileCallbackInterface.html)
* `\Amp\Cancellation`




### <a name="uploadGif"></a> `uploadGif((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, boolean $spoiler = false, ?int $duration = NULL, ?int $width = NULL, ?int $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a gif without actually sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$peer`: `(integer|string|null)` Optional: associate the media to the peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$spoiler`: `boolean` Whether the message is a spoiler  
* `$duration`: `?int`   
* `$width`: `?int`   
* `$height`: `?int`   
* `$thumbSeek`: `string`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadPhoto"></a> `uploadPhoto((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, bool $spoiler = false, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, bool $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a photo, without sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$peer`: `(integer|string|null)` Optional: associate the media to the specified peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$spoiler`: `bool`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadSticker"></a> `uploadSticker((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $mimeType, (integer|string|null) $peer = NULL, string $emoji = '', array $stickerSet = [  '_' => 'inputStickerSetEmpty',], ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, boolean $forceResend = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a sticker without sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$mimeType`: `string`   
* `$peer`: `(integer|string|null)` Optional: associate the file to the specified peer or username.  
* `$emoji`: `string`   
* `$stickerSet`: `array`   
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### <a name="uploadVideo"></a> `uploadVideo((\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null) $thumb = NULL, (integer|string|null) $peer = NULL, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, string $mimeType = 'video/mp4', boolean $spoiler = false, boolean $roundMessage = false, boolean $supportsStreaming = true, boolean $noSound = false, (integer|null) $duration = NULL, (integer|null) $width = NULL, (integer|null) $height = NULL, string $thumbSeek = '00:00:01.000', (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, bool $updateStickersetsOrder = false, \Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a video, without actually sending it.
  
Please use named arguments to call this method.  


Parameters:

* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$thumb`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream|null)` Optional: Thumbnail to upload  
* `$peer`: `(integer|string|null)` Optional: associate the media to the specified peer or username.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$mimeType`: `string`   
* `$spoiler`: `boolean` Whether the message is a spoiler  
* `$roundMessage`: `boolean` Whether the message should be round  
* `$supportsStreaming`: `boolean` Whether the video supports streaming  
* `$noSound`: `boolean` Whether the video has no sound  
* `$duration`: `(integer|null)` Duration of the video  
* `$width`: `(integer|null)` Width of the video  
* `$height`: `(integer|null)` Height of the video  
* `$thumbSeek`: `string`   
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$updateStickersetsOrder`: `bool`   
* `$cancellation`: `\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="uploadVoice"></a> `uploadVoice((integer|string|null) $peer, (\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream) $file, string $caption = '', \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, ?callable $callback = NULL, ?string $fileName = NULL, (integer|null) $duration = NULL, (array|null) $waveform = NULL, (integer|null) $replyToMsgId = NULL, (integer|null) $topMsgId = NULL, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $forceResend = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Media`

Uploads a voice without actually sending it to the chat.
  
Please use named arguments to call this method.  


Parameters:

* `$peer`: `(integer|string|null)` Optional: associate the media to the specified peer or username.  
* `$file`: `(\danog\MadelineProto\EventHandler\Message|\danog\MadelineProto\EventHandler\Media|\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\danog\MadelineProto\BotApiFileId|\Amp\ByteStream\ReadableStream)` File to upload: can be a message to reuse media present in a message.  
* `$caption`: `string` Caption of document  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Text parse mode for the caption  
* `$callback`: `?callable`   
* `$fileName`: `?string` Optional file name, if absent will be extracted from the passed $file.  
* `$duration`: `(integer|null)` Duration of the voice  
* `$waveform`: `(array|null)` Waveform of the voice  
* `$replyToMsgId`: `(integer|null)` ID of message to reply to.  
* `$topMsgId`: `(integer|null)` ID of thread where to send the message.  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Whether to disable forwards for this message.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$forceResend`: `boolean` Whether to forcefully resend the file, even if its type and name are the same.  
* `$cancellation`: `?\Amp\Cancellation` Cancellation.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/Message.html)
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\BotApiFileId`: Indicates a bot API file ID to upload using sendDocument, sendPhoto etc...](../../danog/MadelineProto/BotApiFileId.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`




### <a name="validateEventHandlerClass"></a> `validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`

Perform static analysis on a certain event handler class, to make sure it satisfies some performance requirements.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>` Class name  


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)
* [`\danog\MadelineProto\EventHandlerIssue`: Represents an event handler issue.](../../danog/MadelineProto/EventHandlerIssue.html)




### <a name="viewSponsoredMessage"></a> `viewSponsoredMessage((int|array) $peer, (string|array{random_id: string}) $message): bool`

Mark sponsored message as read.


Parameters:

* `$peer`: `(int|array)` Channel ID, or Update, or Message, or Peer.  
* `$message`: `(string|array{random_id: string})` Random ID or sponsored message to mark as read.  



### <a name="wrapMedia"></a> `wrapMedia(array $media, bool $protected = false): ?\danog\MadelineProto\EventHandler\Media`

Wrap a media constructor into an abstract Media object.


Parameters:

* `$media`: `array`   
* `$protected`: `bool`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Media`: Represents a generic media.](../../danog/MadelineProto/EventHandler/Media.html)




### <a name="wrapMessage"></a> `wrapMessage(array $message, bool $scheduled = false): ?\danog\MadelineProto\EventHandler\AbstractMessage`

Wrap a Message constructor into an abstract Message object.


Parameters:

* `$message`: `array`   
* `$scheduled`: `bool`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\AbstractMessage`: Represents an incoming or outgoing message.](../../danog/MadelineProto/EventHandler/AbstractMessage.html)




### <a name="wrapPin"></a> `wrapPin(array $message): ?\danog\MadelineProto\EventHandler\Pinned`

Wrap a Pin constructor into an abstract Pinned object.


Parameters:

* `$message`: `array`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Pinned`: Indicates that some messages were pinned/unpinned.](../../danog/MadelineProto/EventHandler/Pinned.html)




### <a name="wrapUpdate"></a> `wrapUpdate(array $update): ?\danog\MadelineProto\EventHandler\Update`

Wrap an Update constructor into an abstract Update object.


Parameters:

* `$update`: `array`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Update`: Represents a generic update.](../../danog/MadelineProto/EventHandler/Update.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

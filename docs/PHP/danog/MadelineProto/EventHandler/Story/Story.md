---
title: "danog\\MadelineProto\\EventHandler\\Story\\Story: Represents a Telegram story."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Story\Story`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a Telegram story.  



## Properties
* `$pinned`: `bool` Whether this story is pinned
* `$public`: `bool` Whether this story is visible to everyone
* `$closeFriends`: `bool` Whether this story is visible to only close friends of the user (@see Privacy::AllowCloseFriends)
* `$contacts`: `bool` Whether this story is only visible to your countacts
* `$selectedContacts`: `bool` Whether this story is only visible to a select list of contacts
* `$protected`: `bool` Whether this media is protected
* `$edited`: `bool` Whether this story was edited
* `$date`: `int` When was the story sent
* `$expireDate`: `int` Expiration date of the story
* `$caption`: `string` Story caption
* `$entities`: `list<\MessageEntity>` Message [entities](https://core.telegram.org/api/entities) for story caption
* `$media`: `\danog\MadelineProto\EventHandler\Media\Gif|\danog\MadelineProto\EventHandler\Media\Photo|\danog\MadelineProto\EventHandler\Media\Video` Attached media.
* `$privacy`: `list<\RuleDestination>` 
* `$sentReaction`: `string|int|null` Our reaction to the story
* `$reactionCount`: `?int` Reaction counter
* `$views`: `?int` View counter
* `$recentViewers`: `list<int>` List of users who recently viewed the story
* `$senderId`: `int` ID of the sender of the story
* `$id`: `int` Story ID

## Method list:
* [`reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#reply-string-message-danog-madelineproto-parsemode-parsemode-danog-madelineproto-parsemode-text-array-null-replymarkup-null-int-null-scheduledate-null-bool-silent-false-bool-background-false-bool-cleardraft-false-bool-nowebpage-false-bool-updatestickersetsorder-false-danog-madelineproto-eventhandler-message)
* [`delete(): void`](#delete-void)
* [`exportLink(): string`](#exportlink-string)
* [`report(\danog\MadelineProto\EventHandler\Message\ReportReason $reason, string $message = ''): bool`](#report-danog-madelineproto-eventhandler-message-reportreason-reason-string-message-bool)
* [`pin(): void`](#pin-void)
* [`unpin(): void`](#unpin-void)
* [`view(): bool`](#view-bool)
* [`addReaction(int|string $reaction, bool $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`](#addreaction-int-string-reaction-bool-recent-true-danog-madelineproto-eventhandler-story-storyreaction)
* [`delReaction(bool $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`](#delreaction-bool-recent-true-danog-madelineproto-eventhandler-story-storyreaction)
* [`getHTML(bool $allowTelegramTags = false): string`](#gethtml-bool-allowtelegramtags-false-string)

## Methods:
### `reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $scheduleDate = NULL, bool $silent = false, bool $background = false, bool $clearDraft = false, bool $noWebpage = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Reply to the story.


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$noWebpage`: `bool` Set this flag to disable generation of the webpage preview  
* `$updateStickersetsOrder`: `bool` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### `delete(): void`

Delete the story.



### `exportLink(): string`

Export story link e.g: https://t.me/username/s/storyid.



### `report(\danog\MadelineProto\EventHandler\Message\ReportReason $reason, string $message = ''): bool`

Report a story for violation of telegram’s Terms of Service.


Parameters:

* `$reason`: `\danog\MadelineProto\EventHandler\Message\ReportReason` Why is story being reported  
* `$message`: `string` Comment for report moderation  


#### See also: 
* [\danog\MadelineProto\EventHandler\Message\ReportReason](../../../../danog/MadelineProto/EventHandler/Message/ReportReason.html)




### `pin(): void`

Pin a story.



### `unpin(): void`

Unpin a story.



### `view(): bool`

Mark story as read.



### `addReaction(int|string $reaction, bool $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`

Reaction to story.


Parameters:

* `$reaction`: `int|string` string or int Reaction  
* `$recent`: `bool`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Story\StoryReaction`: Represents a reaction to a story.](../../../../danog/MadelineProto/EventHandler/Story/StoryReaction.html)




### `delReaction(bool $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`

Delete reaction from story.


Parameters:

* `$recent`: `bool` string or int Reaction  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Story\StoryReaction`: Represents a reaction to a story.](../../../../danog/MadelineProto/EventHandler/Story/StoryReaction.html)




### `getHTML(bool $allowTelegramTags = false): string`

Get an HTML version of the story caption.


Parameters:

* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

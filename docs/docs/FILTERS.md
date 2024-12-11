---
title: "Filters"
description: "MadelineProto offers a very simple and intuitive message filtering system, based on PHP's type system and attributes."
nav_order: 13
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Filters

MadelineProto offers a very simple and intuitive message filtering system, based on PHP's type system and attributes.

There are two filter types:

* [Simple filters](#simple-filters)
* [Attribute filters](#attribute-filters)
  * [Creating custom attribute filters](#creating-custom-attribute-filters)
* [MTProto filters](#mtproto-filters)

## Simple filters

Simple filters are implemented using simple PHP types, for example:

```php
use danog\MadelineProto\SimpleEventHandler;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\Message\PrivateMessage;
use danog\MadelineProto\EventHandler\Message\GroupMessage;
use danog\MadelineProto\EventHandler\Message\ChannelMessage;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\EventHandler\SimpleFilter\Outgoing;
use danog\MadelineProto\EventHandler\SimpleFilter\HasMedia;

class MyEventHandler extends SimpleEventHandler
{
    #[Handler]
    public function h1(Incoming & Message $message): void
    {
        // Handle all incoming messages (private+groups+channels).
    }

    #[Handler]
    public function h2(Outgoing & PrivateMessage $message): void
    {
        // Handle all outgoing messages (private).
    }

    #[Handler]
    public function h3((Incoming & GroupMessage & HasMedia) | (Incoming & ChannelMessage & HasMedia) $message): void
    {
        // Handle all incoming messages with media attached (groups+channels).
    }
}
```

MadelineProto will send updates about new messages to all methods marked with the `Handler` attribute, appropriately filtering them first according to the typehint.  

A filter typehint is composed of:

* A single concrete type: `A`
  * Concrete types are objects with useful bound methods and properties containing the fields of the message.
* A single concrete type intersected with one or more filter interfaces: `A&B&C` (used to AND filters)
  * Filter interfaces are PHP interfaces that are automatically parsed using reflection.  
    Unlike concrete types, they cannot be used for type assertions outside of a method marked by `#[Handler]` or `#[Filter...]` attributes.
* A union of concrete types: `A|B|C` (used to OR filters)
* A union of concrete types or intersections: `(A&B)|C|(D&F)` (used to OR filters in DNF form)

Single concrete type examples:

* `Message` - Handle all incoming and outgoing messages (private or groups or channels).
* `ChannelMessage` - Handle all incoming and outgoing messages (channels).
* `GroupMessage` - Handle all incoming and outgoing messages (groups).
* `PrivateMessage` - Handle all incoming and outgoing messages (private).
* `ServiceMessage` - Handle all incoming and outgoing service messages (private or groups or channels).
* `AbstractMessage` - Handle all incoming and outgoing service+normal messages (private or groups or channels).

Intersection examples:

* `Incoming & Message` - Handle all incoming messages (private or groups or channels).
* `Incoming & GroupMessage & HasMedia` - Handle all incoming media messages (groups).

Union/DNF examples:

* `GroupMessage|ChannelMessage` - Handle all incoming and outgoing messages (groups or channels).
* `(Incoming&GroupMessage)|(Incoming&ChannelMessage)` - Handle all incoming messages (groups or channels).
* `ServiceMessage|(ChannelMessage&HasMedia)` - Handle all service messages or incoming and outgoing media channel messages.

Simple filters can optionally be combined with [attribute filters](#attribute-filters), in which case they will be AND-ed together.  

Here's the full list of all concrete types:

<!-- cut_here concretefilters -->

* [danog\MadelineProto\Broadcast\Progress &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html) - Broadcast progress.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractPrivateMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html) - Represents a private or secret chat message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractStory &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html) - Represents a Telegram Story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html#method-list)
* [danog\MadelineProto\EventHandler\BotCommands &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html) - The [command set](https://core.telegram.org/api/bots/commands) of a certain bot in a certain chat has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html#method-list)
* [danog\MadelineProto\EventHandler\CallbackQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html) - Represents a query sent by the user by clicking on a button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\ChannelParticipant &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/ChannelParticipant.html) - A participant has left, joined, was banned or admin'd in a [channel or supergroup](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/ChannelParticipant.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/ChannelParticipant.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\MessageForwards &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html) - Indicates that the forward counter of a message in a channel has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\MessageViewsChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html) - Indicates that the view counter of a message in a channel has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\UpdateChannel &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html) - A new channel is available, or info about an existing channel was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html) - Indicates someone has requested to join a chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester\BotChatInviteRequest &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html) - Indicates someone has requested to join a chat or channel (bots only).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester\PendingJoinRequests &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html) - Someone has requested to join a chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html#method-list)
* [danog\MadelineProto\EventHandler\Delete &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html) - Indicates that some messages were deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteChannelMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html) - Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html) - Some messages were deleted in a private chat or simple group.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteScheduledMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html) - Some [scheduled messages](https://core.telegram.org/api/scheduled-messages) were deleted from the schedule queue of a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html#method-list)
* [danog\MadelineProto\EventHandler\InlineQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html) - An incoming inline query.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Message &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ChannelMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html) - Represents an incoming or outgoing channel message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\CommentReply &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/CommentReply.html) - Represents a reply to one of our messages in a channel comment group that we're not a member of (i.e. received via `@replies`).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/CommentReply.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/CommentReply.html#method-list)
* [danog\MadelineProto\EventHandler\Message\GroupMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html) - Represents an incoming or outgoing group message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\PrivateMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html) - Represents an incoming or outgoing private message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\SecretMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html) - Represents New encrypted message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogBotAllowed &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html) - We have given the bot permission to send us direct messages.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChannelCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html) - The channel was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChannelMigrateFrom &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html) - Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChatJoinedByLink &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html) - A user joined the chat via an invite link.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChatMigrateTo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html) - Indicates the chat was [migrated](https://core.telegram.org/api/channel) to the specified supergroup.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogContactSignUp &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html) - A contact just signed up to telegram.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html) - A chat or channel was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogDeleteMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html) - Deleted messages.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGameScore &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html) - Someone scored in a game.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGeoProximityReached &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html) - A user of the chat is now in proximity of another user.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGiftPremium &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html) - Info about a gifted Telegram Premium subscription.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGiftStars &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftStars.html) - Info about a gifted Telegram Stars.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftStars.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftStars.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html) - Represents a service message about a group call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html) - The group call has started or ended.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCallInvited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html) - A set of users was invited to the group call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCallScheduled &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html) - A group call was scheduled.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogHistoryCleared &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html) - Chat history was cleared.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMemberJoinedByRequest &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html) - A user was accepted into the group by an admin.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMemberLeft &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html) - A member left the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMembersJoined &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html) - Some members joined the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMessagePinned &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html) - A message was pinned in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPeerRequested &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html) - Contains info about a peer that the user shared with the bot after clicking on a [keyboardButtonRequestPeer](https://docs.madelineproto.xyz/API_docs/constructors/keyboardButtonRequestPeer.html) button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPhoneCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html) - A phone call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPhotoChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html) - The photo of the dialog was changed or deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogReadMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html) - Messages marked as read.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogScreenshotTaken &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html) - A screenshot of the chat was taken.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetChatTheme &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html) - The chat theme was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetChatWallPaper &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html) - The [wallpaper](https://core.telegram.org/api/wallpapers) of the current chat was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html) - The Time-To-Live of messages in this chat was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogStarGift &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogStarGift.html) - Info about a Star gifted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogStarGift.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogStarGift.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSuggestProfilePhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html) - A new profile picture was suggested using [photos.uploadContactProfilePhoto](https://docs.madelineproto.xyz/API_docs/methods/photos.uploadContactProfilePhoto.html).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTitleChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html) - The title of a channel or group has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTopicCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html) - A [forum topic](https://core.telegram.org/api/forum#forum-topics) was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTopicEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html) - [Forum topic](https://core.telegram.org/api/forum#forum-topics) information was edited.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogWebView &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html) - Data from an opened [reply keyboard bot web app](https://core.telegram.org/api/bots/webapps) was relayed to the bot that owns it (user & bot side service message).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html#method-list)
* [danog\MadelineProto\EventHandler\Payments\Payment &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Payments/Payment.html) - This object contains information about an incoming pre-checkout query.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Payments/Payment.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Payments/Payment.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html) - Indicates that some messages were pinned/unpinned.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedChannelMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html) - Represents messages that were pinned/unpinned in a [channel](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedGroupMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html) - Represents messages that were pinned/unpinned in a [chat/supergroup](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedPrivateMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html) - Some messages were pinned in a private chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Privacy &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html) - Indicates some privacy rules for a user or set of users.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html) - Represents a query sent by the user by clicking on a button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ChatButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html) - Represents a query sent by the user by clicking on a button in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ChatGameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\GameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\InlineButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html) - Represents a query sent by the user by clicking on a button in an inline message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\InlineGameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button in an inline message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Story\Story &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html) - Represents a Telegram story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html#method-list)
* [danog\MadelineProto\EventHandler\Story\StoryDeleted &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html) - Represents a deleted story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html#method-list)
* [danog\MadelineProto\EventHandler\Story\StoryReaction &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html) - Represents a reaction to a story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html#method-list)
* [danog\MadelineProto\EventHandler\Typing &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html) - A user is typing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\ChatUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html) - The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\SecretUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html) - The user is preparing a message in a secret chat; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\SupergroupUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html) - A user is typing in a [supergroup](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\UserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html) - The user is preparing a message; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\User\Blocked &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html) - A peer was blocked.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html#method-list)
* [danog\MadelineProto\EventHandler\User\BotStopped &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html) - A bot was stopped or re-started.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html#method-list)
* [danog\MadelineProto\EventHandler\User\Phone &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html) - A user’s phone number was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html) - Contains a status update.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Emoji &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html) - The [emoji status](https://core.telegram.org/api/emoji-status) of a certain user has changed or was removed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\EmptyStatus &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html) - User status has not been set yet.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\LastMonth &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html) - Online status: last seen last month.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\LastWeek &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html) - Online status: last seen last week.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Offline &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html) - The user’s offline status.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Online &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html) - Online status of the user.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Recently &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html) - Online status: last seen recently.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html#method-list)
* [danog\MadelineProto\EventHandler\User\Username &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html) - Changes were made to the user’s first name, last name or username.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html#method-list)
* [danog\MadelineProto\VoIP &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) - This update represents a VoIP Telegram call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html#method-list)


<!-- cut_here_end concretefilters -->

Here's the full list of simple filter interfaces (see [attribute filters](#attribute-filters) for more advanced filters like commands, regexes, and much more!):

<!-- cut_here simplefilters -->

* [danog\MadelineProto\EventHandler\SimpleFilter\Ended &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/Ended.html) - Represents an ended call
* [danog\MadelineProto\EventHandler\SimpleFilter\FromAdmin &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/FromAdmin.html) - Allows messages from the bot admin
* [danog\MadelineProto\EventHandler\SimpleFilter\FromAdminOrOutgoing &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/FromAdminOrOutgoing.html) - Allows messages from the bot admin or outgoing messages
* [danog\MadelineProto\EventHandler\SimpleFilter\HasAudio &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasAudio.html) - Allows only audio messages
* [danog\MadelineProto\EventHandler\SimpleFilter\HasDocument &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasDocument.html) - Allows only documents
* [danog\MadelineProto\EventHandler\SimpleFilter\HasDocumentPhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasDocumentPhoto.html) - Allows only document photos
* [danog\MadelineProto\EventHandler\SimpleFilter\HasGif &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasGif.html) - Allows only GIFs
* [danog\MadelineProto\EventHandler\SimpleFilter\HasMedia &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasMedia.html) - Allows only media messages
* [danog\MadelineProto\EventHandler\SimpleFilter\HasMultiplePoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasMultiplePoll.html) - Allows only messages that contain a multiple poll
* [danog\MadelineProto\EventHandler\SimpleFilter\HasNoMedia &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasNoMedia.html) - Allows only messages with no media
* [danog\MadelineProto\EventHandler\SimpleFilter\HasPhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasPhoto.html) - Allows only photos
* [danog\MadelineProto\EventHandler\SimpleFilter\HasPoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasPoll.html) - Allows only messages that contain a poll
* [danog\MadelineProto\EventHandler\SimpleFilter\HasQuizPoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasQuizPoll.html) - Allows only messages that contain a quiz poll
* [danog\MadelineProto\EventHandler\SimpleFilter\HasRoundVideo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasRoundVideo.html) - Allows only round videos
* [danog\MadelineProto\EventHandler\SimpleFilter\HasSinglePoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasSinglePoll.html) - Allows only messages that contain a single poll
* [danog\MadelineProto\EventHandler\SimpleFilter\HasSticker &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasSticker.html) - Allows only stickers
* [danog\MadelineProto\EventHandler\SimpleFilter\HasTopic &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasTopic.html) - Allow only messages coming from groups that has topics (Supergroups only).
* [danog\MadelineProto\EventHandler\SimpleFilter\HasVideo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasVideo.html) - Allows only videos
* [danog\MadelineProto\EventHandler\SimpleFilter\HasVoice &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/HasVoice.html) - Allows only voice messages
* [danog\MadelineProto\EventHandler\SimpleFilter\Incoming &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/Incoming.html) - Represents an incoming message
* [danog\MadelineProto\EventHandler\SimpleFilter\IsEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/IsEdited.html) - Allows messages that were edited.
* [danog\MadelineProto\EventHandler\SimpleFilter\IsForwarded &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/IsForwarded.html) - Allows only forwarded messages
* [danog\MadelineProto\EventHandler\SimpleFilter\IsNotEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/IsNotEdited.html) - Allows messages that weren't edited.
* [danog\MadelineProto\EventHandler\SimpleFilter\IsReply &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/IsReply.html) - Allows only messages that reply to other messages
* [danog\MadelineProto\EventHandler\SimpleFilter\IsReplyToSelf &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/IsReplyToSelf.html) - Allows only messages that reply to one of our messages
* [danog\MadelineProto\EventHandler\SimpleFilter\Outgoing &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/Outgoing.html) - Represents an outgoing message
* [danog\MadelineProto\EventHandler\SimpleFilter\Running &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/SimpleFilter/Running.html) - Allow only currently running calls


<!-- cut_here_end simplefilters -->

## Attribute filters

Attribute filters are implemented using PHP attributes, for example:

```php
use danog\MadelineProto\SimpleEventHandler;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\Message\PrivateMessage;
use danog\MadelineProto\EventHandler\Message\GroupMessage;
use danog\MadelineProto\EventHandler\Message\ChannelMessage;
use danog\MadelineProto\EventHandler\Filter\FilterIncoming;

class MyEventHandler extends SimpleEventHandler
{
    #[FilterIncoming]
    public function h1(Message $message): void
    {
        // Handle all incoming messages (private+groups+channels).
    }

    #[FiltersAnd(new FilterOutgoing, new FilterPrivate)]
    public function h2(Message $message): void
    {
        // Handle all outgoing messages (private).
    }

    #[FiltersAnd(new FilterIncoming, new FiltersOr(new FilterGroup, new FilterChannel), new FilterMedia)]
    public function h3(Message $message): void
    {
        // Handle all incoming messages with media attached (groups+channels).
    }
    
    #[FiltersOr(new FilterGroup, new FilterChannel)]
    public function h4(Incoming&Message&HasMedia $message): void
    {
        // Same as h3, but combining simple filters with attribute filters.
    }
}
```

Attribute filters are usual combined with [simple filters](#simple-filters).  
Attribute filters are ANDed with simple filters defined on the same method, for example this:

```php
#[FiltersOr(new FilterGroup, new FilterChannel)]
public function h4(Incoming&Message&HasMedia $message)
```

Is exactly the same as this:

```php
#[FiltersAnd(new FilterIncoming, new FilterMessage, new FilterMedia, new FiltersOr(new FilterGroup, new FilterChannel))]
public function h3($message): void
```

Which can also be written using only [simple filters](#simple-filters):

```php
#[Handler]
public function h3((Incoming & GroupMessage & HasMedia) | (Incoming & ChannelMessage & HasMedia) $message): void
```


Here's the full list of filter attributes (see the [MTProto filters &raquo;](#mtproto-filters) for even more low-level filters):

<!-- cut_here attributefilters -->

* [danog\MadelineProto\EventHandler\Filter\FilterAllowAll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterAllowAll.html) - Allow all updates.
* [danog\MadelineProto\EventHandler\Filter\FilterButtonQueryData(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterButtonQueryData.html) - Filters based on the content of a button query.
* [danog\MadelineProto\EventHandler\Filter\FilterChannel &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterChannel.html) - Allow only updates coming from channels.
* [danog\MadelineProto\EventHandler\Filter\FilterCommand(string $command, list<CommandType> $types = [  0 =>   \danog\MadelineProto\EventHandler\CommandType::BANG,  1 =>   \danog\MadelineProto\EventHandler\CommandType::DOT,  2 =>   \danog\MadelineProto\EventHandler\CommandType::SLASH,]) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterCommand.html) - Allow only messages containing the specified command.
* [danog\MadelineProto\EventHandler\Filter\FilterCommandCaseInsensitive(string $command, list<CommandType> $types = [  0 =>   \danog\MadelineProto\EventHandler\CommandType::BANG,  1 =>   \danog\MadelineProto\EventHandler\CommandType::DOT,  2 =>   \danog\MadelineProto\EventHandler\CommandType::SLASH,]) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterCommandCaseInsensitive.html) - Allow only messages containing the specified case-insensitive command.
* [danog\MadelineProto\EventHandler\Filter\FilterCommentReply &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterCommentReply.html) - Allow messages that coming from @replies.
* [danog\MadelineProto\EventHandler\Filter\FilterEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterEdited.html) - Allows messages that were edited.
* [danog\MadelineProto\EventHandler\Filter\FilterEnded &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterEnded.html) - Allow only ended calls.
* [danog\MadelineProto\EventHandler\Filter\FilterForwarded &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterForwarded.html) - Allow only forwarded messages.
* [danog\MadelineProto\EventHandler\Filter\FilterForwardedFrom(string|int $peer) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterForwardedFrom.html) - Allow only forwarded messages from a certain sender.
* [danog\MadelineProto\EventHandler\Filter\FilterFromAdmin &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterFromAdmin.html) - Allow only messages coming from the admin (defined as the peers returned by getReportPeers).
* [danog\MadelineProto\EventHandler\Filter\FilterFromBot &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterFromBot.html) - Allow only messages coming from bots.
* [danog\MadelineProto\EventHandler\Filter\FilterFromSender(string|int $peer) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterFromSender.html) - Allow incoming or outgoing group messages made by a certain sender.
* [danog\MadelineProto\EventHandler\Filter\FilterFromSenders(string|int ...$idOrUsername) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterFromSenders.html) - Allow incoming or outgoing group messages made by a certain list of senders.
* [danog\MadelineProto\EventHandler\Filter\FilterGroup &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterGroup.html) - Allow only updates coming from groups.
* [danog\MadelineProto\EventHandler\Filter\FilterIncoming &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterIncoming.html) - Allow only incoming messages.
* [danog\MadelineProto\EventHandler\Filter\FilterMedia &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterMedia.html) - Allow any media messages.
* [danog\MadelineProto\EventHandler\Filter\FilterMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterMessage.html) - Allow any non-service message.
* [danog\MadelineProto\EventHandler\Filter\FilterNoMedia &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterNoMedia.html) - Allow any messages except media messages.
* [danog\MadelineProto\EventHandler\Filter\FilterNotEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterNotEdited.html) - Allows messages that weren't edited.
* [danog\MadelineProto\EventHandler\Filter\FilterOutgoing &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterOutgoing.html) - Allow only outgoing messages.
* [danog\MadelineProto\EventHandler\Filter\FilterPeer(string|int $peer) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterPeer.html) - Allow messages coming from or sent to a certain peer.
* [danog\MadelineProto\EventHandler\Filter\FilterPoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterPoll.html) - Allow only messages that contain a poll.
* [danog\MadelineProto\EventHandler\Filter\FilterPrivate &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterPrivate.html) - Allow only updates coming from private chats.
* [danog\MadelineProto\EventHandler\Filter\FilterRegex(non-empty-string $regex, int-mask<0, 256, 512> $flags = 0, int $offset = 0) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterRegex.html) - Allow only messages or button queries matching the specified regex.
* [danog\MadelineProto\EventHandler\Filter\FilterRegexMatchAll(non-empty-string $regex, int $flags = 0, int $offset = 0) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterRegexMatchAll.html) - Allow only messages or button queries matching the specified regex.
* [danog\MadelineProto\EventHandler\Filter\FilterReply &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterReply.html) - Allow messages that reply to other messages.
* [danog\MadelineProto\EventHandler\Filter\FilterReplyToSelf &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterReplyToSelf.html) - Allow messages that reply to one of our messages.
* [danog\MadelineProto\EventHandler\Filter\FilterRunning &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterRunning.html) - Allow only running calls.
* [danog\MadelineProto\EventHandler\Filter\FilterSecret &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterSecret.html) - Allow only updates coming from secret chats.
* [danog\MadelineProto\EventHandler\Filter\FilterSender(string|int $peer) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterSender.html) - Allow incoming or outgoing group messages made by a certain sender.
* [danog\MadelineProto\EventHandler\Filter\FilterSenders(string|int ...$idOrUsername) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterSenders.html) - Allow incoming or outgoing group messages made by a certain list of senders.
* [danog\MadelineProto\EventHandler\Filter\FilterService &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterService.html) - Allow only service messages of any type.
* [danog\MadelineProto\EventHandler\Filter\FilterText(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterText.html) - Allow only messages with a specific content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextCaseInsensitive(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextCaseInsensitive.html) - Allow only messages with a specific case-insensitive content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextContains(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextContains.html) - Allow only messages that contain a specific content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextContainsCaseInsensitive(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextContainsCaseInsensitive.html) - Allow only messages that contain a specific case-insensitive content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextEnds(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextEnds.html) - Allow only messages that ends with a specific content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextEndsCaseInsensitive(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextEndsCaseInsensitive.html) - Allow only messages that ends with a specific case-insensitive content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextStarts(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextStarts.html) - Allow only messages that start with a specific content.
* [danog\MadelineProto\EventHandler\Filter\FilterTextStartsCaseInsensitive(string $content) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTextStartsCaseInsensitive.html) - Allow only messages that start with a specific case-insensitive content.
* [danog\MadelineProto\EventHandler\Filter\FilterTopic &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTopic.html) - Allow only messages coming from groups that has topics (Supergroups only).
* [danog\MadelineProto\EventHandler\Filter\FilterTopicId(int $topicId) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/FilterTopicId.html) - Allow only messages with a specific topic id (Supergroups only).
* [danog\MadelineProto\EventHandler\Filter\Combinator\FilterNot(Filter $filter) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Combinator/FilterNot.html) - NOTs a filter.
* [danog\MadelineProto\EventHandler\Filter\Combinator\FiltersAnd(Filter ...$filters) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Combinator/FiltersAnd.html) - ANDs multiple filters.
* [danog\MadelineProto\EventHandler\Filter\Combinator\FiltersOr(Filter ...$filters) &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Combinator/FiltersOr.html) - ORs multiple filters.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterAudio &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterAudio.html) - Allow only audio files.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterDocument &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterDocument.html) - Allow only documents.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterDocumentPhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterDocumentPhoto.html) - Allow only documents containing an image.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterGif &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterGif.html) - Allow only GIFs.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterPhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterPhoto.html) - Allow only photos.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterRoundVideo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterRoundVideo.html) - Allow only round videos.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterSticker &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterSticker.html) - Allow only stickers.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterVideo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterVideo.html) - Allow only videos.
* [danog\MadelineProto\EventHandler\Filter\Media\FilterVoice &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Media/FilterVoice.html) - Allow only voice messages.
* [danog\MadelineProto\EventHandler\Filter\Poll\FilterMultiplePoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Poll/FilterMultiplePoll.html) - Allow only messages that contain a multiple poll.
* [danog\MadelineProto\EventHandler\Filter\Poll\FilterQuizPoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Poll/FilterQuizPoll.html) - Allow only messages that contain a quiz poll.
* [danog\MadelineProto\EventHandler\Filter\Poll\FilterSinglePoll &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Filter/Poll/FilterSinglePoll.html) - Allow only messages that contain a single poll.


<!-- cut_here_end attributefilters -->

### Creating custom attribute filters

To create a custom attribute filter, simply create a method attribute that extends the Filter class.  

You must implement an `apply(Update $update): bool` method, that returns true or false according to the filter's logic.  

```php
<?php declare(strict_types=1);

use Attribute;
use danog\MadelineProto\EventHandler\Update;

/**
 * Use with #[FilterBoolean(true/false)]
 */
#[Attribute(Attribute::TARGET_METHOD)]
final class FilterBoolean extends Filter
{
    public function __construct(private readonly bool $applyIf) {}
    public function apply(Update $update): bool
    {
        return $this->applyIf;
    }
}
```

You can also optionally implement the `public function initialize(EventHandler $API): Filter` function.  

This function is useful to perform expensive one-time initialization tasks, to avoid performing them during filtering, for example:

<!-- cut_here src/EventHandler/Filter/AbstractFilterFromSenders.php -->

```php
<?php declare(strict_types=1);

/**
 * This file is part of MadelineProto.
 * MadelineProto is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
 * MadelineProto is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Affero General Public License for more details.
 * You should have received a copy of the GNU General Public License along with MadelineProto.
 * If not, see <http://www.gnu.org/licenses/>.
 *
 * @author    Daniil Gentili <daniil@daniil.it>
 * @copyright 2016-2023 Daniil Gentili <daniil@daniil.it>
 * @license   https://opensource.org/licenses/AGPL-3.0 AGPLv3
 * @link https://docs.madelineproto.xyz MadelineProto documentation
 */

namespace danog\MadelineProto\EventHandler\Filter;

use danog\MadelineProto\EventHandler;
use danog\MadelineProto\EventHandler\AbstractMessage;
use danog\MadelineProto\EventHandler\AbstractStory;
use danog\MadelineProto\EventHandler\BotCommands;
use danog\MadelineProto\EventHandler\ChatInviteRequester\BotChatInviteRequest;
use danog\MadelineProto\EventHandler\InlineQuery;
use danog\MadelineProto\EventHandler\Query\ButtonQuery;
use danog\MadelineProto\EventHandler\Story\StoryReaction;
use danog\MadelineProto\EventHandler\Typing;
use danog\MadelineProto\EventHandler\Update;
use danog\MadelineProto\EventHandler\User\Blocked;
use danog\MadelineProto\EventHandler\User\BotStopped;
use danog\MadelineProto\EventHandler\User\Phone;
use danog\MadelineProto\EventHandler\User\Status;
use danog\MadelineProto\EventHandler\User\Username;

/**
 * Allow incoming or outgoing group messages made by a certain list of senders.
 *
 * @internal
 */
abstract class AbstractFilterFromSenders extends Filter
{
    /** @var array<string|int> */
    private readonly array $peers;
    /** @var list<int> */
    private readonly array $peersResolved;
    public function __construct(string|int ...$idOrUsername)
    {
        $this->peers = array_unique($idOrUsername);
    }
    public function initialize(EventHandler $API): Filter
    {
        if (\count($this->peers) === 1) {
            return (new FilterFromSender(array_values($this->peers)[0]))->initialize($API);
        }
        $res = [];
        foreach ($this->peers as $peer) {
            $res []= $API->getId($peer);
        }
        /** @psalm-suppress InaccessibleProperty */
        $this->peersResolved = $res;
        return $this;
    }
    public function apply(Update $update): bool
    {
        return $update instanceof AbstractMessage && \in_array($update->senderId, $this->peersResolved, true) ||
            ($update instanceof AbstractStory && \in_array($update->senderId, $this->peersResolved, true)) ||
            ($update instanceof StoryReaction && \in_array($update->senderId, $this->peersResolved, true)) ||
            ($update instanceof ButtonQuery && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof InlineQuery && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof Typing && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof Blocked && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof BotStopped && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof Phone && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof Status && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof Username && \in_array($update->userId, $this->peersResolved, true)) ||
            ($update instanceof BotCommands && \in_array($update->botId, $this->peersResolved, true)) ||
            ($update instanceof BotChatInviteRequest && \in_array($update->userId, $this->peersResolved, true));
    }
}

```

<!-- cut_here_end src/EventHandler/Filter/AbstractFilterFromSenders.php -->

Usually you should return `$this` from `initialize()`, but if you want to replace the current filter with another filter, you can return the new filter, instead:

```php
<?php declare(strict_types=1);

use Attribute;
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\EventHandler\Filter\Filter;
use danog\MadelineProto\EventHandler\Filter\FilterPrivate;
use danog\MadelineProto\EventHandler\Filter\FilterFromAdmin;
use danog\MadelineProto\EventHandler\Update;

/**
 * A shorthand filter for FilterPrivate && FilterFromAdmin
 */
#[Attribute(Attribute::TARGET_METHOD)]
final class FilterPrivateAdmin extends Filter
{
    public function initialize(EventHandler $API): Filter
    {
        return (new FiltersAnd(new FilterPrivate, new FilterFromAdmin))->initialize($API);
    }

    public function apply(Update $update): bool
    {
        throw new AssertionError("Unreachable!");
    }
}
```

Another example:

<!-- cut_here src/EventHandler/Filter/Combinator/FilterNot.php -->

```php
<?php declare(strict_types=1);

/**
 * This file is part of MadelineProto.
 * MadelineProto is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
 * MadelineProto is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Affero General Public License for more details.
 * You should have received a copy of the GNU General Public License along with MadelineProto.
 * If not, see <http://www.gnu.org/licenses/>.
 *
 * @author    Daniil Gentili <daniil@daniil.it>
 * @copyright 2016-2023 Daniil Gentili <daniil@daniil.it>
 * @license   https://opensource.org/licenses/AGPL-3.0 AGPLv3
 * @link https://docs.madelineproto.xyz MadelineProto documentation
 */

namespace danog\MadelineProto\EventHandler\Filter\Combinator;

use Attribute;
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\EventHandler\Filter\Filter;
use danog\MadelineProto\EventHandler\Update;

/**
 * NOTs a filter.
 */
#[Attribute(Attribute::TARGET_METHOD)]
final class FilterNot extends Filter
{
    public function __construct(private readonly Filter $filter)
    {
    }
    public function initialize(EventHandler $API): Filter
    {
        $filter = $this->filter->initialize($API);
        if ($filter instanceof self) {
            // The nested filter is a FilterNot, optimize !!A => A
            return $filter->filter;
        }
        if ($filter === $this->filter) {
            // The nested filter didn't replace itself
            return $this;
        }
        // The nested filter replaced itself, re-wrap it
        return new self($filter);
    }

    public function apply(Update $update): bool
    {
        return !$this->filter->apply($update);
    }
}

```

<!-- cut_here_end src/EventHandler/Filter/Combinator/FilterNot.php -->

## MTProto filters

MTProto filters are used to obtain raw MTProto updates in the form of arrays.  
Unlike [simple updates](#simple-filters), raw MTProto updates do not have bound methods, but MadelineProto offers a bunch of [helper methods](https://docs.madelineproto.xyz/API_docs/methods/) that can be used, instead.  

**Please note that MTProto filters are not covered by any backwards compatibility promise**: they may change at any time, including in minor versions, because they're related directly to the Telegram API schema.  
Use [simple filters](#simple-filters) for a stable object-oriented update API.  

MTProto filters are defined by creating a function with the appropriate name, for example to handle [updateNewMessage](https://docs.madelineproto.xyz/API_docs/constructors/updateNewMessage.html) updates:

```php
use danog\MadelineProto\SimpleEventHandler;

class MyEventHandler extends SimpleEventHandler
{
    /**
     * Handle updates from users.
     *
     * 100+ other types of onUpdate... method types are available, see https://docs.madelineproto.xyz/API_docs/types/Update.html for the full list.
     * You can also use onAny to catch all update types (only for debugging)
     * A special onUpdateCustomEvent method can also be defined, to send messages to the event handler from an API instance, using the sendCustomEvent method.
     *
     * @param array $update Update
     */
    public function onUpdateNewMessage(array $update): void
    {
        if ($update['message']['_'] === 'messageEmpty') {
            return;
        }

        $this->logger($update);

        // Chat ID
        $id = $this->getId($update);

        // Sender ID, not always present
        $from_id = isset($update['message']['from_id'])
            ? $this->getId($update['message']['from_id'])
            : null;
        

        // In this example code, send the "This userbot is powered by MadelineProto!" message only once per chat.
        // Ignore all further messages coming from this chat.
        if (!isset($this->notifiedChats[$id])) {
            $this->notifiedChats[$id] = true;

            $this->messages->sendMessage(
                peer: $update,
                message: "This userbot is powered by [MadelineProto](https://t.me/MadelineProto)!",
                reply_to_msg_id: $update['message']['id'] ?? null,
                parse_mode: 'Markdown'
            );
        }
    }
}
```

Here's a full list of all MTProto filters (click on each filter name to view the structure of the array that will be passed to it):

<!-- cut_here mtprotofilters -->

 * onUpdateCustomEvent: Receives messages sent to the event handler from an API instance using the [`sendCustomEvent` &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/API.html#sendcustomevent-mixed-payload-void) method.
 * onAny: Catch-all filter, if defined catches all updates that aren't catched by any other filter.
 * [onUpdateBroadcastProgress &raquo;](https://docs.madelineproto.xyz/docs/BROADCAST.html#get-progress): Used to receive updates to an in-progress [message broadcast &raquo;](https://docs.madelineproto.xyz/docs/BROADCAST.html)* [onUpdateNewMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewMessage.html) - New message in a private chat or in a [basic group](https://core.telegram.org/api/channel#basic-groups).
* [onUpdateMessageID &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMessageID.html) - Sent message with **random\_id** client identifier was assigned an identifier.
* [onUpdateDeleteMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDeleteMessages.html) - Messages were deleted.
* [onUpdateUserTyping &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUserTyping.html) - The user is preparing a message; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing
* [onUpdateChatUserTyping &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatUserTyping.html) - The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing
* [onUpdateChatParticipants &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatParticipants.html) - Composition of chat participants changed.
* [onUpdateUserStatus &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUserStatus.html) - Contact status update.
* [onUpdateUserName &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUserName.html) - Changes the user's first name, last name and username.
* [onUpdateNewAuthorization &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewAuthorization.html) - A new session logged into the current user's account through an unknown device.
* [onUpdateNewEncryptedMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewEncryptedMessage.html) - New encrypted message.
* [onUpdateEncryptedChatTyping &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateEncryptedChatTyping.html) - Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing.
* [onUpdateEncryption &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateEncryption.html) - Change of state in an encrypted chat.
* [onUpdateEncryptedMessagesRead &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateEncryptedMessagesRead.html) - Communication history in an encrypted chat was marked as read.
* [onUpdateChatParticipantAdd &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatParticipantAdd.html) - New group member.
* [onUpdateChatParticipantDelete &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatParticipantDelete.html) - A member has left the group.
* [onUpdateDcOptions &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDcOptions.html) - Changes in the data center configuration options.
* [onUpdateNotifySettings &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNotifySettings.html) - Changes in notification settings.
* [onUpdateServiceNotification &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateServiceNotification.html) - A service message for the user.
* [onUpdatePrivacy &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePrivacy.html) - Privacy rules were changed
* [onUpdateUserPhone &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUserPhone.html) - A user's phone number was changed
* [onUpdateReadHistoryInbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadHistoryInbox.html) - Incoming messages were read
* [onUpdateReadHistoryOutbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadHistoryOutbox.html) - Outgoing messages were read
* [onUpdateWebPage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateWebPage.html) - An [instant view](https://instantview.telegram.org) webpage preview was generated
* [onUpdateReadMessagesContents &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadMessagesContents.html) - Contents of messages in the common [message box](https://core.telegram.org/api/updates) were read
* [onUpdateChannelTooLong &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelTooLong.html) - There are new updates in the specified channel, the client must fetch them.  
* [onUpdateChannel &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannel.html) - A new channel or supergroup is available, or info about an existing channel has changed and must be refeteched.
* [onUpdateNewChannelMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewChannelMessage.html) - A new message was sent in a [channel/supergroup](https://core.telegram.org/api/channel)
* [onUpdateReadChannelInbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadChannelInbox.html) - Incoming messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read
* [onUpdateDeleteChannelMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDeleteChannelMessages.html) - Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted
* [onUpdateChannelMessageViews &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelMessageViews.html) - The view counter of a message in a channel has changed
* [onUpdateChatParticipantAdmin &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatParticipantAdmin.html) - Admin permissions of a user in a [basic group](https://core.telegram.org/api/channel#basic-groups) were changed
* [onUpdateNewStickerSet &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewStickerSet.html) - A new stickerset was installed
* [onUpdateStickerSetsOrder &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStickerSetsOrder.html) - The order of stickersets was changed
* [onUpdateStickerSets &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStickerSets.html) - Installed stickersets have changed, the client should refetch them as [described in the docs](https://core.telegram.org/api/stickers#installing-stickersets).
* [onUpdateSavedGifs &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSavedGifs.html) - The saved gif list has changed, the client should refetch it using [messages.getSavedGifs](https://core.telegram.org/method/messages.getSavedGifs)
* [onUpdateBotInlineQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotInlineQuery.html) - An incoming inline query
* [onUpdateBotInlineSend &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotInlineSend.html) - The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.
* [onUpdateEditChannelMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateEditChannelMessage.html) - A message was edited in a [channel/supergroup](https://core.telegram.org/api/channel)
* [onUpdateBotCallbackQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotCallbackQuery.html) - A callback button was pressed, and the button data was sent to the bot that created the button
* [onUpdateEditMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateEditMessage.html) - A message was edited
* [onUpdateInlineBotCallbackQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateInlineBotCallbackQuery.html) - This notification is received by bots when a button is pressed
* [onUpdateReadChannelOutbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadChannelOutbox.html) - Outgoing messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read
* [onUpdateDraftMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDraftMessage.html) - Notifies a change of a message [draft](https://core.telegram.org/api/drafts).
* [onUpdateReadFeaturedStickers &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadFeaturedStickers.html) - Some featured stickers were marked as read
* [onUpdateRecentStickers &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateRecentStickers.html) - The recent sticker list was updated
* [onUpdateConfig &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateConfig.html) - The server-side configuration has changed; the client should re-fetch the config using [help.getConfig](https://docs.madelineproto.xyz/API_docs/methods/help.getConfig.html)
* [onUpdatePtsChanged &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePtsChanged.html) - [Common message box sequence PTS](https://core.telegram.org/api/updates) has changed, [state has to be refetched using updates.getState](https://core.telegram.org/api/updates#fetching-state)
* [onUpdateChannelWebPage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelWebPage.html) - A webpage preview of a link in a [channel/supergroup](https://core.telegram.org/api/channel) message was generated
* [onUpdateDialogPinned &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDialogPinned.html) - A dialog was pinned/unpinned
* [onUpdatePinnedDialogs &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePinnedDialogs.html) - Pinned dialogs were updated
* [onUpdateBotWebhookJSON &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotWebhookJSON.html) - A new incoming event; for bots only
* [onUpdateBotWebhookJSONQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotWebhookJSONQuery.html) - A new incoming query; for bots only
* [onUpdateBotShippingQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotShippingQuery.html) - This object contains information about an incoming shipping query.
* [onUpdateBotPrecheckoutQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotPrecheckoutQuery.html) - This object contains information about an incoming pre-checkout query.
* [onUpdatePhoneCall &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePhoneCall.html) - An incoming phone call
* [onUpdateLangPackTooLong &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateLangPackTooLong.html) - A language pack has changed, the client should manually fetch the changed strings using [langpack.getDifference](https://docs.madelineproto.xyz/API_docs/methods/langpack.getDifference.html)
* [onUpdateLangPack &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateLangPack.html) - Language pack updated
* [onUpdateFavedStickers &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateFavedStickers.html) - The list of favorited stickers was changed, the client should call [messages.getFavedStickers](https://docs.madelineproto.xyz/API_docs/methods/messages.getFavedStickers.html) to refetch the new list
* [onUpdateChannelReadMessagesContents &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelReadMessagesContents.html) - The specified [channel/supergroup](https://core.telegram.org/api/channel) messages were read
* [onUpdateContactsReset &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateContactsReset.html) - All contacts were deleted
* [onUpdateChannelAvailableMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelAvailableMessages.html) - The history of a [channel/supergroup](https://core.telegram.org/api/channel) was hidden.
* [onUpdateDialogUnreadMark &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDialogUnreadMark.html) - The manual unread mark of a chat was changed
* [onUpdateMessagePoll &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMessagePoll.html) - The results of a poll have changed
* [onUpdateChatDefaultBannedRights &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatDefaultBannedRights.html) - Default banned rights in a [normal chat](https://core.telegram.org/api/channel) were updated
* [onUpdateFolderPeers &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateFolderPeers.html) - The peer list of a [peer folder](https://core.telegram.org/api/folders#peer-folders) was updated
* [onUpdatePeerSettings &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePeerSettings.html) - Settings of a certain peer have changed
* [onUpdatePeerLocated &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePeerLocated.html) - List of peers near you was updated
* [onUpdateNewScheduledMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewScheduledMessage.html) - A message was added to the [schedule queue of a chat](https://core.telegram.org/api/scheduled-messages)
* [onUpdateDeleteScheduledMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDeleteScheduledMessages.html) - Some [scheduled messages](https://core.telegram.org/api/scheduled-messages) were deleted from the schedule queue of a chat
* [onUpdateTheme &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateTheme.html) - A cloud theme was updated
* [onUpdateGeoLiveViewed &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateGeoLiveViewed.html) - Live geoposition message was viewed
* [onUpdateLoginToken &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateLoginToken.html) - A login token (for login via QR code) was accepted.
* [onUpdateMessagePollVote &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMessagePollVote.html) - A specific peer has voted in a poll
* [onUpdateDialogFilter &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDialogFilter.html) - A new [folder](https://core.telegram.org/api/folders) was added
* [onUpdateDialogFilterOrder &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDialogFilterOrder.html) - New [folder](https://core.telegram.org/api/folders) order
* [onUpdateDialogFilters &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDialogFilters.html) - Clients should update [folder](https://core.telegram.org/api/folders) info
* [onUpdatePhoneCallSignalingData &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePhoneCallSignalingData.html) - Incoming phone call signaling payload
* [onUpdateChannelMessageForwards &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelMessageForwards.html) - The forward counter of a message in a channel has changed
* [onUpdateReadChannelDiscussionInbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadChannelDiscussionInbox.html) - Incoming comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read
* [onUpdateReadChannelDiscussionOutbox &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadChannelDiscussionOutbox.html) - Outgoing comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read
* [onUpdatePeerBlocked &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePeerBlocked.html) - We blocked a peer, see [here »](https://core.telegram.org/api/block) for more info on blocklists.
* [onUpdateChannelUserTyping &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelUserTyping.html) - A user is typing in a [supergroup, channel](https://core.telegram.org/api/channel) or [message thread](https://core.telegram.org/api/threads)
* [onUpdatePinnedMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePinnedMessages.html) - Some messages were pinned in a chat
* [onUpdatePinnedChannelMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePinnedChannelMessages.html) - Messages were pinned/unpinned in a [channel/supergroup](https://core.telegram.org/api/channel)
* [onUpdateChat &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChat.html) - A new chat is available
* [onUpdateGroupCallParticipants &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateGroupCallParticipants.html) - The participant list of a certain group call has changed
* [onUpdateGroupCall &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateGroupCall.html) - A new groupcall was started
* [onUpdatePeerHistoryTTL &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePeerHistoryTTL.html) - The Time-To-Live for messages sent by the current user in a specific chat has changed
* [onUpdateChatParticipant &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChatParticipant.html) - A user has joined or left a specific chat
* [onUpdateChannelParticipant &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelParticipant.html) - A participant has left, joined, was banned or admined in a [channel or supergroup](https://core.telegram.org/api/channel).
* [onUpdateBotStopped &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotStopped.html) - A bot was stopped or re-started.
* [onUpdateGroupCallConnection &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateGroupCallConnection.html) - New WebRTC parameters
* [onUpdateBotCommands &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotCommands.html) - The [command set](https://core.telegram.org/api/bots/commands) of a certain bot in a certain chat has changed.
* [onUpdatePendingJoinRequests &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePendingJoinRequests.html) - Someone has requested to join a chat or channel
* [onUpdateBotChatInviteRequester &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotChatInviteRequester.html) - Someone has requested to join a chat or channel (bots only, users will receive an [updatePendingJoinRequests](https://docs.madelineproto.xyz/API_docs/constructors/updatePendingJoinRequests.html), instead)
* [onUpdateMessageReactions &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMessageReactions.html) - New [message reactions »](https://core.telegram.org/api/reactions) are available
* [onUpdateAttachMenuBots &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateAttachMenuBots.html) - The list of installed [attachment menu entries »](https://core.telegram.org/api/bots/attach) has changed, use [messages.getAttachMenuBots](https://docs.madelineproto.xyz/API_docs/methods/messages.getAttachMenuBots.html) to fetch the updated list.
* [onUpdateWebViewResultSent &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateWebViewResultSent.html) - Indicates to a bot that a webview was closed and an inline message was sent on behalf of the user using [messages.sendWebViewResultMessage](https://docs.madelineproto.xyz/API_docs/methods/messages.sendWebViewResultMessage.html)
* [onUpdateBotMenuButton &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotMenuButton.html) - The menu button behavior for the specified bot has changed
* [onUpdateSavedRingtones &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSavedRingtones.html) - The list of saved notification sounds has changed, use [account.getSavedRingtones](https://docs.madelineproto.xyz/API_docs/methods/account.getSavedRingtones.html) to fetch the new list.
* [onUpdateTranscribedAudio &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateTranscribedAudio.html) - A pending [voice message transcription »](https://core.telegram.org/api/transcribe) initiated with [messages.transcribeAudio](https://docs.madelineproto.xyz/API_docs/methods/messages.transcribeAudio.html) was updated.
* [onUpdateReadFeaturedEmojiStickers &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadFeaturedEmojiStickers.html) - Some featured [custom emoji stickers](https://core.telegram.org/api/custom-emoji) were marked as read
* [onUpdateUserEmojiStatus &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUserEmojiStatus.html) - The [emoji status](https://core.telegram.org/api/emoji-status) of a certain user has changed
* [onUpdateRecentEmojiStatuses &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateRecentEmojiStatuses.html) - The list of recent [emoji statuses](https://core.telegram.org/api/emoji-status) has changed
* [onUpdateRecentReactions &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateRecentReactions.html) - The list of recent [message reactions](https://core.telegram.org/api/reactions) has changed
* [onUpdateMoveStickerSetToTop &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMoveStickerSetToTop.html) - A stickerset was just moved to top, [see here for more info »](https://core.telegram.org/api/stickers#recent-stickersets)
* [onUpdateMessageExtendedMedia &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateMessageExtendedMedia.html) - Extended media update
* [onUpdateChannelPinnedTopic &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelPinnedTopic.html) - A [forum topic »](https://core.telegram.org/api/forum#forum-topics) was pinned or unpinned.
* [onUpdateChannelPinnedTopics &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelPinnedTopics.html) - The [pinned topics](https://core.telegram.org/api/forum#forum-topics) of a forum have changed.
* [onUpdateUser &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateUser.html) - User information was updated, it must be refetched using [users.getFullUser](https://docs.madelineproto.xyz/API_docs/methods/users.getFullUser.html).
* [onUpdateAutoSaveSettings &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateAutoSaveSettings.html) - Media autosave settings have changed and must be refetched using [account.getAutoSaveSettings](https://docs.madelineproto.xyz/API_docs/methods/account.getAutoSaveSettings.html).
* [onUpdateStory &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStory.html) - A new story was posted.
* [onUpdateReadStories &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateReadStories.html) - Stories of a specific peer were marked as read.
* [onUpdateStoryID &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStoryID.html) - A story was successfully uploaded.
* [onUpdateStoriesStealthMode &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStoriesStealthMode.html) - Indicates that [stories stealth mode](https://core.telegram.org/api/stories#stealth-mode) was activated.
* [onUpdateSentStoryReaction &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSentStoryReaction.html) - Indicates we [reacted to a story »](https://core.telegram.org/api/stories#reactions).
* [onUpdateBotChatBoost &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotChatBoost.html) - A [channel boost](https://core.telegram.org/api/boost) has changed (bots only)
* [onUpdateChannelViewForumAsMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateChannelViewForumAsMessages.html) - Users may also choose to display messages from all topics as if they were sent to a normal group, using a "View as messages" setting in the local client.  
* [onUpdatePeerWallpaper &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePeerWallpaper.html) - The [wallpaper »](https://core.telegram.org/api/wallpapers) of a given peer has changed.
* [onUpdateBotMessageReaction &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotMessageReaction.html) - Bots only: a user has changed their reactions on a message with public reactions.
* [onUpdateBotMessageReactions &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotMessageReactions.html) - Bots only: the number of reactions on a message with anonymous reactions has changed.
* [onUpdateSavedDialogPinned &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSavedDialogPinned.html) - A [saved message dialog](https://core.telegram.org/api/saved-messages) was pinned/unpinned
* [onUpdatePinnedSavedDialogs &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePinnedSavedDialogs.html) - [Pinned saved dialogs »](https://core.telegram.org/api/saved-messages) were updated
* [onUpdateSavedReactionTags &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSavedReactionTags.html) - 
* [onUpdateSmsJob &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateSmsJob.html) - 
* [onUpdateQuickReplies &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateQuickReplies.html) - 
* [onUpdateNewQuickReply &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewQuickReply.html) - 
* [onUpdateDeleteQuickReply &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDeleteQuickReply.html) - 
* [onUpdateQuickReplyMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateQuickReplyMessage.html) - 
* [onUpdateDeleteQuickReplyMessages &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateDeleteQuickReplyMessages.html) - 
* [onUpdateBotBusinessConnect &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotBusinessConnect.html) - 
* [onUpdateBotNewBusinessMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotNewBusinessMessage.html) - 
* [onUpdateBotEditBusinessMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotEditBusinessMessage.html) - 
* [onUpdateBotDeleteBusinessMessage &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotDeleteBusinessMessage.html) - 
* [onUpdateNewStoryReaction &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateNewStoryReaction.html) - 
* [onUpdateBroadcastRevenueTransactions &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBroadcastRevenueTransactions.html) - 
* [onUpdateStarsBalance &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStarsBalance.html) - 
* [onUpdateBusinessBotCallbackQuery &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBusinessBotCallbackQuery.html) - 
* [onUpdateStarsRevenueStatus &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateStarsRevenueStatus.html) - 
* [onUpdateBotPurchasedPaidMedia &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updateBotPurchasedPaidMedia.html) - 
* [onUpdatePaidReactionPrivacy &raquo;](https://docs.madelineproto.xyz/API_docs/constructors/updatePaidReactionPrivacy.html) - 


<!-- cut_here_end mtprotofilters -->

<a href="https://docs.madelineproto.xyz/docs/PLUGINS.html">Next section</a>
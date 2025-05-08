---
title: Updates
description: constructors and methods of type Updates
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: Updates
[Back to types index](index.html)

You can use the following methods to extract information from this constructor:

```php
// Extract an array of Update constructors
$vector_of_update = $MadelineProto->extractUpdates($Updates);

// Extract an updateNewMessage, updateNewChannelMessage, updateEditMessage, updateEditChannelMessage constructor
$message_update = $MadelineProto->extractMessageUpdate($Updates);

// Extract a message constructor
$message = $MadelineProto->extractMessage($Updates);

// Extract a message ID
$message = $MadelineProto->extractMessageId($Updates);
```


### Possible values (constructors):

[updatesTooLong](/API_docs/constructors/updatesTooLong.html)  

[updateShortMessage](/API_docs/constructors/updateShortMessage.html)  

[updateShortChatMessage](/API_docs/constructors/updateShortChatMessage.html)  

[updateShort](/API_docs/constructors/updateShort.html)  

[updatesCombined](/API_docs/constructors/updatesCombined.html)  

[updates](/API_docs/constructors/updates.html)  

[updateShortSentMessage](/API_docs/constructors/updateShortSentMessage.html)  



### Methods that return an object of this type (methods):

[$MadelineProto->account->getNotifyExceptions](/API_docs/methods/account.getNotifyExceptions.html)  

[$MadelineProto->account->updateConnectedBot](/API_docs/methods/account.updateConnectedBot.html)  

[$MadelineProto->account->getBotBusinessConnection](/API_docs/methods/account.getBotBusinessConnection.html)  

[$MadelineProto->contacts->deleteContacts](/API_docs/methods/contacts.deleteContacts.html)  

[$MadelineProto->contacts->addContact](/API_docs/methods/contacts.addContact.html)  

[$MadelineProto->contacts->acceptContact](/API_docs/methods/contacts.acceptContact.html)  

[$MadelineProto->contacts->getLocated](/API_docs/methods/contacts.getLocated.html)  

[$MadelineProto->contacts->blockFromReplies](/API_docs/methods/contacts.blockFromReplies.html)  

[$MadelineProto->messages->sendMessage](/API_docs/methods/messages.sendMessage.html)  

[$MadelineProto->messages->sendMedia](/API_docs/methods/messages.sendMedia.html)  

[$MadelineProto->messages->forwardMessages](/API_docs/methods/messages.forwardMessages.html)  

[$MadelineProto->messages->editChatTitle](/API_docs/methods/messages.editChatTitle.html)  

[$MadelineProto->messages->editChatPhoto](/API_docs/methods/messages.editChatPhoto.html)  

[$MadelineProto->messages->deleteChatUser](/API_docs/methods/messages.deleteChatUser.html)  

[$MadelineProto->messages->importChatInvite](/API_docs/methods/messages.importChatInvite.html)  

[$MadelineProto->messages->startBot](/API_docs/methods/messages.startBot.html)  

[$MadelineProto->messages->migrateChat](/API_docs/methods/messages.migrateChat.html)  

[$MadelineProto->messages->sendInlineBotResult](/API_docs/methods/messages.sendInlineBotResult.html)  

[$MadelineProto->messages->editMessage](/API_docs/methods/messages.editMessage.html)  

[$MadelineProto->messages->getAllDrafts](/API_docs/methods/messages.getAllDrafts.html)  

[$MadelineProto->messages->setGameScore](/API_docs/methods/messages.setGameScore.html)  

[$MadelineProto->messages->sendScreenshotNotification](/API_docs/methods/messages.sendScreenshotNotification.html)  

[$MadelineProto->messages->sendMultiMedia](/API_docs/methods/messages.sendMultiMedia.html)  

[$MadelineProto->messages->updatePinnedMessage](/API_docs/methods/messages.updatePinnedMessage.html)  

[$MadelineProto->messages->sendVote](/API_docs/methods/messages.sendVote.html)  

[$MadelineProto->messages->getPollResults](/API_docs/methods/messages.getPollResults.html)  

[$MadelineProto->messages->editChatDefaultBannedRights](/API_docs/methods/messages.editChatDefaultBannedRights.html)  

[$MadelineProto->messages->sendScheduledMessages](/API_docs/methods/messages.sendScheduledMessages.html)  

[$MadelineProto->messages->deleteScheduledMessages](/API_docs/methods/messages.deleteScheduledMessages.html)  

[$MadelineProto->messages->setHistoryTTL](/API_docs/methods/messages.setHistoryTTL.html)  

[$MadelineProto->messages->setChatTheme](/API_docs/methods/messages.setChatTheme.html)  

[$MadelineProto->messages->hideChatJoinRequest](/API_docs/methods/messages.hideChatJoinRequest.html)  

[$MadelineProto->messages->hideAllChatJoinRequests](/API_docs/methods/messages.hideAllChatJoinRequests.html)  

[$MadelineProto->messages->toggleNoForwards](/API_docs/methods/messages.toggleNoForwards.html)  

[$MadelineProto->messages->sendReaction](/API_docs/methods/messages.sendReaction.html)  

[$MadelineProto->messages->getMessagesReactions](/API_docs/methods/messages.getMessagesReactions.html)  

[$MadelineProto->messages->setChatAvailableReactions](/API_docs/methods/messages.setChatAvailableReactions.html)  

[$MadelineProto->messages->sendWebViewData](/API_docs/methods/messages.sendWebViewData.html)  

[$MadelineProto->messages->getExtendedMedia](/API_docs/methods/messages.getExtendedMedia.html)  

[$MadelineProto->messages->sendBotRequestedPeer](/API_docs/methods/messages.sendBotRequestedPeer.html)  

[$MadelineProto->messages->setChatWallPaper](/API_docs/methods/messages.setChatWallPaper.html)  

[$MadelineProto->messages->sendQuickReplyMessages](/API_docs/methods/messages.sendQuickReplyMessages.html)  

[$MadelineProto->messages->deleteQuickReplyMessages](/API_docs/methods/messages.deleteQuickReplyMessages.html)  

[$MadelineProto->messages->editFactCheck](/API_docs/methods/messages.editFactCheck.html)  

[$MadelineProto->messages->deleteFactCheck](/API_docs/methods/messages.deleteFactCheck.html)  

[$MadelineProto->messages->sendPaidReaction](/API_docs/methods/messages.sendPaidReaction.html)  

[$MadelineProto->messages->getPaidReactionPrivacy](/API_docs/methods/messages.getPaidReactionPrivacy.html)  

[$MadelineProto->channels->createChannel](/API_docs/methods/channels.createChannel.html)  

[$MadelineProto->channels->editAdmin](/API_docs/methods/channels.editAdmin.html)  

[$MadelineProto->channels->editTitle](/API_docs/methods/channels.editTitle.html)  

[$MadelineProto->channels->editPhoto](/API_docs/methods/channels.editPhoto.html)  

[$MadelineProto->channels->joinChannel](/API_docs/methods/channels.joinChannel.html)  

[$MadelineProto->channels->leaveChannel](/API_docs/methods/channels.leaveChannel.html)  

[$MadelineProto->channels->deleteChannel](/API_docs/methods/channels.deleteChannel.html)  

[$MadelineProto->channels->toggleSignatures](/API_docs/methods/channels.toggleSignatures.html)  

[$MadelineProto->channels->editBanned](/API_docs/methods/channels.editBanned.html)  

[$MadelineProto->channels->deleteHistory](/API_docs/methods/channels.deleteHistory.html)  

[$MadelineProto->channels->togglePreHistoryHidden](/API_docs/methods/channels.togglePreHistoryHidden.html)  

[$MadelineProto->channels->editCreator](/API_docs/methods/channels.editCreator.html)  

[$MadelineProto->channels->toggleSlowMode](/API_docs/methods/channels.toggleSlowMode.html)  

[$MadelineProto->channels->convertToGigagroup](/API_docs/methods/channels.convertToGigagroup.html)  

[$MadelineProto->channels->toggleJoinToSend](/API_docs/methods/channels.toggleJoinToSend.html)  

[$MadelineProto->channels->toggleJoinRequest](/API_docs/methods/channels.toggleJoinRequest.html)  

[$MadelineProto->channels->toggleForum](/API_docs/methods/channels.toggleForum.html)  

[$MadelineProto->channels->createForumTopic](/API_docs/methods/channels.createForumTopic.html)  

[$MadelineProto->channels->editForumTopic](/API_docs/methods/channels.editForumTopic.html)  

[$MadelineProto->channels->updatePinnedForumTopic](/API_docs/methods/channels.updatePinnedForumTopic.html)  

[$MadelineProto->channels->reorderPinnedForumTopics](/API_docs/methods/channels.reorderPinnedForumTopics.html)  

[$MadelineProto->channels->toggleAntiSpam](/API_docs/methods/channels.toggleAntiSpam.html)  

[$MadelineProto->channels->toggleParticipantsHidden](/API_docs/methods/channels.toggleParticipantsHidden.html)  

[$MadelineProto->channels->updateColor](/API_docs/methods/channels.updateColor.html)  

[$MadelineProto->channels->toggleViewForumAsMessages](/API_docs/methods/channels.toggleViewForumAsMessages.html)  

[$MadelineProto->channels->updateEmojiStatus](/API_docs/methods/channels.updateEmojiStatus.html)  

[$MadelineProto->channels->setBoostsToUnblockRestrictions](/API_docs/methods/channels.setBoostsToUnblockRestrictions.html)  

[$MadelineProto->channels->restrictSponsoredMessages](/API_docs/methods/channels.restrictSponsoredMessages.html)  

[$MadelineProto->channels->updatePaidMessagesPrice](/API_docs/methods/channels.updatePaidMessagesPrice.html)  

[$MadelineProto->channels->toggleAutotranslation](/API_docs/methods/channels.toggleAutotranslation.html)  

[$MadelineProto->bots->allowSendMessage](/API_docs/methods/bots.allowSendMessage.html)  

[$MadelineProto->payments->assignAppStoreTransaction](/API_docs/methods/payments.assignAppStoreTransaction.html)  

[$MadelineProto->payments->assignPlayMarketTransaction](/API_docs/methods/payments.assignPlayMarketTransaction.html)  

[$MadelineProto->payments->applyGiftCode](/API_docs/methods/payments.applyGiftCode.html)  

[$MadelineProto->payments->launchPrepaidGiveaway](/API_docs/methods/payments.launchPrepaidGiveaway.html)  

[$MadelineProto->payments->refundStarsCharge](/API_docs/methods/payments.refundStarsCharge.html)  

[$MadelineProto->payments->upgradeStarGift](/API_docs/methods/payments.upgradeStarGift.html)  

[$MadelineProto->payments->transferStarGift](/API_docs/methods/payments.transferStarGift.html)  

[$MadelineProto->payments->updateStarGiftPrice](/API_docs/methods/payments.updateStarGiftPrice.html)  

[$MadelineProto->phone->discardCall](/API_docs/methods/phone.discardCall.html)  

[$MadelineProto->phone->setCallRating](/API_docs/methods/phone.setCallRating.html)  

[$MadelineProto->phone->createGroupCall](/API_docs/methods/phone.createGroupCall.html)  

[$MadelineProto->phone->joinGroupCall](/API_docs/methods/phone.joinGroupCall.html)  

[$MadelineProto->phone->leaveGroupCall](/API_docs/methods/phone.leaveGroupCall.html)  

[$MadelineProto->phone->inviteToGroupCall](/API_docs/methods/phone.inviteToGroupCall.html)  

[$MadelineProto->phone->discardGroupCall](/API_docs/methods/phone.discardGroupCall.html)  

[$MadelineProto->phone->toggleGroupCallSettings](/API_docs/methods/phone.toggleGroupCallSettings.html)  

[$MadelineProto->phone->toggleGroupCallRecord](/API_docs/methods/phone.toggleGroupCallRecord.html)  

[$MadelineProto->phone->editGroupCallParticipant](/API_docs/methods/phone.editGroupCallParticipant.html)  

[$MadelineProto->phone->editGroupCallTitle](/API_docs/methods/phone.editGroupCallTitle.html)  

[$MadelineProto->phone->toggleGroupCallStartSubscription](/API_docs/methods/phone.toggleGroupCallStartSubscription.html)  

[$MadelineProto->phone->startScheduledGroupCall](/API_docs/methods/phone.startScheduledGroupCall.html)  

[$MadelineProto->phone->joinGroupCallPresentation](/API_docs/methods/phone.joinGroupCallPresentation.html)  

[$MadelineProto->phone->leaveGroupCallPresentation](/API_docs/methods/phone.leaveGroupCallPresentation.html)  

[$MadelineProto->phone->createConferenceCall](/API_docs/methods/phone.createConferenceCall.html)  

[$MadelineProto->phone->deleteConferenceCallParticipants](/API_docs/methods/phone.deleteConferenceCallParticipants.html)  

[$MadelineProto->phone->sendConferenceCallBroadcast](/API_docs/methods/phone.sendConferenceCallBroadcast.html)  

[$MadelineProto->phone->inviteConferenceCallParticipant](/API_docs/methods/phone.inviteConferenceCallParticipant.html)  

[$MadelineProto->phone->declineConferenceCallInvite](/API_docs/methods/phone.declineConferenceCallInvite.html)  

[$MadelineProto->phone->getGroupCallChainBlocks](/API_docs/methods/phone.getGroupCallChainBlocks.html)  

[$MadelineProto->folders->editPeerFolders](/API_docs/methods/folders.editPeerFolders.html)  

[$MadelineProto->chatlists->joinChatlistInvite](/API_docs/methods/chatlists.joinChatlistInvite.html)  

[$MadelineProto->chatlists->joinChatlistUpdates](/API_docs/methods/chatlists.joinChatlistUpdates.html)  

[$MadelineProto->chatlists->leaveChatlist](/API_docs/methods/chatlists.leaveChatlist.html)  

[$MadelineProto->stories->sendStory](/API_docs/methods/stories.sendStory.html)  

[$MadelineProto->stories->editStory](/API_docs/methods/stories.editStory.html)  

[$MadelineProto->stories->activateStealthMode](/API_docs/methods/stories.activateStealthMode.html)  

[$MadelineProto->stories->sendReaction](/API_docs/methods/stories.sendReaction.html)  

[$MadelineProto->stories->getAllReadPeerStories](/API_docs/methods/stories.getAllReadPeerStories.html)  




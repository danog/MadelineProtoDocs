---
title: Methods
description: What do you want to do?
parent: "Telegram RPC API"
has_children: true
nav_order: 3
has_toc: false
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# What do you want to do?  
[Go back to API documentation index](..)  

[Go to the old code-version method index](api_index.html)  

* [Logout](https://docs.madelineproto.xyz/logout.html)

* [Login](https://docs.madelineproto.xyz/docs/LOGIN.html)

* [Change 2FA password](https://docs.madelineproto.xyz/update2fa.html)

* [Get all chats, broadcast a message to all chats](https://docs.madelineproto.xyz/docs/DIALOGS.html)

* [Get the full participant list of a channel/group/supergroup](https://docs.madelineproto.xyz/getPwrChat.html)

* [Get full info about a user/chat/supergroup/channel](https://docs.madelineproto.xyz/getFullInfo.html)

* [Get info about a user/chat/supergroup/channel](https://docs.madelineproto.xyz/getInfo.html)

* [Get info about the currently logged-in user](https://docs.madelineproto.xyz/getSelf.html)

* [Upload or download files up to 2 GB](https://docs.madelineproto.xyz/docs/FILES.html)

* [Make a phone call and play a song](https://docs.madelineproto.xyz/docs/CALLS.html)

* [Create a secret chat bot](https://docs.madelineproto.xyz/docs/SECRET_CHATS.html)

* <a href="account.declinePasswordReset.html" name="account.declinePasswordReset">Abort a pending 2FA password reset, see here for more info »: account.declinePasswordReset</a>

* <a href="auth.acceptLoginToken.html" name="auth.acceptLoginToken">Accept QR code login token, logging in the app that generated it: auth.acceptLoginToken</a>

* <a href="help.acceptTermsOfService.html" name="help.acceptTermsOfService">Accept the new terms of service: help.acceptTermsOfService</a>

* <a href="messages.saveGif.html" name="messages.saveGif">Add GIF to saved gifs list: messages.saveGif</a>

* <a href="stickers.addStickerToSet.html" name="stickers.addStickerToSet">Add a sticker to a stickerset, bots only. The sticker set must have been created by the bot: stickers.addStickerToSet</a>

* <a href="contacts.addContact.html" name="contacts.addContact">Add an existing telegram user as contact: contacts.addContact</a>

* <a href="messages.saveRecentSticker.html" name="messages.saveRecentSticker">Add/remove sticker from recent stickers list: messages.saveRecentSticker</a>

* <a href="messages.addChatUser.html" name="messages.addChatUser">Adds a user to a chat and sends a service message on it: messages.addChatUser</a>

* <a href="contacts.block.html" name="contacts.block">Adds the user to the blacklist: contacts.block</a>

* <a href="messages.setInlineBotResults.html" name="messages.setInlineBotResults">Answer an inline query, for bots only: messages.setInlineBotResults</a>

* <a href="bots.answerWebhookJSONQuery.html" name="bots.answerWebhookJSONQuery">Answers a custom query; for bots only: bots.answerWebhookJSONQuery</a>

* <a href="messages.toggleStickerSets.html" name="messages.toggleStickerSets">Apply changes to multiple stickersets: messages.toggleStickerSets</a>

* <a href="channels.setDiscussionGroup.html" name="channels.setDiscussionGroup">Associate a group to a channel as discussion group for that channel: channels.setDiscussionGroup</a>

* <a href="channels.setStickers.html" name="channels.setStickers">Associate a stickerset to the supergroup: channels.setStickers</a>

* <a href="channels.editBanned.html" name="channels.editBanned">Ban/unban/kick a user in a supergroup/channel: channels.editBanned</a>

* <a href="account.cancelPasswordEmail.html" name="account.cancelPasswordEmail">Cancel the code that was sent to verify an email to use as 2FA recovery method: account.cancelPasswordEmail</a>

* <a href="auth.cancelCode.html" name="auth.cancelCode">Cancel the login verification code: auth.cancelCode</a>

* <a href="account.changeAuthorizationSettings.html" name="account.changeAuthorizationSettings">Change authorization settings: account.changeAuthorizationSettings</a>

* <a href="messages.setDefaultReaction.html" name="messages.setDefaultReaction">Change default emoji reaction to use in the quick reaction menu: the value is synced across devices and can be fetched using help.getAppConfig, reactions_default field: messages.setDefaultReaction</a>

* <a href="phone.toggleGroupCallSettings.html" name="phone.toggleGroupCallSettings">Change group call settings: phone.toggleGroupCallSettings</a>

* <a href="account.saveAutoDownloadSettings.html" name="account.saveAutoDownloadSettings">Change media autodownload settings: account.saveAutoDownloadSettings</a>

* <a href="account.setPrivacy.html" name="account.setPrivacy">Change privacy settings of current account: account.setPrivacy</a>

* <a href="messages.setChatTheme.html" name="messages.setChatTheme">Change the chat theme of a certain chat: messages.setChatTheme</a>

* <a href="messages.saveDefaultSendAs.html" name="messages.saveDefaultSendAs">Change the default peer that should be used when sending messages to a specific group: messages.saveDefaultSendAs</a>

* <a href="account.changePhone.html" name="account.changePhone">Change the phone number of the current account: account.changePhone</a>

* <a href="channels.editPhoto.html" name="channels.editPhoto">Change the photo of a channel/supergroup: channels.editPhoto</a>

* <a href="messages.setChatAvailableReactions.html" name="messages.setChatAvailableReactions">Change the set of message reactions » that can be used in a certain group, supergroup or channel: messages.setChatAvailableReactions</a>

* <a href="channels.updateUsername.html" name="channels.updateUsername">Change the username of a supergroup/channel: channels.updateUsername</a>

* <a href="messages.editChatTitle.html" name="messages.editChatTitle">Changes chat name and sends a service message on it: messages.editChatTitle</a>

* <a href="messages.editChatPhoto.html" name="messages.editChatPhoto">Changes chat photo and sends a service message on it: messages.editChatPhoto</a>

* <a href="stickers.changeStickerPosition.html" name="stickers.changeStickerPosition">Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot: stickers.changeStickerPosition</a>

* <a href="account.updateUsername.html" name="account.updateUsername">Changes username for the current user: account.updateUsername</a>

* <a href="channels.checkUsername.html" name="channels.checkUsername">Check if a username is free and can be assigned to a channel/supergroup: channels.checkUsername</a>

* <a href="auth.checkRecoveryPassword.html" name="auth.checkRecoveryPassword">Check if the 2FA recovery code sent using auth.requestPasswordRecovery is valid, before passing it to auth.recoverPassword: auth.checkRecoveryPassword</a>

* <a href="messages.checkChatInvite.html" name="messages.checkChatInvite">Check the validity of a chat invite link and get basic info about it: messages.checkChatInvite</a>

* <a href="messages.checkHistoryImportPeer.html" name="messages.checkHistoryImportPeer">Check whether chat history exported from another chat app can be imported into a specific Telegram chat, click here for more info »: messages.checkHistoryImportPeer</a>

* <a href="stickers.checkShortName.html" name="stickers.checkShortName">Check whether the given short name is available: stickers.checkShortName</a>

* <a href="phone.checkGroupCall.html" name="phone.checkGroupCall">Check whether the group call Server Forwarding Unit is currently receiving the streams with the specified WebRTC source IDs: phone.checkGroupCall</a>

* <a href="messages.clearAllDrafts.html" name="messages.clearAllDrafts">Clear all drafts: messages.clearAllDrafts</a>

* <a href="bots.resetBotCommands.html" name="bots.resetBotCommands">Clear bot commands for the specified bot scope and language code: bots.resetBotCommands</a>

* <a href="messages.clearRecentStickers.html" name="messages.clearRecentStickers">Clear recent stickers: messages.clearRecentStickers</a>

* <a href="payments.clearSavedInfo.html" name="payments.clearSavedInfo">Clear saved payment information: payments.clearSavedInfo</a>

* <a href="messages.startHistoryImport.html" name="messages.startHistoryImport">Complete the history import process, importing all messages into the chat.  : messages.startHistoryImport</a>

* <a href="account.confirmPhone.html" name="account.confirmPhone">Confirm a phone number to cancel account deletion, for more info click here »: account.confirmPhone</a>

* <a href="messages.receivedMessages.html" name="messages.receivedMessages">Confirms receipt of messages by a client, cancels PUSH-notification sending: messages.receivedMessages</a>

* <a href="channels.convertToGigagroup.html" name="channels.convertToGigagroup">Convert a supergroup to a gigagroup, when requested by channel suggestions: channels.convertToGigagroup</a>

* <a href="channels.createChannel.html" name="channels.createChannel">Create a supergroup/channel: channels.createChannel</a>

* <a href="phone.createGroupCall.html" name="phone.createGroupCall">Create a group call or livestream: phone.createGroupCall</a>

* <a href="stickers.createStickerSet.html" name="stickers.createStickerSet">Create a stickerset, bots only: stickers.createStickerSet</a>

* <a href="account.createTheme.html" name="account.createTheme">Create a theme: account.createTheme</a>

* <a href="account.uploadWallPaper.html" name="account.uploadWallPaper">Create and upload a new wallpaper: account.uploadWallPaper</a>

* <a href="messages.createChat.html" name="messages.createChat">Creates a new chat: messages.createChat</a>

* <a href="channels.deleteChannel.html" name="channels.deleteChannel">Delete a channel/supergroup: channels.deleteChannel</a>

* <a href="messages.deleteChat.html" name="messages.deleteChat">Delete a chat: messages.deleteChat</a>

* <a href="folders.deleteFolder.html" name="folders.deleteFolder">Delete a peer folder: folders.deleteFolder</a>

* <a href="messages.deleteExportedChatInvite.html" name="messages.deleteExportedChatInvite">Delete a chat invite: messages.deleteExportedChatInvite</a>

* <a href="channels.deleteParticipantHistory.html" name="channels.deleteParticipantHistory">Delete all messages sent by a specific participant of a given supergroup: channels.deleteParticipantHistory</a>

* <a href="messages.deleteRevokedExportedChatInvites.html" name="messages.deleteRevokedExportedChatInvites">Delete all revoked chat invites: messages.deleteRevokedExportedChatInvites</a>

* <a href="auth.dropTempAuthKeys.html" name="auth.dropTempAuthKeys">Delete all temporary authorization keys except for the ones specified: auth.dropTempAuthKeys</a>

* <a href="contacts.deleteByPhones.html" name="contacts.deleteByPhones">Delete contacts by phone number: contacts.deleteByPhones</a>

* <a href="account.resetWallPapers.html" name="account.resetWallPapers">Delete installed wallpapers: account.resetWallPapers</a>

* <a href="channels.deleteMessages.html" name="channels.deleteMessages">Delete messages in a channel/supergroup: channels.deleteMessages</a>

* <a href="contacts.resetSaved.html" name="contacts.resetSaved">Delete saved contacts: contacts.resetSaved</a>

* <a href="messages.deleteScheduledMessages.html" name="messages.deleteScheduledMessages">Delete scheduled messages: messages.deleteScheduledMessages</a>

* <a href="account.deleteSecureValue.html" name="account.deleteSecureValue">Delete stored Telegram Passport documents, for more info see the passport docs »: account.deleteSecureValue</a>

* <a href="messages.deletePhoneCallHistory.html" name="messages.deletePhoneCallHistory">Delete the entire phone call history: messages.deletePhoneCallHistory</a>

* <a href="channels.deleteHistory.html" name="channels.deleteHistory">Delete the history of a supergroup: channels.deleteHistory</a>

* <a href="account.deleteAccount.html" name="account.deleteAccount">Delete the user's account from the telegram servers. Can be used, for example, to delete the account of a user that provided the login code, but forgot the 2FA password and no recovery method is configured: account.deleteAccount</a>

* <a href="account.unregisterDevice.html" name="account.unregisterDevice">Deletes a device by its token, stops sending PUSH-notifications to it: account.unregisterDevice</a>

* <a href="messages.deleteChatUser.html" name="messages.deleteChatUser">Deletes a user from a chat and sends a service message on it: messages.deleteChatUser</a>

* <a href="messages.deleteHistory.html" name="messages.deleteHistory">Deletes communication history: messages.deleteHistory</a>

* <a href="messages.deleteMessages.html" name="messages.deleteMessages">Deletes messages by their identifiers: messages.deleteMessages</a>

* <a href="photos.deletePhotos.html" name="photos.deletePhotos">Deletes profile photos: photos.deletePhotos</a>

* <a href="contacts.deleteContacts.html" name="contacts.deleteContacts">Deletes several contacts from the list: contacts.deleteContacts</a>

* <a href="contacts.unblock.html" name="contacts.unblock">Deletes the user from the blacklist: contacts.unblock</a>

* <a href="help.dismissSuggestion.html" name="help.dismissSuggestion">Dismiss a suggestion, see here for more info »: help.dismissSuggestion</a>

* <a href="messages.hideChatJoinRequest.html" name="messages.hideChatJoinRequest">Dismiss or approve a chat join request related to a specific chat or channel: messages.hideChatJoinRequest</a>

* <a href="messages.hideAllChatJoinRequests.html" name="messages.hideAllChatJoinRequests">Dismiss or approve all join requests related to a specific chat or channel: messages.hideAllChatJoinRequests</a>

* <a href="messages.editExportedChatInvite.html" name="messages.editExportedChatInvite">Edit an exported chat invite: messages.editExportedChatInvite</a>

* <a href="messages.editInlineBotMessage.html" name="messages.editInlineBotMessage">Edit an inline bot message: messages.editInlineBotMessage</a>

* <a href="phone.editGroupCallParticipant.html" name="phone.editGroupCallParticipant">Edit information about a given group call participant: phone.editGroupCallParticipant</a>

* <a href="channels.editLocation.html" name="channels.editLocation">Edit location of geogroup: channels.editLocation</a>

* <a href="messages.editMessage.html" name="messages.editMessage">Edit message: messages.editMessage</a>

* <a href="folders.editPeerFolders.html" name="folders.editPeerFolders">Edit peers in peer folder: folders.editPeerFolders</a>

* <a href="messages.editChatDefaultBannedRights.html" name="messages.editChatDefaultBannedRights">Edit the default banned rights of a channel/supergroup/group: messages.editChatDefaultBannedRights</a>

* <a href="messages.editChatAbout.html" name="messages.editChatAbout">Edit the description of a group/supergroup/channel: messages.editChatAbout</a>

* <a href="channels.editTitle.html" name="channels.editTitle">Edit the name of a channel/supergroup: channels.editTitle</a>

* <a href="phone.editGroupCallTitle.html" name="phone.editGroupCallTitle">Edit the title of a group call or livestream: phone.editGroupCallTitle</a>

* <a href="account.updateNotifySettings.html" name="account.updateNotifySettings">Edits notification settings from a given user/group, from all users/all groups: account.updateNotifySettings</a>

* <a href="messages.toggleNoForwards.html" name="messages.toggleNoForwards">Enable or disable content protection on a channel or chat: messages.toggleNoForwards</a>

* <a href="contacts.toggleTopPeers.html" name="contacts.toggleTopPeers">Enable/disable top peers: contacts.toggleTopPeers</a>

* <a href="channels.toggleSignatures.html" name="channels.toggleSignatures">Enable/disable message signatures in channels: channels.toggleSignatures</a>

* <a href="messages.exportChatInvite.html" name="messages.exportChatInvite">Export an invite link for a chat: messages.exportChatInvite</a>

* <a href="messages.getMessageEditData.html" name="messages.getMessageEditData">Find out if a media message's caption can be edited: messages.getMessageEditData</a>

* <a href="account.finishTakeoutSession.html" name="account.finishTakeoutSession">Finish account takeout session: account.finishTakeoutSession</a>

* <a href="messages.forwardMessages.html" name="messages.forwardMessages">Forwards messages by their IDs: messages.forwardMessages</a>

* <a href="auth.exportLoginToken.html" name="auth.exportLoginToken">Generate a login token, for login via QR code.  : auth.exportLoginToken</a>

* <a href="help.getPromoData.html" name="help.getPromoData">Get MTProxy/Public Service Announcement information: help.getPromoData</a>

* <a href="phone.getGroupCallStreamRtmpUrl.html" name="phone.getGroupCallStreamRtmpUrl">Get RTMP URL and stream key for RTMP livestreams. Can be used even before creating the actual RTMP livestream with phone.createGroupCall (the rtmp_stream flag must be set): phone.getGroupCallStreamRtmpUrl</a>

* <a href="stats.getBroadcastStats.html" name="stats.getBroadcastStats">Get channel statistics: stats.getBroadcastStats</a>

* <a href="channels.getMessages.html" name="channels.getMessages">Get channel/supergroup messages: channels.getMessages</a>

* <a href="channels.getAdminedPublicChannels.html" name="channels.getAdminedPublicChannels">Get channels/supergroups/geogroups we're admin in. Usually called when the user exceeds the limit for owned public channels/supergroups/geogroups, and the user is given the choice to remove one of his channels/supergroups/geogroups: channels.getAdminedPublicChannels</a>

* <a href="messages.getDiscussionMessage.html" name="messages.getDiscussionMessage">Get discussion message from the associated discussion group of a channel to show it on top of the comment section, without actually joining the group: messages.getDiscussionMessage</a>

* <a href="messages.getDialogFilters.html" name="messages.getDialogFilters">Get folders: messages.getDialogFilters</a>

* <a href="messages.getWebPage.html" name="messages.getWebPage">Get instant view page: messages.getWebPage</a>

* <a href="messages.getMessageReactionsList.html" name="messages.getMessageReactionsList">Get message reaction list, along with the sender of each reaction: messages.getMessageReactionsList</a>

* <a href="messages.getMessagesReactions.html" name="messages.getMessagesReactions">Get message reactions »: messages.getMessagesReactions</a>

* <a href="stats.getMessageStats.html" name="stats.getMessageStats">Get message statistics: stats.getMessageStats</a>

* <a href="help.getPassportConfig.html" name="help.getPassportConfig">Get passport configuration: help.getPassportConfig</a>

* <a href="messages.getSuggestedDialogFilters.html" name="messages.getSuggestedDialogFilters">Get suggested folders: messages.getSuggestedDialogFilters</a>

* <a href="stats.getMegagroupStats.html" name="stats.getMegagroupStats">Get supergroup statistics: stats.getMegagroupStats</a>

* <a href="messages.getDocumentByHash.html" name="messages.getDocumentByHash">Get a document by its SHA256 hash, mainly used for gifs: messages.getDocumentByHash</a>

* <a href="channels.getLeftChannels.html" name="channels.getLeftChannels">Get a list of channels/supergroups we left: channels.getLeftChannels</a>

* <a href="phone.getGroupCallJoinAs.html" name="phone.getGroupCallJoinAs">Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel: phone.getGroupCallJoinAs</a>

* <a href="channels.getSponsoredMessages.html" name="channels.getSponsoredMessages">Get a list of sponsored messages: channels.getSponsoredMessages</a>

* <a href="payments.getPaymentForm.html" name="payments.getPaymentForm">Get a payment form: payments.getPaymentForm</a>

* <a href="messages.getArchivedStickers.html" name="messages.getArchivedStickers">Get all archived stickers: messages.getArchivedStickers</a>

* <a href="account.getChatThemes.html" name="account.getChatThemes">Get all available chat themes: account.getChatThemes</a>

* <a href="messages.getAllChats.html" name="messages.getAllChats">Get all chats, channels and supergroups: messages.getAllChats</a>

* <a href="contacts.getSaved.html" name="contacts.getSaved">Get all contacts: contacts.getSaved</a>

* <a href="channels.getGroupsForDiscussion.html" name="channels.getGroupsForDiscussion">Get all groups that can be used as discussion groups: channels.getGroupsForDiscussion</a>

* <a href="messages.getAllStickers.html" name="messages.getAllStickers">Get all installed stickers: messages.getAllStickers</a>

* <a href="account.getAllSecureValues.html" name="account.getAllSecureValues">Get all saved Telegram Passport documents, for more info see the passport docs »: account.getAllSecureValues</a>

* <a href="phone.exportGroupCallInvite.html" name="phone.exportGroupCallInvite">Get an invite link for a group call or livestream: phone.exportGroupCallInvite</a>

* <a href="messages.getMessagesViews.html" name="messages.getMessagesViews">Get and increase the view counter of a message sent or forwarded from a channel: messages.getMessagesViews</a>

* <a href="help.getAppConfig.html" name="help.getAppConfig">Get app-specific configuration, see client configuration for more info on the result: help.getAppConfig</a>

* <a href="messages.getEmojiKeywordsDifference.html" name="messages.getEmojiKeywordsDifference">Get changed emoji keywords: messages.getEmojiKeywordsDifference</a>

* <a href="help.getAppChangelog.html" name="help.getAppChangelog">Get changelog of current app.  : help.getAppChangelog</a>

* <a href="messages.getCommonChats.html" name="messages.getCommonChats">Get chats in common with a user: messages.getCommonChats</a>

* <a href="help.getCdnConfig.html" name="help.getCdnConfig">Get configuration for CDN file downloads: help.getCdnConfig</a>

* <a href="contacts.getContactIDs.html" name="contacts.getContactIDs">Get contact by telegram IDs: contacts.getContactIDs</a>

* <a href="contacts.getLocated.html" name="contacts.getLocated">Get contacts near you: contacts.getLocated</a>

* <a href="messages.getOnlines.html" name="messages.getOnlines">Get count of online users in a chat: messages.getOnlines</a>

* <a href="account.getAccountTTL.html" name="account.getAccountTTL">Get days to live of account: account.getAccountTTL</a>

* <a href="messages.getPeerDialogs.html" name="messages.getPeerDialogs">Get dialog info of specified peers: messages.getPeerDialogs</a>

* <a href="messages.getDialogUnreadMarks.html" name="messages.getDialogUnreadMarks">Get dialogs manually marked as unread: messages.getDialogUnreadMarks</a>

* <a href="messages.getFavedStickers.html" name="messages.getFavedStickers">Get faved stickers: messages.getFavedStickers</a>

* <a href="messages.getFeaturedStickers.html" name="messages.getFeaturedStickers">Get featured stickers: messages.getFeaturedStickers</a>

* <a href="account.getGlobalPrivacySettings.html" name="account.getGlobalPrivacySettings">Get global privacy settings: account.getGlobalPrivacySettings</a>

* <a href="phone.getGroupParticipants.html" name="phone.getGroupParticipants">Get group call participants: phone.getGroupParticipants</a>

* <a href="messages.getInlineGameHighScores.html" name="messages.getInlineGameHighScores">Get highscores of a game sent using an inline bot: messages.getInlineGameHighScores</a>

* <a href="messages.getGameHighScores.html" name="messages.getGameHighScores">Get highscores of a game: messages.getGameHighScores</a>

* <a href="channels.getInactiveChannels.html" name="channels.getInactiveChannels">Get inactive channels and supergroups: channels.getInactiveChannels</a>

* <a href="phone.getGroupCallStreamChannels.html" name="phone.getGroupCallStreamChannels">Get info about RTMP streams in a group call or livestream.  : phone.getGroupCallStreamChannels</a>

* <a href="channels.getChannels.html" name="channels.getChannels">Get info about channels/supergroups: channels.getChannels</a>

* <a href="channels.getParticipant.html" name="channels.getParticipant">Get info about a channel/supergroup participant: channels.getParticipant</a>

* <a href="help.getDeepLinkInfo.html" name="help.getDeepLinkInfo">Get info about a t.me link: help.getDeepLinkInfo</a>

* <a href="account.getWallPaper.html" name="account.getWallPaper">Get info about a certain wallpaper: account.getWallPaper</a>

* <a href="messages.getExportedChatInvite.html" name="messages.getExportedChatInvite">Get info about a chat invite: messages.getExportedChatInvite</a>

* <a href="payments.getBankCardData.html" name="payments.getBankCardData">Get info about a credit card: payments.getBankCardData</a>

* <a href="phone.getGroupCall.html" name="phone.getGroupCall">Get info about a group call: phone.getGroupCall</a>

* <a href="messages.getStickerSet.html" name="messages.getStickerSet">Get info about a stickerset: messages.getStickerSet</a>

* <a href="messages.getEmojiKeywordsLanguages.html" name="messages.getEmojiKeywordsLanguages">Get info about an emoji keyword localization: messages.getEmojiKeywordsLanguages</a>

* <a href="messages.getAdminsWithInvites.html" name="messages.getAdminsWithInvites">Get info about chat invites generated by admins: messages.getAdminsWithInvites</a>

* <a href="account.getMultiWallPapers.html" name="account.getMultiWallPapers">Get info about multiple wallpapers: account.getMultiWallPapers</a>

* <a href="messages.getExportedChatInvites.html" name="messages.getExportedChatInvites">Get info about the chat invites of a specific chat: messages.getExportedChatInvites</a>

* <a href="messages.getChatInviteImporters.html" name="messages.getChatInviteImporters">Get info about the users that joined the chat using a specific chat invite: messages.getChatInviteImporters</a>

* <a href="langpack.getLanguage.html" name="langpack.getLanguage">Get information about a language in a localization pack: langpack.getLanguage</a>

* <a href="langpack.getLanguages.html" name="langpack.getLanguages">Get information about all languages in a localization pack: langpack.getLanguages</a>

* <a href="messages.getMaskStickers.html" name="messages.getMaskStickers">Get installed mask stickers: messages.getMaskStickers</a>

* <a href="account.getThemes.html" name="account.getThemes">Get installed themes: account.getThemes</a>

* <a href="channels.exportMessageLink.html" name="channels.exportMessageLink">Get link and embed info of a message in a channel/supergroup: channels.exportMessageLink</a>

* <a href="messages.getRecentLocations.html" name="messages.getRecentLocations">Get live location history of a certain user: messages.getRecentLocations</a>

* <a href="langpack.getLangPack.html" name="langpack.getLangPack">Get localization pack strings: langpack.getLangPack</a>

* <a href="messages.getEmojiKeywords.html" name="messages.getEmojiKeywords">Get localized emoji keywords: messages.getEmojiKeywords</a>

* <a href="help.getSupportName.html" name="help.getSupportName">Get localized name of the telegram support user: help.getSupportName</a>

* <a href="account.getAuthorizations.html" name="account.getAuthorizations">Get logged-in sessions: account.getAuthorizations</a>

* <a href="account.getAutoDownloadSettings.html" name="account.getAutoDownloadSettings">Get media autodownload settings: account.getAutoDownloadSettings</a>

* <a href="messages.getSplitRanges.html" name="messages.getSplitRanges">Get message ranges for saving the user's chat history: messages.getSplitRanges</a>

* <a href="messages.getReplies.html" name="messages.getReplies">Get messages in a reply thread: messages.getReplies</a>

* <a href="messages.requestUrlAuth.html" name="messages.requestUrlAuth">Get more info about a Seamless Telegram Login authorization request, for more info click here »: messages.requestUrlAuth</a>

* <a href="contacts.getTopPeers.html" name="contacts.getTopPeers">Get most used peers: contacts.getTopPeers</a>

* <a href="help.getCountriesList.html" name="help.getCountriesList">Get name, ISO code, localized name and phone codes/patterns of all available countries: help.getCountriesList</a>

* <a href="langpack.getDifference.html" name="langpack.getDifference">Get new strings in language pack: langpack.getDifference</a>

* <a href="payments.getPaymentReceipt.html" name="payments.getPaymentReceipt">Get payment receipt: payments.getPaymentReceipt</a>

* <a href="messages.getPeerSettings.html" name="messages.getPeerSettings">Get peer settings: messages.getPeerSettings</a>

* <a href="phone.getCallConfig.html" name="phone.getCallConfig">Get phone call configuration to be passed to libtgvoip's shared config: phone.getCallConfig</a>

* <a href="messages.getPinnedDialogs.html" name="messages.getPinnedDialogs">Get pinned dialogs: messages.getPinnedDialogs</a>

* <a href="messages.getPollVotes.html" name="messages.getPollVotes">Get poll results for non-anonymous polls: messages.getPollVotes</a>

* <a href="messages.getPollResults.html" name="messages.getPollResults">Get poll results: messages.getPollResults</a>

* <a href="messages.getWebPagePreview.html" name="messages.getWebPagePreview">Get preview of webpage: messages.getWebPagePreview</a>

* <a href="account.getPrivacy.html" name="account.getPrivacy">Get privacy settings of current account: account.getPrivacy</a>

* <a href="messages.getRecentStickers.html" name="messages.getRecentStickers">Get recent stickers: messages.getRecentStickers</a>

* <a href="help.getRecentMeUrls.html" name="help.getRecentMeUrls">Get recently used t.me links: help.getRecentMeUrls</a>

* <a href="messages.getSavedGifs.html" name="messages.getSavedGifs">Get saved GIFs: messages.getSavedGifs</a>

* <a href="account.getSecureValue.html" name="account.getSecureValue">Get saved Telegram Passport document, for more info see the passport docs »: account.getSecureValue</a>

* <a href="payments.getSavedInfo.html" name="payments.getSavedInfo">Get saved payment information: payments.getSavedInfo</a>

* <a href="messages.getScheduledHistory.html" name="messages.getScheduledHistory">Get scheduled messages: messages.getScheduledHistory</a>

* <a href="messages.getScheduledMessages.html" name="messages.getScheduledMessages">Get scheduled messages: messages.getScheduledMessages</a>

* <a href="account.getContentSettings.html" name="account.getContentSettings">Get sensitive content settings: account.getContentSettings</a>

* <a href="messages.getAttachedStickers.html" name="messages.getAttachedStickers">Get stickers attached to a photo or video: messages.getAttachedStickers</a>

* <a href="messages.getStickers.html" name="messages.getStickers">Get stickers by emoji: messages.getStickers</a>

* <a href="langpack.getStrings.html" name="langpack.getStrings">Get strings from a language pack: langpack.getStrings</a>

* <a href="account.getTmpPassword.html" name="account.getTmpPassword">Get temporary payment password: account.getTmpPassword</a>

* <a href="channels.getAdminLog.html" name="channels.getAdminLog">Get the admin log of a channel/supergroup: channels.getAdminLog</a>

* <a href="messages.getSearchCounters.html" name="messages.getSearchCounters">Get the number of results that would be found by a messages.search call with the same parameters: messages.getSearchCounters</a>

* <a href="channels.getParticipants.html" name="channels.getParticipants">Get the participants of a supergroup/channel: channels.getParticipants</a>

* <a href="account.getTheme.html" name="account.getTheme">Get theme information: account.getTheme</a>

* <a href="messages.getUnreadMentions.html" name="messages.getUnreadMentions">Get unread messages where we were mentioned: messages.getUnreadMentions</a>

* <a href="messages.getUnreadReactions.html" name="messages.getUnreadReactions">Get unread reactions to messages you sent: messages.getUnreadReactions</a>

* <a href="account.getWebAuthorizations.html" name="account.getWebAuthorizations">Get web login widget authorizations: account.getWebAuthorizations</a>

* <a href="messages.getMessageReadParticipants.html" name="messages.getMessageReadParticipants">Get which users read a specific message: only available for groups and supergroups with less than chat_read_mark_size_threshold members, read receipts will be stored for chat_read_mark_expire_period seconds after the message was sent, see client configuration for more info »: messages.getMessageReadParticipants</a>

* <a href="messages.search.html" name="messages.search">Gets back found messages: messages.search</a>

* <a href="messages.getHistory.html" name="messages.getHistory">Gets back the conversation history with one interlocutor / within a chat: messages.getHistory</a>

* <a href="account.getNotifySettings.html" name="account.getNotifySettings">Gets current notification settings for a given user/group, from all users/all groups: account.getNotifySettings</a>

* <a href="help.hidePromoData.html" name="help.hidePromoData">Hide MTProxy/Public Service Announcement information: help.hidePromoData</a>

* <a href="channels.togglePreHistoryHidden.html" name="channels.togglePreHistoryHidden">Hide/unhide message history for new channel/supergroup users: channels.togglePreHistoryHidden</a>

* <a href="contacts.acceptContact.html" name="contacts.acceptContact">If the peer settings of a new user allow us to add them as contact, add that user as contact: contacts.acceptContact</a>

* <a href="messages.setBotShippingResults.html" name="messages.setBotShippingResults">If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the bot will receive an updateBotShippingQuery update. Use this method to reply to shipping queries: messages.setBotShippingResults</a>

* <a href="messages.importChatInvite.html" name="messages.importChatInvite">Import a chat invite and join a private chat/supergroup/channel: messages.importChatInvite</a>

* <a href="messages.initHistoryImport.html" name="messages.initHistoryImport">Import chat history from a foreign chat app into a specific Telegram chat, click here for more info about imported chats »: messages.initHistoryImport</a>

* <a href="contacts.importContacts.html" name="contacts.importContacts">Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info: contacts.importContacts</a>

* <a href="help.setBotUpdatesStatus.html" name="help.setBotUpdatesStatus">Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only: help.setBotUpdatesStatus</a>

* <a href="account.initTakeoutSession.html" name="account.initTakeoutSession">Initialize account takeout session: account.initTakeoutSession</a>

* <a href="initConnection.html" name="initConnection">Initialize connection: initConnection</a>

* <a href="account.resetPassword.html" name="account.resetPassword">Initiate a 2FA password reset: can only be used if the user is already logged-in, see here for more info »: account.resetPassword</a>

* <a href="messages.installStickerSet.html" name="messages.installStickerSet">Install a stickerset: messages.installStickerSet</a>

* <a href="account.installTheme.html" name="account.installTheme">Install a theme: account.installTheme</a>

* <a href="account.installWallPaper.html" name="account.installWallPaper">Install wallpaper: account.installWallPaper</a>

* <a href="account.saveWallPaper.html" name="account.saveWallPaper">Install/uninstall wallpaper: account.saveWallPaper</a>

* <a href="photos.updateProfilePhoto.html" name="photos.updateProfilePhoto">Installs a previously uploaded photo as a profile photo: photos.updateProfilePhoto</a>

* <a href="help.editUserInfo.html" name="help.editUserInfo">Internal use: help.editUserInfo</a>

* <a href="help.getUserInfo.html" name="help.getUserInfo">Internal use: help.getUserInfo</a>

* <a href="phone.inviteToGroupCall.html" name="phone.inviteToGroupCall">Invite a set of users to a group call: phone.inviteToGroupCall</a>

* <a href="channels.inviteToChannel.html" name="channels.inviteToChannel">Invite users to a channel/supergroup: channels.inviteToChannel</a>

* <a href="invokeWithTakeout.html" name="invokeWithTakeout">Invoke a method within a takeout session: invokeWithTakeout</a>

* <a href="invokeWithoutUpdates.html" name="invokeWithoutUpdates">Invoke a request without subscribing the used connection for updates (this is enabled by default for file queries): invokeWithoutUpdates</a>

* <a href="invokeWithLayer.html" name="invokeWithLayer">Invoke the specified query using the specified API layer: invokeWithLayer</a>

* <a href="invokeWithMessagesRange.html" name="invokeWithMessagesRange">Invoke with the given message range: invokeWithMessagesRange</a>

* <a href="invokeAfterMsgs.html" name="invokeAfterMsgs">Invokes a query after a successful completion of previous queries: invokeAfterMsgs</a>

* <a href="invokeAfterMsg.html" name="invokeAfterMsg">Invokes a query after successful completion of one of the previous queries: invokeAfterMsg</a>

* <a href="channels.joinChannel.html" name="channels.joinChannel">Join a channel/supergroup: channels.joinChannel</a>

* <a href="phone.joinGroupCall.html" name="phone.joinGroupCall">Join a group call: phone.joinGroupCall</a>

* <a href="channels.leaveChannel.html" name="channels.leaveChannel">Leave a channel/supergroup: channels.leaveChannel</a>

* <a href="phone.leaveGroupCall.html" name="phone.leaveGroupCall">Leave a group call: phone.leaveGroupCall</a>

* <a href="stats.loadAsyncGraph.html" name="stats.loadAsyncGraph">Load channel statistics graph asynchronously: stats.loadAsyncGraph</a>

* <a href="account.resetAuthorization.html" name="account.resetAuthorization">Log out an active authorized session by its hash: account.resetAuthorization</a>

* <a href="account.resetWebAuthorization.html" name="account.resetWebAuthorization">Log out an active web telegram login session: account.resetWebAuthorization</a>

* <a href="auth.importLoginToken.html" name="auth.importLoginToken">Login using a redirected login token, generated in case of DC mismatch during QR code login: auth.importLoginToken</a>

* <a href="help.getTermsOfServiceUpdate.html" name="help.getTermsOfServiceUpdate">Look for updates of telegram's terms of service: help.getTermsOfServiceUpdate</a>

* <a href="messages.editChatAdmin.html" name="messages.editChatAdmin">Make a user admin in a basic group: messages.editChatAdmin</a>

* <a href="messages.markDialogUnread.html" name="messages.markDialogUnread">Manually mark dialog as unread: messages.markDialogUnread</a>

* <a href="channels.readHistory.html" name="channels.readHistory">Mark channel/supergroup history as read: channels.readHistory</a>

* <a href="channels.readMessageContents.html" name="channels.readMessageContents">Mark channel/supergroup message contents as read: channels.readMessageContents</a>

* <a href="messages.readReactions.html" name="messages.readReactions">Mark message reactions » as read: messages.readReactions</a>

* <a href="messages.readDiscussion.html" name="messages.readDiscussion">Mark a thread as read: messages.readDiscussion</a>

* <a href="channels.viewSponsoredMessage.html" name="channels.viewSponsoredMessage">Mark a specific sponsored message as read: channels.viewSponsoredMessage</a>

* <a href="messages.readMentions.html" name="messages.readMentions">Mark mentions as read: messages.readMentions</a>

* <a href="messages.readFeaturedStickers.html" name="messages.readFeaturedStickers">Mark new featured stickers as read: messages.readFeaturedStickers</a>

* <a href="messages.faveSticker.html" name="messages.faveSticker">Mark or unmark a sticker as favorite: messages.faveSticker</a>

* <a href="messages.readHistory.html" name="messages.readHistory">Marks message history as read: messages.readHistory</a>

* <a href="messages.readEncryptedHistory.html" name="messages.readEncryptedHistory">Marks message history within a secret chat as read: messages.readEncryptedHistory</a>

* <a href="messages.getOldFeaturedStickers.html" name="messages.getOldFeaturedStickers">Method for fetching previously featured stickers: messages.getOldFeaturedStickers</a>

* <a href="channels.editAdmin.html" name="channels.editAdmin">Modify the admin rights of a user in a supergroup/channel: channels.editAdmin</a>

* <a href="messages.readMessageContents.html" name="messages.readMessageContents">Notifies the sender about the recipient having listened a voice message or watched a video: messages.readMessageContents</a>

* <a href="messages.sendScreenshotNotification.html" name="messages.sendScreenshotNotification">Notify the other user in a private chat that a screenshot of the chat was taken: messages.sendScreenshotNotification</a>

* <a href="users.setSecureValueErrors.html" name="users.setSecureValueErrors">Notify the user that the sent passport data contains some errors The user will not be able to re-submit their Passport data to you until the errors are fixed (the contents of the field for which you returned the error must change): users.setSecureValueErrors</a>

* <a href="bots.getBotCommands.html" name="bots.getBotCommands">Obtain a list of bot commands for the specified bot scope and language code: bots.getBotCommands</a>

* <a href="messages.getAvailableReactions.html" name="messages.getAvailableReactions">Obtain available message reactions »: messages.getAvailableReactions</a>

* <a href="account.getPassword.html" name="account.getPassword">Obtain configuration for two-factor authorization with password: account.getPassword</a>

* <a href="stats.getMessagePublicForwards.html" name="stats.getMessagePublicForwards">Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  : stats.getMessagePublicForwards</a>

* <a href="channels.getSendAs.html" name="channels.getSendAs">Obtains a list of peers that can be used to send messages in a specific group: channels.getSendAs</a>

* <a href="messages.checkHistoryImport.html" name="messages.checkHistoryImport">Obtains information about a chat export file, generated by a foreign chat app, click here for more info about imported chats »: messages.checkHistoryImport</a>

* <a href="messages.setBotPrecheckoutResults.html" name="messages.setBotPrecheckoutResults">Once the user has confirmed their payment and shipping details, the bot receives an updateBotPrecheckoutQuery update.  : messages.setBotPrecheckoutResults</a>

* <a href="phone.receivedCall.html" name="phone.receivedCall">Optional: notify the server that the user is currently busy in a call: this will automatically refuse all incoming phone calls until the current phone call is ended: phone.receivedCall</a>

* <a href="messages.updatePinnedMessage.html" name="messages.updatePinnedMessage">Pin a message: messages.updatePinnedMessage</a>

* <a href="messages.toggleDialogPin.html" name="messages.toggleDialogPin">Pin/unpin a dialog: messages.toggleDialogPin</a>

* <a href="messages.getBotCallbackAnswer.html" name="messages.getBotCallbackAnswer">Press an inline callback button and get a callback answer from the bot: messages.getBotCallbackAnswer</a>

* <a href="messages.getInlineBotResults.html" name="messages.getInlineBotResults">Query an inline bot: messages.getInlineBotResults</a>

* <a href="phone.setCallRating.html" name="phone.setCallRating">Rate a call: phone.setCallRating</a>

* <a href="messages.sendReaction.html" name="messages.sendReaction">React to message: messages.sendReaction</a>

* <a href="account.registerDevice.html" name="account.registerDevice">Register device to receive PUSH notifications: account.registerDevice</a>

* <a href="stickers.removeStickerFromSet.html" name="stickers.removeStickerFromSet">Remove a sticker from the set where it belongs, bots only. The sticker set must have been created by the bot: stickers.removeStickerFromSet</a>

* <a href="messages.updateDialogFiltersOrder.html" name="messages.updateDialogFiltersOrder">Reorder folders: messages.updateDialogFiltersOrder</a>

* <a href="messages.reorderStickerSets.html" name="messages.reorderStickerSets">Reorder installed stickersets: messages.reorderStickerSets</a>

* <a href="messages.reorderPinnedDialogs.html" name="messages.reorderPinnedDialogs">Reorder pinned dialogs: messages.reorderPinnedDialogs</a>

* <a href="messages.report.html" name="messages.report">Report a message in a chat for violation of telegram's Terms of Service: messages.report</a>

* <a href="messages.reportSpam.html" name="messages.reportSpam">Report a new incoming chat for spam, if the peer settings of the chat allow us to do that: messages.reportSpam</a>

* <a href="account.reportPeer.html" name="account.reportPeer">Report a peer for violation of telegram's Terms of Service: account.reportPeer</a>

* <a href="account.reportProfilePhoto.html" name="account.reportProfilePhoto">Report a profile photo of a dialog: account.reportProfilePhoto</a>

* <a href="messages.reportEncryptedSpam.html" name="messages.reportEncryptedSpam">Report a secret chat for spam: messages.reportEncryptedSpam</a>

* <a href="channels.reportSpam.html" name="channels.reportSpam">Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup: channels.reportSpam</a>

* <a href="auth.requestPasswordRecovery.html" name="auth.requestPasswordRecovery">Request recovery code of a 2FA password, only for accounts with a recovery email configured: auth.requestPasswordRecovery</a>

* <a href="account.resendPasswordEmail.html" name="account.resendPasswordEmail">Resend the code to verify an email to use as 2FA recovery method: account.resendPasswordEmail</a>

* <a href="auth.resendCode.html" name="auth.resendCode">Resend the login code via another medium, the phone code type is determined by the return value of the previous auth.sendCode/auth.resendCode: see login for more info: auth.resendCode</a>

* <a href="contacts.resetTopPeerRating.html" name="contacts.resetTopPeerRating">Reset rating of top peer: contacts.resetTopPeerRating</a>

* <a href="account.resetWebAuthorizations.html" name="account.resetWebAuthorizations">Reset all active web telegram login sessions: account.resetWebAuthorizations</a>

* <a href="auth.recoverPassword.html" name="auth.recoverPassword">Reset the 2FA password using the recovery code sent using auth.requestPasswordRecovery: auth.recoverPassword</a>

* <a href="account.resetNotifySettings.html" name="account.resetNotifySettings">Resets all notification settings from users and groups: account.resetNotifySettings</a>

* <a href="contacts.resolvePhone.html" name="contacts.resolvePhone">Resolve a phone number to get user info, if their privacy settings allow it: contacts.resolvePhone</a>

* <a href="account.getAuthorizationForm.html" name="account.getAuthorizationForm">Returns a Telegram Passport authorization form for sharing data with a service: account.getAuthorizationForm</a>

* <a href="account.getWallPapers.html" name="account.getWallPapers">Returns a list of available wallpapers: account.getWallPapers</a>

* <a href="messages.getEmojiURL.html" name="messages.getEmojiURL">Returns an HTTP URL which can be used to automatically log in into translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation: messages.getEmojiURL</a>

* <a href="users.getUsers.html" name="users.getUsers">Returns basic user info according to their identifiers: users.getUsers</a>

* <a href="messages.getChats.html" name="messages.getChats">Returns chat basic info on their IDs: messages.getChats</a>

* <a href="upload.getWebFile.html" name="upload.getWebFile">Returns content of an HTTP file or a part, by proxying the request through telegram: upload.getWebFile</a>

* <a href="help.getConfig.html" name="help.getConfig">Returns current configuration, including data center configuration: help.getConfig</a>

* <a href="help.getNearestDc.html" name="help.getNearestDc">Returns info on data center nearest to the user: help.getNearestDc</a>

* <a href="messages.getSearchResultsCalendar.html" name="messages.getSearchResultsCalendar">Returns information about the next messages of the specified type in the chat split by days: messages.getSearchResultsCalendar</a>

* <a href="help.getAppUpdate.html" name="help.getAppUpdate">Returns information on update availability for the current application: help.getAppUpdate</a>

* <a href="account.getNotifyExceptions.html" name="account.getNotifyExceptions">Returns list of chats with non-default notification settings: account.getNotifyExceptions</a>

* <a href="help.getInviteText.html" name="help.getInviteText">Returns localized text of a text message with an invitation: help.getInviteText</a>

* <a href="messages.getSearchResultsPositions.html" name="messages.getSearchResultsPositions">Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation: messages.getSearchResultsPositions</a>

* <a href="messages.getDialogs.html" name="messages.getDialogs">Returns the current user dialog list: messages.getDialogs</a>

* <a href="contacts.getContacts.html" name="contacts.getContacts">Returns the current user's contact list: contacts.getContacts</a>

* <a href="contacts.getBlocked.html" name="contacts.getBlocked">Returns the list of blocked users: contacts.getBlocked</a>

* <a href="contacts.getStatuses.html" name="contacts.getStatuses">Returns the list of contact statuses: contacts.getStatuses</a>

* <a href="messages.getMessages.html" name="messages.getMessages">Returns the list of messages by their IDs: messages.getMessages</a>

* <a href="photos.getUserPhotos.html" name="photos.getUserPhotos">Returns the list of user photos: photos.getUserPhotos</a>

* <a href="help.getSupport.html" name="help.getSupport">Returns the support user for the "ask a question" feature: help.getSupport</a>

* <a href="contacts.search.html" name="contacts.search">Returns users found by username substring: contacts.search</a>

* <a href="messages.saveDraft.html" name="messages.saveDraft">Save a message draft associated to a chat: messages.saveDraft</a>

* <a href="account.saveTheme.html" name="account.saveTheme">Save a theme: account.saveTheme</a>

* <a href="messages.getAllDrafts.html" name="messages.getAllDrafts">Save get all message drafts: messages.getAllDrafts</a>

* <a href="help.saveAppLog.html" name="help.saveAppLog">Saves logs of application on the server: help.saveAppLog</a>

* <a href="messages.searchGlobal.html" name="messages.searchGlobal">Search for messages and peers globally: messages.searchGlobal</a>

* <a href="messages.searchStickerSets.html" name="messages.searchStickerSets">Search for stickersets: messages.searchStickerSets</a>

* <a href="account.saveSecureValue.html" name="account.saveSecureValue">Securely save Telegram Passport document, for more info see the passport docs »: account.saveSecureValue</a>

* <a href="phone.sendSignalingData.html" name="phone.sendSignalingData">Send VoIP signaling data: phone.sendSignalingData</a>

* <a href="messages.sendMedia.html" name="messages.sendMedia">Send a media: messages.sendMedia</a>

* <a href="messages.sendInlineBotResult.html" name="messages.sendInlineBotResult">Send a result obtained using messages.getInlineBotResults: messages.sendInlineBotResult</a>

* <a href="messages.sendMultiMedia.html" name="messages.sendMultiMedia">Send an album or grouped media: messages.sendMultiMedia</a>

* <a href="payments.sendPaymentForm.html" name="payments.sendPaymentForm">Send compiled payment form: payments.sendPaymentForm</a>

* <a href="account.sendConfirmPhoneCode.html" name="account.sendConfirmPhoneCode">Send confirmation code to cancel account deletion, for more info click here »: account.sendConfirmPhoneCode</a>

* <a href="phone.saveCallDebug.html" name="phone.saveCallDebug">Send phone call debug data to server: phone.saveCallDebug</a>

* <a href="messages.sendScheduledMessages.html" name="messages.sendScheduledMessages">Send scheduled messages right away: messages.sendScheduledMessages</a>

* <a href="account.sendVerifyEmailCode.html" name="account.sendVerifyEmailCode">Send the verification email code for telegram passport: account.sendVerifyEmailCode</a>

* <a href="account.sendVerifyPhoneCode.html" name="account.sendVerifyPhoneCode">Send the verification phone code for telegram passport: account.sendVerifyPhoneCode</a>

* <a href="messages.setEncryptedTyping.html" name="messages.setEncryptedTyping">Send typing event by the current user to a secret chat: messages.setEncryptedTyping</a>

* <a href="account.acceptAuthorization.html" name="account.acceptAuthorization">Sends a Telegram Passport authorization form, effectively sharing data with the service: account.acceptAuthorization</a>

* <a href="messages.setTyping.html" name="messages.setTyping">Sends a current user typing event (see SendMessageAction for all event types) to a conversation partner or group: messages.setTyping</a>

* <a href="bots.sendCustomRequest.html" name="bots.sendCustomRequest">Sends a custom request; for bots only: bots.sendCustomRequest</a>

* <a href="messages.sendMessage.html" name="messages.sendMessage">Sends a message to a chat: messages.sendMessage</a>

* <a href="messages.sendEncryptedFile.html" name="messages.sendEncryptedFile">Sends a message with a file attachment to a secret chat: messages.sendEncryptedFile</a>

* <a href="messages.sendEncryptedService.html" name="messages.sendEncryptedService">Sends a service message to a secret chat: messages.sendEncryptedService</a>

* <a href="messages.sendEncrypted.html" name="messages.sendEncrypted">Sends a text message to a secret chat: messages.sendEncrypted</a>

* <a href="account.setAccountTTL.html" name="account.setAccountTTL">Set account self-destruction period: account.setAccountTTL</a>

* <a href="bots.setBotCommands.html" name="bots.setBotCommands">Set bot command list: bots.setBotCommands</a>

* <a href="account.setGlobalPrivacySettings.html" name="account.setGlobalPrivacySettings">Set global privacy settings: account.setGlobalPrivacySettings</a>

* <a href="messages.setHistoryTTL.html" name="messages.setHistoryTTL">Set maximum Time-To-Live of all messages in the specified chat: messages.setHistoryTTL</a>

* <a href="account.setContentSettings.html" name="account.setContentSettings">Set sensitive content settings (for viewing or hiding NSFW content): account.setContentSettings</a>

* <a href="stickers.setStickerSetThumb.html" name="stickers.setStickerSetThumb">Set stickerset thumbnail: stickers.setStickerSetThumb</a>

* <a href="messages.setBotCallbackAnswer.html" name="messages.setBotCallbackAnswer">Set the callback answer to a user button press (bots only): messages.setBotCallbackAnswer</a>

* <a href="phone.saveDefaultGroupCallJoinAs.html" name="phone.saveDefaultGroupCallJoinAs">Set the default peer that will be used to join a group call in a specific dialog: phone.saveDefaultGroupCallJoinAs</a>

* <a href="account.setAuthorizationTTL.html" name="account.setAuthorizationTTL">Set time-to-live of current session: account.setAuthorizationTTL</a>

* <a href="messages.hidePeerSettingsBar.html" name="messages.hidePeerSettingsBar">Should be called after the user hides the report spam/add as contact bar of a new chat, effectively prevents the user from executing the actions specified in the peer's settings: messages.hidePeerSettingsBar</a>

* <a href="messages.startBot.html" name="messages.startBot">Start a conversation with a bot using a deep linking parameter: messages.startBot</a>

* <a href="phone.startScheduledGroupCall.html" name="phone.startScheduledGroupCall">Start a scheduled group call: phone.startScheduledGroupCall</a>

* <a href="phone.toggleGroupCallRecord.html" name="phone.toggleGroupCallRecord">Start or stop recording a group call: the recorded audio and video streams will be automatically sent to Saved messages (the chat with ourselves): phone.toggleGroupCallRecord</a>

* <a href="phone.joinGroupCallPresentation.html" name="phone.joinGroupCallPresentation">Start screen sharing in a call: phone.joinGroupCallPresentation</a>

* <a href="contacts.blockFromReplies.html" name="contacts.blockFromReplies">Stop getting notifications about thread replies of a certain user in @replies: contacts.blockFromReplies</a>

* <a href="phone.leaveGroupCallPresentation.html" name="phone.leaveGroupCallPresentation">Stop screen sharing in a group call: phone.leaveGroupCallPresentation</a>

* <a href="payments.validateRequestedInfo.html" name="payments.validateRequestedInfo">Submit requested order information for validation: payments.validateRequestedInfo</a>

* <a href="phone.toggleGroupCallStartSubscription.html" name="phone.toggleGroupCallStartSubscription">Subscribe or unsubscribe to a scheduled group call: phone.toggleGroupCallStartSubscription</a>

* <a href="stickers.suggestShortName.html" name="stickers.suggestShortName">Suggests a short name for a given stickerpack name: stickers.suggestShortName</a>

* <a href="phone.discardGroupCall.html" name="phone.discardGroupCall">Terminate a group call: phone.discardGroupCall</a>

* <a href="auth.resetAuthorizations.html" name="auth.resetAuthorizations">Terminates all user's authorized sessions except for the current one: auth.resetAuthorizations</a>

* <a href="account.setContactSignUpNotification.html" name="account.setContactSignUpNotification">Toggle contact sign up notifications: account.setContactSignUpNotification</a>

* <a href="channels.toggleSlowMode.html" name="channels.toggleSlowMode">Toggle supergroup slow mode: if enabled, users will only be able to send one message every seconds seconds: channels.toggleSlowMode</a>

* <a href="channels.editCreator.html" name="channels.editCreator">Transfer channel ownership: channels.editCreator</a>

* <a href="messages.translateText.html" name="messages.translateText">Translate a given text: messages.translateText</a>

* <a href="messages.migrateChat.html" name="messages.migrateChat">Turn a basic group into a supergroup: messages.migrateChat</a>

* <a href="messages.uninstallStickerSet.html" name="messages.uninstallStickerSet">Uninstall a stickerset: messages.uninstallStickerSet</a>

* <a href="messages.updateDialogFilter.html" name="messages.updateDialogFilter">Update folder: messages.updateDialogFilter</a>

* <a href="account.updateTheme.html" name="account.updateTheme">Update theme: account.updateTheme</a>

* <a href="photos.uploadProfilePhoto.html" name="photos.uploadProfilePhoto">Updates current user profile photo: photos.uploadProfilePhoto</a>

* <a href="account.updateStatus.html" name="account.updateStatus">Updates online user status: account.updateStatus</a>

* <a href="account.updateProfile.html" name="account.updateProfile">Updates user profile: account.updateProfile</a>

* <a href="messages.uploadMedia.html" name="messages.uploadMedia">Upload a file and associate it to a chat (without actually sending it to the chat): messages.uploadMedia</a>

* <a href="messages.uploadImportedMedia.html" name="messages.uploadImportedMedia">Upload a media file associated with an imported chat, click here for more info »: messages.uploadImportedMedia</a>

* <a href="messages.uploadEncryptedFile.html" name="messages.uploadEncryptedFile">Upload encrypted file and associate it to a secret chat: messages.uploadEncryptedFile</a>

* <a href="account.uploadTheme.html" name="account.uploadTheme">Upload theme: account.uploadTheme</a>

* <a href="messages.setGameScore.html" name="messages.setGameScore">Use this method to set the score of the specified user in a game sent as a normal message (bots only): messages.setGameScore</a>

* <a href="messages.setInlineGameScore.html" name="messages.setInlineGameScore">Use this method to set the score of the specified user in a game sent as an inline message (bots only): messages.setInlineGameScore</a>

* <a href="messages.acceptUrlAuth.html" name="messages.acceptUrlAuth">Use this to accept a Seamless Telegram Login authorization request, for more info click here »: messages.acceptUrlAuth</a>

* <a href="account.checkUsername.html" name="account.checkUsername">Validates a username and checks availability: account.checkUsername</a>

* <a href="account.sendChangePhoneCode.html" name="account.sendChangePhoneCode">Verify a new phone number to associate to the current account: account.sendChangePhoneCode</a>

* <a href="account.verifyPhone.html" name="account.verifyPhone">Verify a phone number for telegram passport: account.verifyPhone</a>

* <a href="account.verifyEmail.html" name="account.verifyEmail">Verify an email address for telegram passport: account.verifyEmail</a>

* <a href="account.confirmPasswordEmail.html" name="account.confirmPasswordEmail">Verify an email to use as 2FA recovery method: account.confirmPasswordEmail</a>

* <a href="messages.searchSentMedia.html" name="messages.searchSentMedia">View and search recently sent media.  : messages.searchSentMedia</a>

* <a href="messages.sendVote.html" name="messages.sendVote">Vote in a poll: messages.sendVote</a>

* <a href="account.updateDeviceLocked.html" name="account.updateDeviceLocked">When client-side passcode lock feature is enabled, will not show message texts in incoming PUSH notifications: account.updateDeviceLocked</a>

* <a href="account.getContactSignUpNotification.html" name="account.getContactSignUpNotification">Whether the user will receive notifications when contacts sign up: account.getContactSignUpNotification</a>

* <a href="auth.bindTempAuthKey.html" name="auth.bindTempAuthKey">You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info: auth.bindTempAuthKey</a>

* <a href="messages.getDhConfig.html" name="messages.getDhConfig">You cannot use this method directly, instead use $MadelineProto->getDhConfig();: messages.getDhConfig</a>

* <a href="messages.acceptEncryption.html" name="messages.acceptEncryption">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats: messages.acceptEncryption</a>

* <a href="messages.discardEncryption.html" name="messages.discardEncryption">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats: messages.discardEncryption</a>

* <a href="messages.requestEncryption.html" name="messages.requestEncryption">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats: messages.requestEncryption</a>

* <a href="updates.getChannelDifference.html" name="updates.getChannelDifference">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates: updates.getChannelDifference</a>

* <a href="updates.getDifference.html" name="updates.getDifference">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates: updates.getDifference</a>

* <a href="updates.getState.html" name="updates.getState">You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates: updates.getState</a>

* <a href="phone.acceptCall.html" name="phone.acceptCall">You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls: phone.acceptCall</a>

* <a href="phone.confirmCall.html" name="phone.confirmCall">You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls: phone.confirmCall</a>

* <a href="phone.discardCall.html" name="phone.discardCall">You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls: phone.discardCall</a>

* <a href="phone.requestCall.html" name="phone.requestCall">You cannot use this method directly, see https://docs.madelineproto.xyz#calls for more info on handling calls: phone.requestCall</a>

* <a href="auth.exportAuthorization.html" name="auth.exportAuthorization">You cannot use this method directly, use $MadelineProto->exportAuthorization() instead, see https://docs.madelineproto.xyz/docs/LOGIN.html: auth.exportAuthorization</a>

* <a href="auth.importAuthorization.html" name="auth.importAuthorization">You cannot use this method directly, use $MadelineProto->importAuthorization($authorization) instead, see https://docs.madelineproto.xyz/docs/LOGIN.html: auth.importAuthorization</a>

* <a href="auth.importBotAuthorization.html" name="auth.importBotAuthorization">You cannot use this method directly, use the botLogin method instead (see https://docs.madelineproto.xyz for more info): auth.importBotAuthorization</a>

* <a href="auth.checkPassword.html" name="auth.checkPassword">You cannot use this method directly, use the complete2falogin method instead (see https://docs.madelineproto.xyz for more info): auth.checkPassword</a>

* <a href="auth.signIn.html" name="auth.signIn">You cannot use this method directly, use the completePhoneLogin method instead (see https://docs.madelineproto.xyz for more info): auth.signIn</a>

* <a href="auth.signUp.html" name="auth.signUp">You cannot use this method directly, use the completeSignup method instead (see https://docs.madelineproto.xyz for more info): auth.signUp</a>

* <a href="channels.getFullChannel.html" name="channels.getFullChannel">You cannot use this method directly, use the getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info): channels.getFullChannel</a>

* <a href="messages.getFullChat.html" name="messages.getFullChat">You cannot use this method directly, use the getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info): messages.getFullChat</a>

* <a href="users.getFullUser.html" name="users.getFullUser">You cannot use this method directly, use the getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info): users.getFullUser</a>

* <a href="auth.logOut.html" name="auth.logOut">You cannot use this method directly, use the logout method instead (see https://docs.madelineproto.xyz for more info): auth.logOut</a>

* <a href="auth.sendCode.html" name="auth.sendCode">You cannot use this method directly, use the phoneLogin method instead (see https://docs.madelineproto.xyz for more info): auth.sendCode</a>

* <a href="contacts.resolveUsername.html" name="contacts.resolveUsername">You cannot use this method directly, use the resolveUsername, getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info): contacts.resolveUsername</a>

* <a href="upload.getCdnFile.html" name="upload.getCdnFile">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.getCdnFile</a>

* <a href="upload.getCdnFileHashes.html" name="upload.getCdnFileHashes">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.getCdnFileHashes</a>

* <a href="upload.getFile.html" name="upload.getFile">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.getFile</a>

* <a href="upload.getFileHashes.html" name="upload.getFileHashes">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.getFileHashes</a>

* <a href="upload.reuploadCdnFile.html" name="upload.reuploadCdnFile">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.reuploadCdnFile</a>

* <a href="upload.saveBigFilePart.html" name="upload.saveBigFilePart">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.saveBigFilePart</a>

* <a href="upload.saveFilePart.html" name="upload.saveFilePart">You cannot use this method directly, use the upload, downloadToStream, downloadToFile, downloadToDir methods instead; see https://docs.madelineproto.xyz for more info: upload.saveFilePart</a>

* <a href="messages.receivedQueue.html" name="messages.receivedQueue">You cannot use this method directly: messages.receivedQueue</a>

* <a href="account.getPasswordSettings.html" name="account.getPasswordSettings">You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info): account.getPasswordSettings</a>

* <a href="account.updatePasswordSettings.html" name="account.updatePasswordSettings">You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info): account.updatePasswordSettings</a>

* <a href="messages.unpinAllMessages.html" name="messages.unpinAllMessages">Unpin all pinned messages: messages.unpinAllMessages</a>



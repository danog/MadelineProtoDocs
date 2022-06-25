---
title: Constructors
description: List of constructors
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructors  
[Back to API documentation index](..)

***
<br><br>[$account.authorizationForm](/API_docs/constructors/account.authorizationForm.html) = \['required_types' => \[[SecureRequiredType](/API_docs/types/SecureRequiredType.html)\], 'values' => \[[SecureValue](/API_docs/types/SecureValue.html)\], 'errors' => \[[SecureValueError](/API_docs/types/SecureValueError.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'privacy_policy_url' => [string](/API_docs/types/string.html), \];<a name="account.authorizationForm"></a>  

***
<br><br>[$account.authorizations](/API_docs/constructors/account.authorizations.html) = \['authorization_ttl_days' => [int](/API_docs/types/int.html), 'authorizations' => \[[Authorization](/API_docs/types/Authorization.html)\], \];<a name="account.authorizations"></a>  

***
<br><br>[$account.autoDownloadSettings](/API_docs/constructors/account.autoDownloadSettings.html) = \['low' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html), 'medium' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html), 'high' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html), \];<a name="account.autoDownloadSettings"></a>  

***
<br><br>[$account.contentSettings](/API_docs/constructors/account.contentSettings.html) = \['sensitive_enabled' => [Bool](/API_docs/types/Bool.html), 'sensitive_can_change' => [Bool](/API_docs/types/Bool.html), \];<a name="account.contentSettings"></a>  

***
<br><br>[$account.password](/API_docs/constructors/account.password.html) = \['has_recovery' => [Bool](/API_docs/types/Bool.html), 'has_secure_values' => [Bool](/API_docs/types/Bool.html), 'has_password' => [Bool](/API_docs/types/Bool.html), 'current_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html), 'srp_B' => [bytes](/API_docs/types/bytes.html), 'srp_id' => [long](/API_docs/types/long.html), 'hint' => [string](/API_docs/types/string.html), 'email_unconfirmed_pattern' => [string](/API_docs/types/string.html), 'new_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html), 'new_secure_algo' => [SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.html), 'secure_random' => [bytes](/API_docs/types/bytes.html), 'pending_reset_date' => [int](/API_docs/types/int.html), \];<a name="account.password"></a>  

***
<br><br>[$account.passwordInputSettings](/API_docs/constructors/account.passwordInputSettings.html) = \['new_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html), 'new_password_hash' => [bytes](/API_docs/types/bytes.html), 'hint' => [string](/API_docs/types/string.html), 'email' => [string](/API_docs/types/string.html), 'new_secure_settings' => [SecureSecretSettings](/API_docs/types/SecureSecretSettings.html), \];<a name="account.passwordInputSettings"></a>  

***
<br><br>[$account.passwordSettings](/API_docs/constructors/account.passwordSettings.html) = \['email' => [string](/API_docs/types/string.html), 'secure_settings' => [SecureSecretSettings](/API_docs/types/SecureSecretSettings.html), \];<a name="account.passwordSettings"></a>  

***
<br><br>[$account.privacyRules](/API_docs/constructors/account.privacyRules.html) = \['rules' => \[[PrivacyRule](/API_docs/types/PrivacyRule.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="account.privacyRules"></a>  

***
<br><br>[$account.resetPasswordFailedWait](/API_docs/constructors/account.resetPasswordFailedWait.html) = \['retry_date' => [int](/API_docs/types/int.html), \];<a name="account.resetPasswordFailedWait"></a>  

***
<br><br>[$account.resetPasswordOk](/API_docs/constructors/account.resetPasswordOk.html) = \[\];<a name="account.resetPasswordOk"></a>  

***
<br><br>[$account.resetPasswordRequestedWait](/API_docs/constructors/account.resetPasswordRequestedWait.html) = \['until_date' => [int](/API_docs/types/int.html), \];<a name="account.resetPasswordRequestedWait"></a>  

***
<br><br>[$account.savedRingtone](/API_docs/constructors/account.savedRingtone.html) = \[\];<a name="account.savedRingtone"></a>  

***
<br><br>[$account.savedRingtoneConverted](/API_docs/constructors/account.savedRingtoneConverted.html) = \['document' => [Document](/API_docs/types/Document.html), \];<a name="account.savedRingtoneConverted"></a>  

***
<br><br>[$account.savedRingtones](/API_docs/constructors/account.savedRingtones.html) = \['hash' => [long](/API_docs/types/long.html), 'ringtones' => \[[Document](/API_docs/types/Document.html)\], \];<a name="account.savedRingtones"></a>  

***
<br><br>[$account.savedRingtonesNotModified](/API_docs/constructors/account.savedRingtonesNotModified.html) = \[\];<a name="account.savedRingtonesNotModified"></a>  

***
<br><br>[$account.sentEmailCode](/API_docs/constructors/account.sentEmailCode.html) = \['email_pattern' => [string](/API_docs/types/string.html), 'length' => [int](/API_docs/types/int.html), \];<a name="account.sentEmailCode"></a>  

***
<br><br>[$account.takeout](/API_docs/constructors/account.takeout.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="account.takeout"></a>  

***
<br><br>[$account.themes](/API_docs/constructors/account.themes.html) = \['hash' => [long](/API_docs/types/long.html), 'themes' => \[[Theme](/API_docs/types/Theme.html)\], \];<a name="account.themes"></a>  

***
<br><br>[$account.themesNotModified](/API_docs/constructors/account.themesNotModified.html) = \[\];<a name="account.themesNotModified"></a>  

***
<br><br>[$account.tmpPassword](/API_docs/constructors/account.tmpPassword.html) = \['tmp_password' => [bytes](/API_docs/types/bytes.html), 'valid_until' => [int](/API_docs/types/int.html), \];<a name="account.tmpPassword"></a>  

***
<br><br>[$account.wallPapers](/API_docs/constructors/account.wallPapers.html) = \['hash' => [long](/API_docs/types/long.html), 'wallpapers' => \[[WallPaper](/API_docs/types/WallPaper.html)\], \];<a name="account.wallPapers"></a>  

***
<br><br>[$account.wallPapersNotModified](/API_docs/constructors/account.wallPapersNotModified.html) = \[\];<a name="account.wallPapersNotModified"></a>  

***
<br><br>[$account.webAuthorizations](/API_docs/constructors/account.webAuthorizations.html) = \['authorizations' => \[[WebAuthorization](/API_docs/types/WebAuthorization.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="account.webAuthorizations"></a>  

***
<br><br>[$accountDaysTTL](/API_docs/constructors/accountDaysTTL.html) = \['days' => [int](/API_docs/types/int.html), \];<a name="accountDaysTTL"></a>  

***
<br><br>[$attachMenuBot](/API_docs/constructors/attachMenuBot.html) = \['inactive' => [Bool](/API_docs/types/Bool.html), 'has_settings' => [Bool](/API_docs/types/Bool.html), 'bot_id' => [long](/API_docs/types/long.html), 'short_name' => [string](/API_docs/types/string.html), 'peer_types' => \[[AttachMenuPeerType](/API_docs/types/AttachMenuPeerType.html)\], 'icons' => \[[AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html)\], \];<a name="attachMenuBot"></a>  

***
<br><br>[$attachMenuBotIcon](/API_docs/constructors/attachMenuBotIcon.html) = \['name' => [string](/API_docs/types/string.html), 'icon' => [Document](/API_docs/types/Document.html), 'colors' => \[[AttachMenuBotIconColor](/API_docs/types/AttachMenuBotIconColor.html)\], \];<a name="attachMenuBotIcon"></a>  

***
<br><br>[$attachMenuBotIconColor](/API_docs/constructors/attachMenuBotIconColor.html) = \['name' => [string](/API_docs/types/string.html), 'color' => [int](/API_docs/types/int.html), \];<a name="attachMenuBotIconColor"></a>  

***
<br><br>[$attachMenuBots](/API_docs/constructors/attachMenuBots.html) = \['hash' => [long](/API_docs/types/long.html), 'bots' => \[[AttachMenuBot](/API_docs/types/AttachMenuBot.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="attachMenuBots"></a>  

***
<br><br>[$attachMenuBotsBot](/API_docs/constructors/attachMenuBotsBot.html) = \['bot' => [AttachMenuBot](/API_docs/types/AttachMenuBot.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="attachMenuBotsBot"></a>  

***
<br><br>[$attachMenuBotsNotModified](/API_docs/constructors/attachMenuBotsNotModified.html) = \[\];<a name="attachMenuBotsNotModified"></a>  

***
<br><br>[$attachMenuPeerTypeBotPM](/API_docs/constructors/attachMenuPeerTypeBotPM.html) = \[\];<a name="attachMenuPeerTypeBotPM"></a>  

***
<br><br>[$attachMenuPeerTypeBroadcast](/API_docs/constructors/attachMenuPeerTypeBroadcast.html) = \[\];<a name="attachMenuPeerTypeBroadcast"></a>  

***
<br><br>[$attachMenuPeerTypeChat](/API_docs/constructors/attachMenuPeerTypeChat.html) = \[\];<a name="attachMenuPeerTypeChat"></a>  

***
<br><br>[$attachMenuPeerTypePM](/API_docs/constructors/attachMenuPeerTypePM.html) = \[\];<a name="attachMenuPeerTypePM"></a>  

***
<br><br>[$attachMenuPeerTypeSameBotPM](/API_docs/constructors/attachMenuPeerTypeSameBotPM.html) = \[\];<a name="attachMenuPeerTypeSameBotPM"></a>  

***
<br><br>[$auth.authorization](/API_docs/constructors/auth.authorization.html) = \['setup_password_required' => [Bool](/API_docs/types/Bool.html), 'otherwise_relogin_days' => [int](/API_docs/types/int.html), 'tmp_sessions' => [int](/API_docs/types/int.html), 'user' => [User](/API_docs/types/User.html), \];<a name="auth.authorization"></a>  

***
<br><br>[$auth.authorizationSignUpRequired](/API_docs/constructors/auth.authorizationSignUpRequired.html) = \['terms_of_service' => [help.TermsOfService](/API_docs/types/help.TermsOfService.html), \];<a name="auth.authorizationSignUpRequired"></a>  

***
<br><br>[$auth.codeTypeCall](/API_docs/constructors/auth.codeTypeCall.html) = \[\];<a name="auth.codeTypeCall"></a>  

***
<br><br>[$auth.codeTypeFlashCall](/API_docs/constructors/auth.codeTypeFlashCall.html) = \[\];<a name="auth.codeTypeFlashCall"></a>  

***
<br><br>[$auth.codeTypeMissedCall](/API_docs/constructors/auth.codeTypeMissedCall.html) = \[\];<a name="auth.codeTypeMissedCall"></a>  

***
<br><br>[$auth.codeTypeSms](/API_docs/constructors/auth.codeTypeSms.html) = \[\];<a name="auth.codeTypeSms"></a>  

***
<br><br>[$auth.exportedAuthorization](/API_docs/constructors/auth.exportedAuthorization.html) = \['id' => [long](/API_docs/types/long.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="auth.exportedAuthorization"></a>  

***
<br><br>[$auth.loggedOut](/API_docs/constructors/auth.loggedOut.html) = \['future_auth_token' => [bytes](/API_docs/types/bytes.html), \];<a name="auth.loggedOut"></a>  

***
<br><br>[$auth.loginToken](/API_docs/constructors/auth.loginToken.html) = \['expires' => [int](/API_docs/types/int.html), 'token' => [bytes](/API_docs/types/bytes.html), \];<a name="auth.loginToken"></a>  

***
<br><br>[$auth.loginTokenMigrateTo](/API_docs/constructors/auth.loginTokenMigrateTo.html) = \['dc_id' => [int](/API_docs/types/int.html), 'token' => [bytes](/API_docs/types/bytes.html), \];<a name="auth.loginTokenMigrateTo"></a>  

***
<br><br>[$auth.loginTokenSuccess](/API_docs/constructors/auth.loginTokenSuccess.html) = \['authorization' => [auth.Authorization](/API_docs/types/auth.Authorization.html), \];<a name="auth.loginTokenSuccess"></a>  

***
<br><br>[$auth.passwordRecovery](/API_docs/constructors/auth.passwordRecovery.html) = \['email_pattern' => [string](/API_docs/types/string.html), \];<a name="auth.passwordRecovery"></a>  

***
<br><br>[$auth.sentCode](/API_docs/constructors/auth.sentCode.html) = \['type' => [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html), 'phone_code_hash' => [string](/API_docs/types/string.html), 'next_type' => [auth.CodeType](/API_docs/types/auth.CodeType.html), 'timeout' => [int](/API_docs/types/int.html), \];<a name="auth.sentCode"></a>  

***
<br><br>[$auth.sentCodeTypeApp](/API_docs/constructors/auth.sentCodeTypeApp.html) = \['length' => [int](/API_docs/types/int.html), \];<a name="auth.sentCodeTypeApp"></a>  

***
<br><br>[$auth.sentCodeTypeCall](/API_docs/constructors/auth.sentCodeTypeCall.html) = \['length' => [int](/API_docs/types/int.html), \];<a name="auth.sentCodeTypeCall"></a>  

***
<br><br>[$auth.sentCodeTypeFlashCall](/API_docs/constructors/auth.sentCodeTypeFlashCall.html) = \['pattern' => [string](/API_docs/types/string.html), \];<a name="auth.sentCodeTypeFlashCall"></a>  

***
<br><br>[$auth.sentCodeTypeMissedCall](/API_docs/constructors/auth.sentCodeTypeMissedCall.html) = \['prefix' => [string](/API_docs/types/string.html), 'length' => [int](/API_docs/types/int.html), \];<a name="auth.sentCodeTypeMissedCall"></a>  

***
<br><br>[$auth.sentCodeTypeSms](/API_docs/constructors/auth.sentCodeTypeSms.html) = \['length' => [int](/API_docs/types/int.html), \];<a name="auth.sentCodeTypeSms"></a>  

***
<br><br>[$authorization](/API_docs/constructors/authorization.html) = \['current' => [Bool](/API_docs/types/Bool.html), 'official_app' => [Bool](/API_docs/types/Bool.html), 'password_pending' => [Bool](/API_docs/types/Bool.html), 'encrypted_requests_disabled' => [Bool](/API_docs/types/Bool.html), 'call_requests_disabled' => [Bool](/API_docs/types/Bool.html), 'hash' => [long](/API_docs/types/long.html), 'device_model' => [string](/API_docs/types/string.html), 'platform' => [string](/API_docs/types/string.html), 'system_version' => [string](/API_docs/types/string.html), 'api_id' => [int](/API_docs/types/int.html), 'app_name' => [string](/API_docs/types/string.html), 'app_version' => [string](/API_docs/types/string.html), 'date_created' => [int](/API_docs/types/int.html), 'date_active' => [int](/API_docs/types/int.html), 'ip' => [string](/API_docs/types/string.html), 'country' => [string](/API_docs/types/string.html), 'region' => [string](/API_docs/types/string.html), \];<a name="authorization"></a>  

***
<br><br>[$autoDownloadSettings](/API_docs/constructors/autoDownloadSettings.html) = \['disabled' => [Bool](/API_docs/types/Bool.html), 'video_preload_large' => [Bool](/API_docs/types/Bool.html), 'audio_preload_next' => [Bool](/API_docs/types/Bool.html), 'phonecalls_less_data' => [Bool](/API_docs/types/Bool.html), 'photo_size_max' => [int](/API_docs/types/int.html), 'video_size_max' => [long](/API_docs/types/long.html), 'file_size_max' => [long](/API_docs/types/long.html), 'video_upload_maxbitrate' => [int](/API_docs/types/int.html), \];<a name="autoDownloadSettings"></a>  

***
<br><br>[$availableReaction](/API_docs/constructors/availableReaction.html) = \['inactive' => [Bool](/API_docs/types/Bool.html), 'premium' => [Bool](/API_docs/types/Bool.html), 'reaction' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'static_icon' => [Document](/API_docs/types/Document.html), 'appear_animation' => [Document](/API_docs/types/Document.html), 'select_animation' => [Document](/API_docs/types/Document.html), 'activate_animation' => [Document](/API_docs/types/Document.html), 'effect_animation' => [Document](/API_docs/types/Document.html), 'around_animation' => [Document](/API_docs/types/Document.html), 'center_icon' => [Document](/API_docs/types/Document.html), \];<a name="availableReaction"></a>  

***
<br><br>[$bankCardOpenUrl](/API_docs/constructors/bankCardOpenUrl.html) = \['url' => [string](/API_docs/types/string.html), 'name' => [string](/API_docs/types/string.html), \];<a name="bankCardOpenUrl"></a>  

***
<br><br>[$baseThemeArctic](/API_docs/constructors/baseThemeArctic.html) = \[\];<a name="baseThemeArctic"></a>  

***
<br><br>[$baseThemeClassic](/API_docs/constructors/baseThemeClassic.html) = \[\];<a name="baseThemeClassic"></a>  

***
<br><br>[$baseThemeDay](/API_docs/constructors/baseThemeDay.html) = \[\];<a name="baseThemeDay"></a>  

***
<br><br>[$baseThemeNight](/API_docs/constructors/baseThemeNight.html) = \[\];<a name="baseThemeNight"></a>  

***
<br><br>[$baseThemeTinted](/API_docs/constructors/baseThemeTinted.html) = \[\];<a name="baseThemeTinted"></a>  

***
<br><br>[$boolFalse](/API_docs/constructors/boolFalse.html) = \[\];<a name="boolFalse"></a>  

***
<br><br>[$boolTrue](/API_docs/constructors/boolTrue.html) = \[\];<a name="boolTrue"></a>  

***
<br><br>[$botCommand](/API_docs/constructors/botCommand.html) = \['command' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), \];<a name="botCommand"></a>  

***
<br><br>[$botCommandScopeChatAdmins](/API_docs/constructors/botCommandScopeChatAdmins.html) = \[\];<a name="botCommandScopeChatAdmins"></a>  

***
<br><br>[$botCommandScopeChats](/API_docs/constructors/botCommandScopeChats.html) = \[\];<a name="botCommandScopeChats"></a>  

***
<br><br>[$botCommandScopeDefault](/API_docs/constructors/botCommandScopeDefault.html) = \[\];<a name="botCommandScopeDefault"></a>  

***
<br><br>[$botCommandScopePeer](/API_docs/constructors/botCommandScopePeer.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), \];<a name="botCommandScopePeer"></a>  

***
<br><br>[$botCommandScopePeerAdmins](/API_docs/constructors/botCommandScopePeerAdmins.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), \];<a name="botCommandScopePeerAdmins"></a>  

***
<br><br>[$botCommandScopePeerUser](/API_docs/constructors/botCommandScopePeerUser.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'user_id' => [InputUser](/API_docs/types/InputUser.html), \];<a name="botCommandScopePeerUser"></a>  

***
<br><br>[$botCommandScopeUsers](/API_docs/constructors/botCommandScopeUsers.html) = \[\];<a name="botCommandScopeUsers"></a>  

***
<br><br>[$botInfo](/API_docs/constructors/botInfo.html) = \['user_id' => [long](/API_docs/types/long.html), 'description' => [string](/API_docs/types/string.html), 'description_photo' => [Photo](/API_docs/types/Photo.html), 'description_document' => [Document](/API_docs/types/Document.html), 'commands' => \[[BotCommand](/API_docs/types/BotCommand.html)\], 'menu_button' => [BotMenuButton](/API_docs/types/BotMenuButton.html), \];<a name="botInfo"></a>  

***
<br><br>[$botInlineMediaResult](/API_docs/constructors/botInlineMediaResult.html) = \['id' => [string](/API_docs/types/string.html), 'type' => [string](/API_docs/types/string.html), 'photo' => [Photo](/API_docs/types/Photo.html), 'document' => [Document](/API_docs/types/Document.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'send_message' => [BotInlineMessage](/API_docs/types/BotInlineMessage.html), \];<a name="botInlineMediaResult"></a>  

***
<br><br>[$botInlineMessageMediaAuto](/API_docs/constructors/botInlineMessageMediaAuto.html) = \['message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageMediaAuto"></a>  

***
<br><br>[$botInlineMessageMediaContact](/API_docs/constructors/botInlineMessageMediaContact.html) = \['phone_number' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'vcard' => [string](/API_docs/types/string.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageMediaContact"></a>  

***
<br><br>[$botInlineMessageMediaGeo](/API_docs/constructors/botInlineMessageMediaGeo.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'heading' => [int](/API_docs/types/int.html), 'period' => [int](/API_docs/types/int.html), 'proximity_notification_radius' => [int](/API_docs/types/int.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageMediaGeo"></a>  

***
<br><br>[$botInlineMessageMediaInvoice](/API_docs/constructors/botInlineMessageMediaInvoice.html) = \['shipping_address_requested' => [Bool](/API_docs/types/Bool.html), 'test' => [Bool](/API_docs/types/Bool.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [WebDocument](/API_docs/types/WebDocument.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageMediaInvoice"></a>  

***
<br><br>[$botInlineMessageMediaVenue](/API_docs/constructors/botInlineMessageMediaVenue.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'title' => [string](/API_docs/types/string.html), 'address' => [string](/API_docs/types/string.html), 'provider' => [string](/API_docs/types/string.html), 'venue_id' => [string](/API_docs/types/string.html), 'venue_type' => [string](/API_docs/types/string.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageMediaVenue"></a>  

***
<br><br>[$botInlineMessageText](/API_docs/constructors/botInlineMessageText.html) = \['no_webpage' => [Bool](/API_docs/types/Bool.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="botInlineMessageText"></a>  

***
<br><br>[$botInlineResult](/API_docs/constructors/botInlineResult.html) = \['id' => [string](/API_docs/types/string.html), 'type' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), 'thumb' => [WebDocument](/API_docs/types/WebDocument.html), 'content' => [WebDocument](/API_docs/types/WebDocument.html), 'send_message' => [BotInlineMessage](/API_docs/types/BotInlineMessage.html), \];<a name="botInlineResult"></a>  

***
<br><br>[$botMenuButton](/API_docs/constructors/botMenuButton.html) = \['text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), \];<a name="botMenuButton"></a>  

***
<br><br>[$botMenuButtonCommands](/API_docs/constructors/botMenuButtonCommands.html) = \[\];<a name="botMenuButtonCommands"></a>  

***
<br><br>[$botMenuButtonDefault](/API_docs/constructors/botMenuButtonDefault.html) = \[\];<a name="botMenuButtonDefault"></a>  

***
<br><br>[$cdnConfig](/API_docs/constructors/cdnConfig.html) = \['public_keys' => \[[CdnPublicKey](/API_docs/types/CdnPublicKey.html)\], \];<a name="cdnConfig"></a>  

***
<br><br>[$cdnPublicKey](/API_docs/constructors/cdnPublicKey.html) = \['dc_id' => [int](/API_docs/types/int.html), 'public_key' => [string](/API_docs/types/string.html), \];<a name="cdnPublicKey"></a>  

***
<br><br>[$channel](/API_docs/constructors/channel.html) = \['creator' => [Bool](/API_docs/types/Bool.html), 'left' => [Bool](/API_docs/types/Bool.html), 'broadcast' => [Bool](/API_docs/types/Bool.html), 'verified' => [Bool](/API_docs/types/Bool.html), 'megagroup' => [Bool](/API_docs/types/Bool.html), 'restricted' => [Bool](/API_docs/types/Bool.html), 'signatures' => [Bool](/API_docs/types/Bool.html), 'min' => [Bool](/API_docs/types/Bool.html), 'scam' => [Bool](/API_docs/types/Bool.html), 'has_link' => [Bool](/API_docs/types/Bool.html), 'has_geo' => [Bool](/API_docs/types/Bool.html), 'slowmode_enabled' => [Bool](/API_docs/types/Bool.html), 'call_active' => [Bool](/API_docs/types/Bool.html), 'call_not_empty' => [Bool](/API_docs/types/Bool.html), 'fake' => [Bool](/API_docs/types/Bool.html), 'gigagroup' => [Bool](/API_docs/types/Bool.html), 'noforwards' => [Bool](/API_docs/types/Bool.html), 'join_to_send' => [Bool](/API_docs/types/Bool.html), 'join_request' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'username' => [string](/API_docs/types/string.html), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.html), 'date' => [int](/API_docs/types/int.html), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.html)\], 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), 'participants_count' => [int](/API_docs/types/int.html), \];<a name="channel"></a>  

***
<br><br>[$channelAdminLogEvent](/API_docs/constructors/channelAdminLogEvent.html) = \['id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), 'action' => [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html), \];<a name="channelAdminLogEvent"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAbout](/API_docs/constructors/channelAdminLogEventActionChangeAbout.html) = \['prev_value' => [string](/API_docs/types/string.html), 'new_value' => [string](/API_docs/types/string.html), \];<a name="channelAdminLogEventActionChangeAbout"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAvailableReactions](/API_docs/constructors/channelAdminLogEventActionChangeAvailableReactions.html) = \['prev_value' => \[[string](/API_docs/types/string.html)\], 'new_value' => \[[string](/API_docs/types/string.html)\], \];<a name="channelAdminLogEventActionChangeAvailableReactions"></a>  

***
<br><br>[$channelAdminLogEventActionChangeHistoryTTL](/API_docs/constructors/channelAdminLogEventActionChangeHistoryTTL.html) = \['prev_value' => [int](/API_docs/types/int.html), 'new_value' => [int](/API_docs/types/int.html), \];<a name="channelAdminLogEventActionChangeHistoryTTL"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLinkedChat](/API_docs/constructors/channelAdminLogEventActionChangeLinkedChat.html) = \['prev_value' => [long](/API_docs/types/long.html), 'new_value' => [long](/API_docs/types/long.html), \];<a name="channelAdminLogEventActionChangeLinkedChat"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLocation](/API_docs/constructors/channelAdminLogEventActionChangeLocation.html) = \['prev_value' => [ChannelLocation](/API_docs/types/ChannelLocation.html), 'new_value' => [ChannelLocation](/API_docs/types/ChannelLocation.html), \];<a name="channelAdminLogEventActionChangeLocation"></a>  

***
<br><br>[$channelAdminLogEventActionChangePhoto](/API_docs/constructors/channelAdminLogEventActionChangePhoto.html) = \['prev_photo' => [Photo](/API_docs/types/Photo.html), 'new_photo' => [Photo](/API_docs/types/Photo.html), \];<a name="channelAdminLogEventActionChangePhoto"></a>  

***
<br><br>[$channelAdminLogEventActionChangeStickerSet](/API_docs/constructors/channelAdminLogEventActionChangeStickerSet.html) = \['prev_stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.html), 'new_stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.html), \];<a name="channelAdminLogEventActionChangeStickerSet"></a>  

***
<br><br>[$channelAdminLogEventActionChangeTitle](/API_docs/constructors/channelAdminLogEventActionChangeTitle.html) = \['prev_value' => [string](/API_docs/types/string.html), 'new_value' => [string](/API_docs/types/string.html), \];<a name="channelAdminLogEventActionChangeTitle"></a>  

***
<br><br>[$channelAdminLogEventActionChangeUsername](/API_docs/constructors/channelAdminLogEventActionChangeUsername.html) = \['prev_value' => [string](/API_docs/types/string.html), 'new_value' => [string](/API_docs/types/string.html), \];<a name="channelAdminLogEventActionChangeUsername"></a>  

***
<br><br>[$channelAdminLogEventActionDefaultBannedRights](/API_docs/constructors/channelAdminLogEventActionDefaultBannedRights.html) = \['prev_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), 'new_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), \];<a name="channelAdminLogEventActionDefaultBannedRights"></a>  

***
<br><br>[$channelAdminLogEventActionDeleteMessage](/API_docs/constructors/channelAdminLogEventActionDeleteMessage.html) = \['message' => [Message](/API_docs/types/Message.html), \];<a name="channelAdminLogEventActionDeleteMessage"></a>  

***
<br><br>[$channelAdminLogEventActionDiscardGroupCall](/API_docs/constructors/channelAdminLogEventActionDiscardGroupCall.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), \];<a name="channelAdminLogEventActionDiscardGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionEditMessage](/API_docs/constructors/channelAdminLogEventActionEditMessage.html) = \['prev_message' => [Message](/API_docs/types/Message.html), 'new_message' => [Message](/API_docs/types/Message.html), \];<a name="channelAdminLogEventActionEditMessage"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteDelete](/API_docs/constructors/channelAdminLogEventActionExportedInviteDelete.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), \];<a name="channelAdminLogEventActionExportedInviteDelete"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteEdit](/API_docs/constructors/channelAdminLogEventActionExportedInviteEdit.html) = \['prev_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'new_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), \];<a name="channelAdminLogEventActionExportedInviteEdit"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteRevoke](/API_docs/constructors/channelAdminLogEventActionExportedInviteRevoke.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), \];<a name="channelAdminLogEventActionExportedInviteRevoke"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantInvite](/API_docs/constructors/channelAdminLogEventActionParticipantInvite.html) = \['participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), \];<a name="channelAdminLogEventActionParticipantInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoin](/API_docs/constructors/channelAdminLogEventActionParticipantJoin.html) = \[\];<a name="channelAdminLogEventActionParticipantJoin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByInvite](/API_docs/constructors/channelAdminLogEventActionParticipantJoinByInvite.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), \];<a name="channelAdminLogEventActionParticipantJoinByInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByRequest](/API_docs/constructors/channelAdminLogEventActionParticipantJoinByRequest.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'approved_by' => [long](/API_docs/types/long.html), \];<a name="channelAdminLogEventActionParticipantJoinByRequest"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantLeave](/API_docs/constructors/channelAdminLogEventActionParticipantLeave.html) = \[\];<a name="channelAdminLogEventActionParticipantLeave"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantMute](/API_docs/constructors/channelAdminLogEventActionParticipantMute.html) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html), \];<a name="channelAdminLogEventActionParticipantMute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleAdmin](/API_docs/constructors/channelAdminLogEventActionParticipantToggleAdmin.html) = \['prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), \];<a name="channelAdminLogEventActionParticipantToggleAdmin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleBan](/API_docs/constructors/channelAdminLogEventActionParticipantToggleBan.html) = \['prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), \];<a name="channelAdminLogEventActionParticipantToggleBan"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantUnmute](/API_docs/constructors/channelAdminLogEventActionParticipantUnmute.html) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html), \];<a name="channelAdminLogEventActionParticipantUnmute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantVolume](/API_docs/constructors/channelAdminLogEventActionParticipantVolume.html) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html), \];<a name="channelAdminLogEventActionParticipantVolume"></a>  

***
<br><br>[$channelAdminLogEventActionSendMessage](/API_docs/constructors/channelAdminLogEventActionSendMessage.html) = \['message' => [Message](/API_docs/types/Message.html), \];<a name="channelAdminLogEventActionSendMessage"></a>  

***
<br><br>[$channelAdminLogEventActionStartGroupCall](/API_docs/constructors/channelAdminLogEventActionStartGroupCall.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), \];<a name="channelAdminLogEventActionStartGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionStopPoll](/API_docs/constructors/channelAdminLogEventActionStopPoll.html) = \['message' => [Message](/API_docs/types/Message.html), \];<a name="channelAdminLogEventActionStopPoll"></a>  

***
<br><br>[$channelAdminLogEventActionToggleGroupCallSetting](/API_docs/constructors/channelAdminLogEventActionToggleGroupCallSetting.html) = \['join_muted' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventActionToggleGroupCallSetting"></a>  

***
<br><br>[$channelAdminLogEventActionToggleInvites](/API_docs/constructors/channelAdminLogEventActionToggleInvites.html) = \['new_value' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventActionToggleInvites"></a>  

***
<br><br>[$channelAdminLogEventActionToggleNoForwards](/API_docs/constructors/channelAdminLogEventActionToggleNoForwards.html) = \['new_value' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventActionToggleNoForwards"></a>  

***
<br><br>[$channelAdminLogEventActionTogglePreHistoryHidden](/API_docs/constructors/channelAdminLogEventActionTogglePreHistoryHidden.html) = \['new_value' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventActionTogglePreHistoryHidden"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSignatures](/API_docs/constructors/channelAdminLogEventActionToggleSignatures.html) = \['new_value' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventActionToggleSignatures"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSlowMode](/API_docs/constructors/channelAdminLogEventActionToggleSlowMode.html) = \['prev_value' => [int](/API_docs/types/int.html), 'new_value' => [int](/API_docs/types/int.html), \];<a name="channelAdminLogEventActionToggleSlowMode"></a>  

***
<br><br>[$channelAdminLogEventActionUpdatePinned](/API_docs/constructors/channelAdminLogEventActionUpdatePinned.html) = \['message' => [Message](/API_docs/types/Message.html), \];<a name="channelAdminLogEventActionUpdatePinned"></a>  

***
<br><br>[$channelAdminLogEventsFilter](/API_docs/constructors/channelAdminLogEventsFilter.html) = \['join' => [Bool](/API_docs/types/Bool.html), 'leave' => [Bool](/API_docs/types/Bool.html), 'invite' => [Bool](/API_docs/types/Bool.html), 'ban' => [Bool](/API_docs/types/Bool.html), 'unban' => [Bool](/API_docs/types/Bool.html), 'kick' => [Bool](/API_docs/types/Bool.html), 'unkick' => [Bool](/API_docs/types/Bool.html), 'promote' => [Bool](/API_docs/types/Bool.html), 'demote' => [Bool](/API_docs/types/Bool.html), 'info' => [Bool](/API_docs/types/Bool.html), 'settings' => [Bool](/API_docs/types/Bool.html), 'pinned' => [Bool](/API_docs/types/Bool.html), 'edit' => [Bool](/API_docs/types/Bool.html), 'delete' => [Bool](/API_docs/types/Bool.html), 'group_call' => [Bool](/API_docs/types/Bool.html), 'invites' => [Bool](/API_docs/types/Bool.html), 'send' => [Bool](/API_docs/types/Bool.html), \];<a name="channelAdminLogEventsFilter"></a>  

***
<br><br>[$channelForbidden](/API_docs/constructors/channelForbidden.html) = \['broadcast' => [Bool](/API_docs/types/Bool.html), 'megagroup' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'until_date' => [int](/API_docs/types/int.html), \];<a name="channelForbidden"></a>  

***
<br><br>[$channelFull](/API_docs/constructors/channelFull.html) = \['can_view_participants' => [Bool](/API_docs/types/Bool.html), 'can_set_username' => [Bool](/API_docs/types/Bool.html), 'can_set_stickers' => [Bool](/API_docs/types/Bool.html), 'hidden_prehistory' => [Bool](/API_docs/types/Bool.html), 'can_set_location' => [Bool](/API_docs/types/Bool.html), 'has_scheduled' => [Bool](/API_docs/types/Bool.html), 'can_view_stats' => [Bool](/API_docs/types/Bool.html), 'blocked' => [Bool](/API_docs/types/Bool.html), 'can_delete_channel' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'about' => [string](/API_docs/types/string.html), 'participants_count' => [int](/API_docs/types/int.html), 'admins_count' => [int](/API_docs/types/int.html), 'kicked_count' => [int](/API_docs/types/int.html), 'banned_count' => [int](/API_docs/types/int.html), 'online_count' => [int](/API_docs/types/int.html), 'read_inbox_max_id' => [int](/API_docs/types/int.html), 'read_outbox_max_id' => [int](/API_docs/types/int.html), 'unread_count' => [int](/API_docs/types/int.html), 'chat_photo' => [Photo](/API_docs/types/Photo.html), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html), 'exported_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'bot_info' => \[[BotInfo](/API_docs/types/BotInfo.html)\], 'migrated_from_chat_id' => [long](/API_docs/types/long.html), 'migrated_from_max_id' => [int](/API_docs/types/int.html), 'pinned_msg_id' => [int](/API_docs/types/int.html), 'stickerset' => [StickerSet](/API_docs/types/StickerSet.html), 'available_min_id' => [int](/API_docs/types/int.html), 'folder_id' => [int](/API_docs/types/int.html), 'linked_chat_id' => [long](/API_docs/types/long.html), 'location' => [ChannelLocation](/API_docs/types/ChannelLocation.html), 'slowmode_seconds' => [int](/API_docs/types/int.html), 'slowmode_next_send_date' => [int](/API_docs/types/int.html), 'stats_dc' => [int](/API_docs/types/int.html), 'pts' => [int](/API_docs/types/int.html), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'ttl_period' => [int](/API_docs/types/int.html), 'pending_suggestions' => \[[string](/API_docs/types/string.html)\], 'groupcall_default_join_as' => [Peer](/API_docs/types/Peer.html), 'theme_emoticon' => [string](/API_docs/types/string.html), 'requests_pending' => [int](/API_docs/types/int.html), 'recent_requesters' => \[[long](/API_docs/types/long.html)\], 'default_send_as' => [Peer](/API_docs/types/Peer.html), 'available_reactions' => \[[string](/API_docs/types/string.html)\], \];<a name="channelFull"></a>  

***
<br><br>[$channelLocation](/API_docs/constructors/channelLocation.html) = \['geo_point' => [GeoPoint](/API_docs/types/GeoPoint.html), 'address' => [string](/API_docs/types/string.html), \];<a name="channelLocation"></a>  

***
<br><br>[$channelLocationEmpty](/API_docs/constructors/channelLocationEmpty.html) = \[\];<a name="channelLocationEmpty"></a>  

***
<br><br>[$channelMessagesFilter](/API_docs/constructors/channelMessagesFilter.html) = \['exclude_new_messages' => [Bool](/API_docs/types/Bool.html), 'ranges' => \[[MessageRange](/API_docs/types/MessageRange.html)\], \];<a name="channelMessagesFilter"></a>  

***
<br><br>[$channelMessagesFilterEmpty](/API_docs/constructors/channelMessagesFilterEmpty.html) = \[\];<a name="channelMessagesFilterEmpty"></a>  

***
<br><br>[$channelParticipant](/API_docs/constructors/channelParticipant.html) = \['user_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="channelParticipant"></a>  

***
<br><br>[$channelParticipantAdmin](/API_docs/constructors/channelParticipantAdmin.html) = \['can_edit' => [Bool](/API_docs/types/Bool.html), 'self' => [Bool](/API_docs/types/Bool.html), 'user_id' => [long](/API_docs/types/long.html), 'inviter_id' => [long](/API_docs/types/long.html), 'promoted_by' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), 'rank' => [string](/API_docs/types/string.html), \];<a name="channelParticipantAdmin"></a>  

***
<br><br>[$channelParticipantBanned](/API_docs/constructors/channelParticipantBanned.html) = \['left' => [Bool](/API_docs/types/Bool.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'kicked_by' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), \];<a name="channelParticipantBanned"></a>  

***
<br><br>[$channelParticipantCreator](/API_docs/constructors/channelParticipantCreator.html) = \['user_id' => [long](/API_docs/types/long.html), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), 'rank' => [string](/API_docs/types/string.html), \];<a name="channelParticipantCreator"></a>  

***
<br><br>[$channelParticipantLeft](/API_docs/constructors/channelParticipantLeft.html) = \['peer' => [Peer](/API_docs/types/Peer.html), \];<a name="channelParticipantLeft"></a>  

***
<br><br>[$channelParticipantSelf](/API_docs/constructors/channelParticipantSelf.html) = \['via_request' => [Bool](/API_docs/types/Bool.html), 'user_id' => [long](/API_docs/types/long.html), 'inviter_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="channelParticipantSelf"></a>  

***
<br><br>[$channelParticipantsAdmins](/API_docs/constructors/channelParticipantsAdmins.html) = \[\];<a name="channelParticipantsAdmins"></a>  

***
<br><br>[$channelParticipantsBanned](/API_docs/constructors/channelParticipantsBanned.html) = \['q' => [string](/API_docs/types/string.html), \];<a name="channelParticipantsBanned"></a>  

***
<br><br>[$channelParticipantsBots](/API_docs/constructors/channelParticipantsBots.html) = \[\];<a name="channelParticipantsBots"></a>  

***
<br><br>[$channelParticipantsContacts](/API_docs/constructors/channelParticipantsContacts.html) = \['q' => [string](/API_docs/types/string.html), \];<a name="channelParticipantsContacts"></a>  

***
<br><br>[$channelParticipantsKicked](/API_docs/constructors/channelParticipantsKicked.html) = \['q' => [string](/API_docs/types/string.html), \];<a name="channelParticipantsKicked"></a>  

***
<br><br>[$channelParticipantsMentions](/API_docs/constructors/channelParticipantsMentions.html) = \['q' => [string](/API_docs/types/string.html), 'top_msg_id' => [int](/API_docs/types/int.html), \];<a name="channelParticipantsMentions"></a>  

***
<br><br>[$channelParticipantsRecent](/API_docs/constructors/channelParticipantsRecent.html) = \[\];<a name="channelParticipantsRecent"></a>  

***
<br><br>[$channelParticipantsSearch](/API_docs/constructors/channelParticipantsSearch.html) = \['q' => [string](/API_docs/types/string.html), \];<a name="channelParticipantsSearch"></a>  

***
<br><br>[$channels.adminLogResults](/API_docs/constructors/channels.adminLogResults.html) = \['events' => \[[ChannelAdminLogEvent](/API_docs/types/ChannelAdminLogEvent.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="channels.adminLogResults"></a>  

***
<br><br>[$channels.channelParticipant](/API_docs/constructors/channels.channelParticipant.html) = \['participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="channels.channelParticipant"></a>  

***
<br><br>[$channels.channelParticipants](/API_docs/constructors/channels.channelParticipants.html) = \['count' => [int](/API_docs/types/int.html), 'participants' => \[[ChannelParticipant](/API_docs/types/ChannelParticipant.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="channels.channelParticipants"></a>  

***
<br><br>[$channels.channelParticipantsNotModified](/API_docs/constructors/channels.channelParticipantsNotModified.html) = \[\];<a name="channels.channelParticipantsNotModified"></a>  

***
<br><br>[$channels.sendAsPeers](/API_docs/constructors/channels.sendAsPeers.html) = \['peers' => \[[Peer](/API_docs/types/Peer.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="channels.sendAsPeers"></a>  

***
<br><br>[$chat](/API_docs/constructors/chat.html) = \['creator' => [Bool](/API_docs/types/Bool.html), 'left' => [Bool](/API_docs/types/Bool.html), 'deactivated' => [Bool](/API_docs/types/Bool.html), 'call_active' => [Bool](/API_docs/types/Bool.html), 'call_not_empty' => [Bool](/API_docs/types/Bool.html), 'noforwards' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.html), 'participants_count' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'version' => [int](/API_docs/types/int.html), 'migrated_to' => [InputChannel](/API_docs/types/InputChannel.html), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), \];<a name="chat"></a>  

***
<br><br>[$chatAdminRights](/API_docs/constructors/chatAdminRights.html) = \['change_info' => [Bool](/API_docs/types/Bool.html), 'post_messages' => [Bool](/API_docs/types/Bool.html), 'edit_messages' => [Bool](/API_docs/types/Bool.html), 'delete_messages' => [Bool](/API_docs/types/Bool.html), 'ban_users' => [Bool](/API_docs/types/Bool.html), 'invite_users' => [Bool](/API_docs/types/Bool.html), 'pin_messages' => [Bool](/API_docs/types/Bool.html), 'add_admins' => [Bool](/API_docs/types/Bool.html), 'anonymous' => [Bool](/API_docs/types/Bool.html), 'manage_call' => [Bool](/API_docs/types/Bool.html), 'other' => [Bool](/API_docs/types/Bool.html), \];<a name="chatAdminRights"></a>  

***
<br><br>[$chatAdminWithInvites](/API_docs/constructors/chatAdminWithInvites.html) = \['admin_id' => [long](/API_docs/types/long.html), 'invites_count' => [int](/API_docs/types/int.html), 'revoked_invites_count' => [int](/API_docs/types/int.html), \];<a name="chatAdminWithInvites"></a>  

***
<br><br>[$chatBannedRights](/API_docs/constructors/chatBannedRights.html) = \['view_messages' => [Bool](/API_docs/types/Bool.html), 'send_messages' => [Bool](/API_docs/types/Bool.html), 'send_media' => [Bool](/API_docs/types/Bool.html), 'send_stickers' => [Bool](/API_docs/types/Bool.html), 'send_gifs' => [Bool](/API_docs/types/Bool.html), 'send_games' => [Bool](/API_docs/types/Bool.html), 'send_inline' => [Bool](/API_docs/types/Bool.html), 'embed_links' => [Bool](/API_docs/types/Bool.html), 'send_polls' => [Bool](/API_docs/types/Bool.html), 'change_info' => [Bool](/API_docs/types/Bool.html), 'invite_users' => [Bool](/API_docs/types/Bool.html), 'pin_messages' => [Bool](/API_docs/types/Bool.html), 'until_date' => [int](/API_docs/types/int.html), \];<a name="chatBannedRights"></a>  

***
<br><br>[$chatEmpty](/API_docs/constructors/chatEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="chatEmpty"></a>  

***
<br><br>[$chatForbidden](/API_docs/constructors/chatForbidden.html) = \['id' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), \];<a name="chatForbidden"></a>  

***
<br><br>[$chatFull](/API_docs/constructors/chatFull.html) = \['can_set_username' => [Bool](/API_docs/types/Bool.html), 'has_scheduled' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'about' => [string](/API_docs/types/string.html), 'participants' => [ChatParticipants](/API_docs/types/ChatParticipants.html), 'chat_photo' => [Photo](/API_docs/types/Photo.html), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html), 'exported_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'bot_info' => \[[BotInfo](/API_docs/types/BotInfo.html)\], 'pinned_msg_id' => [int](/API_docs/types/int.html), 'folder_id' => [int](/API_docs/types/int.html), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'ttl_period' => [int](/API_docs/types/int.html), 'groupcall_default_join_as' => [Peer](/API_docs/types/Peer.html), 'theme_emoticon' => [string](/API_docs/types/string.html), 'requests_pending' => [int](/API_docs/types/int.html), 'recent_requesters' => \[[long](/API_docs/types/long.html)\], 'available_reactions' => \[[string](/API_docs/types/string.html)\], \];<a name="chatFull"></a>  

***
<br><br>[$chatInvite](/API_docs/constructors/chatInvite.html) = \['channel' => [Bool](/API_docs/types/Bool.html), 'broadcast' => [Bool](/API_docs/types/Bool.html), 'public' => [Bool](/API_docs/types/Bool.html), 'megagroup' => [Bool](/API_docs/types/Bool.html), 'request_needed' => [Bool](/API_docs/types/Bool.html), 'title' => [string](/API_docs/types/string.html), 'about' => [string](/API_docs/types/string.html), 'photo' => [Photo](/API_docs/types/Photo.html), 'participants_count' => [int](/API_docs/types/int.html), 'participants' => \[[User](/API_docs/types/User.html)\], \];<a name="chatInvite"></a>  

***
<br><br>[$chatInviteAlready](/API_docs/constructors/chatInviteAlready.html) = \['chat' => [Chat](/API_docs/types/Chat.html), \];<a name="chatInviteAlready"></a>  

***
<br><br>[$chatInviteExported](/API_docs/constructors/chatInviteExported.html) = \['revoked' => [Bool](/API_docs/types/Bool.html), 'permanent' => [Bool](/API_docs/types/Bool.html), 'request_needed' => [Bool](/API_docs/types/Bool.html), 'link' => [string](/API_docs/types/string.html), 'admin_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'start_date' => [int](/API_docs/types/int.html), 'expire_date' => [int](/API_docs/types/int.html), 'usage_limit' => [int](/API_docs/types/int.html), 'usage' => [int](/API_docs/types/int.html), 'requested' => [int](/API_docs/types/int.html), 'title' => [string](/API_docs/types/string.html), \];<a name="chatInviteExported"></a>  

***
<br><br>[$chatInviteImporter](/API_docs/constructors/chatInviteImporter.html) = \['requested' => [Bool](/API_docs/types/Bool.html), 'user_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'about' => [string](/API_docs/types/string.html), 'approved_by' => [long](/API_docs/types/long.html), \];<a name="chatInviteImporter"></a>  

***
<br><br>[$chatInvitePeek](/API_docs/constructors/chatInvitePeek.html) = \['chat' => [Chat](/API_docs/types/Chat.html), 'expires' => [int](/API_docs/types/int.html), \];<a name="chatInvitePeek"></a>  

***
<br><br>[$chatInvitePublicJoinRequests](/API_docs/constructors/chatInvitePublicJoinRequests.html) = \[\];<a name="chatInvitePublicJoinRequests"></a>  

***
<br><br>[$chatOnlines](/API_docs/constructors/chatOnlines.html) = \['onlines' => [int](/API_docs/types/int.html), \];<a name="chatOnlines"></a>  

***
<br><br>[$chatParticipant](/API_docs/constructors/chatParticipant.html) = \['user_id' => [long](/API_docs/types/long.html), 'inviter_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="chatParticipant"></a>  

***
<br><br>[$chatParticipantAdmin](/API_docs/constructors/chatParticipantAdmin.html) = \['user_id' => [long](/API_docs/types/long.html), 'inviter_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="chatParticipantAdmin"></a>  

***
<br><br>[$chatParticipantCreator](/API_docs/constructors/chatParticipantCreator.html) = \['user_id' => [long](/API_docs/types/long.html), \];<a name="chatParticipantCreator"></a>  

***
<br><br>[$chatParticipants](/API_docs/constructors/chatParticipants.html) = \['chat_id' => [long](/API_docs/types/long.html), 'participants' => \[[ChatParticipant](/API_docs/types/ChatParticipant.html)\], 'version' => [int](/API_docs/types/int.html), \];<a name="chatParticipants"></a>  

***
<br><br>[$chatParticipantsForbidden](/API_docs/constructors/chatParticipantsForbidden.html) = \['chat_id' => [long](/API_docs/types/long.html), 'self_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.html), \];<a name="chatParticipantsForbidden"></a>  

***
<br><br>[$chatPhoto](/API_docs/constructors/chatPhoto.html) = \['has_video' => [Bool](/API_docs/types/Bool.html), 'photo_id' => [long](/API_docs/types/long.html), 'stripped_thumb' => [bytes](/API_docs/types/bytes.html), 'dc_id' => [int](/API_docs/types/int.html), \];<a name="chatPhoto"></a>  

***
<br><br>[$chatPhotoEmpty](/API_docs/constructors/chatPhotoEmpty.html) = \[\];<a name="chatPhotoEmpty"></a>  

***
<br><br>[$codeSettings](/API_docs/constructors/codeSettings.html) = \['allow_flashcall' => [Bool](/API_docs/types/Bool.html), 'current_number' => [Bool](/API_docs/types/Bool.html), 'allow_app_hash' => [Bool](/API_docs/types/Bool.html), 'allow_missed_call' => [Bool](/API_docs/types/Bool.html), 'logout_tokens' => \[[bytes](/API_docs/types/bytes.html)\], \];<a name="codeSettings"></a>  

***
<br><br>[$config](/API_docs/constructors/config.html) = \['phonecalls_enabled' => [Bool](/API_docs/types/Bool.html), 'default_p2p_contacts' => [Bool](/API_docs/types/Bool.html), 'preload_featured_stickers' => [Bool](/API_docs/types/Bool.html), 'ignore_phone_entities' => [Bool](/API_docs/types/Bool.html), 'revoke_pm_inbox' => [Bool](/API_docs/types/Bool.html), 'blocked_mode' => [Bool](/API_docs/types/Bool.html), 'pfs_enabled' => [Bool](/API_docs/types/Bool.html), 'force_try_ipv6' => [Bool](/API_docs/types/Bool.html), 'date' => [int](/API_docs/types/int.html), 'expires' => [int](/API_docs/types/int.html), 'test_mode' => [Bool](/API_docs/types/Bool.html), 'this_dc' => [int](/API_docs/types/int.html), 'dc_options' => \[[DcOption](/API_docs/types/DcOption.html)\], 'dc_txt_domain_name' => [string](/API_docs/types/string.html), 'chat_size_max' => [int](/API_docs/types/int.html), 'megagroup_size_max' => [int](/API_docs/types/int.html), 'forwarded_count_max' => [int](/API_docs/types/int.html), 'online_update_period_ms' => [int](/API_docs/types/int.html), 'offline_blur_timeout_ms' => [int](/API_docs/types/int.html), 'offline_idle_timeout_ms' => [int](/API_docs/types/int.html), 'online_cloud_timeout_ms' => [int](/API_docs/types/int.html), 'notify_cloud_delay_ms' => [int](/API_docs/types/int.html), 'notify_default_delay_ms' => [int](/API_docs/types/int.html), 'push_chat_period_ms' => [int](/API_docs/types/int.html), 'push_chat_limit' => [int](/API_docs/types/int.html), 'saved_gifs_limit' => [int](/API_docs/types/int.html), 'edit_time_limit' => [int](/API_docs/types/int.html), 'revoke_time_limit' => [int](/API_docs/types/int.html), 'revoke_pm_time_limit' => [int](/API_docs/types/int.html), 'rating_e_decay' => [int](/API_docs/types/int.html), 'stickers_recent_limit' => [int](/API_docs/types/int.html), 'stickers_faved_limit' => [int](/API_docs/types/int.html), 'channels_read_media_period' => [int](/API_docs/types/int.html), 'tmp_sessions' => [int](/API_docs/types/int.html), 'pinned_dialogs_count_max' => [int](/API_docs/types/int.html), 'pinned_infolder_count_max' => [int](/API_docs/types/int.html), 'call_receive_timeout_ms' => [int](/API_docs/types/int.html), 'call_ring_timeout_ms' => [int](/API_docs/types/int.html), 'call_connect_timeout_ms' => [int](/API_docs/types/int.html), 'call_packet_timeout_ms' => [int](/API_docs/types/int.html), 'me_url_prefix' => [string](/API_docs/types/string.html), 'autoupdate_url_prefix' => [string](/API_docs/types/string.html), 'gif_search_username' => [string](/API_docs/types/string.html), 'venue_search_username' => [string](/API_docs/types/string.html), 'img_search_username' => [string](/API_docs/types/string.html), 'static_maps_provider' => [string](/API_docs/types/string.html), 'caption_length_max' => [int](/API_docs/types/int.html), 'message_length_max' => [int](/API_docs/types/int.html), 'webfile_dc_id' => [int](/API_docs/types/int.html), 'suggested_lang_code' => [string](/API_docs/types/string.html), 'lang_pack_version' => [int](/API_docs/types/int.html), 'base_lang_pack_version' => [int](/API_docs/types/int.html), \];<a name="config"></a>  

***
<br><br>[$contact](/API_docs/constructors/contact.html) = \['user_id' => [long](/API_docs/types/long.html), 'mutual' => [Bool](/API_docs/types/Bool.html), \];<a name="contact"></a>  

***
<br><br>[$contactStatus](/API_docs/constructors/contactStatus.html) = \['user_id' => [long](/API_docs/types/long.html), 'status' => [UserStatus](/API_docs/types/UserStatus.html), \];<a name="contactStatus"></a>  

***
<br><br>[$contacts.blocked](/API_docs/constructors/contacts.blocked.html) = \['blocked' => \[[PeerBlocked](/API_docs/types/PeerBlocked.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.blocked"></a>  

***
<br><br>[$contacts.blockedSlice](/API_docs/constructors/contacts.blockedSlice.html) = \['count' => [int](/API_docs/types/int.html), 'blocked' => \[[PeerBlocked](/API_docs/types/PeerBlocked.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.blockedSlice"></a>  

***
<br><br>[$contacts.contacts](/API_docs/constructors/contacts.contacts.html) = \['contacts' => \[[Contact](/API_docs/types/Contact.html)\], 'saved_count' => [int](/API_docs/types/int.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.contacts"></a>  

***
<br><br>[$contacts.contactsNotModified](/API_docs/constructors/contacts.contactsNotModified.html) = \[\];<a name="contacts.contactsNotModified"></a>  

***
<br><br>[$contacts.found](/API_docs/constructors/contacts.found.html) = \['my_results' => \[[Peer](/API_docs/types/Peer.html)\], 'results' => \[[Peer](/API_docs/types/Peer.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.found"></a>  

***
<br><br>[$contacts.importedContacts](/API_docs/constructors/contacts.importedContacts.html) = \['imported' => \[[ImportedContact](/API_docs/types/ImportedContact.html)\], 'popular_invites' => \[[PopularContact](/API_docs/types/PopularContact.html)\], 'retry_contacts' => \[[long](/API_docs/types/long.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.importedContacts"></a>  

***
<br><br>[$contacts.resolvedPeer](/API_docs/constructors/contacts.resolvedPeer.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.resolvedPeer"></a>  

***
<br><br>[$contacts.topPeers](/API_docs/constructors/contacts.topPeers.html) = \['categories' => \[[TopPeerCategoryPeers](/API_docs/types/TopPeerCategoryPeers.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="contacts.topPeers"></a>  

***
<br><br>[$contacts.topPeersDisabled](/API_docs/constructors/contacts.topPeersDisabled.html) = \[\];<a name="contacts.topPeersDisabled"></a>  

***
<br><br>[$contacts.topPeersNotModified](/API_docs/constructors/contacts.topPeersNotModified.html) = \[\];<a name="contacts.topPeersNotModified"></a>  

***
<br><br>[$dataJSON](/API_docs/constructors/dataJSON.html) = \['data' => [string](/API_docs/types/string.html), \];<a name="dataJSON"></a>  

***
<br><br>[$dcOption](/API_docs/constructors/dcOption.html) = \['ipv6' => [Bool](/API_docs/types/Bool.html), 'media_only' => [Bool](/API_docs/types/Bool.html), 'tcpo_only' => [Bool](/API_docs/types/Bool.html), 'cdn' => [Bool](/API_docs/types/Bool.html), 'static' => [Bool](/API_docs/types/Bool.html), 'this_port_only' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'ip_address' => [string](/API_docs/types/string.html), 'port' => [int](/API_docs/types/int.html), 'secret' => [bytes](/API_docs/types/bytes.html), \];<a name="dcOption"></a>  

***
<br><br>[$decryptedMessage\_73](/API_docs/constructors/decryptedMessage_73.html) = \['ttl' => [int](/API_docs/types/int.html), 'message' => [string](/API_docs/types/string.html), 'media' => [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'via_bot_name' => [string](/API_docs/types/string.html), 'reply_to_random_id' => [long](/API_docs/types/long.html), 'grouped_id' => [long](/API_docs/types/long.html), \];<a name="decryptedMessage_73"></a>  

***
<br><br>[$decryptedMessageActionAbortKey\_20](/API_docs/constructors/decryptedMessageActionAbortKey_20.html) = \['exchange_id' => [long](/API_docs/types/long.html), \];<a name="decryptedMessageActionAbortKey_20"></a>  

***
<br><br>[$decryptedMessageActionAcceptKey\_20](/API_docs/constructors/decryptedMessageActionAcceptKey_20.html) = \['exchange_id' => [long](/API_docs/types/long.html), 'g_b' => [bytes](/API_docs/types/bytes.html), 'key_fingerprint' => [long](/API_docs/types/long.html), \];<a name="decryptedMessageActionAcceptKey_20"></a>  

***
<br><br>[$decryptedMessageActionCommitKey\_20](/API_docs/constructors/decryptedMessageActionCommitKey_20.html) = \['exchange_id' => [long](/API_docs/types/long.html), 'key_fingerprint' => [long](/API_docs/types/long.html), \];<a name="decryptedMessageActionCommitKey_20"></a>  

***
<br><br>[$decryptedMessageActionDeleteMessages\_8](/API_docs/constructors/decryptedMessageActionDeleteMessages_8.html) = \['random_ids' => \[[long](/API_docs/types/long.html)\], \];<a name="decryptedMessageActionDeleteMessages_8"></a>  

***
<br><br>[$decryptedMessageActionFlushHistory\_8](/API_docs/constructors/decryptedMessageActionFlushHistory_8.html) = \[\];<a name="decryptedMessageActionFlushHistory_8"></a>  

***
<br><br>[$decryptedMessageActionNoop\_20](/API_docs/constructors/decryptedMessageActionNoop_20.html) = \[\];<a name="decryptedMessageActionNoop_20"></a>  

***
<br><br>[$decryptedMessageActionNotifyLayer\_17](/API_docs/constructors/decryptedMessageActionNotifyLayer_17.html) = \['layer' => [int](/API_docs/types/int.html), \];<a name="decryptedMessageActionNotifyLayer_17"></a>  

***
<br><br>[$decryptedMessageActionReadMessages\_8](/API_docs/constructors/decryptedMessageActionReadMessages_8.html) = \['random_ids' => \[[long](/API_docs/types/long.html)\], \];<a name="decryptedMessageActionReadMessages_8"></a>  

***
<br><br>[$decryptedMessageActionRequestKey\_20](/API_docs/constructors/decryptedMessageActionRequestKey_20.html) = \['exchange_id' => [long](/API_docs/types/long.html), 'g_a' => [bytes](/API_docs/types/bytes.html), \];<a name="decryptedMessageActionRequestKey_20"></a>  

***
<br><br>[$decryptedMessageActionResend\_17](/API_docs/constructors/decryptedMessageActionResend_17.html) = \['start_seq_no' => [int](/API_docs/types/int.html), 'end_seq_no' => [int](/API_docs/types/int.html), \];<a name="decryptedMessageActionResend_17"></a>  

***
<br><br>[$decryptedMessageActionScreenshotMessages\_8](/API_docs/constructors/decryptedMessageActionScreenshotMessages_8.html) = \['random_ids' => \[[long](/API_docs/types/long.html)\], \];<a name="decryptedMessageActionScreenshotMessages_8"></a>  

***
<br><br>[$decryptedMessageActionSetMessageTTL\_8](/API_docs/constructors/decryptedMessageActionSetMessageTTL_8.html) = \['ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="decryptedMessageActionSetMessageTTL_8"></a>  

***
<br><br>[$decryptedMessageActionTyping\_17](/API_docs/constructors/decryptedMessageActionTyping_17.html) = \['action' => [SendMessageAction](/API_docs/types/SendMessageAction.html), \];<a name="decryptedMessageActionTyping_17"></a>  

***
<br><br>[$decryptedMessageLayer\_17](/API_docs/constructors/decryptedMessageLayer_17.html) = \['layer' => [int](/API_docs/types/int.html), 'in_seq_no' => [int](/API_docs/types/int.html), 'out_seq_no' => [int](/API_docs/types/int.html), 'message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.html), \];<a name="decryptedMessageLayer_17"></a>  

***
<br><br>[$decryptedMessageMediaAudio\_17](/API_docs/constructors/decryptedMessageMediaAudio_17.html) = \['duration' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'size' => [int](/API_docs/types/int.html), 'key' => [bytes](/API_docs/types/bytes.html), 'iv' => [bytes](/API_docs/types/bytes.html), \];<a name="decryptedMessageMediaAudio_17"></a>  

***
<br><br>[$decryptedMessageMediaContact\_8](/API_docs/constructors/decryptedMessageMediaContact_8.html) = \['phone_number' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'user_id' => [int](/API_docs/types/int.html), \];<a name="decryptedMessageMediaContact_8"></a>  

***
<br><br>[$decryptedMessageMediaDocument\_45](/API_docs/constructors/decryptedMessageMediaDocument_45.html) = \['thumb' => [bytes](/API_docs/types/bytes.html), 'thumb_w' => [int](/API_docs/types/int.html), 'thumb_h' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'size' => [int](/API_docs/types/int.html), 'key' => [bytes](/API_docs/types/bytes.html), 'iv' => [bytes](/API_docs/types/bytes.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], 'caption' => [string](/API_docs/types/string.html), \];<a name="decryptedMessageMediaDocument_45"></a>  

***
<br><br>[$decryptedMessageMediaEmpty\_8](/API_docs/constructors/decryptedMessageMediaEmpty_8.html) = \[\];<a name="decryptedMessageMediaEmpty_8"></a>  

***
<br><br>[$decryptedMessageMediaExternalDocument\_23](/API_docs/constructors/decryptedMessageMediaExternalDocument_23.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'size' => [int](/API_docs/types/int.html), 'thumb' => [PhotoSize](/API_docs/types/PhotoSize.html), 'dc_id' => [int](/API_docs/types/int.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], \];<a name="decryptedMessageMediaExternalDocument_23"></a>  

***
<br><br>[$decryptedMessageMediaGeoPoint\_8](/API_docs/constructors/decryptedMessageMediaGeoPoint_8.html) = \['lat' => [double](/API_docs/types/double.html), 'long' => [double](/API_docs/types/double.html), \];<a name="decryptedMessageMediaGeoPoint_8"></a>  

***
<br><br>[$decryptedMessageMediaPhoto\_45](/API_docs/constructors/decryptedMessageMediaPhoto_45.html) = \['thumb' => [bytes](/API_docs/types/bytes.html), 'thumb_w' => [int](/API_docs/types/int.html), 'thumb_h' => [int](/API_docs/types/int.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'size' => [int](/API_docs/types/int.html), 'key' => [bytes](/API_docs/types/bytes.html), 'iv' => [bytes](/API_docs/types/bytes.html), 'caption' => [string](/API_docs/types/string.html), \];<a name="decryptedMessageMediaPhoto_45"></a>  

***
<br><br>[$decryptedMessageMediaVenue\_46](/API_docs/constructors/decryptedMessageMediaVenue_46.html) = \['lat' => [double](/API_docs/types/double.html), 'long' => [double](/API_docs/types/double.html), 'title' => [string](/API_docs/types/string.html), 'address' => [string](/API_docs/types/string.html), 'provider' => [string](/API_docs/types/string.html), 'venue_id' => [string](/API_docs/types/string.html), \];<a name="decryptedMessageMediaVenue_46"></a>  

***
<br><br>[$decryptedMessageMediaVideo\_45](/API_docs/constructors/decryptedMessageMediaVideo_45.html) = \['thumb' => [bytes](/API_docs/types/bytes.html), 'thumb_w' => [int](/API_docs/types/int.html), 'thumb_h' => [int](/API_docs/types/int.html), 'duration' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'size' => [int](/API_docs/types/int.html), 'key' => [bytes](/API_docs/types/bytes.html), 'iv' => [bytes](/API_docs/types/bytes.html), 'caption' => [string](/API_docs/types/string.html), \];<a name="decryptedMessageMediaVideo_45"></a>  

***
<br><br>[$decryptedMessageMediaWebPage\_46](/API_docs/constructors/decryptedMessageMediaWebPage_46.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="decryptedMessageMediaWebPage_46"></a>  

***
<br><br>[$decryptedMessageService\_17](/API_docs/constructors/decryptedMessageService_17.html) = \['action' => [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html), \];<a name="decryptedMessageService_17"></a>  

***
<br><br>[$dialog](/API_docs/constructors/dialog.html) = \['pinned' => [Bool](/API_docs/types/Bool.html), 'unread_mark' => [Bool](/API_docs/types/Bool.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'top_message' => [int](/API_docs/types/int.html), 'read_inbox_max_id' => [int](/API_docs/types/int.html), 'read_outbox_max_id' => [int](/API_docs/types/int.html), 'unread_count' => [int](/API_docs/types/int.html), 'unread_mentions_count' => [int](/API_docs/types/int.html), 'unread_reactions_count' => [int](/API_docs/types/int.html), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html), 'pts' => [int](/API_docs/types/int.html), 'draft' => [DraftMessage](/API_docs/types/DraftMessage.html), 'folder_id' => [int](/API_docs/types/int.html), \];<a name="dialog"></a>  

***
<br><br>[$dialogFilter](/API_docs/constructors/dialogFilter.html) = \['contacts' => [Bool](/API_docs/types/Bool.html), 'non_contacts' => [Bool](/API_docs/types/Bool.html), 'groups' => [Bool](/API_docs/types/Bool.html), 'broadcasts' => [Bool](/API_docs/types/Bool.html), 'bots' => [Bool](/API_docs/types/Bool.html), 'exclude_muted' => [Bool](/API_docs/types/Bool.html), 'exclude_read' => [Bool](/API_docs/types/Bool.html), 'exclude_archived' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'title' => [string](/API_docs/types/string.html), 'emoticon' => [string](/API_docs/types/string.html), 'pinned_peers' => \[[InputPeer](/API_docs/types/InputPeer.html)\], 'include_peers' => \[[InputPeer](/API_docs/types/InputPeer.html)\], 'exclude_peers' => \[[InputPeer](/API_docs/types/InputPeer.html)\], \];<a name="dialogFilter"></a>  

***
<br><br>[$dialogFilterDefault](/API_docs/constructors/dialogFilterDefault.html) = \[\];<a name="dialogFilterDefault"></a>  

***
<br><br>[$dialogFilterSuggested](/API_docs/constructors/dialogFilterSuggested.html) = \['filter' => [DialogFilter](/API_docs/types/DialogFilter.html), 'description' => [string](/API_docs/types/string.html), \];<a name="dialogFilterSuggested"></a>  

***
<br><br>[$dialogFolder](/API_docs/constructors/dialogFolder.html) = \['pinned' => [Bool](/API_docs/types/Bool.html), 'folder' => [Folder](/API_docs/types/Folder.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'top_message' => [int](/API_docs/types/int.html), 'unread_muted_peers_count' => [int](/API_docs/types/int.html), 'unread_unmuted_peers_count' => [int](/API_docs/types/int.html), 'unread_muted_messages_count' => [int](/API_docs/types/int.html), 'unread_unmuted_messages_count' => [int](/API_docs/types/int.html), \];<a name="dialogFolder"></a>  

***
<br><br>[$dialogPeer](/API_docs/constructors/dialogPeer.html) = \['peer' => [Peer](/API_docs/types/Peer.html), \];<a name="dialogPeer"></a>  

***
<br><br>[$dialogPeerFolder](/API_docs/constructors/dialogPeerFolder.html) = \['folder_id' => [int](/API_docs/types/int.html), \];<a name="dialogPeerFolder"></a>  

***
<br><br>[$document](/API_docs/constructors/document.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), 'date' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'size' => [long](/API_docs/types/long.html), 'thumbs' => \[[PhotoSize](/API_docs/types/PhotoSize.html)\], 'video_thumbs' => \[[VideoSize](/API_docs/types/VideoSize.html)\], 'dc_id' => [int](/API_docs/types/int.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], \];<a name="document"></a>  

***
<br><br>[$documentAttributeAnimated](/API_docs/constructors/documentAttributeAnimated.html) = \[\];<a name="documentAttributeAnimated"></a>  

***
<br><br>[$documentAttributeAudio\_46](/API_docs/constructors/documentAttributeAudio_46.html) = \['duration' => [int](/API_docs/types/int.html), 'title' => [string](/API_docs/types/string.html), 'performer' => [string](/API_docs/types/string.html), \];<a name="documentAttributeAudio_46"></a>  

***
<br><br>[$documentAttributeFilename](/API_docs/constructors/documentAttributeFilename.html) = \['file_name' => [string](/API_docs/types/string.html), \];<a name="documentAttributeFilename"></a>  

***
<br><br>[$documentAttributeHasStickers](/API_docs/constructors/documentAttributeHasStickers.html) = \[\];<a name="documentAttributeHasStickers"></a>  

***
<br><br>[$documentAttributeImageSize](/API_docs/constructors/documentAttributeImageSize.html) = \['w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), \];<a name="documentAttributeImageSize"></a>  

***
<br><br>[$documentAttributeSticker\_55](/API_docs/constructors/documentAttributeSticker_55.html) = \['alt' => [string](/API_docs/types/string.html), 'stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.html), \];<a name="documentAttributeSticker_55"></a>  

***
<br><br>[$documentAttributeVideo\_23](/API_docs/constructors/documentAttributeVideo_23.html) = \['duration' => [int](/API_docs/types/int.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), \];<a name="documentAttributeVideo_23"></a>  

***
<br><br>[$documentEmpty](/API_docs/constructors/documentEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="documentEmpty"></a>  

***
<br><br>[$draftMessage](/API_docs/constructors/draftMessage.html) = \['no_webpage' => [Bool](/API_docs/types/Bool.html), 'reply_to_msg_id' => [int](/API_docs/types/int.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'date' => [int](/API_docs/types/int.html), \];<a name="draftMessage"></a>  

***
<br><br>[$draftMessageEmpty](/API_docs/constructors/draftMessageEmpty.html) = \['date' => [int](/API_docs/types/int.html), \];<a name="draftMessageEmpty"></a>  

***
<br><br>[$emojiKeyword](/API_docs/constructors/emojiKeyword.html) = \['keyword' => [string](/API_docs/types/string.html), 'emoticons' => \[[string](/API_docs/types/string.html)\], \];<a name="emojiKeyword"></a>  

***
<br><br>[$emojiKeywordDeleted](/API_docs/constructors/emojiKeywordDeleted.html) = \['keyword' => [string](/API_docs/types/string.html), 'emoticons' => \[[string](/API_docs/types/string.html)\], \];<a name="emojiKeywordDeleted"></a>  

***
<br><br>[$emojiKeywordsDifference](/API_docs/constructors/emojiKeywordsDifference.html) = \['lang_code' => [string](/API_docs/types/string.html), 'from_version' => [int](/API_docs/types/int.html), 'version' => [int](/API_docs/types/int.html), 'keywords' => \[[EmojiKeyword](/API_docs/types/EmojiKeyword.html)\], \];<a name="emojiKeywordsDifference"></a>  

***
<br><br>[$emojiLanguage](/API_docs/constructors/emojiLanguage.html) = \['lang_code' => [string](/API_docs/types/string.html), \];<a name="emojiLanguage"></a>  

***
<br><br>[$emojiURL](/API_docs/constructors/emojiURL.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="emojiURL"></a>  

***
<br><br>[$encryptedChat](/API_docs/constructors/encryptedChat.html) = \['id' => [int](/API_docs/types/int.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'g_a_or_b' => [bytes](/API_docs/types/bytes.html), 'key_fingerprint' => [long](/API_docs/types/long.html), \];<a name="encryptedChat"></a>  

***
<br><br>[$encryptedChatDiscarded](/API_docs/constructors/encryptedChatDiscarded.html) = \['history_deleted' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), \];<a name="encryptedChatDiscarded"></a>  

***
<br><br>[$encryptedChatEmpty](/API_docs/constructors/encryptedChatEmpty.html) = \['id' => [int](/API_docs/types/int.html), \];<a name="encryptedChatEmpty"></a>  

***
<br><br>[$encryptedChatRequested](/API_docs/constructors/encryptedChatRequested.html) = \['folder_id' => [int](/API_docs/types/int.html), 'id' => [int](/API_docs/types/int.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'g_a' => [bytes](/API_docs/types/bytes.html), \];<a name="encryptedChatRequested"></a>  

***
<br><br>[$encryptedChatWaiting](/API_docs/constructors/encryptedChatWaiting.html) = \['id' => [int](/API_docs/types/int.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), \];<a name="encryptedChatWaiting"></a>  

***
<br><br>[$encryptedFile](/API_docs/constructors/encryptedFile.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'size' => [long](/API_docs/types/long.html), 'dc_id' => [int](/API_docs/types/int.html), 'key_fingerprint' => [int](/API_docs/types/int.html), \];<a name="encryptedFile"></a>  

***
<br><br>[$encryptedFileEmpty](/API_docs/constructors/encryptedFileEmpty.html) = \[\];<a name="encryptedFileEmpty"></a>  

***
<br><br>[$encryptedMessage](/API_docs/constructors/encryptedMessage.html) = \['chat_id' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'decrypted_message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.html), 'file' => [EncryptedFile](/API_docs/types/EncryptedFile.html), \];<a name="encryptedMessage"></a>  

***
<br><br>[$encryptedMessageService](/API_docs/constructors/encryptedMessageService.html) = \['chat_id' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'decrypted_message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.html), \];<a name="encryptedMessageService"></a>  

***
<br><br>[$error](/API_docs/constructors/error.html) = \['code' => [int](/API_docs/types/int.html), 'text' => [string](/API_docs/types/string.html), \];<a name="error"></a>  

***
<br><br>[$exportedMessageLink](/API_docs/constructors/exportedMessageLink.html) = \['link' => [string](/API_docs/types/string.html), 'html' => [string](/API_docs/types/string.html), \];<a name="exportedMessageLink"></a>  

***
<br><br>[$fileHash](/API_docs/constructors/fileHash.html) = \['offset' => [long](/API_docs/types/long.html), 'limit' => [int](/API_docs/types/int.html), 'hash' => [bytes](/API_docs/types/bytes.html), \];<a name="fileHash"></a>  

***
<br><br>[$fileLocation\_23](/API_docs/constructors/fileLocation_23.html) = \['dc_id' => [int](/API_docs/types/int.html), 'volume_id' => [long](/API_docs/types/long.html), 'local_id' => [int](/API_docs/types/int.html), 'secret' => [long](/API_docs/types/long.html), \];<a name="fileLocation_23"></a>  

***
<br><br>[$fileLocationUnavailable\_23](/API_docs/constructors/fileLocationUnavailable_23.html) = \['volume_id' => [long](/API_docs/types/long.html), 'local_id' => [int](/API_docs/types/int.html), 'secret' => [long](/API_docs/types/long.html), \];<a name="fileLocationUnavailable_23"></a>  

***
<br><br>[$folder](/API_docs/constructors/folder.html) = \['autofill_new_broadcasts' => [Bool](/API_docs/types/Bool.html), 'autofill_public_groups' => [Bool](/API_docs/types/Bool.html), 'autofill_new_correspondents' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'title' => [string](/API_docs/types/string.html), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.html), \];<a name="folder"></a>  

***
<br><br>[$folderPeer](/API_docs/constructors/folderPeer.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'folder_id' => [int](/API_docs/types/int.html), \];<a name="folderPeer"></a>  

***
<br><br>[$game](/API_docs/constructors/game.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'short_name' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [Photo](/API_docs/types/Photo.html), 'document' => [Document](/API_docs/types/Document.html), \];<a name="game"></a>  

***
<br><br>[$geoPoint](/API_docs/constructors/geoPoint.html) = \['long' => [double](/API_docs/types/double.html), 'lat' => [double](/API_docs/types/double.html), 'access_hash' => [long](/API_docs/types/long.html), 'accuracy_radius' => [int](/API_docs/types/int.html), \];<a name="geoPoint"></a>  

***
<br><br>[$geoPointEmpty](/API_docs/constructors/geoPointEmpty.html) = \[\];<a name="geoPointEmpty"></a>  

***
<br><br>[$globalPrivacySettings](/API_docs/constructors/globalPrivacySettings.html) = \['archive_and_mute_new_noncontact_peers' => [Bool](/API_docs/types/Bool.html), \];<a name="globalPrivacySettings"></a>  

***
<br><br>[$groupCall](/API_docs/constructors/groupCall.html) = \['join_muted' => [Bool](/API_docs/types/Bool.html), 'can_change_join_muted' => [Bool](/API_docs/types/Bool.html), 'join_date_asc' => [Bool](/API_docs/types/Bool.html), 'schedule_start_subscribed' => [Bool](/API_docs/types/Bool.html), 'can_start_video' => [Bool](/API_docs/types/Bool.html), 'record_video_active' => [Bool](/API_docs/types/Bool.html), 'rtmp_stream' => [Bool](/API_docs/types/Bool.html), 'listeners_hidden' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'participants_count' => [int](/API_docs/types/int.html), 'title' => [string](/API_docs/types/string.html), 'stream_dc_id' => [int](/API_docs/types/int.html), 'record_start_date' => [int](/API_docs/types/int.html), 'schedule_date' => [int](/API_docs/types/int.html), 'unmuted_video_count' => [int](/API_docs/types/int.html), 'unmuted_video_limit' => [int](/API_docs/types/int.html), 'version' => [int](/API_docs/types/int.html), \];<a name="groupCall"></a>  

***
<br><br>[$groupCallDiscarded](/API_docs/constructors/groupCallDiscarded.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'duration' => [int](/API_docs/types/int.html), \];<a name="groupCallDiscarded"></a>  

***
<br><br>[$groupCallParticipant](/API_docs/constructors/groupCallParticipant.html) = \['muted' => [Bool](/API_docs/types/Bool.html), 'left' => [Bool](/API_docs/types/Bool.html), 'can_self_unmute' => [Bool](/API_docs/types/Bool.html), 'just_joined' => [Bool](/API_docs/types/Bool.html), 'versioned' => [Bool](/API_docs/types/Bool.html), 'min' => [Bool](/API_docs/types/Bool.html), 'muted_by_you' => [Bool](/API_docs/types/Bool.html), 'volume_by_admin' => [Bool](/API_docs/types/Bool.html), 'self' => [Bool](/API_docs/types/Bool.html), 'video_joined' => [Bool](/API_docs/types/Bool.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'date' => [int](/API_docs/types/int.html), 'active_date' => [int](/API_docs/types/int.html), 'source' => [int](/API_docs/types/int.html), 'volume' => [int](/API_docs/types/int.html), 'about' => [string](/API_docs/types/string.html), 'raise_hand_rating' => [long](/API_docs/types/long.html), 'video' => [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html), 'presentation' => [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.html), \];<a name="groupCallParticipant"></a>  

***
<br><br>[$groupCallParticipantVideo](/API_docs/constructors/groupCallParticipantVideo.html) = \['paused' => [Bool](/API_docs/types/Bool.html), 'endpoint' => [string](/API_docs/types/string.html), 'source_groups' => \[[GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.html)\], 'audio_source' => [int](/API_docs/types/int.html), \];<a name="groupCallParticipantVideo"></a>  

***
<br><br>[$groupCallParticipantVideoSourceGroup](/API_docs/constructors/groupCallParticipantVideoSourceGroup.html) = \['semantics' => [string](/API_docs/types/string.html), 'sources' => \[[int](/API_docs/types/int.html)\], \];<a name="groupCallParticipantVideoSourceGroup"></a>  

***
<br><br>[$groupCallStreamChannel](/API_docs/constructors/groupCallStreamChannel.html) = \['channel' => [int](/API_docs/types/int.html), 'scale' => [int](/API_docs/types/int.html), 'last_timestamp_ms' => [long](/API_docs/types/long.html), \];<a name="groupCallStreamChannel"></a>  

***
<br><br>[$help.appUpdate](/API_docs/constructors/help.appUpdate.html) = \['can_not_skip' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'version' => [string](/API_docs/types/string.html), 'text' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'document' => [Document](/API_docs/types/Document.html), 'url' => [string](/API_docs/types/string.html), 'sticker' => [Document](/API_docs/types/Document.html), \];<a name="help.appUpdate"></a>  

***
<br><br>[$help.countriesList](/API_docs/constructors/help.countriesList.html) = \['countries' => \[[help.Country](/API_docs/types/help.Country.html)\], 'hash' => [int](/API_docs/types/int.html), \];<a name="help.countriesList"></a>  

***
<br><br>[$help.countriesListNotModified](/API_docs/constructors/help.countriesListNotModified.html) = \[\];<a name="help.countriesListNotModified"></a>  

***
<br><br>[$help.country](/API_docs/constructors/help.country.html) = \['hidden' => [Bool](/API_docs/types/Bool.html), 'iso2' => [string](/API_docs/types/string.html), 'default_name' => [string](/API_docs/types/string.html), 'name' => [string](/API_docs/types/string.html), 'country_codes' => \[[help.CountryCode](/API_docs/types/help.CountryCode.html)\], \];<a name="help.country"></a>  

***
<br><br>[$help.countryCode](/API_docs/constructors/help.countryCode.html) = \['country_code' => [string](/API_docs/types/string.html), 'prefixes' => \[[string](/API_docs/types/string.html)\], 'patterns' => \[[string](/API_docs/types/string.html)\], \];<a name="help.countryCode"></a>  

***
<br><br>[$help.deepLinkInfo](/API_docs/constructors/help.deepLinkInfo.html) = \['update_app' => [Bool](/API_docs/types/Bool.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="help.deepLinkInfo"></a>  

***
<br><br>[$help.deepLinkInfoEmpty](/API_docs/constructors/help.deepLinkInfoEmpty.html) = \[\];<a name="help.deepLinkInfoEmpty"></a>  

***
<br><br>[$help.inviteText](/API_docs/constructors/help.inviteText.html) = \['message' => [string](/API_docs/types/string.html), \];<a name="help.inviteText"></a>  

***
<br><br>[$help.noAppUpdate](/API_docs/constructors/help.noAppUpdate.html) = \[\];<a name="help.noAppUpdate"></a>  

***
<br><br>[$help.passportConfig](/API_docs/constructors/help.passportConfig.html) = \['hash' => [int](/API_docs/types/int.html), 'countries_langs' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="help.passportConfig"></a>  

***
<br><br>[$help.passportConfigNotModified](/API_docs/constructors/help.passportConfigNotModified.html) = \[\];<a name="help.passportConfigNotModified"></a>  

***
<br><br>[$help.premiumPromo](/API_docs/constructors/help.premiumPromo.html) = \['status_text' => [string](/API_docs/types/string.html), 'status_entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'video_sections' => \[[string](/API_docs/types/string.html)\], 'videos' => \[[Document](/API_docs/types/Document.html)\], 'currency' => [string](/API_docs/types/string.html), 'monthly_amount' => [long](/API_docs/types/long.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="help.premiumPromo"></a>  

***
<br><br>[$help.promoData](/API_docs/constructors/help.promoData.html) = \['proxy' => [Bool](/API_docs/types/Bool.html), 'expires' => [int](/API_docs/types/int.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'psa_type' => [string](/API_docs/types/string.html), 'psa_message' => [string](/API_docs/types/string.html), \];<a name="help.promoData"></a>  

***
<br><br>[$help.promoDataEmpty](/API_docs/constructors/help.promoDataEmpty.html) = \['expires' => [int](/API_docs/types/int.html), \];<a name="help.promoDataEmpty"></a>  

***
<br><br>[$help.recentMeUrls](/API_docs/constructors/help.recentMeUrls.html) = \['urls' => \[[RecentMeUrl](/API_docs/types/RecentMeUrl.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="help.recentMeUrls"></a>  

***
<br><br>[$help.support](/API_docs/constructors/help.support.html) = \['phone_number' => [string](/API_docs/types/string.html), 'user' => [User](/API_docs/types/User.html), \];<a name="help.support"></a>  

***
<br><br>[$help.supportName](/API_docs/constructors/help.supportName.html) = \['name' => [string](/API_docs/types/string.html), \];<a name="help.supportName"></a>  

***
<br><br>[$help.termsOfService](/API_docs/constructors/help.termsOfService.html) = \['popup' => [Bool](/API_docs/types/Bool.html), 'id' => [DataJSON](/API_docs/types/DataJSON.html), 'text' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'min_age_confirm' => [int](/API_docs/types/int.html), \];<a name="help.termsOfService"></a>  

***
<br><br>[$help.termsOfServiceUpdate](/API_docs/constructors/help.termsOfServiceUpdate.html) = \['expires' => [int](/API_docs/types/int.html), 'terms_of_service' => [help.TermsOfService](/API_docs/types/help.TermsOfService.html), \];<a name="help.termsOfServiceUpdate"></a>  

***
<br><br>[$help.termsOfServiceUpdateEmpty](/API_docs/constructors/help.termsOfServiceUpdateEmpty.html) = \['expires' => [int](/API_docs/types/int.html), \];<a name="help.termsOfServiceUpdateEmpty"></a>  

***
<br><br>[$help.userInfo](/API_docs/constructors/help.userInfo.html) = \['message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'author' => [string](/API_docs/types/string.html), 'date' => [int](/API_docs/types/int.html), \];<a name="help.userInfo"></a>  

***
<br><br>[$help.userInfoEmpty](/API_docs/constructors/help.userInfoEmpty.html) = \[\];<a name="help.userInfoEmpty"></a>  

***
<br><br>[$highScore](/API_docs/constructors/highScore.html) = \['pos' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), 'score' => [int](/API_docs/types/int.html), \];<a name="highScore"></a>  

***
<br><br>[$importedContact](/API_docs/constructors/importedContact.html) = \['user_id' => [long](/API_docs/types/long.html), 'client_id' => [long](/API_docs/types/long.html), \];<a name="importedContact"></a>  

***
<br><br>[$inlineBotSwitchPM](/API_docs/constructors/inlineBotSwitchPM.html) = \['text' => [string](/API_docs/types/string.html), 'start_param' => [string](/API_docs/types/string.html), \];<a name="inlineBotSwitchPM"></a>  

***
<br><br>[$inlineQueryPeerTypeBroadcast](/API_docs/constructors/inlineQueryPeerTypeBroadcast.html) = \[\];<a name="inlineQueryPeerTypeBroadcast"></a>  

***
<br><br>[$inlineQueryPeerTypeChat](/API_docs/constructors/inlineQueryPeerTypeChat.html) = \[\];<a name="inlineQueryPeerTypeChat"></a>  

***
<br><br>[$inlineQueryPeerTypeMegagroup](/API_docs/constructors/inlineQueryPeerTypeMegagroup.html) = \[\];<a name="inlineQueryPeerTypeMegagroup"></a>  

***
<br><br>[$inlineQueryPeerTypePM](/API_docs/constructors/inlineQueryPeerTypePM.html) = \[\];<a name="inlineQueryPeerTypePM"></a>  

***
<br><br>[$inlineQueryPeerTypeSameBotPM](/API_docs/constructors/inlineQueryPeerTypeSameBotPM.html) = \[\];<a name="inlineQueryPeerTypeSameBotPM"></a>  

***
<br><br>[$inputAppEvent](/API_docs/constructors/inputAppEvent.html) = \['time' => [double](/API_docs/types/double.html), 'type' => [string](/API_docs/types/string.html), 'peer' => [long](/API_docs/types/long.html), 'data' => [JSONValue](/API_docs/types/JSONValue.html), \];<a name="inputAppEvent"></a>  

***
<br><br>[$inputBotInlineMessageGame](/API_docs/constructors/inputBotInlineMessageGame.html) = \['reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageGame"></a>  

***
<br><br>[$inputBotInlineMessageID](/API_docs/constructors/inputBotInlineMessageID.html) = \['dc_id' => [int](/API_docs/types/int.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputBotInlineMessageID"></a>  

***
<br><br>[$inputBotInlineMessageID64](/API_docs/constructors/inputBotInlineMessageID64.html) = \['dc_id' => [int](/API_docs/types/int.html), 'owner_id' => [long](/API_docs/types/long.html), 'id' => [int](/API_docs/types/int.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputBotInlineMessageID64"></a>  

***
<br><br>[$inputBotInlineMessageMediaAuto](/API_docs/constructors/inputBotInlineMessageMediaAuto.html) = \['message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageMediaAuto"></a>  

***
<br><br>[$inputBotInlineMessageMediaContact](/API_docs/constructors/inputBotInlineMessageMediaContact.html) = \['phone_number' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'vcard' => [string](/API_docs/types/string.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageMediaContact"></a>  

***
<br><br>[$inputBotInlineMessageMediaGeo](/API_docs/constructors/inputBotInlineMessageMediaGeo.html) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), 'heading' => [int](/API_docs/types/int.html), 'period' => [int](/API_docs/types/int.html), 'proximity_notification_radius' => [int](/API_docs/types/int.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageMediaGeo"></a>  

***
<br><br>[$inputBotInlineMessageMediaInvoice](/API_docs/constructors/inputBotInlineMessageMediaInvoice.html) = \['title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [InputWebDocument](/API_docs/types/InputWebDocument.html), 'invoice' => [Invoice](/API_docs/types/Invoice.html), 'payload' => [bytes](/API_docs/types/bytes.html), 'provider' => [string](/API_docs/types/string.html), 'provider_data' => [DataJSON](/API_docs/types/DataJSON.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageMediaInvoice"></a>  

***
<br><br>[$inputBotInlineMessageMediaVenue](/API_docs/constructors/inputBotInlineMessageMediaVenue.html) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), 'title' => [string](/API_docs/types/string.html), 'address' => [string](/API_docs/types/string.html), 'provider' => [string](/API_docs/types/string.html), 'venue_id' => [string](/API_docs/types/string.html), 'venue_type' => [string](/API_docs/types/string.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageMediaVenue"></a>  

***
<br><br>[$inputBotInlineMessageText](/API_docs/constructors/inputBotInlineMessageText.html) = \['no_webpage' => [Bool](/API_docs/types/Bool.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), \];<a name="inputBotInlineMessageText"></a>  

***
<br><br>[$inputBotInlineResult](/API_docs/constructors/inputBotInlineResult.html) = \['id' => [string](/API_docs/types/string.html), 'type' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), 'thumb' => [InputWebDocument](/API_docs/types/InputWebDocument.html), 'content' => [InputWebDocument](/API_docs/types/InputWebDocument.html), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html), \];<a name="inputBotInlineResult"></a>  

***
<br><br>[$inputBotInlineResultDocument](/API_docs/constructors/inputBotInlineResultDocument.html) = \['id' => [string](/API_docs/types/string.html), 'type' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'document' => [InputDocument](/API_docs/types/InputDocument.html), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html), \];<a name="inputBotInlineResultDocument"></a>  

***
<br><br>[$inputBotInlineResultGame](/API_docs/constructors/inputBotInlineResultGame.html) = \['id' => [string](/API_docs/types/string.html), 'short_name' => [string](/API_docs/types/string.html), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html), \];<a name="inputBotInlineResultGame"></a>  

***
<br><br>[$inputBotInlineResultPhoto](/API_docs/constructors/inputBotInlineResultPhoto.html) = \['id' => [string](/API_docs/types/string.html), 'type' => [string](/API_docs/types/string.html), 'photo' => [InputPhoto](/API_docs/types/InputPhoto.html), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html), \];<a name="inputBotInlineResultPhoto"></a>  

***
<br><br>[$inputChannel](/API_docs/constructors/inputChannel.html) = \['channel_id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputChannel"></a>  

***
<br><br>[$inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.html) = \[\];<a name="inputChannelEmpty"></a>  

***
<br><br>[$inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'msg_id' => [int](/API_docs/types/int.html), 'channel_id' => [long](/API_docs/types/long.html), \];<a name="inputChannelFromMessage"></a>  

***
<br><br>[$inputChatPhoto](/API_docs/constructors/inputChatPhoto.html) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.html), \];<a name="inputChatPhoto"></a>  

***
<br><br>[$inputChatPhotoEmpty](/API_docs/constructors/inputChatPhotoEmpty.html) = \[\];<a name="inputChatPhotoEmpty"></a>  

***
<br><br>[$inputChatUploadedPhoto](/API_docs/constructors/inputChatUploadedPhoto.html) = \['file' => [InputFile](/API_docs/types/InputFile.html), 'video' => [InputFile](/API_docs/types/InputFile.html), 'video_start_ts' => [double](/API_docs/types/double.html), \];<a name="inputChatUploadedPhoto"></a>  

***
<br><br>[$inputCheckPasswordEmpty](/API_docs/constructors/inputCheckPasswordEmpty.html) = \[\];<a name="inputCheckPasswordEmpty"></a>  

***
<br><br>[$inputCheckPasswordSRP](/API_docs/constructors/inputCheckPasswordSRP.html) = \['srp_id' => [long](/API_docs/types/long.html), 'A' => [bytes](/API_docs/types/bytes.html), 'M1' => [bytes](/API_docs/types/bytes.html), \];<a name="inputCheckPasswordSRP"></a>  

***
<br><br>[$inputClientProxy](/API_docs/constructors/inputClientProxy.html) = \['address' => [string](/API_docs/types/string.html), 'port' => [int](/API_docs/types/int.html), \];<a name="inputClientProxy"></a>  

***
<br><br>[$inputDialogPeer](/API_docs/constructors/inputDialogPeer.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), \];<a name="inputDialogPeer"></a>  

***
<br><br>[$inputDialogPeerFolder](/API_docs/constructors/inputDialogPeerFolder.html) = \['folder_id' => [int](/API_docs/types/int.html), \];<a name="inputDialogPeerFolder"></a>  

***
<br><br>[$inputDocument](/API_docs/constructors/inputDocument.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), \];<a name="inputDocument"></a>  

***
<br><br>[$inputDocumentEmpty](/API_docs/constructors/inputDocumentEmpty.html) = \[\];<a name="inputDocumentEmpty"></a>  

***
<br><br>[$inputDocumentFileLocation](/API_docs/constructors/inputDocumentFileLocation.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), 'thumb_size' => [string](/API_docs/types/string.html), \];<a name="inputDocumentFileLocation"></a>  

***
<br><br>[$inputEncryptedChat](/API_docs/constructors/inputEncryptedChat.html) = \['chat_id' => [int](/API_docs/types/int.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputEncryptedChat"></a>  

***
<br><br>[$inputEncryptedFile](/API_docs/constructors/inputEncryptedFile.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputEncryptedFile"></a>  

***
<br><br>[$inputEncryptedFileBigUploaded](/API_docs/constructors/inputEncryptedFileBigUploaded.html) = \['id' => [long](/API_docs/types/long.html), 'parts' => [int](/API_docs/types/int.html), 'key_fingerprint' => [int](/API_docs/types/int.html), \];<a name="inputEncryptedFileBigUploaded"></a>  

***
<br><br>[$inputEncryptedFileEmpty](/API_docs/constructors/inputEncryptedFileEmpty.html) = \[\];<a name="inputEncryptedFileEmpty"></a>  

***
<br><br>[$inputEncryptedFileLocation](/API_docs/constructors/inputEncryptedFileLocation.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputEncryptedFileLocation"></a>  

***
<br><br>[$inputEncryptedFileUploaded](/API_docs/constructors/inputEncryptedFileUploaded.html) = \['id' => [long](/API_docs/types/long.html), 'parts' => [int](/API_docs/types/int.html), 'md5_checksum' => [string](/API_docs/types/string.html), 'key_fingerprint' => [int](/API_docs/types/int.html), \];<a name="inputEncryptedFileUploaded"></a>  

***
<br><br>[$inputFile](/API_docs/constructors/inputFile.html) = \['id' => [long](/API_docs/types/long.html), 'parts' => [int](/API_docs/types/int.html), 'name' => [string](/API_docs/types/string.html), 'md5_checksum' => [string](/API_docs/types/string.html), \];<a name="inputFile"></a>  

***
<br><br>[$inputFileBig](/API_docs/constructors/inputFileBig.html) = \['id' => [long](/API_docs/types/long.html), 'parts' => [int](/API_docs/types/int.html), 'name' => [string](/API_docs/types/string.html), \];<a name="inputFileBig"></a>  

***
<br><br>[$inputFileLocation](/API_docs/constructors/inputFileLocation.html) = \['volume_id' => [long](/API_docs/types/long.html), 'local_id' => [int](/API_docs/types/int.html), 'secret' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), \];<a name="inputFileLocation"></a>  

***
<br><br>[$inputFolderPeer](/API_docs/constructors/inputFolderPeer.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'folder_id' => [int](/API_docs/types/int.html), \];<a name="inputFolderPeer"></a>  

***
<br><br>[$inputGameID](/API_docs/constructors/inputGameID.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputGameID"></a>  

***
<br><br>[$inputGameShortName](/API_docs/constructors/inputGameShortName.html) = \['bot_id' => [InputUser](/API_docs/types/InputUser.html), 'short_name' => [string](/API_docs/types/string.html), \];<a name="inputGameShortName"></a>  

***
<br><br>[$inputGeoPoint](/API_docs/constructors/inputGeoPoint.html) = \['lat' => [double](/API_docs/types/double.html), 'long' => [double](/API_docs/types/double.html), 'accuracy_radius' => [int](/API_docs/types/int.html), \];<a name="inputGeoPoint"></a>  

***
<br><br>[$inputGeoPointEmpty](/API_docs/constructors/inputGeoPointEmpty.html) = \[\];<a name="inputGeoPointEmpty"></a>  

***
<br><br>[$inputGroupCall](/API_docs/constructors/inputGroupCall.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputGroupCall"></a>  

***
<br><br>[$inputGroupCallStream](/API_docs/constructors/inputGroupCallStream.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'time_ms' => [long](/API_docs/types/long.html), 'scale' => [int](/API_docs/types/int.html), 'video_channel' => [int](/API_docs/types/int.html), 'video_quality' => [int](/API_docs/types/int.html), \];<a name="inputGroupCallStream"></a>  

***
<br><br>[$inputInvoiceMessage](/API_docs/constructors/inputInvoiceMessage.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'msg_id' => [int](/API_docs/types/int.html), \];<a name="inputInvoiceMessage"></a>  

***
<br><br>[$inputInvoiceSlug](/API_docs/constructors/inputInvoiceSlug.html) = \['slug' => [string](/API_docs/types/string.html), \];<a name="inputInvoiceSlug"></a>  

***
<br><br>[$inputKeyboardButtonUrlAuth](/API_docs/constructors/inputKeyboardButtonUrlAuth.html) = \['request_write_access' => [Bool](/API_docs/types/Bool.html), 'text' => [string](/API_docs/types/string.html), 'fwd_text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), 'bot' => [InputUser](/API_docs/types/InputUser.html), \];<a name="inputKeyboardButtonUrlAuth"></a>  

***
<br><br>[$inputKeyboardButtonUserProfile](/API_docs/constructors/inputKeyboardButtonUserProfile.html) = \['text' => [string](/API_docs/types/string.html), 'user_id' => [InputUser](/API_docs/types/InputUser.html), \];<a name="inputKeyboardButtonUserProfile"></a>  

***
<br><br>[$inputMediaContact](/API_docs/constructors/inputMediaContact.html) = \['phone_number' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'vcard' => [string](/API_docs/types/string.html), \];<a name="inputMediaContact"></a>  

***
<br><br>[$inputMediaDice](/API_docs/constructors/inputMediaDice.html) = \['emoticon' => [string](/API_docs/types/string.html), \];<a name="inputMediaDice"></a>  

***
<br><br>[$inputMediaDocument](/API_docs/constructors/inputMediaDocument.html) = \['id' => [InputDocument](/API_docs/types/InputDocument.html), 'ttl_seconds' => [int](/API_docs/types/int.html), 'query' => [string](/API_docs/types/string.html), \];<a name="inputMediaDocument"></a>  

***
<br><br>[$inputMediaDocumentExternal](/API_docs/constructors/inputMediaDocumentExternal.html) = \['url' => [string](/API_docs/types/string.html), 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="inputMediaDocumentExternal"></a>  

***
<br><br>[$inputMediaEmpty](/API_docs/constructors/inputMediaEmpty.html) = \[\];<a name="inputMediaEmpty"></a>  

***
<br><br>[$inputMediaGame](/API_docs/constructors/inputMediaGame.html) = \['id' => [InputGame](/API_docs/types/InputGame.html), \];<a name="inputMediaGame"></a>  

***
<br><br>[$inputMediaGeoLive](/API_docs/constructors/inputMediaGeoLive.html) = \['stopped' => [Bool](/API_docs/types/Bool.html), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), 'heading' => [int](/API_docs/types/int.html), 'period' => [int](/API_docs/types/int.html), 'proximity_notification_radius' => [int](/API_docs/types/int.html), \];<a name="inputMediaGeoLive"></a>  

***
<br><br>[$inputMediaGeoPoint](/API_docs/constructors/inputMediaGeoPoint.html) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), \];<a name="inputMediaGeoPoint"></a>  

***
<br><br>[$inputMediaInvoice](/API_docs/constructors/inputMediaInvoice.html) = \['title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [InputWebDocument](/API_docs/types/InputWebDocument.html), 'invoice' => [Invoice](/API_docs/types/Invoice.html), 'payload' => [bytes](/API_docs/types/bytes.html), 'provider' => [string](/API_docs/types/string.html), 'provider_data' => [DataJSON](/API_docs/types/DataJSON.html), 'start_param' => [string](/API_docs/types/string.html), \];<a name="inputMediaInvoice"></a>  

***
<br><br>[$inputMediaPhoto](/API_docs/constructors/inputMediaPhoto.html) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.html), 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="inputMediaPhoto"></a>  

***
<br><br>[$inputMediaPhotoExternal](/API_docs/constructors/inputMediaPhotoExternal.html) = \['url' => [string](/API_docs/types/string.html), 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="inputMediaPhotoExternal"></a>  

***
<br><br>[$inputMediaPoll](/API_docs/constructors/inputMediaPoll.html) = \['poll' => [Poll](/API_docs/types/Poll.html), 'correct_answers' => \[[bytes](/API_docs/types/bytes.html)\], 'solution' => [string](/API_docs/types/string.html), 'solution_entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="inputMediaPoll"></a>  

***
<br><br>[$inputMediaUploadedDocument](/API_docs/constructors/inputMediaUploadedDocument.html) = \['nosound_video' => [Bool](/API_docs/types/Bool.html), 'force_file' => [Bool](/API_docs/types/Bool.html), 'file' => [InputFile](/API_docs/types/InputFile.html), 'thumb' => [InputFile](/API_docs/types/InputFile.html), 'mime_type' => [string](/API_docs/types/string.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], 'stickers' => \[[InputDocument](/API_docs/types/InputDocument.html)\], 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="inputMediaUploadedDocument"></a>  

***
<br><br>[$inputMediaUploadedPhoto](/API_docs/constructors/inputMediaUploadedPhoto.html) = \['file' => [InputFile](/API_docs/types/InputFile.html), 'stickers' => \[[InputDocument](/API_docs/types/InputDocument.html)\], 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="inputMediaUploadedPhoto"></a>  

***
<br><br>[$inputMediaVenue](/API_docs/constructors/inputMediaVenue.html) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), 'title' => [string](/API_docs/types/string.html), 'address' => [string](/API_docs/types/string.html), 'provider' => [string](/API_docs/types/string.html), 'venue_id' => [string](/API_docs/types/string.html), 'venue_type' => [string](/API_docs/types/string.html), \];<a name="inputMediaVenue"></a>  

***
<br><br>[$inputMessageCallbackQuery](/API_docs/constructors/inputMessageCallbackQuery.html) = \['id' => [int](/API_docs/types/int.html), 'query_id' => [long](/API_docs/types/long.html), \];<a name="inputMessageCallbackQuery"></a>  

***
<br><br>[$inputMessageEntityMentionName](/API_docs/constructors/inputMessageEntityMentionName.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), 'user_id' => [InputUser](/API_docs/types/InputUser.html), \];<a name="inputMessageEntityMentionName"></a>  

***
<br><br>[$inputMessageID](/API_docs/constructors/inputMessageID.html) = \['id' => [int](/API_docs/types/int.html), \];<a name="inputMessageID"></a>  

***
<br><br>[$inputMessagePinned](/API_docs/constructors/inputMessagePinned.html) = \[\];<a name="inputMessagePinned"></a>  

***
<br><br>[$inputMessageReplyTo](/API_docs/constructors/inputMessageReplyTo.html) = \['id' => [int](/API_docs/types/int.html), \];<a name="inputMessageReplyTo"></a>  

***
<br><br>[$inputMessagesFilterChatPhotos](/API_docs/constructors/inputMessagesFilterChatPhotos.html) = \[\];<a name="inputMessagesFilterChatPhotos"></a>  

***
<br><br>[$inputMessagesFilterContacts](/API_docs/constructors/inputMessagesFilterContacts.html) = \[\];<a name="inputMessagesFilterContacts"></a>  

***
<br><br>[$inputMessagesFilterDocument](/API_docs/constructors/inputMessagesFilterDocument.html) = \[\];<a name="inputMessagesFilterDocument"></a>  

***
<br><br>[$inputMessagesFilterEmpty](/API_docs/constructors/inputMessagesFilterEmpty.html) = \[\];<a name="inputMessagesFilterEmpty"></a>  

***
<br><br>[$inputMessagesFilterGeo](/API_docs/constructors/inputMessagesFilterGeo.html) = \[\];<a name="inputMessagesFilterGeo"></a>  

***
<br><br>[$inputMessagesFilterGif](/API_docs/constructors/inputMessagesFilterGif.html) = \[\];<a name="inputMessagesFilterGif"></a>  

***
<br><br>[$inputMessagesFilterMusic](/API_docs/constructors/inputMessagesFilterMusic.html) = \[\];<a name="inputMessagesFilterMusic"></a>  

***
<br><br>[$inputMessagesFilterMyMentions](/API_docs/constructors/inputMessagesFilterMyMentions.html) = \[\];<a name="inputMessagesFilterMyMentions"></a>  

***
<br><br>[$inputMessagesFilterPhoneCalls](/API_docs/constructors/inputMessagesFilterPhoneCalls.html) = \['missed' => [Bool](/API_docs/types/Bool.html), \];<a name="inputMessagesFilterPhoneCalls"></a>  

***
<br><br>[$inputMessagesFilterPhotoVideo](/API_docs/constructors/inputMessagesFilterPhotoVideo.html) = \[\];<a name="inputMessagesFilterPhotoVideo"></a>  

***
<br><br>[$inputMessagesFilterPhotos](/API_docs/constructors/inputMessagesFilterPhotos.html) = \[\];<a name="inputMessagesFilterPhotos"></a>  

***
<br><br>[$inputMessagesFilterPinned](/API_docs/constructors/inputMessagesFilterPinned.html) = \[\];<a name="inputMessagesFilterPinned"></a>  

***
<br><br>[$inputMessagesFilterRoundVideo](/API_docs/constructors/inputMessagesFilterRoundVideo.html) = \[\];<a name="inputMessagesFilterRoundVideo"></a>  

***
<br><br>[$inputMessagesFilterRoundVoice](/API_docs/constructors/inputMessagesFilterRoundVoice.html) = \[\];<a name="inputMessagesFilterRoundVoice"></a>  

***
<br><br>[$inputMessagesFilterUrl](/API_docs/constructors/inputMessagesFilterUrl.html) = \[\];<a name="inputMessagesFilterUrl"></a>  

***
<br><br>[$inputMessagesFilterVideo](/API_docs/constructors/inputMessagesFilterVideo.html) = \[\];<a name="inputMessagesFilterVideo"></a>  

***
<br><br>[$inputMessagesFilterVoice](/API_docs/constructors/inputMessagesFilterVoice.html) = \[\];<a name="inputMessagesFilterVoice"></a>  

***
<br><br>[$inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.html) = \[\];<a name="inputNotifyBroadcasts"></a>  

***
<br><br>[$inputNotifyChats](/API_docs/constructors/inputNotifyChats.html) = \[\];<a name="inputNotifyChats"></a>  

***
<br><br>[$inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), \];<a name="inputNotifyPeer"></a>  

***
<br><br>[$inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.html) = \[\];<a name="inputNotifyUsers"></a>  

***
<br><br>[$inputPaymentCredentials](/API_docs/constructors/inputPaymentCredentials.html) = \['save' => [Bool](/API_docs/types/Bool.html), 'data' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="inputPaymentCredentials"></a>  

***
<br><br>[$inputPaymentCredentialsApplePay](/API_docs/constructors/inputPaymentCredentialsApplePay.html) = \['payment_data' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="inputPaymentCredentialsApplePay"></a>  

***
<br><br>[$inputPaymentCredentialsGooglePay](/API_docs/constructors/inputPaymentCredentialsGooglePay.html) = \['payment_token' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="inputPaymentCredentialsGooglePay"></a>  

***
<br><br>[$inputPaymentCredentialsSaved](/API_docs/constructors/inputPaymentCredentialsSaved.html) = \['id' => [string](/API_docs/types/string.html), 'tmp_password' => [bytes](/API_docs/types/bytes.html), \];<a name="inputPaymentCredentialsSaved"></a>  

***
<br><br>[$inputPeerChannel](/API_docs/constructors/inputPeerChannel.html) = \['channel_id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputPeerChannel"></a>  

***
<br><br>[$inputPeerChannelFromMessage](/API_docs/constructors/inputPeerChannelFromMessage.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'msg_id' => [int](/API_docs/types/int.html), 'channel_id' => [long](/API_docs/types/long.html), \];<a name="inputPeerChannelFromMessage"></a>  

***
<br><br>[$inputPeerChat](/API_docs/constructors/inputPeerChat.html) = \['chat_id' => [long](/API_docs/types/long.html), \];<a name="inputPeerChat"></a>  

***
<br><br>[$inputPeerEmpty](/API_docs/constructors/inputPeerEmpty.html) = \[\];<a name="inputPeerEmpty"></a>  

***
<br><br>[$inputPeerNotifySettings](/API_docs/constructors/inputPeerNotifySettings.html) = \['show_previews' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'mute_until' => [int](/API_docs/types/int.html), 'sound' => [NotificationSound](/API_docs/types/NotificationSound.html), \];<a name="inputPeerNotifySettings"></a>  

***
<br><br>[$inputPeerPhotoFileLocation](/API_docs/constructors/inputPeerPhotoFileLocation.html) = \['big' => [Bool](/API_docs/types/Bool.html), 'peer' => [InputPeer](/API_docs/types/InputPeer.html), 'photo_id' => [long](/API_docs/types/long.html), \];<a name="inputPeerPhotoFileLocation"></a>  

***
<br><br>[$inputPeerSelf](/API_docs/constructors/inputPeerSelf.html) = \[\];<a name="inputPeerSelf"></a>  

***
<br><br>[$inputPeerUser](/API_docs/constructors/inputPeerUser.html) = \['user_id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputPeerUser"></a>  

***
<br><br>[$inputPeerUserFromMessage](/API_docs/constructors/inputPeerUserFromMessage.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'msg_id' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="inputPeerUserFromMessage"></a>  

***
<br><br>[$inputPhoneCall](/API_docs/constructors/inputPhoneCall.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputPhoneCall"></a>  

***
<br><br>[$inputPhoneContact](/API_docs/constructors/inputPhoneContact.html) = \['client_id' => [long](/API_docs/types/long.html), 'phone' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), \];<a name="inputPhoneContact"></a>  

***
<br><br>[$inputPhoto](/API_docs/constructors/inputPhoto.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), \];<a name="inputPhoto"></a>  

***
<br><br>[$inputPhotoEmpty](/API_docs/constructors/inputPhotoEmpty.html) = \[\];<a name="inputPhotoEmpty"></a>  

***
<br><br>[$inputPhotoFileLocation](/API_docs/constructors/inputPhotoFileLocation.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), 'thumb_size' => [string](/API_docs/types/string.html), \];<a name="inputPhotoFileLocation"></a>  

***
<br><br>[$inputPhotoLegacyFileLocation](/API_docs/constructors/inputPhotoLegacyFileLocation.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), 'volume_id' => [long](/API_docs/types/long.html), 'local_id' => [int](/API_docs/types/int.html), 'secret' => [long](/API_docs/types/long.html), \];<a name="inputPhotoLegacyFileLocation"></a>  

***
<br><br>[$inputPrivacyKeyAddedByPhone](/API_docs/constructors/inputPrivacyKeyAddedByPhone.html) = \[\];<a name="inputPrivacyKeyAddedByPhone"></a>  

***
<br><br>[$inputPrivacyKeyChatInvite](/API_docs/constructors/inputPrivacyKeyChatInvite.html) = \[\];<a name="inputPrivacyKeyChatInvite"></a>  

***
<br><br>[$inputPrivacyKeyForwards](/API_docs/constructors/inputPrivacyKeyForwards.html) = \[\];<a name="inputPrivacyKeyForwards"></a>  

***
<br><br>[$inputPrivacyKeyPhoneCall](/API_docs/constructors/inputPrivacyKeyPhoneCall.html) = \[\];<a name="inputPrivacyKeyPhoneCall"></a>  

***
<br><br>[$inputPrivacyKeyPhoneNumber](/API_docs/constructors/inputPrivacyKeyPhoneNumber.html) = \[\];<a name="inputPrivacyKeyPhoneNumber"></a>  

***
<br><br>[$inputPrivacyKeyPhoneP2P](/API_docs/constructors/inputPrivacyKeyPhoneP2P.html) = \[\];<a name="inputPrivacyKeyPhoneP2P"></a>  

***
<br><br>[$inputPrivacyKeyProfilePhoto](/API_docs/constructors/inputPrivacyKeyProfilePhoto.html) = \[\];<a name="inputPrivacyKeyProfilePhoto"></a>  

***
<br><br>[$inputPrivacyKeyStatusTimestamp](/API_docs/constructors/inputPrivacyKeyStatusTimestamp.html) = \[\];<a name="inputPrivacyKeyStatusTimestamp"></a>  

***
<br><br>[$inputPrivacyValueAllowAll](/API_docs/constructors/inputPrivacyValueAllowAll.html) = \[\];<a name="inputPrivacyValueAllowAll"></a>  

***
<br><br>[$inputPrivacyValueAllowChatParticipants](/API_docs/constructors/inputPrivacyValueAllowChatParticipants.html) = \['chats' => \[[long](/API_docs/types/long.html)\], \];<a name="inputPrivacyValueAllowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueAllowContacts](/API_docs/constructors/inputPrivacyValueAllowContacts.html) = \[\];<a name="inputPrivacyValueAllowContacts"></a>  

***
<br><br>[$inputPrivacyValueAllowUsers](/API_docs/constructors/inputPrivacyValueAllowUsers.html) = \['users' => \[[InputUser](/API_docs/types/InputUser.html)\], \];<a name="inputPrivacyValueAllowUsers"></a>  

***
<br><br>[$inputPrivacyValueDisallowAll](/API_docs/constructors/inputPrivacyValueDisallowAll.html) = \[\];<a name="inputPrivacyValueDisallowAll"></a>  

***
<br><br>[$inputPrivacyValueDisallowChatParticipants](/API_docs/constructors/inputPrivacyValueDisallowChatParticipants.html) = \['chats' => \[[long](/API_docs/types/long.html)\], \];<a name="inputPrivacyValueDisallowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueDisallowContacts](/API_docs/constructors/inputPrivacyValueDisallowContacts.html) = \[\];<a name="inputPrivacyValueDisallowContacts"></a>  

***
<br><br>[$inputPrivacyValueDisallowUsers](/API_docs/constructors/inputPrivacyValueDisallowUsers.html) = \['users' => \[[InputUser](/API_docs/types/InputUser.html)\], \];<a name="inputPrivacyValueDisallowUsers"></a>  

***
<br><br>[$inputReportReasonChildAbuse](/API_docs/constructors/inputReportReasonChildAbuse.html) = \[\];<a name="inputReportReasonChildAbuse"></a>  

***
<br><br>[$inputReportReasonCopyright](/API_docs/constructors/inputReportReasonCopyright.html) = \[\];<a name="inputReportReasonCopyright"></a>  

***
<br><br>[$inputReportReasonFake](/API_docs/constructors/inputReportReasonFake.html) = \[\];<a name="inputReportReasonFake"></a>  

***
<br><br>[$inputReportReasonGeoIrrelevant](/API_docs/constructors/inputReportReasonGeoIrrelevant.html) = \[\];<a name="inputReportReasonGeoIrrelevant"></a>  

***
<br><br>[$inputReportReasonIllegalDrugs](/API_docs/constructors/inputReportReasonIllegalDrugs.html) = \[\];<a name="inputReportReasonIllegalDrugs"></a>  

***
<br><br>[$inputReportReasonOther](/API_docs/constructors/inputReportReasonOther.html) = \[\];<a name="inputReportReasonOther"></a>  

***
<br><br>[$inputReportReasonPersonalDetails](/API_docs/constructors/inputReportReasonPersonalDetails.html) = \[\];<a name="inputReportReasonPersonalDetails"></a>  

***
<br><br>[$inputReportReasonPornography](/API_docs/constructors/inputReportReasonPornography.html) = \[\];<a name="inputReportReasonPornography"></a>  

***
<br><br>[$inputReportReasonSpam](/API_docs/constructors/inputReportReasonSpam.html) = \[\];<a name="inputReportReasonSpam"></a>  

***
<br><br>[$inputReportReasonViolence](/API_docs/constructors/inputReportReasonViolence.html) = \[\];<a name="inputReportReasonViolence"></a>  

***
<br><br>[$inputSecureFile](/API_docs/constructors/inputSecureFile.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputSecureFile"></a>  

***
<br><br>[$inputSecureFileLocation](/API_docs/constructors/inputSecureFileLocation.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputSecureFileLocation"></a>  

***
<br><br>[$inputSecureFileUploaded](/API_docs/constructors/inputSecureFileUploaded.html) = \['id' => [long](/API_docs/types/long.html), 'parts' => [int](/API_docs/types/int.html), 'md5_checksum' => [string](/API_docs/types/string.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'secret' => [bytes](/API_docs/types/bytes.html), \];<a name="inputSecureFileUploaded"></a>  

***
<br><br>[$inputSecureValue](/API_docs/constructors/inputSecureValue.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'data' => [SecureData](/API_docs/types/SecureData.html), 'front_side' => [InputSecureFile](/API_docs/types/InputSecureFile.html), 'reverse_side' => [InputSecureFile](/API_docs/types/InputSecureFile.html), 'selfie' => [InputSecureFile](/API_docs/types/InputSecureFile.html), 'translation' => \[[InputSecureFile](/API_docs/types/InputSecureFile.html)\], 'files' => \[[InputSecureFile](/API_docs/types/InputSecureFile.html)\], 'plain_data' => [SecurePlainData](/API_docs/types/SecurePlainData.html), \];<a name="inputSecureValue"></a>  

***
<br><br>[$inputSingleMedia](/API_docs/constructors/inputSingleMedia.html) = \['media' => [InputMedia](/API_docs/types/InputMedia.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="inputSingleMedia"></a>  

***
<br><br>[$inputStickerSetAnimatedEmoji](/API_docs/constructors/inputStickerSetAnimatedEmoji.html) = \[\];<a name="inputStickerSetAnimatedEmoji"></a>  

***
<br><br>[$inputStickerSetAnimatedEmojiAnimations](/API_docs/constructors/inputStickerSetAnimatedEmojiAnimations.html) = \[\];<a name="inputStickerSetAnimatedEmojiAnimations"></a>  

***
<br><br>[$inputStickerSetDice](/API_docs/constructors/inputStickerSetDice.html) = \['emoticon' => [string](/API_docs/types/string.html), \];<a name="inputStickerSetDice"></a>  

***
<br><br>[$inputStickerSetEmpty](/API_docs/constructors/inputStickerSetEmpty.html) = \[\];<a name="inputStickerSetEmpty"></a>  

***
<br><br>[$inputStickerSetID](/API_docs/constructors/inputStickerSetID.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputStickerSetID"></a>  

***
<br><br>[$inputStickerSetItem](/API_docs/constructors/inputStickerSetItem.html) = \['document' => [InputDocument](/API_docs/types/InputDocument.html), 'emoji' => [string](/API_docs/types/string.html), 'mask_coords' => [MaskCoords](/API_docs/types/MaskCoords.html), \];<a name="inputStickerSetItem"></a>  

***
<br><br>[$inputStickerSetShortName](/API_docs/constructors/inputStickerSetShortName.html) = \['short_name' => [string](/API_docs/types/string.html), \];<a name="inputStickerSetShortName"></a>  

***
<br><br>[$inputStickerSetThumb](/API_docs/constructors/inputStickerSetThumb.html) = \['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.html), 'thumb_version' => [int](/API_docs/types/int.html), \];<a name="inputStickerSetThumb"></a>  

***
<br><br>[$inputStickeredMediaDocument](/API_docs/constructors/inputStickeredMediaDocument.html) = \['id' => [InputDocument](/API_docs/types/InputDocument.html), \];<a name="inputStickeredMediaDocument"></a>  

***
<br><br>[$inputStickeredMediaPhoto](/API_docs/constructors/inputStickeredMediaPhoto.html) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.html), \];<a name="inputStickeredMediaPhoto"></a>  

***
<br><br>[$inputTakeoutFileLocation](/API_docs/constructors/inputTakeoutFileLocation.html) = \[\];<a name="inputTakeoutFileLocation"></a>  

***
<br><br>[$inputTheme](/API_docs/constructors/inputTheme.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputTheme"></a>  

***
<br><br>[$inputThemeSettings](/API_docs/constructors/inputThemeSettings.html) = \['message_colors_animated' => [Bool](/API_docs/types/Bool.html), 'base_theme' => [BaseTheme](/API_docs/types/BaseTheme.html), 'accent_color' => [int](/API_docs/types/int.html), 'outbox_accent_color' => [int](/API_docs/types/int.html), 'message_colors' => \[[int](/API_docs/types/int.html)\], 'wallpaper' => [InputWallPaper](/API_docs/types/InputWallPaper.html), 'wallpaper_settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \];<a name="inputThemeSettings"></a>  

***
<br><br>[$inputThemeSlug](/API_docs/constructors/inputThemeSlug.html) = \['slug' => [string](/API_docs/types/string.html), \];<a name="inputThemeSlug"></a>  

***
<br><br>[$inputUser](/API_docs/constructors/inputUser.html) = \['user_id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputUser"></a>  

***
<br><br>[$inputUserEmpty](/API_docs/constructors/inputUserEmpty.html) = \[\];<a name="inputUserEmpty"></a>  

***
<br><br>[$inputUserFromMessage](/API_docs/constructors/inputUserFromMessage.html) = \['peer' => [InputPeer](/API_docs/types/InputPeer.html), 'msg_id' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="inputUserFromMessage"></a>  

***
<br><br>[$inputUserSelf](/API_docs/constructors/inputUserSelf.html) = \[\];<a name="inputUserSelf"></a>  

***
<br><br>[$inputWallPaper](/API_docs/constructors/inputWallPaper.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputWallPaper"></a>  

***
<br><br>[$inputWallPaperNoFile](/API_docs/constructors/inputWallPaperNoFile.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="inputWallPaperNoFile"></a>  

***
<br><br>[$inputWallPaperSlug](/API_docs/constructors/inputWallPaperSlug.html) = \['slug' => [string](/API_docs/types/string.html), \];<a name="inputWallPaperSlug"></a>  

***
<br><br>[$inputWebDocument](/API_docs/constructors/inputWebDocument.html) = \['url' => [string](/API_docs/types/string.html), 'size' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], \];<a name="inputWebDocument"></a>  

***
<br><br>[$inputWebFileGeoPointLocation](/API_docs/constructors/inputWebFileGeoPointLocation.html) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.html), 'access_hash' => [long](/API_docs/types/long.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'zoom' => [int](/API_docs/types/int.html), 'scale' => [int](/API_docs/types/int.html), \];<a name="inputWebFileGeoPointLocation"></a>  

***
<br><br>[$inputWebFileLocation](/API_docs/constructors/inputWebFileLocation.html) = \['url' => [string](/API_docs/types/string.html), 'access_hash' => [long](/API_docs/types/long.html), \];<a name="inputWebFileLocation"></a>  

***
<br><br>[$invoice](/API_docs/constructors/invoice.html) = \['test' => [Bool](/API_docs/types/Bool.html), 'name_requested' => [Bool](/API_docs/types/Bool.html), 'phone_requested' => [Bool](/API_docs/types/Bool.html), 'email_requested' => [Bool](/API_docs/types/Bool.html), 'shipping_address_requested' => [Bool](/API_docs/types/Bool.html), 'flexible' => [Bool](/API_docs/types/Bool.html), 'phone_to_provider' => [Bool](/API_docs/types/Bool.html), 'email_to_provider' => [Bool](/API_docs/types/Bool.html), 'recurring' => [Bool](/API_docs/types/Bool.html), 'currency' => [string](/API_docs/types/string.html), 'prices' => \[[LabeledPrice](/API_docs/types/LabeledPrice.html)\], 'max_tip_amount' => [long](/API_docs/types/long.html), 'suggested_tip_amounts' => \[[long](/API_docs/types/long.html)\], 'recurring_terms_url' => [string](/API_docs/types/string.html), \];<a name="invoice"></a>  

***
<br><br>[$jsonArray](/API_docs/constructors/jsonArray.html) = \['value' => \[[JSONValue](/API_docs/types/JSONValue.html)\], \];<a name="jsonArray"></a>  

***
<br><br>[$jsonBool](/API_docs/constructors/jsonBool.html) = \['value' => [Bool](/API_docs/types/Bool.html), \];<a name="jsonBool"></a>  

***
<br><br>[$jsonNull](/API_docs/constructors/jsonNull.html) = \[\];<a name="jsonNull"></a>  

***
<br><br>[$jsonNumber](/API_docs/constructors/jsonNumber.html) = \['value' => [double](/API_docs/types/double.html), \];<a name="jsonNumber"></a>  

***
<br><br>[$jsonObject](/API_docs/constructors/jsonObject.html) = \['value' => \[[JSONObjectValue](/API_docs/types/JSONObjectValue.html)\], \];<a name="jsonObject"></a>  

***
<br><br>[$jsonObjectValue](/API_docs/constructors/jsonObjectValue.html) = \['key' => [string](/API_docs/types/string.html), 'value' => [JSONValue](/API_docs/types/JSONValue.html), \];<a name="jsonObjectValue"></a>  

***
<br><br>[$jsonString](/API_docs/constructors/jsonString.html) = \['value' => [string](/API_docs/types/string.html), \];<a name="jsonString"></a>  

***
<br><br>[$keyboardButton](/API_docs/constructors/keyboardButton.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="keyboardButton"></a>  

***
<br><br>[$keyboardButtonBuy](/API_docs/constructors/keyboardButtonBuy.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonBuy"></a>  

***
<br><br>[$keyboardButtonCallback](/API_docs/constructors/keyboardButtonCallback.html) = \['requires_password' => [Bool](/API_docs/types/Bool.html), 'text' => [string](/API_docs/types/string.html), 'data' => [bytes](/API_docs/types/bytes.html), \];<a name="keyboardButtonCallback"></a>  

***
<br><br>[$keyboardButtonGame](/API_docs/constructors/keyboardButtonGame.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonGame"></a>  

***
<br><br>[$keyboardButtonRequestGeoLocation](/API_docs/constructors/keyboardButtonRequestGeoLocation.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonRequestGeoLocation"></a>  

***
<br><br>[$keyboardButtonRequestPhone](/API_docs/constructors/keyboardButtonRequestPhone.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonRequestPhone"></a>  

***
<br><br>[$keyboardButtonRequestPoll](/API_docs/constructors/keyboardButtonRequestPoll.html) = \['quiz' => [Bool](/API_docs/types/Bool.html), 'text' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonRequestPoll"></a>  

***
<br><br>[$keyboardButtonRow](/API_docs/constructors/keyboardButtonRow.html) = \['buttons' => \[[KeyboardButton](/API_docs/types/KeyboardButton.html)\], \];<a name="keyboardButtonRow"></a>  

***
<br><br>[$keyboardButtonSimpleWebView](/API_docs/constructors/keyboardButtonSimpleWebView.html) = \['text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonSimpleWebView"></a>  

***
<br><br>[$keyboardButtonSwitchInline](/API_docs/constructors/keyboardButtonSwitchInline.html) = \['same_peer' => [Bool](/API_docs/types/Bool.html), 'text' => [string](/API_docs/types/string.html), 'query' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonSwitchInline"></a>  

***
<br><br>[$keyboardButtonUrl](/API_docs/constructors/keyboardButtonUrl.html) = \['text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonUrl"></a>  

***
<br><br>[$keyboardButtonUrlAuth](/API_docs/constructors/keyboardButtonUrlAuth.html) = \['text' => [string](/API_docs/types/string.html), 'fwd_text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), 'button_id' => [int](/API_docs/types/int.html), \];<a name="keyboardButtonUrlAuth"></a>  

***
<br><br>[$keyboardButtonUserProfile](/API_docs/constructors/keyboardButtonUserProfile.html) = \['text' => [string](/API_docs/types/string.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="keyboardButtonUserProfile"></a>  

***
<br><br>[$keyboardButtonWebView](/API_docs/constructors/keyboardButtonWebView.html) = \['text' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), \];<a name="keyboardButtonWebView"></a>  

***
<br><br>[$labeledPrice](/API_docs/constructors/labeledPrice.html) = \['label' => [string](/API_docs/types/string.html), 'amount' => [long](/API_docs/types/long.html), \];<a name="labeledPrice"></a>  

***
<br><br>[$langPackDifference](/API_docs/constructors/langPackDifference.html) = \['lang_code' => [string](/API_docs/types/string.html), 'from_version' => [int](/API_docs/types/int.html), 'version' => [int](/API_docs/types/int.html), 'strings' => \[[LangPackString](/API_docs/types/LangPackString.html)\], \];<a name="langPackDifference"></a>  

***
<br><br>[$langPackLanguage](/API_docs/constructors/langPackLanguage.html) = \['official' => [Bool](/API_docs/types/Bool.html), 'rtl' => [Bool](/API_docs/types/Bool.html), 'beta' => [Bool](/API_docs/types/Bool.html), 'name' => [string](/API_docs/types/string.html), 'native_name' => [string](/API_docs/types/string.html), 'lang_code' => [string](/API_docs/types/string.html), 'base_lang_code' => [string](/API_docs/types/string.html), 'plural_code' => [string](/API_docs/types/string.html), 'strings_count' => [int](/API_docs/types/int.html), 'translated_count' => [int](/API_docs/types/int.html), 'translations_url' => [string](/API_docs/types/string.html), \];<a name="langPackLanguage"></a>  

***
<br><br>[$langPackString](/API_docs/constructors/langPackString.html) = \['key' => [string](/API_docs/types/string.html), 'value' => [string](/API_docs/types/string.html), \];<a name="langPackString"></a>  

***
<br><br>[$langPackStringDeleted](/API_docs/constructors/langPackStringDeleted.html) = \['key' => [string](/API_docs/types/string.html), \];<a name="langPackStringDeleted"></a>  

***
<br><br>[$langPackStringPluralized](/API_docs/constructors/langPackStringPluralized.html) = \['key' => [string](/API_docs/types/string.html), 'zero_value' => [string](/API_docs/types/string.html), 'one_value' => [string](/API_docs/types/string.html), 'two_value' => [string](/API_docs/types/string.html), 'few_value' => [string](/API_docs/types/string.html), 'many_value' => [string](/API_docs/types/string.html), 'other_value' => [string](/API_docs/types/string.html), \];<a name="langPackStringPluralized"></a>  

***
<br><br>[$maskCoords](/API_docs/constructors/maskCoords.html) = \['n' => [int](/API_docs/types/int.html), 'x' => [double](/API_docs/types/double.html), 'y' => [double](/API_docs/types/double.html), 'zoom' => [double](/API_docs/types/double.html), \];<a name="maskCoords"></a>  

***
<br><br>[$message](/API_docs/constructors/message.html) = \['out' => [Bool](/API_docs/types/Bool.html), 'mentioned' => [Bool](/API_docs/types/Bool.html), 'media_unread' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'post' => [Bool](/API_docs/types/Bool.html), 'from_scheduled' => [Bool](/API_docs/types/Bool.html), 'legacy' => [Bool](/API_docs/types/Bool.html), 'edit_hide' => [Bool](/API_docs/types/Bool.html), 'pinned' => [Bool](/API_docs/types/Bool.html), 'noforwards' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'peer_id' => [Peer](/API_docs/types/Peer.html), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.html), 'via_bot_id' => [long](/API_docs/types/long.html), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html), 'date' => [int](/API_docs/types/int.html), 'message' => [string](/API_docs/types/string.html), 'media' => [MessageMedia](/API_docs/types/MessageMedia.html), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'views' => [int](/API_docs/types/int.html), 'forwards' => [int](/API_docs/types/int.html), 'replies' => [MessageReplies](/API_docs/types/MessageReplies.html), 'edit_date' => [int](/API_docs/types/int.html), 'post_author' => [string](/API_docs/types/string.html), 'grouped_id' => [long](/API_docs/types/long.html), 'reactions' => [MessageReactions](/API_docs/types/MessageReactions.html), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.html)\], 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="message"></a>  

***
<br><br>[$messageActionBotAllowed](/API_docs/constructors/messageActionBotAllowed.html) = \['domain' => [string](/API_docs/types/string.html), \];<a name="messageActionBotAllowed"></a>  

***
<br><br>[$messageActionChannelCreate](/API_docs/constructors/messageActionChannelCreate.html) = \['title' => [string](/API_docs/types/string.html), \];<a name="messageActionChannelCreate"></a>  

***
<br><br>[$messageActionChannelMigrateFrom](/API_docs/constructors/messageActionChannelMigrateFrom.html) = \['title' => [string](/API_docs/types/string.html), 'chat_id' => [long](/API_docs/types/long.html), \];<a name="messageActionChannelMigrateFrom"></a>  

***
<br><br>[$messageActionChatAddUser](/API_docs/constructors/messageActionChatAddUser.html) = \['users' => \[[long](/API_docs/types/long.html)\], \];<a name="messageActionChatAddUser"></a>  

***
<br><br>[$messageActionChatCreate](/API_docs/constructors/messageActionChatCreate.html) = \['title' => [string](/API_docs/types/string.html), 'users' => \[[long](/API_docs/types/long.html)\], \];<a name="messageActionChatCreate"></a>  

***
<br><br>[$messageActionChatDeletePhoto](/API_docs/constructors/messageActionChatDeletePhoto.html) = \[\];<a name="messageActionChatDeletePhoto"></a>  

***
<br><br>[$messageActionChatDeleteUser](/API_docs/constructors/messageActionChatDeleteUser.html) = \['user_id' => [long](/API_docs/types/long.html), \];<a name="messageActionChatDeleteUser"></a>  

***
<br><br>[$messageActionChatEditPhoto](/API_docs/constructors/messageActionChatEditPhoto.html) = \['photo' => [Photo](/API_docs/types/Photo.html), \];<a name="messageActionChatEditPhoto"></a>  

***
<br><br>[$messageActionChatEditTitle](/API_docs/constructors/messageActionChatEditTitle.html) = \['title' => [string](/API_docs/types/string.html), \];<a name="messageActionChatEditTitle"></a>  

***
<br><br>[$messageActionChatJoinedByLink](/API_docs/constructors/messageActionChatJoinedByLink.html) = \['inviter_id' => [long](/API_docs/types/long.html), \];<a name="messageActionChatJoinedByLink"></a>  

***
<br><br>[$messageActionChatJoinedByRequest](/API_docs/constructors/messageActionChatJoinedByRequest.html) = \[\];<a name="messageActionChatJoinedByRequest"></a>  

***
<br><br>[$messageActionChatMigrateTo](/API_docs/constructors/messageActionChatMigrateTo.html) = \['channel_id' => [long](/API_docs/types/long.html), \];<a name="messageActionChatMigrateTo"></a>  

***
<br><br>[$messageActionContactSignUp](/API_docs/constructors/messageActionContactSignUp.html) = \[\];<a name="messageActionContactSignUp"></a>  

***
<br><br>[$messageActionCustomAction](/API_docs/constructors/messageActionCustomAction.html) = \['message' => [string](/API_docs/types/string.html), \];<a name="messageActionCustomAction"></a>  

***
<br><br>[$messageActionEmpty](/API_docs/constructors/messageActionEmpty.html) = \[\];<a name="messageActionEmpty"></a>  

***
<br><br>[$messageActionGameScore](/API_docs/constructors/messageActionGameScore.html) = \['game_id' => [long](/API_docs/types/long.html), 'score' => [int](/API_docs/types/int.html), \];<a name="messageActionGameScore"></a>  

***
<br><br>[$messageActionGeoProximityReached](/API_docs/constructors/messageActionGeoProximityReached.html) = \['from_id' => [Peer](/API_docs/types/Peer.html), 'to_id' => [Peer](/API_docs/types/Peer.html), 'distance' => [int](/API_docs/types/int.html), \];<a name="messageActionGeoProximityReached"></a>  

***
<br><br>[$messageActionGroupCall](/API_docs/constructors/messageActionGroupCall.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'duration' => [int](/API_docs/types/int.html), \];<a name="messageActionGroupCall"></a>  

***
<br><br>[$messageActionGroupCallScheduled](/API_docs/constructors/messageActionGroupCallScheduled.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'schedule_date' => [int](/API_docs/types/int.html), \];<a name="messageActionGroupCallScheduled"></a>  

***
<br><br>[$messageActionHistoryClear](/API_docs/constructors/messageActionHistoryClear.html) = \[\];<a name="messageActionHistoryClear"></a>  

***
<br><br>[$messageActionInviteToGroupCall](/API_docs/constructors/messageActionInviteToGroupCall.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'users' => \[[long](/API_docs/types/long.html)\], \];<a name="messageActionInviteToGroupCall"></a>  

***
<br><br>[$messageActionPaymentSent](/API_docs/constructors/messageActionPaymentSent.html) = \['recurring_init' => [Bool](/API_docs/types/Bool.html), 'recurring_used' => [Bool](/API_docs/types/Bool.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), 'invoice_slug' => [string](/API_docs/types/string.html), \];<a name="messageActionPaymentSent"></a>  

***
<br><br>[$messageActionPaymentSentMe](/API_docs/constructors/messageActionPaymentSentMe.html) = \['recurring_init' => [Bool](/API_docs/types/Bool.html), 'recurring_used' => [Bool](/API_docs/types/Bool.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), 'payload' => [bytes](/API_docs/types/bytes.html), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), 'shipping_option_id' => [string](/API_docs/types/string.html), 'charge' => [PaymentCharge](/API_docs/types/PaymentCharge.html), \];<a name="messageActionPaymentSentMe"></a>  

***
<br><br>[$messageActionPhoneCall](/API_docs/constructors/messageActionPhoneCall.html) = \['video' => [Bool](/API_docs/types/Bool.html), 'call_id' => [long](/API_docs/types/long.html), 'reason' => [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html), 'duration' => [int](/API_docs/types/int.html), \];<a name="messageActionPhoneCall"></a>  

***
<br><br>[$messageActionPinMessage](/API_docs/constructors/messageActionPinMessage.html) = \[\];<a name="messageActionPinMessage"></a>  

***
<br><br>[$messageActionScreenshotTaken](/API_docs/constructors/messageActionScreenshotTaken.html) = \[\];<a name="messageActionScreenshotTaken"></a>  

***
<br><br>[$messageActionSecureValuesSent](/API_docs/constructors/messageActionSecureValuesSent.html) = \['types' => \[[SecureValueType](/API_docs/types/SecureValueType.html)\], \];<a name="messageActionSecureValuesSent"></a>  

***
<br><br>[$messageActionSecureValuesSentMe](/API_docs/constructors/messageActionSecureValuesSentMe.html) = \['values' => \[[SecureValue](/API_docs/types/SecureValue.html)\], 'credentials' => [SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.html), \];<a name="messageActionSecureValuesSentMe"></a>  

***
<br><br>[$messageActionSetChatTheme](/API_docs/constructors/messageActionSetChatTheme.html) = \['emoticon' => [string](/API_docs/types/string.html), \];<a name="messageActionSetChatTheme"></a>  

***
<br><br>[$messageActionSetMessagesTTL](/API_docs/constructors/messageActionSetMessagesTTL.html) = \['period' => [int](/API_docs/types/int.html), \];<a name="messageActionSetMessagesTTL"></a>  

***
<br><br>[$messageActionWebViewDataSent](/API_docs/constructors/messageActionWebViewDataSent.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="messageActionWebViewDataSent"></a>  

***
<br><br>[$messageActionWebViewDataSentMe](/API_docs/constructors/messageActionWebViewDataSentMe.html) = \['text' => [string](/API_docs/types/string.html), 'data' => [string](/API_docs/types/string.html), \];<a name="messageActionWebViewDataSentMe"></a>  

***
<br><br>[$messageEmpty](/API_docs/constructors/messageEmpty.html) = \['id' => [int](/API_docs/types/int.html), 'peer_id' => [Peer](/API_docs/types/Peer.html), \];<a name="messageEmpty"></a>  

***
<br><br>[$messageEntityBankCard](/API_docs/constructors/messageEntityBankCard.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityBankCard"></a>  

***
<br><br>[$messageEntityBlockquote](/API_docs/constructors/messageEntityBlockquote.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityBlockquote"></a>  

***
<br><br>[$messageEntityBold](/API_docs/constructors/messageEntityBold.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityBold"></a>  

***
<br><br>[$messageEntityBotCommand](/API_docs/constructors/messageEntityBotCommand.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityBotCommand"></a>  

***
<br><br>[$messageEntityCashtag](/API_docs/constructors/messageEntityCashtag.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityCashtag"></a>  

***
<br><br>[$messageEntityCode](/API_docs/constructors/messageEntityCode.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityCode"></a>  

***
<br><br>[$messageEntityEmail](/API_docs/constructors/messageEntityEmail.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityEmail"></a>  

***
<br><br>[$messageEntityHashtag](/API_docs/constructors/messageEntityHashtag.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityHashtag"></a>  

***
<br><br>[$messageEntityItalic](/API_docs/constructors/messageEntityItalic.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityItalic"></a>  

***
<br><br>[$messageEntityMention](/API_docs/constructors/messageEntityMention.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityMention"></a>  

***
<br><br>[$messageEntityMentionName](/API_docs/constructors/messageEntityMentionName.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="messageEntityMentionName"></a>  

***
<br><br>[$messageEntityPhone](/API_docs/constructors/messageEntityPhone.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityPhone"></a>  

***
<br><br>[$messageEntityPre](/API_docs/constructors/messageEntityPre.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), 'language' => [string](/API_docs/types/string.html), \];<a name="messageEntityPre"></a>  

***
<br><br>[$messageEntitySpoiler](/API_docs/constructors/messageEntitySpoiler.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntitySpoiler"></a>  

***
<br><br>[$messageEntityStrike](/API_docs/constructors/messageEntityStrike.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityStrike"></a>  

***
<br><br>[$messageEntityTextUrl](/API_docs/constructors/messageEntityTextUrl.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), 'url' => [string](/API_docs/types/string.html), \];<a name="messageEntityTextUrl"></a>  

***
<br><br>[$messageEntityUnderline](/API_docs/constructors/messageEntityUnderline.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityUnderline"></a>  

***
<br><br>[$messageEntityUnknown](/API_docs/constructors/messageEntityUnknown.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityUnknown"></a>  

***
<br><br>[$messageEntityUrl](/API_docs/constructors/messageEntityUrl.html) = \['offset' => [int](/API_docs/types/int.html), 'length' => [int](/API_docs/types/int.html), \];<a name="messageEntityUrl"></a>  

***
<br><br>[$messageFwdHeader](/API_docs/constructors/messageFwdHeader.html) = \['imported' => [Bool](/API_docs/types/Bool.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'from_name' => [string](/API_docs/types/string.html), 'date' => [int](/API_docs/types/int.html), 'channel_post' => [int](/API_docs/types/int.html), 'post_author' => [string](/API_docs/types/string.html), 'saved_from_peer' => [Peer](/API_docs/types/Peer.html), 'saved_from_msg_id' => [int](/API_docs/types/int.html), 'psa_type' => [string](/API_docs/types/string.html), \];<a name="messageFwdHeader"></a>  

***
<br><br>[$messageInteractionCounters](/API_docs/constructors/messageInteractionCounters.html) = \['msg_id' => [int](/API_docs/types/int.html), 'views' => [int](/API_docs/types/int.html), 'forwards' => [int](/API_docs/types/int.html), \];<a name="messageInteractionCounters"></a>  

***
<br><br>[$messageMediaContact](/API_docs/constructors/messageMediaContact.html) = \['phone_number' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'vcard' => [string](/API_docs/types/string.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="messageMediaContact"></a>  

***
<br><br>[$messageMediaDice](/API_docs/constructors/messageMediaDice.html) = \['value' => [int](/API_docs/types/int.html), 'emoticon' => [string](/API_docs/types/string.html), \];<a name="messageMediaDice"></a>  

***
<br><br>[$messageMediaDocument](/API_docs/constructors/messageMediaDocument.html) = \['nopremium' => [Bool](/API_docs/types/Bool.html), 'document' => [Document](/API_docs/types/Document.html), 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="messageMediaDocument"></a>  

***
<br><br>[$messageMediaEmpty](/API_docs/constructors/messageMediaEmpty.html) = \[\];<a name="messageMediaEmpty"></a>  

***
<br><br>[$messageMediaGame](/API_docs/constructors/messageMediaGame.html) = \['game' => [Game](/API_docs/types/Game.html), \];<a name="messageMediaGame"></a>  

***
<br><br>[$messageMediaGeo](/API_docs/constructors/messageMediaGeo.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), \];<a name="messageMediaGeo"></a>  

***
<br><br>[$messageMediaGeoLive](/API_docs/constructors/messageMediaGeoLive.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'heading' => [int](/API_docs/types/int.html), 'period' => [int](/API_docs/types/int.html), 'proximity_notification_radius' => [int](/API_docs/types/int.html), \];<a name="messageMediaGeoLive"></a>  

***
<br><br>[$messageMediaInvoice](/API_docs/constructors/messageMediaInvoice.html) = \['shipping_address_requested' => [Bool](/API_docs/types/Bool.html), 'test' => [Bool](/API_docs/types/Bool.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [WebDocument](/API_docs/types/WebDocument.html), 'receipt_msg_id' => [int](/API_docs/types/int.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), 'start_param' => [string](/API_docs/types/string.html), \];<a name="messageMediaInvoice"></a>  

***
<br><br>[$messageMediaPhoto](/API_docs/constructors/messageMediaPhoto.html) = \['photo' => [Photo](/API_docs/types/Photo.html), 'ttl_seconds' => [int](/API_docs/types/int.html), \];<a name="messageMediaPhoto"></a>  

***
<br><br>[$messageMediaPoll](/API_docs/constructors/messageMediaPoll.html) = \['poll' => [Poll](/API_docs/types/Poll.html), 'results' => [PollResults](/API_docs/types/PollResults.html), \];<a name="messageMediaPoll"></a>  

***
<br><br>[$messageMediaUnsupported](/API_docs/constructors/messageMediaUnsupported.html) = \[\];<a name="messageMediaUnsupported"></a>  

***
<br><br>[$messageMediaVenue](/API_docs/constructors/messageMediaVenue.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'title' => [string](/API_docs/types/string.html), 'address' => [string](/API_docs/types/string.html), 'provider' => [string](/API_docs/types/string.html), 'venue_id' => [string](/API_docs/types/string.html), 'venue_type' => [string](/API_docs/types/string.html), \];<a name="messageMediaVenue"></a>  

***
<br><br>[$messageMediaWebPage](/API_docs/constructors/messageMediaWebPage.html) = \['webpage' => [WebPage](/API_docs/types/WebPage.html), \];<a name="messageMediaWebPage"></a>  

***
<br><br>[$messagePeerReaction](/API_docs/constructors/messagePeerReaction.html) = \['big' => [Bool](/API_docs/types/Bool.html), 'unread' => [Bool](/API_docs/types/Bool.html), 'peer_id' => [Peer](/API_docs/types/Peer.html), 'reaction' => [string](/API_docs/types/string.html), \];<a name="messagePeerReaction"></a>  

***
<br><br>[$messageRange](/API_docs/constructors/messageRange.html) = \['min_id' => [int](/API_docs/types/int.html), 'max_id' => [int](/API_docs/types/int.html), \];<a name="messageRange"></a>  

***
<br><br>[$messageReactions](/API_docs/constructors/messageReactions.html) = \['min' => [Bool](/API_docs/types/Bool.html), 'can_see_list' => [Bool](/API_docs/types/Bool.html), 'results' => \[[ReactionCount](/API_docs/types/ReactionCount.html)\], 'recent_reactions' => \[[MessagePeerReaction](/API_docs/types/MessagePeerReaction.html)\], \];<a name="messageReactions"></a>  

***
<br><br>[$messageReplies](/API_docs/constructors/messageReplies.html) = \['comments' => [Bool](/API_docs/types/Bool.html), 'replies' => [int](/API_docs/types/int.html), 'replies_pts' => [int](/API_docs/types/int.html), 'recent_repliers' => \[[Peer](/API_docs/types/Peer.html)\], 'channel_id' => [long](/API_docs/types/long.html), 'max_id' => [int](/API_docs/types/int.html), 'read_max_id' => [int](/API_docs/types/int.html), \];<a name="messageReplies"></a>  

***
<br><br>[$messageReplyHeader](/API_docs/constructors/messageReplyHeader.html) = \['reply_to_scheduled' => [Bool](/API_docs/types/Bool.html), 'reply_to_msg_id' => [int](/API_docs/types/int.html), 'reply_to_peer_id' => [Peer](/API_docs/types/Peer.html), 'reply_to_top_id' => [int](/API_docs/types/int.html), \];<a name="messageReplyHeader"></a>  

***
<br><br>[$messageService](/API_docs/constructors/messageService.html) = \['out' => [Bool](/API_docs/types/Bool.html), 'mentioned' => [Bool](/API_docs/types/Bool.html), 'media_unread' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'post' => [Bool](/API_docs/types/Bool.html), 'legacy' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'peer_id' => [Peer](/API_docs/types/Peer.html), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html), 'date' => [int](/API_docs/types/int.html), 'action' => [MessageAction](/API_docs/types/MessageAction.html), 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="messageService"></a>  

***
<br><br>[$messageUserVote](/API_docs/constructors/messageUserVote.html) = \['user_id' => [long](/API_docs/types/long.html), 'option' => [bytes](/API_docs/types/bytes.html), 'date' => [int](/API_docs/types/int.html), \];<a name="messageUserVote"></a>  

***
<br><br>[$messageUserVoteInputOption](/API_docs/constructors/messageUserVoteInputOption.html) = \['user_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="messageUserVoteInputOption"></a>  

***
<br><br>[$messageUserVoteMultiple](/API_docs/constructors/messageUserVoteMultiple.html) = \['user_id' => [long](/API_docs/types/long.html), 'options' => \[[bytes](/API_docs/types/bytes.html)\], 'date' => [int](/API_docs/types/int.html), \];<a name="messageUserVoteMultiple"></a>  

***
<br><br>[$messageViews](/API_docs/constructors/messageViews.html) = \['views' => [int](/API_docs/types/int.html), 'forwards' => [int](/API_docs/types/int.html), 'replies' => [MessageReplies](/API_docs/types/MessageReplies.html), \];<a name="messageViews"></a>  

***
<br><br>[$messages.affectedFoundMessages](/API_docs/constructors/messages.affectedFoundMessages.html) = \['pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), 'offset' => [int](/API_docs/types/int.html), 'messages' => \[[int](/API_docs/types/int.html)\], \];<a name="messages.affectedFoundMessages"></a>  

***
<br><br>[$messages.affectedHistory](/API_docs/constructors/messages.affectedHistory.html) = \['pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), 'offset' => [int](/API_docs/types/int.html), \];<a name="messages.affectedHistory"></a>  

***
<br><br>[$messages.affectedMessages](/API_docs/constructors/messages.affectedMessages.html) = \['pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="messages.affectedMessages"></a>  

***
<br><br>[$messages.allStickers](/API_docs/constructors/messages.allStickers.html) = \['hash' => [long](/API_docs/types/long.html), 'sets' => \[[StickerSet](/API_docs/types/StickerSet.html)\], \];<a name="messages.allStickers"></a>  

***
<br><br>[$messages.allStickersNotModified](/API_docs/constructors/messages.allStickersNotModified.html) = \[\];<a name="messages.allStickersNotModified"></a>  

***
<br><br>[$messages.archivedStickers](/API_docs/constructors/messages.archivedStickers.html) = \['count' => [int](/API_docs/types/int.html), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.html)\], \];<a name="messages.archivedStickers"></a>  

***
<br><br>[$messages.availableReactions](/API_docs/constructors/messages.availableReactions.html) = \['hash' => [int](/API_docs/types/int.html), 'reactions' => \[[AvailableReaction](/API_docs/types/AvailableReaction.html)\], \];<a name="messages.availableReactions"></a>  

***
<br><br>[$messages.availableReactionsNotModified](/API_docs/constructors/messages.availableReactionsNotModified.html) = \[\];<a name="messages.availableReactionsNotModified"></a>  

***
<br><br>[$messages.botCallbackAnswer](/API_docs/constructors/messages.botCallbackAnswer.html) = \['alert' => [Bool](/API_docs/types/Bool.html), 'has_url' => [Bool](/API_docs/types/Bool.html), 'native_ui' => [Bool](/API_docs/types/Bool.html), 'message' => [string](/API_docs/types/string.html), 'url' => [string](/API_docs/types/string.html), 'cache_time' => [int](/API_docs/types/int.html), \];<a name="messages.botCallbackAnswer"></a>  

***
<br><br>[$messages.botResults](/API_docs/constructors/messages.botResults.html) = \['gallery' => [Bool](/API_docs/types/Bool.html), 'query_id' => [long](/API_docs/types/long.html), 'next_offset' => [string](/API_docs/types/string.html), 'switch_pm' => [InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.html), 'results' => \[[BotInlineResult](/API_docs/types/BotInlineResult.html)\], 'cache_time' => [int](/API_docs/types/int.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.botResults"></a>  

***
<br><br>[$messages.channelMessages](/API_docs/constructors/messages.channelMessages.html) = \['inexact' => [Bool](/API_docs/types/Bool.html), 'pts' => [int](/API_docs/types/int.html), 'count' => [int](/API_docs/types/int.html), 'offset_id_offset' => [int](/API_docs/types/int.html), 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.channelMessages"></a>  

***
<br><br>[$messages.chatAdminsWithInvites](/API_docs/constructors/messages.chatAdminsWithInvites.html) = \['admins' => \[[ChatAdminWithInvites](/API_docs/types/ChatAdminWithInvites.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.chatAdminsWithInvites"></a>  

***
<br><br>[$messages.chatFull](/API_docs/constructors/messages.chatFull.html) = \['full_chat' => [ChatFull](/API_docs/types/ChatFull.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.chatFull"></a>  

***
<br><br>[$messages.chatInviteImporters](/API_docs/constructors/messages.chatInviteImporters.html) = \['count' => [int](/API_docs/types/int.html), 'importers' => \[[ChatInviteImporter](/API_docs/types/ChatInviteImporter.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.chatInviteImporters"></a>  

***
<br><br>[$messages.chats](/API_docs/constructors/messages.chats.html) = \['chats' => \[[Chat](/API_docs/types/Chat.html)\], \];<a name="messages.chats"></a>  

***
<br><br>[$messages.chatsSlice](/API_docs/constructors/messages.chatsSlice.html) = \['count' => [int](/API_docs/types/int.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], \];<a name="messages.chatsSlice"></a>  

***
<br><br>[$messages.checkedHistoryImportPeer](/API_docs/constructors/messages.checkedHistoryImportPeer.html) = \['confirm_text' => [string](/API_docs/types/string.html), \];<a name="messages.checkedHistoryImportPeer"></a>  

***
<br><br>[$messages.dhConfig](/API_docs/constructors/messages.dhConfig.html) = \['g' => [int](/API_docs/types/int.html), 'p' => [bytes](/API_docs/types/bytes.html), 'version' => [int](/API_docs/types/int.html), 'random' => [bytes](/API_docs/types/bytes.html), \];<a name="messages.dhConfig"></a>  

***
<br><br>[$messages.dhConfigNotModified](/API_docs/constructors/messages.dhConfigNotModified.html) = \['random' => [bytes](/API_docs/types/bytes.html), \];<a name="messages.dhConfigNotModified"></a>  

***
<br><br>[$messages.dialogs](/API_docs/constructors/messages.dialogs.html) = \['dialogs' => \[[Dialog](/API_docs/types/Dialog.html)\], 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.dialogs"></a>  

***
<br><br>[$messages.dialogsNotModified](/API_docs/constructors/messages.dialogsNotModified.html) = \['count' => [int](/API_docs/types/int.html), \];<a name="messages.dialogsNotModified"></a>  

***
<br><br>[$messages.dialogsSlice](/API_docs/constructors/messages.dialogsSlice.html) = \['count' => [int](/API_docs/types/int.html), 'dialogs' => \[[Dialog](/API_docs/types/Dialog.html)\], 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.dialogsSlice"></a>  

***
<br><br>[$messages.discussionMessage](/API_docs/constructors/messages.discussionMessage.html) = \['messages' => \[[Message](/API_docs/types/Message.html)\], 'max_id' => [int](/API_docs/types/int.html), 'read_inbox_max_id' => [int](/API_docs/types/int.html), 'read_outbox_max_id' => [int](/API_docs/types/int.html), 'unread_count' => [int](/API_docs/types/int.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.discussionMessage"></a>  

***
<br><br>[$messages.exportedChatInvite](/API_docs/constructors/messages.exportedChatInvite.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.exportedChatInvite"></a>  

***
<br><br>[$messages.exportedChatInviteReplaced](/API_docs/constructors/messages.exportedChatInviteReplaced.html) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'new_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.exportedChatInviteReplaced"></a>  

***
<br><br>[$messages.exportedChatInvites](/API_docs/constructors/messages.exportedChatInvites.html) = \['count' => [int](/API_docs/types/int.html), 'invites' => \[[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.exportedChatInvites"></a>  

***
<br><br>[$messages.favedStickers](/API_docs/constructors/messages.favedStickers.html) = \['hash' => [long](/API_docs/types/long.html), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.html)\], 'stickers' => \[[Document](/API_docs/types/Document.html)\], \];<a name="messages.favedStickers"></a>  

***
<br><br>[$messages.favedStickersNotModified](/API_docs/constructors/messages.favedStickersNotModified.html) = \[\];<a name="messages.favedStickersNotModified"></a>  

***
<br><br>[$messages.featuredStickers](/API_docs/constructors/messages.featuredStickers.html) = \['hash' => [long](/API_docs/types/long.html), 'count' => [int](/API_docs/types/int.html), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.html)\], 'unread' => \[[long](/API_docs/types/long.html)\], \];<a name="messages.featuredStickers"></a>  

***
<br><br>[$messages.featuredStickersNotModified](/API_docs/constructors/messages.featuredStickersNotModified.html) = \['count' => [int](/API_docs/types/int.html), \];<a name="messages.featuredStickersNotModified"></a>  

***
<br><br>[$messages.foundStickerSets](/API_docs/constructors/messages.foundStickerSets.html) = \['hash' => [long](/API_docs/types/long.html), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.html)\], \];<a name="messages.foundStickerSets"></a>  

***
<br><br>[$messages.foundStickerSetsNotModified](/API_docs/constructors/messages.foundStickerSetsNotModified.html) = \[\];<a name="messages.foundStickerSetsNotModified"></a>  

***
<br><br>[$messages.highScores](/API_docs/constructors/messages.highScores.html) = \['scores' => \[[HighScore](/API_docs/types/HighScore.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.highScores"></a>  

***
<br><br>[$messages.historyImport](/API_docs/constructors/messages.historyImport.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="messages.historyImport"></a>  

***
<br><br>[$messages.historyImportParsed](/API_docs/constructors/messages.historyImportParsed.html) = \['pm' => [Bool](/API_docs/types/Bool.html), 'group' => [Bool](/API_docs/types/Bool.html), 'title' => [string](/API_docs/types/string.html), \];<a name="messages.historyImportParsed"></a>  

***
<br><br>[$messages.inactiveChats](/API_docs/constructors/messages.inactiveChats.html) = \['dates' => \[[int](/API_docs/types/int.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.inactiveChats"></a>  

***
<br><br>[$messages.messageEditData](/API_docs/constructors/messages.messageEditData.html) = \['caption' => [Bool](/API_docs/types/Bool.html), \];<a name="messages.messageEditData"></a>  

***
<br><br>[$messages.messageReactionsList](/API_docs/constructors/messages.messageReactionsList.html) = \['count' => [int](/API_docs/types/int.html), 'reactions' => \[[MessagePeerReaction](/API_docs/types/MessagePeerReaction.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'next_offset' => [string](/API_docs/types/string.html), \];<a name="messages.messageReactionsList"></a>  

***
<br><br>[$messages.messageViews](/API_docs/constructors/messages.messageViews.html) = \['views' => \[[MessageViews](/API_docs/types/MessageViews.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.messageViews"></a>  

***
<br><br>[$messages.messages](/API_docs/constructors/messages.messages.html) = \['messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.messages"></a>  

***
<br><br>[$messages.messagesNotModified](/API_docs/constructors/messages.messagesNotModified.html) = \['count' => [int](/API_docs/types/int.html), \];<a name="messages.messagesNotModified"></a>  

***
<br><br>[$messages.messagesSlice](/API_docs/constructors/messages.messagesSlice.html) = \['inexact' => [Bool](/API_docs/types/Bool.html), 'count' => [int](/API_docs/types/int.html), 'next_rate' => [int](/API_docs/types/int.html), 'offset_id_offset' => [int](/API_docs/types/int.html), 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.messagesSlice"></a>  

***
<br><br>[$messages.peerDialogs](/API_docs/constructors/messages.peerDialogs.html) = \['dialogs' => \[[Dialog](/API_docs/types/Dialog.html)\], 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'state' => [updates.State](/API_docs/types/updates.State.html), \];<a name="messages.peerDialogs"></a>  

***
<br><br>[$messages.peerSettings](/API_docs/constructors/messages.peerSettings.html) = \['settings' => [PeerSettings](/API_docs/types/PeerSettings.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.peerSettings"></a>  

***
<br><br>[$messages.recentStickers](/API_docs/constructors/messages.recentStickers.html) = \['hash' => [long](/API_docs/types/long.html), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.html)\], 'stickers' => \[[Document](/API_docs/types/Document.html)\], 'dates' => \[[int](/API_docs/types/int.html)\], \];<a name="messages.recentStickers"></a>  

***
<br><br>[$messages.recentStickersNotModified](/API_docs/constructors/messages.recentStickersNotModified.html) = \[\];<a name="messages.recentStickersNotModified"></a>  

***
<br><br>[$messages.savedGifs](/API_docs/constructors/messages.savedGifs.html) = \['hash' => [long](/API_docs/types/long.html), 'gifs' => \[[Document](/API_docs/types/Document.html)\], \];<a name="messages.savedGifs"></a>  

***
<br><br>[$messages.savedGifsNotModified](/API_docs/constructors/messages.savedGifsNotModified.html) = \[\];<a name="messages.savedGifsNotModified"></a>  

***
<br><br>[$messages.searchCounter](/API_docs/constructors/messages.searchCounter.html) = \['inexact' => [Bool](/API_docs/types/Bool.html), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.html), 'count' => [int](/API_docs/types/int.html), \];<a name="messages.searchCounter"></a>  

***
<br><br>[$messages.searchResultsCalendar](/API_docs/constructors/messages.searchResultsCalendar.html) = \['inexact' => [Bool](/API_docs/types/Bool.html), 'count' => [int](/API_docs/types/int.html), 'min_date' => [int](/API_docs/types/int.html), 'min_msg_id' => [int](/API_docs/types/int.html), 'offset_id_offset' => [int](/API_docs/types/int.html), 'periods' => \[[SearchResultsCalendarPeriod](/API_docs/types/SearchResultsCalendarPeriod.html)\], 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.searchResultsCalendar"></a>  

***
<br><br>[$messages.searchResultsPositions](/API_docs/constructors/messages.searchResultsPositions.html) = \['count' => [int](/API_docs/types/int.html), 'positions' => \[[SearchResultsPosition](/API_docs/types/SearchResultsPosition.html)\], \];<a name="messages.searchResultsPositions"></a>  

***
<br><br>[$messages.sentEncryptedFile](/API_docs/constructors/messages.sentEncryptedFile.html) = \['date' => [int](/API_docs/types/int.html), 'file' => [EncryptedFile](/API_docs/types/EncryptedFile.html), \];<a name="messages.sentEncryptedFile"></a>  

***
<br><br>[$messages.sentEncryptedMessage](/API_docs/constructors/messages.sentEncryptedMessage.html) = \['date' => [int](/API_docs/types/int.html), \];<a name="messages.sentEncryptedMessage"></a>  

***
<br><br>[$messages.sponsoredMessages](/API_docs/constructors/messages.sponsoredMessages.html) = \['messages' => \[[SponsoredMessage](/API_docs/types/SponsoredMessage.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="messages.sponsoredMessages"></a>  

***
<br><br>[$messages.stickerSet](/API_docs/constructors/messages.stickerSet.html) = \['set' => [StickerSet](/API_docs/types/StickerSet.html), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.html)\], 'documents' => \[[Document](/API_docs/types/Document.html)\], \];<a name="messages.stickerSet"></a>  

***
<br><br>[$messages.stickerSetInstallResultArchive](/API_docs/constructors/messages.stickerSetInstallResultArchive.html) = \['sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.html)\], \];<a name="messages.stickerSetInstallResultArchive"></a>  

***
<br><br>[$messages.stickerSetInstallResultSuccess](/API_docs/constructors/messages.stickerSetInstallResultSuccess.html) = \[\];<a name="messages.stickerSetInstallResultSuccess"></a>  

***
<br><br>[$messages.stickerSetNotModified](/API_docs/constructors/messages.stickerSetNotModified.html) = \[\];<a name="messages.stickerSetNotModified"></a>  

***
<br><br>[$messages.stickers](/API_docs/constructors/messages.stickers.html) = \['hash' => [long](/API_docs/types/long.html), 'stickers' => \[[Document](/API_docs/types/Document.html)\], \];<a name="messages.stickers"></a>  

***
<br><br>[$messages.stickersNotModified](/API_docs/constructors/messages.stickersNotModified.html) = \[\];<a name="messages.stickersNotModified"></a>  

***
<br><br>[$messages.transcribedAudio](/API_docs/constructors/messages.transcribedAudio.html) = \['pending' => [Bool](/API_docs/types/Bool.html), 'transcription_id' => [long](/API_docs/types/long.html), 'text' => [string](/API_docs/types/string.html), \];<a name="messages.transcribedAudio"></a>  

***
<br><br>[$messages.translateNoResult](/API_docs/constructors/messages.translateNoResult.html) = \[\];<a name="messages.translateNoResult"></a>  

***
<br><br>[$messages.translateResultText](/API_docs/constructors/messages.translateResultText.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="messages.translateResultText"></a>  

***
<br><br>[$messages.votesList](/API_docs/constructors/messages.votesList.html) = \['count' => [int](/API_docs/types/int.html), 'votes' => \[[MessageUserVote](/API_docs/types/MessageUserVote.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'next_offset' => [string](/API_docs/types/string.html), \];<a name="messages.votesList"></a>  

***
<br><br>[$nearestDc](/API_docs/constructors/nearestDc.html) = \['country' => [string](/API_docs/types/string.html), 'this_dc' => [int](/API_docs/types/int.html), 'nearest_dc' => [int](/API_docs/types/int.html), \];<a name="nearestDc"></a>  

***
<br><br>[$notificationSoundDefault](/API_docs/constructors/notificationSoundDefault.html) = \[\];<a name="notificationSoundDefault"></a>  

***
<br><br>[$notificationSoundLocal](/API_docs/constructors/notificationSoundLocal.html) = \['title' => [string](/API_docs/types/string.html), 'data' => [string](/API_docs/types/string.html), \];<a name="notificationSoundLocal"></a>  

***
<br><br>[$notificationSoundNone](/API_docs/constructors/notificationSoundNone.html) = \[\];<a name="notificationSoundNone"></a>  

***
<br><br>[$notificationSoundRingtone](/API_docs/constructors/notificationSoundRingtone.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="notificationSoundRingtone"></a>  

***
<br><br>[$notifyBroadcasts](/API_docs/constructors/notifyBroadcasts.html) = \[\];<a name="notifyBroadcasts"></a>  

***
<br><br>[$notifyChats](/API_docs/constructors/notifyChats.html) = \[\];<a name="notifyChats"></a>  

***
<br><br>[$notifyPeer](/API_docs/constructors/notifyPeer.html) = \['peer' => [Peer](/API_docs/types/Peer.html), \];<a name="notifyPeer"></a>  

***
<br><br>[$notifyUsers](/API_docs/constructors/notifyUsers.html) = \[\];<a name="notifyUsers"></a>  

***
<br><br>[$null](/API_docs/constructors/null.html) = \[\];<a name="null"></a>  

***
<br><br>[$page](/API_docs/constructors/page.html) = \['part' => [Bool](/API_docs/types/Bool.html), 'rtl' => [Bool](/API_docs/types/Bool.html), 'v2' => [Bool](/API_docs/types/Bool.html), 'url' => [string](/API_docs/types/string.html), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.html)\], 'photos' => \[[Photo](/API_docs/types/Photo.html)\], 'documents' => \[[Document](/API_docs/types/Document.html)\], 'views' => [int](/API_docs/types/int.html), \];<a name="page"></a>  

***
<br><br>[$pageBlockAnchor](/API_docs/constructors/pageBlockAnchor.html) = \['name' => [string](/API_docs/types/string.html), \];<a name="pageBlockAnchor"></a>  

***
<br><br>[$pageBlockAudio](/API_docs/constructors/pageBlockAudio.html) = \['audio_id' => [long](/API_docs/types/long.html), 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockAudio"></a>  

***
<br><br>[$pageBlockAuthorDate](/API_docs/constructors/pageBlockAuthorDate.html) = \['author' => [RichText](/API_docs/types/RichText.html), 'published_date' => [int](/API_docs/types/int.html), \];<a name="pageBlockAuthorDate"></a>  

***
<br><br>[$pageBlockBlockquote](/API_docs/constructors/pageBlockBlockquote.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'caption' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockBlockquote"></a>  

***
<br><br>[$pageBlockChannel](/API_docs/constructors/pageBlockChannel.html) = \['channel' => [Chat](/API_docs/types/Chat.html), \];<a name="pageBlockChannel"></a>  

***
<br><br>[$pageBlockCollage](/API_docs/constructors/pageBlockCollage.html) = \['items' => \[[PageBlock](/API_docs/types/PageBlock.html)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockCollage"></a>  

***
<br><br>[$pageBlockCover](/API_docs/constructors/pageBlockCover.html) = \['cover' => [PageBlock](/API_docs/types/PageBlock.html), \];<a name="pageBlockCover"></a>  

***
<br><br>[$pageBlockDetails](/API_docs/constructors/pageBlockDetails.html) = \['open' => [Bool](/API_docs/types/Bool.html), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.html)\], 'title' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockDetails"></a>  

***
<br><br>[$pageBlockDivider](/API_docs/constructors/pageBlockDivider.html) = \[\];<a name="pageBlockDivider"></a>  

***
<br><br>[$pageBlockEmbed](/API_docs/constructors/pageBlockEmbed.html) = \['full_width' => [Bool](/API_docs/types/Bool.html), 'allow_scrolling' => [Bool](/API_docs/types/Bool.html), 'url' => [string](/API_docs/types/string.html), 'html' => [string](/API_docs/types/string.html), 'poster_photo_id' => [long](/API_docs/types/long.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockEmbed"></a>  

***
<br><br>[$pageBlockEmbedPost](/API_docs/constructors/pageBlockEmbedPost.html) = \['url' => [string](/API_docs/types/string.html), 'webpage_id' => [long](/API_docs/types/long.html), 'author_photo_id' => [long](/API_docs/types/long.html), 'author' => [string](/API_docs/types/string.html), 'date' => [int](/API_docs/types/int.html), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.html)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockEmbedPost"></a>  

***
<br><br>[$pageBlockFooter](/API_docs/constructors/pageBlockFooter.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockFooter"></a>  

***
<br><br>[$pageBlockHeader](/API_docs/constructors/pageBlockHeader.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockHeader"></a>  

***
<br><br>[$pageBlockKicker](/API_docs/constructors/pageBlockKicker.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockKicker"></a>  

***
<br><br>[$pageBlockList](/API_docs/constructors/pageBlockList.html) = \['items' => \[[PageListItem](/API_docs/types/PageListItem.html)\], \];<a name="pageBlockList"></a>  

***
<br><br>[$pageBlockMap](/API_docs/constructors/pageBlockMap.html) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'zoom' => [int](/API_docs/types/int.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockMap"></a>  

***
<br><br>[$pageBlockOrderedList](/API_docs/constructors/pageBlockOrderedList.html) = \['items' => \[[PageListOrderedItem](/API_docs/types/PageListOrderedItem.html)\], \];<a name="pageBlockOrderedList"></a>  

***
<br><br>[$pageBlockParagraph](/API_docs/constructors/pageBlockParagraph.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockParagraph"></a>  

***
<br><br>[$pageBlockPhoto](/API_docs/constructors/pageBlockPhoto.html) = \['photo_id' => [long](/API_docs/types/long.html), 'caption' => [PageCaption](/API_docs/types/PageCaption.html), 'url' => [string](/API_docs/types/string.html), 'webpage_id' => [long](/API_docs/types/long.html), \];<a name="pageBlockPhoto"></a>  

***
<br><br>[$pageBlockPreformatted](/API_docs/constructors/pageBlockPreformatted.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'language' => [string](/API_docs/types/string.html), \];<a name="pageBlockPreformatted"></a>  

***
<br><br>[$pageBlockPullquote](/API_docs/constructors/pageBlockPullquote.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'caption' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockPullquote"></a>  

***
<br><br>[$pageBlockRelatedArticles](/API_docs/constructors/pageBlockRelatedArticles.html) = \['title' => [RichText](/API_docs/types/RichText.html), 'articles' => \[[PageRelatedArticle](/API_docs/types/PageRelatedArticle.html)\], \];<a name="pageBlockRelatedArticles"></a>  

***
<br><br>[$pageBlockSlideshow](/API_docs/constructors/pageBlockSlideshow.html) = \['items' => \[[PageBlock](/API_docs/types/PageBlock.html)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockSlideshow"></a>  

***
<br><br>[$pageBlockSubheader](/API_docs/constructors/pageBlockSubheader.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockSubheader"></a>  

***
<br><br>[$pageBlockSubtitle](/API_docs/constructors/pageBlockSubtitle.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockSubtitle"></a>  

***
<br><br>[$pageBlockTable](/API_docs/constructors/pageBlockTable.html) = \['bordered' => [Bool](/API_docs/types/Bool.html), 'striped' => [Bool](/API_docs/types/Bool.html), 'title' => [RichText](/API_docs/types/RichText.html), 'rows' => \[[PageTableRow](/API_docs/types/PageTableRow.html)\], \];<a name="pageBlockTable"></a>  

***
<br><br>[$pageBlockTitle](/API_docs/constructors/pageBlockTitle.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageBlockTitle"></a>  

***
<br><br>[$pageBlockUnsupported](/API_docs/constructors/pageBlockUnsupported.html) = \[\];<a name="pageBlockUnsupported"></a>  

***
<br><br>[$pageBlockVideo](/API_docs/constructors/pageBlockVideo.html) = \['autoplay' => [Bool](/API_docs/types/Bool.html), 'loop' => [Bool](/API_docs/types/Bool.html), 'video_id' => [long](/API_docs/types/long.html), 'caption' => [PageCaption](/API_docs/types/PageCaption.html), \];<a name="pageBlockVideo"></a>  

***
<br><br>[$pageCaption](/API_docs/constructors/pageCaption.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'credit' => [RichText](/API_docs/types/RichText.html), \];<a name="pageCaption"></a>  

***
<br><br>[$pageListItemBlocks](/API_docs/constructors/pageListItemBlocks.html) = \['blocks' => \[[PageBlock](/API_docs/types/PageBlock.html)\], \];<a name="pageListItemBlocks"></a>  

***
<br><br>[$pageListItemText](/API_docs/constructors/pageListItemText.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageListItemText"></a>  

***
<br><br>[$pageListOrderedItemBlocks](/API_docs/constructors/pageListOrderedItemBlocks.html) = \['num' => [string](/API_docs/types/string.html), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.html)\], \];<a name="pageListOrderedItemBlocks"></a>  

***
<br><br>[$pageListOrderedItemText](/API_docs/constructors/pageListOrderedItemText.html) = \['num' => [string](/API_docs/types/string.html), 'text' => [RichText](/API_docs/types/RichText.html), \];<a name="pageListOrderedItemText"></a>  

***
<br><br>[$pageRelatedArticle](/API_docs/constructors/pageRelatedArticle.html) = \['url' => [string](/API_docs/types/string.html), 'webpage_id' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo_id' => [long](/API_docs/types/long.html), 'author' => [string](/API_docs/types/string.html), 'published_date' => [int](/API_docs/types/int.html), \];<a name="pageRelatedArticle"></a>  

***
<br><br>[$pageTableCell](/API_docs/constructors/pageTableCell.html) = \['header' => [Bool](/API_docs/types/Bool.html), 'align_center' => [Bool](/API_docs/types/Bool.html), 'align_right' => [Bool](/API_docs/types/Bool.html), 'valign_middle' => [Bool](/API_docs/types/Bool.html), 'valign_bottom' => [Bool](/API_docs/types/Bool.html), 'text' => [RichText](/API_docs/types/RichText.html), 'colspan' => [int](/API_docs/types/int.html), 'rowspan' => [int](/API_docs/types/int.html), \];<a name="pageTableCell"></a>  

***
<br><br>[$pageTableRow](/API_docs/constructors/pageTableRow.html) = \['cells' => \[[PageTableCell](/API_docs/types/PageTableCell.html)\], \];<a name="pageTableRow"></a>  

***
<br><br>[$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow](/API_docs/constructors/passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow.html) = \['salt1' => [bytes](/API_docs/types/bytes.html), 'salt2' => [bytes](/API_docs/types/bytes.html), 'g' => [int](/API_docs/types/int.html), 'p' => [bytes](/API_docs/types/bytes.html), \];<a name="passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"></a>  

***
<br><br>[$passwordKdfAlgoUnknown](/API_docs/constructors/passwordKdfAlgoUnknown.html) = \[\];<a name="passwordKdfAlgoUnknown"></a>  

***
<br><br>[$paymentCharge](/API_docs/constructors/paymentCharge.html) = \['id' => [string](/API_docs/types/string.html), 'provider_charge_id' => [string](/API_docs/types/string.html), \];<a name="paymentCharge"></a>  

***
<br><br>[$paymentRequestedInfo](/API_docs/constructors/paymentRequestedInfo.html) = \['name' => [string](/API_docs/types/string.html), 'phone' => [string](/API_docs/types/string.html), 'email' => [string](/API_docs/types/string.html), 'shipping_address' => [PostAddress](/API_docs/types/PostAddress.html), \];<a name="paymentRequestedInfo"></a>  

***
<br><br>[$paymentSavedCredentialsCard](/API_docs/constructors/paymentSavedCredentialsCard.html) = \['id' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), \];<a name="paymentSavedCredentialsCard"></a>  

***
<br><br>[$payments.bankCardData](/API_docs/constructors/payments.bankCardData.html) = \['title' => [string](/API_docs/types/string.html), 'open_urls' => \[[BankCardOpenUrl](/API_docs/types/BankCardOpenUrl.html)\], \];<a name="payments.bankCardData"></a>  

***
<br><br>[$payments.exportedInvoice](/API_docs/constructors/payments.exportedInvoice.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="payments.exportedInvoice"></a>  

***
<br><br>[$payments.paymentForm](/API_docs/constructors/payments.paymentForm.html) = \['can_save_credentials' => [Bool](/API_docs/types/Bool.html), 'password_missing' => [Bool](/API_docs/types/Bool.html), 'form_id' => [long](/API_docs/types/long.html), 'bot_id' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [WebDocument](/API_docs/types/WebDocument.html), 'invoice' => [Invoice](/API_docs/types/Invoice.html), 'provider_id' => [long](/API_docs/types/long.html), 'url' => [string](/API_docs/types/string.html), 'native_provider' => [string](/API_docs/types/string.html), 'native_params' => [DataJSON](/API_docs/types/DataJSON.html), 'saved_info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), 'saved_credentials' => [PaymentSavedCredentials](/API_docs/types/PaymentSavedCredentials.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="payments.paymentForm"></a>  

***
<br><br>[$payments.paymentReceipt](/API_docs/constructors/payments.paymentReceipt.html) = \['date' => [int](/API_docs/types/int.html), 'bot_id' => [long](/API_docs/types/long.html), 'provider_id' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [WebDocument](/API_docs/types/WebDocument.html), 'invoice' => [Invoice](/API_docs/types/Invoice.html), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), 'shipping' => [ShippingOption](/API_docs/types/ShippingOption.html), 'tip_amount' => [long](/API_docs/types/long.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), 'credentials_title' => [string](/API_docs/types/string.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="payments.paymentReceipt"></a>  

***
<br><br>[$payments.paymentResult](/API_docs/constructors/payments.paymentResult.html) = \['updates' => [Updates](/API_docs/types/Updates.html), \];<a name="payments.paymentResult"></a>  

***
<br><br>[$payments.paymentVerificationNeeded](/API_docs/constructors/payments.paymentVerificationNeeded.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="payments.paymentVerificationNeeded"></a>  

***
<br><br>[$payments.savedInfo](/API_docs/constructors/payments.savedInfo.html) = \['has_saved_credentials' => [Bool](/API_docs/types/Bool.html), 'saved_info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), \];<a name="payments.savedInfo"></a>  

***
<br><br>[$payments.validatedRequestedInfo](/API_docs/constructors/payments.validatedRequestedInfo.html) = \['id' => [string](/API_docs/types/string.html), 'shipping_options' => \[[ShippingOption](/API_docs/types/ShippingOption.html)\], \];<a name="payments.validatedRequestedInfo"></a>  

***
<br><br>[$peerBlocked](/API_docs/constructors/peerBlocked.html) = \['peer_id' => [Peer](/API_docs/types/Peer.html), 'date' => [int](/API_docs/types/int.html), \];<a name="peerBlocked"></a>  

***
<br><br>[$peerChannel](/API_docs/constructors/peerChannel.html) = \['channel_id' => [long](/API_docs/types/long.html), \];<a name="peerChannel"></a>  

***
<br><br>[$peerChat](/API_docs/constructors/peerChat.html) = \['chat_id' => [long](/API_docs/types/long.html), \];<a name="peerChat"></a>  

***
<br><br>[$peerLocated](/API_docs/constructors/peerLocated.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'expires' => [int](/API_docs/types/int.html), 'distance' => [int](/API_docs/types/int.html), \];<a name="peerLocated"></a>  

***
<br><br>[$peerNotifySettings](/API_docs/constructors/peerNotifySettings.html) = \['show_previews' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'mute_until' => [int](/API_docs/types/int.html), 'ios_sound' => [NotificationSound](/API_docs/types/NotificationSound.html), 'android_sound' => [NotificationSound](/API_docs/types/NotificationSound.html), 'other_sound' => [NotificationSound](/API_docs/types/NotificationSound.html), \];<a name="peerNotifySettings"></a>  

***
<br><br>[$peerSelfLocated](/API_docs/constructors/peerSelfLocated.html) = \['expires' => [int](/API_docs/types/int.html), \];<a name="peerSelfLocated"></a>  

***
<br><br>[$peerSettings](/API_docs/constructors/peerSettings.html) = \['report_spam' => [Bool](/API_docs/types/Bool.html), 'add_contact' => [Bool](/API_docs/types/Bool.html), 'block_contact' => [Bool](/API_docs/types/Bool.html), 'share_contact' => [Bool](/API_docs/types/Bool.html), 'need_contacts_exception' => [Bool](/API_docs/types/Bool.html), 'report_geo' => [Bool](/API_docs/types/Bool.html), 'autoarchived' => [Bool](/API_docs/types/Bool.html), 'invite_members' => [Bool](/API_docs/types/Bool.html), 'request_chat_broadcast' => [Bool](/API_docs/types/Bool.html), 'geo_distance' => [int](/API_docs/types/int.html), 'request_chat_title' => [string](/API_docs/types/string.html), 'request_chat_date' => [int](/API_docs/types/int.html), \];<a name="peerSettings"></a>  

***
<br><br>[$peerUser](/API_docs/constructors/peerUser.html) = \['user_id' => [long](/API_docs/types/long.html), \];<a name="peerUser"></a>  

***
<br><br>[$phone.exportedGroupCallInvite](/API_docs/constructors/phone.exportedGroupCallInvite.html) = \['link' => [string](/API_docs/types/string.html), \];<a name="phone.exportedGroupCallInvite"></a>  

***
<br><br>[$phone.groupCall](/API_docs/constructors/phone.groupCall.html) = \['call' => [GroupCall](/API_docs/types/GroupCall.html), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html)\], 'participants_next_offset' => [string](/API_docs/types/string.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="phone.groupCall"></a>  

***
<br><br>[$phone.groupCallStreamChannels](/API_docs/constructors/phone.groupCallStreamChannels.html) = \['channels' => \[[GroupCallStreamChannel](/API_docs/types/GroupCallStreamChannel.html)\], \];<a name="phone.groupCallStreamChannels"></a>  

***
<br><br>[$phone.groupCallStreamRtmpUrl](/API_docs/constructors/phone.groupCallStreamRtmpUrl.html) = \['url' => [string](/API_docs/types/string.html), 'key' => [string](/API_docs/types/string.html), \];<a name="phone.groupCallStreamRtmpUrl"></a>  

***
<br><br>[$phone.groupParticipants](/API_docs/constructors/phone.groupParticipants.html) = \['count' => [int](/API_docs/types/int.html), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html)\], 'next_offset' => [string](/API_docs/types/string.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'version' => [int](/API_docs/types/int.html), \];<a name="phone.groupParticipants"></a>  

***
<br><br>[$phone.joinAsPeers](/API_docs/constructors/phone.joinAsPeers.html) = \['peers' => \[[Peer](/API_docs/types/Peer.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="phone.joinAsPeers"></a>  

***
<br><br>[$phone.phoneCall](/API_docs/constructors/phone.phoneCall.html) = \['phone_call' => [PhoneCall](/API_docs/types/PhoneCall.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="phone.phoneCall"></a>  

***
<br><br>[$phoneCall](/API_docs/constructors/phoneCall.html) = \['p2p_allowed' => [Bool](/API_docs/types/Bool.html), 'video' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'g_a_or_b' => [bytes](/API_docs/types/bytes.html), 'key_fingerprint' => [long](/API_docs/types/long.html), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), 'connections' => \[[PhoneConnection](/API_docs/types/PhoneConnection.html)\], 'start_date' => [int](/API_docs/types/int.html), \];<a name="phoneCall"></a>  

***
<br><br>[$phoneCallAccepted](/API_docs/constructors/phoneCallAccepted.html) = \['video' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'g_b' => [bytes](/API_docs/types/bytes.html), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), \];<a name="phoneCallAccepted"></a>  

***
<br><br>[$phoneCallDiscardReasonBusy](/API_docs/constructors/phoneCallDiscardReasonBusy.html) = \[\];<a name="phoneCallDiscardReasonBusy"></a>  

***
<br><br>[$phoneCallDiscardReasonDisconnect](/API_docs/constructors/phoneCallDiscardReasonDisconnect.html) = \[\];<a name="phoneCallDiscardReasonDisconnect"></a>  

***
<br><br>[$phoneCallDiscardReasonHangup](/API_docs/constructors/phoneCallDiscardReasonHangup.html) = \[\];<a name="phoneCallDiscardReasonHangup"></a>  

***
<br><br>[$phoneCallDiscardReasonMissed](/API_docs/constructors/phoneCallDiscardReasonMissed.html) = \[\];<a name="phoneCallDiscardReasonMissed"></a>  

***
<br><br>[$phoneCallDiscarded](/API_docs/constructors/phoneCallDiscarded.html) = \['need_rating' => [Bool](/API_docs/types/Bool.html), 'need_debug' => [Bool](/API_docs/types/Bool.html), 'video' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'reason' => [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html), 'duration' => [int](/API_docs/types/int.html), \];<a name="phoneCallDiscarded"></a>  

***
<br><br>[$phoneCallEmpty](/API_docs/constructors/phoneCallEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="phoneCallEmpty"></a>  

***
<br><br>[$phoneCallProtocol](/API_docs/constructors/phoneCallProtocol.html) = \['udp_p2p' => [Bool](/API_docs/types/Bool.html), 'udp_reflector' => [Bool](/API_docs/types/Bool.html), 'min_layer' => [int](/API_docs/types/int.html), 'max_layer' => [int](/API_docs/types/int.html), 'library_versions' => \[[string](/API_docs/types/string.html)\], \];<a name="phoneCallProtocol"></a>  

***
<br><br>[$phoneCallRequested](/API_docs/constructors/phoneCallRequested.html) = \['video' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'g_a_hash' => [bytes](/API_docs/types/bytes.html), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), \];<a name="phoneCallRequested"></a>  

***
<br><br>[$phoneCallWaiting](/API_docs/constructors/phoneCallWaiting.html) = \['video' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'admin_id' => [long](/API_docs/types/long.html), 'participant_id' => [long](/API_docs/types/long.html), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), 'receive_date' => [int](/API_docs/types/int.html), \];<a name="phoneCallWaiting"></a>  

***
<br><br>[$phoneConnection](/API_docs/constructors/phoneConnection.html) = \['tcp' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'ip' => [string](/API_docs/types/string.html), 'ipv6' => [string](/API_docs/types/string.html), 'port' => [int](/API_docs/types/int.html), 'peer_tag' => [bytes](/API_docs/types/bytes.html), \];<a name="phoneConnection"></a>  

***
<br><br>[$phoneConnectionWebrtc](/API_docs/constructors/phoneConnectionWebrtc.html) = \['turn' => [Bool](/API_docs/types/Bool.html), 'stun' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'ip' => [string](/API_docs/types/string.html), 'ipv6' => [string](/API_docs/types/string.html), 'port' => [int](/API_docs/types/int.html), 'username' => [string](/API_docs/types/string.html), 'password' => [string](/API_docs/types/string.html), \];<a name="phoneConnectionWebrtc"></a>  

***
<br><br>[$photo](/API_docs/constructors/photo.html) = \['has_stickers' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'file_reference' => [bytes](/API_docs/types/bytes.html), 'date' => [int](/API_docs/types/int.html), 'sizes' => \[[PhotoSize](/API_docs/types/PhotoSize.html)\], 'video_sizes' => \[[VideoSize](/API_docs/types/VideoSize.html)\], 'dc_id' => [int](/API_docs/types/int.html), \];<a name="photo"></a>  

***
<br><br>[$photoCachedSize\_23](/API_docs/constructors/photoCachedSize_23.html) = \['type' => [string](/API_docs/types/string.html), 'location' => [FileLocation](/API_docs/types/FileLocation.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="photoCachedSize_23"></a>  

***
<br><br>[$photoEmpty](/API_docs/constructors/photoEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="photoEmpty"></a>  

***
<br><br>[$photoPathSize](/API_docs/constructors/photoPathSize.html) = \['type' => [string](/API_docs/types/string.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="photoPathSize"></a>  

***
<br><br>[$photoSize\_23](/API_docs/constructors/photoSize_23.html) = \['type' => [string](/API_docs/types/string.html), 'location' => [FileLocation](/API_docs/types/FileLocation.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'size' => [int](/API_docs/types/int.html), \];<a name="photoSize_23"></a>  

***
<br><br>[$photoSizeEmpty](/API_docs/constructors/photoSizeEmpty.html) = \['type' => [string](/API_docs/types/string.html), \];<a name="photoSizeEmpty"></a>  

***
<br><br>[$photoSizeProgressive](/API_docs/constructors/photoSizeProgressive.html) = \['type' => [string](/API_docs/types/string.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'sizes' => \[[int](/API_docs/types/int.html)\], \];<a name="photoSizeProgressive"></a>  

***
<br><br>[$photoStrippedSize](/API_docs/constructors/photoStrippedSize.html) = \['type' => [string](/API_docs/types/string.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="photoStrippedSize"></a>  

***
<br><br>[$photos.photo](/API_docs/constructors/photos.photo.html) = \['photo' => [Photo](/API_docs/types/Photo.html), 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="photos.photo"></a>  

***
<br><br>[$photos.photos](/API_docs/constructors/photos.photos.html) = \['photos' => \[[Photo](/API_docs/types/Photo.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="photos.photos"></a>  

***
<br><br>[$photos.photosSlice](/API_docs/constructors/photos.photosSlice.html) = \['count' => [int](/API_docs/types/int.html), 'photos' => \[[Photo](/API_docs/types/Photo.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="photos.photosSlice"></a>  

***
<br><br>[$poll](/API_docs/constructors/poll.html) = \['id' => [long](/API_docs/types/long.html), 'closed' => [Bool](/API_docs/types/Bool.html), 'public_voters' => [Bool](/API_docs/types/Bool.html), 'multiple_choice' => [Bool](/API_docs/types/Bool.html), 'quiz' => [Bool](/API_docs/types/Bool.html), 'question' => [string](/API_docs/types/string.html), 'answers' => \[[PollAnswer](/API_docs/types/PollAnswer.html)\], 'close_period' => [int](/API_docs/types/int.html), 'close_date' => [int](/API_docs/types/int.html), \];<a name="poll"></a>  

***
<br><br>[$pollAnswer](/API_docs/constructors/pollAnswer.html) = \['text' => [string](/API_docs/types/string.html), 'option' => [bytes](/API_docs/types/bytes.html), \];<a name="pollAnswer"></a>  

***
<br><br>[$pollAnswerVoters](/API_docs/constructors/pollAnswerVoters.html) = \['chosen' => [Bool](/API_docs/types/Bool.html), 'correct' => [Bool](/API_docs/types/Bool.html), 'option' => [bytes](/API_docs/types/bytes.html), 'voters' => [int](/API_docs/types/int.html), \];<a name="pollAnswerVoters"></a>  

***
<br><br>[$pollResults](/API_docs/constructors/pollResults.html) = \['min' => [Bool](/API_docs/types/Bool.html), 'results' => \[[PollAnswerVoters](/API_docs/types/PollAnswerVoters.html)\], 'total_voters' => [int](/API_docs/types/int.html), 'recent_voters' => \[[long](/API_docs/types/long.html)\], 'solution' => [string](/API_docs/types/string.html), 'solution_entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="pollResults"></a>  

***
<br><br>[$popularContact](/API_docs/constructors/popularContact.html) = \['client_id' => [long](/API_docs/types/long.html), 'importers' => [int](/API_docs/types/int.html), \];<a name="popularContact"></a>  

***
<br><br>[$postAddress](/API_docs/constructors/postAddress.html) = \['street_line1' => [string](/API_docs/types/string.html), 'street_line2' => [string](/API_docs/types/string.html), 'city' => [string](/API_docs/types/string.html), 'state' => [string](/API_docs/types/string.html), 'country_iso2' => [string](/API_docs/types/string.html), 'post_code' => [string](/API_docs/types/string.html), \];<a name="postAddress"></a>  

***
<br><br>[$privacyKeyAddedByPhone](/API_docs/constructors/privacyKeyAddedByPhone.html) = \[\];<a name="privacyKeyAddedByPhone"></a>  

***
<br><br>[$privacyKeyChatInvite](/API_docs/constructors/privacyKeyChatInvite.html) = \[\];<a name="privacyKeyChatInvite"></a>  

***
<br><br>[$privacyKeyForwards](/API_docs/constructors/privacyKeyForwards.html) = \[\];<a name="privacyKeyForwards"></a>  

***
<br><br>[$privacyKeyPhoneCall](/API_docs/constructors/privacyKeyPhoneCall.html) = \[\];<a name="privacyKeyPhoneCall"></a>  

***
<br><br>[$privacyKeyPhoneNumber](/API_docs/constructors/privacyKeyPhoneNumber.html) = \[\];<a name="privacyKeyPhoneNumber"></a>  

***
<br><br>[$privacyKeyPhoneP2P](/API_docs/constructors/privacyKeyPhoneP2P.html) = \[\];<a name="privacyKeyPhoneP2P"></a>  

***
<br><br>[$privacyKeyProfilePhoto](/API_docs/constructors/privacyKeyProfilePhoto.html) = \[\];<a name="privacyKeyProfilePhoto"></a>  

***
<br><br>[$privacyKeyStatusTimestamp](/API_docs/constructors/privacyKeyStatusTimestamp.html) = \[\];<a name="privacyKeyStatusTimestamp"></a>  

***
<br><br>[$privacyValueAllowAll](/API_docs/constructors/privacyValueAllowAll.html) = \[\];<a name="privacyValueAllowAll"></a>  

***
<br><br>[$privacyValueAllowChatParticipants](/API_docs/constructors/privacyValueAllowChatParticipants.html) = \['chats' => \[[long](/API_docs/types/long.html)\], \];<a name="privacyValueAllowChatParticipants"></a>  

***
<br><br>[$privacyValueAllowContacts](/API_docs/constructors/privacyValueAllowContacts.html) = \[\];<a name="privacyValueAllowContacts"></a>  

***
<br><br>[$privacyValueAllowUsers](/API_docs/constructors/privacyValueAllowUsers.html) = \['users' => \[[long](/API_docs/types/long.html)\], \];<a name="privacyValueAllowUsers"></a>  

***
<br><br>[$privacyValueDisallowAll](/API_docs/constructors/privacyValueDisallowAll.html) = \[\];<a name="privacyValueDisallowAll"></a>  

***
<br><br>[$privacyValueDisallowChatParticipants](/API_docs/constructors/privacyValueDisallowChatParticipants.html) = \['chats' => \[[long](/API_docs/types/long.html)\], \];<a name="privacyValueDisallowChatParticipants"></a>  

***
<br><br>[$privacyValueDisallowContacts](/API_docs/constructors/privacyValueDisallowContacts.html) = \[\];<a name="privacyValueDisallowContacts"></a>  

***
<br><br>[$privacyValueDisallowUsers](/API_docs/constructors/privacyValueDisallowUsers.html) = \['users' => \[[long](/API_docs/types/long.html)\], \];<a name="privacyValueDisallowUsers"></a>  

***
<br><br>[$reactionCount](/API_docs/constructors/reactionCount.html) = \['chosen' => [Bool](/API_docs/types/Bool.html), 'reaction' => [string](/API_docs/types/string.html), 'count' => [int](/API_docs/types/int.html), \];<a name="reactionCount"></a>  

***
<br><br>[$receivedNotifyMessage](/API_docs/constructors/receivedNotifyMessage.html) = \['id' => [int](/API_docs/types/int.html), \];<a name="receivedNotifyMessage"></a>  

***
<br><br>[$recentMeUrlChat](/API_docs/constructors/recentMeUrlChat.html) = \['url' => [string](/API_docs/types/string.html), 'chat_id' => [long](/API_docs/types/long.html), \];<a name="recentMeUrlChat"></a>  

***
<br><br>[$recentMeUrlChatInvite](/API_docs/constructors/recentMeUrlChatInvite.html) = \['url' => [string](/API_docs/types/string.html), 'chat_invite' => [ChatInvite](/API_docs/types/ChatInvite.html), \];<a name="recentMeUrlChatInvite"></a>  

***
<br><br>[$recentMeUrlStickerSet](/API_docs/constructors/recentMeUrlStickerSet.html) = \['url' => [string](/API_docs/types/string.html), 'set' => [StickerSetCovered](/API_docs/types/StickerSetCovered.html), \];<a name="recentMeUrlStickerSet"></a>  

***
<br><br>[$recentMeUrlUnknown](/API_docs/constructors/recentMeUrlUnknown.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="recentMeUrlUnknown"></a>  

***
<br><br>[$recentMeUrlUser](/API_docs/constructors/recentMeUrlUser.html) = \['url' => [string](/API_docs/types/string.html), 'user_id' => [long](/API_docs/types/long.html), \];<a name="recentMeUrlUser"></a>  

***
<br><br>[$replyInlineMarkup](/API_docs/constructors/replyInlineMarkup.html) = \['rows' => \[[KeyboardButtonRow](/API_docs/types/KeyboardButtonRow.html)\], \];<a name="replyInlineMarkup"></a>  

***
<br><br>[$replyKeyboardForceReply](/API_docs/constructors/replyKeyboardForceReply.html) = \['single_use' => [Bool](/API_docs/types/Bool.html), 'selective' => [Bool](/API_docs/types/Bool.html), 'placeholder' => [string](/API_docs/types/string.html), \];<a name="replyKeyboardForceReply"></a>  

***
<br><br>[$replyKeyboardHide](/API_docs/constructors/replyKeyboardHide.html) = \['selective' => [Bool](/API_docs/types/Bool.html), \];<a name="replyKeyboardHide"></a>  

***
<br><br>[$replyKeyboardMarkup](/API_docs/constructors/replyKeyboardMarkup.html) = \['resize' => [Bool](/API_docs/types/Bool.html), 'single_use' => [Bool](/API_docs/types/Bool.html), 'selective' => [Bool](/API_docs/types/Bool.html), 'rows' => \[[KeyboardButtonRow](/API_docs/types/KeyboardButtonRow.html)\], 'placeholder' => [string](/API_docs/types/string.html), \];<a name="replyKeyboardMarkup"></a>  

***
<br><br>[$restrictionReason](/API_docs/constructors/restrictionReason.html) = \['platform' => [string](/API_docs/types/string.html), 'reason' => [string](/API_docs/types/string.html), 'text' => [string](/API_docs/types/string.html), \];<a name="restrictionReason"></a>  

***
<br><br>[$savedPhoneContact](/API_docs/constructors/savedPhoneContact.html) = \['phone' => [string](/API_docs/types/string.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'date' => [int](/API_docs/types/int.html), \];<a name="savedPhoneContact"></a>  

***
<br><br>[$searchResultPosition](/API_docs/constructors/searchResultPosition.html) = \['msg_id' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'offset' => [int](/API_docs/types/int.html), \];<a name="searchResultPosition"></a>  

***
<br><br>[$searchResultsCalendarPeriod](/API_docs/constructors/searchResultsCalendarPeriod.html) = \['date' => [int](/API_docs/types/int.html), 'min_msg_id' => [int](/API_docs/types/int.html), 'max_msg_id' => [int](/API_docs/types/int.html), 'count' => [int](/API_docs/types/int.html), \];<a name="searchResultsCalendarPeriod"></a>  

***
<br><br>[$secureCredentialsEncrypted](/API_docs/constructors/secureCredentialsEncrypted.html) = \['data' => [bytes](/API_docs/types/bytes.html), 'hash' => [bytes](/API_docs/types/bytes.html), 'secret' => [bytes](/API_docs/types/bytes.html), \];<a name="secureCredentialsEncrypted"></a>  

***
<br><br>[$secureData](/API_docs/constructors/secureData.html) = \['data' => [bytes](/API_docs/types/bytes.html), 'data_hash' => [bytes](/API_docs/types/bytes.html), 'secret' => [bytes](/API_docs/types/bytes.html), \];<a name="secureData"></a>  

***
<br><br>[$secureFile](/API_docs/constructors/secureFile.html) = \['id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'size' => [long](/API_docs/types/long.html), 'dc_id' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'secret' => [bytes](/API_docs/types/bytes.html), \];<a name="secureFile"></a>  

***
<br><br>[$secureFileEmpty](/API_docs/constructors/secureFileEmpty.html) = \[\];<a name="secureFileEmpty"></a>  

***
<br><br>[$securePasswordKdfAlgoPBKDF2HMACSHA512iter100000](/API_docs/constructors/securePasswordKdfAlgoPBKDF2HMACSHA512iter100000.html) = \['salt' => [bytes](/API_docs/types/bytes.html), \];<a name="securePasswordKdfAlgoPBKDF2HMACSHA512iter100000"></a>  

***
<br><br>[$securePasswordKdfAlgoSHA512](/API_docs/constructors/securePasswordKdfAlgoSHA512.html) = \['salt' => [bytes](/API_docs/types/bytes.html), \];<a name="securePasswordKdfAlgoSHA512"></a>  

***
<br><br>[$securePasswordKdfAlgoUnknown](/API_docs/constructors/securePasswordKdfAlgoUnknown.html) = \[\];<a name="securePasswordKdfAlgoUnknown"></a>  

***
<br><br>[$securePlainEmail](/API_docs/constructors/securePlainEmail.html) = \['email' => [string](/API_docs/types/string.html), \];<a name="securePlainEmail"></a>  

***
<br><br>[$securePlainPhone](/API_docs/constructors/securePlainPhone.html) = \['phone' => [string](/API_docs/types/string.html), \];<a name="securePlainPhone"></a>  

***
<br><br>[$secureRequiredType](/API_docs/constructors/secureRequiredType.html) = \['native_names' => [Bool](/API_docs/types/Bool.html), 'selfie_required' => [Bool](/API_docs/types/Bool.html), 'translation_required' => [Bool](/API_docs/types/Bool.html), 'type' => [SecureValueType](/API_docs/types/SecureValueType.html), \];<a name="secureRequiredType"></a>  

***
<br><br>[$secureRequiredTypeOneOf](/API_docs/constructors/secureRequiredTypeOneOf.html) = \['types' => \[[SecureRequiredType](/API_docs/types/SecureRequiredType.html)\], \];<a name="secureRequiredTypeOneOf"></a>  

***
<br><br>[$secureSecretSettings](/API_docs/constructors/secureSecretSettings.html) = \['secure_algo' => [SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.html), 'secure_secret' => [bytes](/API_docs/types/bytes.html), 'secure_secret_id' => [long](/API_docs/types/long.html), \];<a name="secureSecretSettings"></a>  

***
<br><br>[$secureValue](/API_docs/constructors/secureValue.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'data' => [SecureData](/API_docs/types/SecureData.html), 'front_side' => [SecureFile](/API_docs/types/SecureFile.html), 'reverse_side' => [SecureFile](/API_docs/types/SecureFile.html), 'selfie' => [SecureFile](/API_docs/types/SecureFile.html), 'translation' => \[[SecureFile](/API_docs/types/SecureFile.html)\], 'files' => \[[SecureFile](/API_docs/types/SecureFile.html)\], 'plain_data' => [SecurePlainData](/API_docs/types/SecurePlainData.html), 'hash' => [bytes](/API_docs/types/bytes.html), \];<a name="secureValue"></a>  

***
<br><br>[$secureValueError](/API_docs/constructors/secureValueError.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueError"></a>  

***
<br><br>[$secureValueErrorData](/API_docs/constructors/secureValueErrorData.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'data_hash' => [bytes](/API_docs/types/bytes.html), 'field' => [string](/API_docs/types/string.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorData"></a>  

***
<br><br>[$secureValueErrorFile](/API_docs/constructors/secureValueErrorFile.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorFile"></a>  

***
<br><br>[$secureValueErrorFiles](/API_docs/constructors/secureValueErrorFiles.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => \[[bytes](/API_docs/types/bytes.html)\], 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorFiles"></a>  

***
<br><br>[$secureValueErrorFrontSide](/API_docs/constructors/secureValueErrorFrontSide.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorFrontSide"></a>  

***
<br><br>[$secureValueErrorReverseSide](/API_docs/constructors/secureValueErrorReverseSide.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorReverseSide"></a>  

***
<br><br>[$secureValueErrorSelfie](/API_docs/constructors/secureValueErrorSelfie.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorSelfie"></a>  

***
<br><br>[$secureValueErrorTranslationFile](/API_docs/constructors/secureValueErrorTranslationFile.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => [bytes](/API_docs/types/bytes.html), 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorTranslationFile"></a>  

***
<br><br>[$secureValueErrorTranslationFiles](/API_docs/constructors/secureValueErrorTranslationFiles.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'file_hash' => \[[bytes](/API_docs/types/bytes.html)\], 'text' => [string](/API_docs/types/string.html), \];<a name="secureValueErrorTranslationFiles"></a>  

***
<br><br>[$secureValueHash](/API_docs/constructors/secureValueHash.html) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.html), 'hash' => [bytes](/API_docs/types/bytes.html), \];<a name="secureValueHash"></a>  

***
<br><br>[$secureValueTypeAddress](/API_docs/constructors/secureValueTypeAddress.html) = \[\];<a name="secureValueTypeAddress"></a>  

***
<br><br>[$secureValueTypeBankStatement](/API_docs/constructors/secureValueTypeBankStatement.html) = \[\];<a name="secureValueTypeBankStatement"></a>  

***
<br><br>[$secureValueTypeDriverLicense](/API_docs/constructors/secureValueTypeDriverLicense.html) = \[\];<a name="secureValueTypeDriverLicense"></a>  

***
<br><br>[$secureValueTypeEmail](/API_docs/constructors/secureValueTypeEmail.html) = \[\];<a name="secureValueTypeEmail"></a>  

***
<br><br>[$secureValueTypeIdentityCard](/API_docs/constructors/secureValueTypeIdentityCard.html) = \[\];<a name="secureValueTypeIdentityCard"></a>  

***
<br><br>[$secureValueTypeInternalPassport](/API_docs/constructors/secureValueTypeInternalPassport.html) = \[\];<a name="secureValueTypeInternalPassport"></a>  

***
<br><br>[$secureValueTypePassport](/API_docs/constructors/secureValueTypePassport.html) = \[\];<a name="secureValueTypePassport"></a>  

***
<br><br>[$secureValueTypePassportRegistration](/API_docs/constructors/secureValueTypePassportRegistration.html) = \[\];<a name="secureValueTypePassportRegistration"></a>  

***
<br><br>[$secureValueTypePersonalDetails](/API_docs/constructors/secureValueTypePersonalDetails.html) = \[\];<a name="secureValueTypePersonalDetails"></a>  

***
<br><br>[$secureValueTypePhone](/API_docs/constructors/secureValueTypePhone.html) = \[\];<a name="secureValueTypePhone"></a>  

***
<br><br>[$secureValueTypeRentalAgreement](/API_docs/constructors/secureValueTypeRentalAgreement.html) = \[\];<a name="secureValueTypeRentalAgreement"></a>  

***
<br><br>[$secureValueTypeTemporaryRegistration](/API_docs/constructors/secureValueTypeTemporaryRegistration.html) = \[\];<a name="secureValueTypeTemporaryRegistration"></a>  

***
<br><br>[$secureValueTypeUtilityBill](/API_docs/constructors/secureValueTypeUtilityBill.html) = \[\];<a name="secureValueTypeUtilityBill"></a>  

***
<br><br>[$sendMessageCancelAction](/API_docs/constructors/sendMessageCancelAction.html) = \[\];<a name="sendMessageCancelAction"></a>  

***
<br><br>[$sendMessageChooseContactAction](/API_docs/constructors/sendMessageChooseContactAction.html) = \[\];<a name="sendMessageChooseContactAction"></a>  

***
<br><br>[$sendMessageChooseStickerAction](/API_docs/constructors/sendMessageChooseStickerAction.html) = \[\];<a name="sendMessageChooseStickerAction"></a>  

***
<br><br>[$sendMessageEmojiInteraction](/API_docs/constructors/sendMessageEmojiInteraction.html) = \['emoticon' => [string](/API_docs/types/string.html), 'msg_id' => [int](/API_docs/types/int.html), 'interaction' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="sendMessageEmojiInteraction"></a>  

***
<br><br>[$sendMessageEmojiInteractionSeen](/API_docs/constructors/sendMessageEmojiInteractionSeen.html) = \['emoticon' => [string](/API_docs/types/string.html), \];<a name="sendMessageEmojiInteractionSeen"></a>  

***
<br><br>[$sendMessageGamePlayAction](/API_docs/constructors/sendMessageGamePlayAction.html) = \[\];<a name="sendMessageGamePlayAction"></a>  

***
<br><br>[$sendMessageGeoLocationAction](/API_docs/constructors/sendMessageGeoLocationAction.html) = \[\];<a name="sendMessageGeoLocationAction"></a>  

***
<br><br>[$sendMessageHistoryImportAction](/API_docs/constructors/sendMessageHistoryImportAction.html) = \['progress' => [int](/API_docs/types/int.html), \];<a name="sendMessageHistoryImportAction"></a>  

***
<br><br>[$sendMessageRecordAudioAction](/API_docs/constructors/sendMessageRecordAudioAction.html) = \[\];<a name="sendMessageRecordAudioAction"></a>  

***
<br><br>[$sendMessageRecordRoundAction](/API_docs/constructors/sendMessageRecordRoundAction.html) = \[\];<a name="sendMessageRecordRoundAction"></a>  

***
<br><br>[$sendMessageRecordVideoAction](/API_docs/constructors/sendMessageRecordVideoAction.html) = \[\];<a name="sendMessageRecordVideoAction"></a>  

***
<br><br>[$sendMessageTypingAction](/API_docs/constructors/sendMessageTypingAction.html) = \[\];<a name="sendMessageTypingAction"></a>  

***
<br><br>[$sendMessageUploadAudioAction\_17](/API_docs/constructors/sendMessageUploadAudioAction_17.html) = \[\];<a name="sendMessageUploadAudioAction_17"></a>  

***
<br><br>[$sendMessageUploadDocumentAction\_17](/API_docs/constructors/sendMessageUploadDocumentAction_17.html) = \[\];<a name="sendMessageUploadDocumentAction_17"></a>  

***
<br><br>[$sendMessageUploadPhotoAction\_17](/API_docs/constructors/sendMessageUploadPhotoAction_17.html) = \[\];<a name="sendMessageUploadPhotoAction_17"></a>  

***
<br><br>[$sendMessageUploadRoundAction](/API_docs/constructors/sendMessageUploadRoundAction.html) = \['progress' => [int](/API_docs/types/int.html), \];<a name="sendMessageUploadRoundAction"></a>  

***
<br><br>[$sendMessageUploadVideoAction\_17](/API_docs/constructors/sendMessageUploadVideoAction_17.html) = \[\];<a name="sendMessageUploadVideoAction_17"></a>  

***
<br><br>[$shippingOption](/API_docs/constructors/shippingOption.html) = \['id' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'prices' => \[[LabeledPrice](/API_docs/types/LabeledPrice.html)\], \];<a name="shippingOption"></a>  

***
<br><br>[$simpleWebViewResultUrl](/API_docs/constructors/simpleWebViewResultUrl.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="simpleWebViewResultUrl"></a>  

***
<br><br>[$speakingInGroupCallAction](/API_docs/constructors/speakingInGroupCallAction.html) = \[\];<a name="speakingInGroupCallAction"></a>  

***
<br><br>[$sponsoredMessage](/API_docs/constructors/sponsoredMessage.html) = \['recommended' => [Bool](/API_docs/types/Bool.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'chat_invite' => [ChatInvite](/API_docs/types/ChatInvite.html), 'chat_invite_hash' => [string](/API_docs/types/string.html), 'channel_post' => [int](/API_docs/types/int.html), 'start_param' => [string](/API_docs/types/string.html), 'message' => [string](/API_docs/types/string.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="sponsoredMessage"></a>  

***
<br><br>[$stats.broadcastStats](/API_docs/constructors/stats.broadcastStats.html) = \['period' => [StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.html), 'followers' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'views_per_post' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'shares_per_post' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'enabled_notifications' => [StatsPercentValue](/API_docs/types/StatsPercentValue.html), 'growth_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'followers_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'mute_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'top_hours_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'interactions_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'iv_interactions_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'views_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'new_followers_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'languages_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'recent_message_interactions' => \[[MessageInteractionCounters](/API_docs/types/MessageInteractionCounters.html)\], \];<a name="stats.broadcastStats"></a>  

***
<br><br>[$stats.megagroupStats](/API_docs/constructors/stats.megagroupStats.html) = \['period' => [StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.html), 'members' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'messages' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'viewers' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'posters' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.html), 'growth_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'members_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'new_members_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'languages_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'messages_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'actions_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'top_hours_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'weekdays_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), 'top_posters' => \[[StatsGroupTopPoster](/API_docs/types/StatsGroupTopPoster.html)\], 'top_admins' => \[[StatsGroupTopAdmin](/API_docs/types/StatsGroupTopAdmin.html)\], 'top_inviters' => \[[StatsGroupTopInviter](/API_docs/types/StatsGroupTopInviter.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="stats.megagroupStats"></a>  

***
<br><br>[$stats.messageStats](/API_docs/constructors/stats.messageStats.html) = \['views_graph' => [StatsGraph](/API_docs/types/StatsGraph.html), \];<a name="stats.messageStats"></a>  

***
<br><br>[$statsAbsValueAndPrev](/API_docs/constructors/statsAbsValueAndPrev.html) = \['current' => [double](/API_docs/types/double.html), 'previous' => [double](/API_docs/types/double.html), \];<a name="statsAbsValueAndPrev"></a>  

***
<br><br>[$statsDateRangeDays](/API_docs/constructors/statsDateRangeDays.html) = \['min_date' => [int](/API_docs/types/int.html), 'max_date' => [int](/API_docs/types/int.html), \];<a name="statsDateRangeDays"></a>  

***
<br><br>[$statsGraph](/API_docs/constructors/statsGraph.html) = \['json' => [DataJSON](/API_docs/types/DataJSON.html), 'zoom_token' => [string](/API_docs/types/string.html), \];<a name="statsGraph"></a>  

***
<br><br>[$statsGraphAsync](/API_docs/constructors/statsGraphAsync.html) = \['token' => [string](/API_docs/types/string.html), \];<a name="statsGraphAsync"></a>  

***
<br><br>[$statsGraphError](/API_docs/constructors/statsGraphError.html) = \['error' => [string](/API_docs/types/string.html), \];<a name="statsGraphError"></a>  

***
<br><br>[$statsGroupTopAdmin](/API_docs/constructors/statsGroupTopAdmin.html) = \['user_id' => [long](/API_docs/types/long.html), 'deleted' => [int](/API_docs/types/int.html), 'kicked' => [int](/API_docs/types/int.html), 'banned' => [int](/API_docs/types/int.html), \];<a name="statsGroupTopAdmin"></a>  

***
<br><br>[$statsGroupTopInviter](/API_docs/constructors/statsGroupTopInviter.html) = \['user_id' => [long](/API_docs/types/long.html), 'invitations' => [int](/API_docs/types/int.html), \];<a name="statsGroupTopInviter"></a>  

***
<br><br>[$statsGroupTopPoster](/API_docs/constructors/statsGroupTopPoster.html) = \['user_id' => [long](/API_docs/types/long.html), 'messages' => [int](/API_docs/types/int.html), 'avg_chars' => [int](/API_docs/types/int.html), \];<a name="statsGroupTopPoster"></a>  

***
<br><br>[$statsPercentValue](/API_docs/constructors/statsPercentValue.html) = \['part' => [double](/API_docs/types/double.html), 'total' => [double](/API_docs/types/double.html), \];<a name="statsPercentValue"></a>  

***
<br><br>[$statsURL](/API_docs/constructors/statsURL.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="statsURL"></a>  

***
<br><br>[$stickerPack](/API_docs/constructors/stickerPack.html) = \['emoticon' => [string](/API_docs/types/string.html), 'documents' => \[[long](/API_docs/types/long.html)\], \];<a name="stickerPack"></a>  

***
<br><br>[$stickerSet](/API_docs/constructors/stickerSet.html) = \['archived' => [Bool](/API_docs/types/Bool.html), 'official' => [Bool](/API_docs/types/Bool.html), 'masks' => [Bool](/API_docs/types/Bool.html), 'animated' => [Bool](/API_docs/types/Bool.html), 'videos' => [Bool](/API_docs/types/Bool.html), 'installed_date' => [int](/API_docs/types/int.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'title' => [string](/API_docs/types/string.html), 'short_name' => [string](/API_docs/types/string.html), 'thumbs' => \[[PhotoSize](/API_docs/types/PhotoSize.html)\], 'thumb_dc_id' => [int](/API_docs/types/int.html), 'thumb_version' => [int](/API_docs/types/int.html), 'count' => [int](/API_docs/types/int.html), 'hash' => [int](/API_docs/types/int.html), \];<a name="stickerSet"></a>  

***
<br><br>[$stickerSetCovered](/API_docs/constructors/stickerSetCovered.html) = \['set' => [StickerSet](/API_docs/types/StickerSet.html), 'cover' => [Document](/API_docs/types/Document.html), \];<a name="stickerSetCovered"></a>  

***
<br><br>[$stickerSetMultiCovered](/API_docs/constructors/stickerSetMultiCovered.html) = \['set' => [StickerSet](/API_docs/types/StickerSet.html), 'covers' => \[[Document](/API_docs/types/Document.html)\], \];<a name="stickerSetMultiCovered"></a>  

***
<br><br>[$stickers.suggestedShortName](/API_docs/constructors/stickers.suggestedShortName.html) = \['short_name' => [string](/API_docs/types/string.html), \];<a name="stickers.suggestedShortName"></a>  

***
<br><br>[$storage.fileGif](/API_docs/constructors/storage.fileGif.html) = \[\];<a name="storage.fileGif"></a>  

***
<br><br>[$storage.fileJpeg](/API_docs/constructors/storage.fileJpeg.html) = \[\];<a name="storage.fileJpeg"></a>  

***
<br><br>[$storage.fileMov](/API_docs/constructors/storage.fileMov.html) = \[\];<a name="storage.fileMov"></a>  

***
<br><br>[$storage.fileMp3](/API_docs/constructors/storage.fileMp3.html) = \[\];<a name="storage.fileMp3"></a>  

***
<br><br>[$storage.fileMp4](/API_docs/constructors/storage.fileMp4.html) = \[\];<a name="storage.fileMp4"></a>  

***
<br><br>[$storage.filePartial](/API_docs/constructors/storage.filePartial.html) = \[\];<a name="storage.filePartial"></a>  

***
<br><br>[$storage.filePdf](/API_docs/constructors/storage.filePdf.html) = \[\];<a name="storage.filePdf"></a>  

***
<br><br>[$storage.filePng](/API_docs/constructors/storage.filePng.html) = \[\];<a name="storage.filePng"></a>  

***
<br><br>[$storage.fileUnknown](/API_docs/constructors/storage.fileUnknown.html) = \[\];<a name="storage.fileUnknown"></a>  

***
<br><br>[$storage.fileWebp](/API_docs/constructors/storage.fileWebp.html) = \[\];<a name="storage.fileWebp"></a>  

***
<br><br>[$textAnchor](/API_docs/constructors/textAnchor.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'name' => [string](/API_docs/types/string.html), \];<a name="textAnchor"></a>  

***
<br><br>[$textBold](/API_docs/constructors/textBold.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textBold"></a>  

***
<br><br>[$textConcat](/API_docs/constructors/textConcat.html) = \['texts' => \[[RichText](/API_docs/types/RichText.html)\], \];<a name="textConcat"></a>  

***
<br><br>[$textEmail](/API_docs/constructors/textEmail.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'email' => [string](/API_docs/types/string.html), \];<a name="textEmail"></a>  

***
<br><br>[$textEmpty](/API_docs/constructors/textEmpty.html) = \[\];<a name="textEmpty"></a>  

***
<br><br>[$textFixed](/API_docs/constructors/textFixed.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textFixed"></a>  

***
<br><br>[$textImage](/API_docs/constructors/textImage.html) = \['document_id' => [long](/API_docs/types/long.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), \];<a name="textImage"></a>  

***
<br><br>[$textItalic](/API_docs/constructors/textItalic.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textItalic"></a>  

***
<br><br>[$textMarked](/API_docs/constructors/textMarked.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textMarked"></a>  

***
<br><br>[$textPhone](/API_docs/constructors/textPhone.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'phone' => [string](/API_docs/types/string.html), \];<a name="textPhone"></a>  

***
<br><br>[$textPlain](/API_docs/constructors/textPlain.html) = \['text' => [string](/API_docs/types/string.html), \];<a name="textPlain"></a>  

***
<br><br>[$textStrike](/API_docs/constructors/textStrike.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textStrike"></a>  

***
<br><br>[$textSubscript](/API_docs/constructors/textSubscript.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textSubscript"></a>  

***
<br><br>[$textSuperscript](/API_docs/constructors/textSuperscript.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textSuperscript"></a>  

***
<br><br>[$textUnderline](/API_docs/constructors/textUnderline.html) = \['text' => [RichText](/API_docs/types/RichText.html), \];<a name="textUnderline"></a>  

***
<br><br>[$textUrl](/API_docs/constructors/textUrl.html) = \['text' => [RichText](/API_docs/types/RichText.html), 'url' => [string](/API_docs/types/string.html), 'webpage_id' => [long](/API_docs/types/long.html), \];<a name="textUrl"></a>  

***
<br><br>[$theme](/API_docs/constructors/theme.html) = \['creator' => [Bool](/API_docs/types/Bool.html), 'default' => [Bool](/API_docs/types/Bool.html), 'for_chat' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'slug' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'document' => [Document](/API_docs/types/Document.html), 'settings' => \[[ThemeSettings](/API_docs/types/ThemeSettings.html)\], 'emoticon' => [string](/API_docs/types/string.html), 'installs_count' => [int](/API_docs/types/int.html), \];<a name="theme"></a>  

***
<br><br>[$themeSettings](/API_docs/constructors/themeSettings.html) = \['message_colors_animated' => [Bool](/API_docs/types/Bool.html), 'base_theme' => [BaseTheme](/API_docs/types/BaseTheme.html), 'accent_color' => [int](/API_docs/types/int.html), 'outbox_accent_color' => [int](/API_docs/types/int.html), 'message_colors' => \[[int](/API_docs/types/int.html)\], 'wallpaper' => [WallPaper](/API_docs/types/WallPaper.html), \];<a name="themeSettings"></a>  

***
<br><br>[$topPeer](/API_docs/constructors/topPeer.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'rating' => [double](/API_docs/types/double.html), \];<a name="topPeer"></a>  

***
<br><br>[$topPeerCategoryBotsInline](/API_docs/constructors/topPeerCategoryBotsInline.html) = \[\];<a name="topPeerCategoryBotsInline"></a>  

***
<br><br>[$topPeerCategoryBotsPM](/API_docs/constructors/topPeerCategoryBotsPM.html) = \[\];<a name="topPeerCategoryBotsPM"></a>  

***
<br><br>[$topPeerCategoryChannels](/API_docs/constructors/topPeerCategoryChannels.html) = \[\];<a name="topPeerCategoryChannels"></a>  

***
<br><br>[$topPeerCategoryCorrespondents](/API_docs/constructors/topPeerCategoryCorrespondents.html) = \[\];<a name="topPeerCategoryCorrespondents"></a>  

***
<br><br>[$topPeerCategoryForwardChats](/API_docs/constructors/topPeerCategoryForwardChats.html) = \[\];<a name="topPeerCategoryForwardChats"></a>  

***
<br><br>[$topPeerCategoryForwardUsers](/API_docs/constructors/topPeerCategoryForwardUsers.html) = \[\];<a name="topPeerCategoryForwardUsers"></a>  

***
<br><br>[$topPeerCategoryGroups](/API_docs/constructors/topPeerCategoryGroups.html) = \[\];<a name="topPeerCategoryGroups"></a>  

***
<br><br>[$topPeerCategoryPeers](/API_docs/constructors/topPeerCategoryPeers.html) = \['category' => [TopPeerCategory](/API_docs/types/TopPeerCategory.html), 'count' => [int](/API_docs/types/int.html), 'peers' => \[[TopPeer](/API_docs/types/TopPeer.html)\], \];<a name="topPeerCategoryPeers"></a>  

***
<br><br>[$topPeerCategoryPhoneCalls](/API_docs/constructors/topPeerCategoryPhoneCalls.html) = \[\];<a name="topPeerCategoryPhoneCalls"></a>  

***
<br><br>[$true](/API_docs/constructors/true.html) = \[\];<a name="true"></a>  

***
<br><br>[$updateAttachMenuBots](/API_docs/constructors/updateAttachMenuBots.html) = \[\];<a name="updateAttachMenuBots"></a>  

***
<br><br>[$updateBotCallbackQuery](/API_docs/constructors/updateBotCallbackQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'msg_id' => [int](/API_docs/types/int.html), 'chat_instance' => [long](/API_docs/types/long.html), 'data' => [bytes](/API_docs/types/bytes.html), 'game_short_name' => [string](/API_docs/types/string.html), \];<a name="updateBotCallbackQuery"></a>  

***
<br><br>[$updateBotChatInviteRequester](/API_docs/constructors/updateBotChatInviteRequester.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'date' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), 'about' => [string](/API_docs/types/string.html), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'qts' => [int](/API_docs/types/int.html), \];<a name="updateBotChatInviteRequester"></a>  

***
<br><br>[$updateBotCommands](/API_docs/constructors/updateBotCommands.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'bot_id' => [long](/API_docs/types/long.html), 'commands' => \[[BotCommand](/API_docs/types/BotCommand.html)\], \];<a name="updateBotCommands"></a>  

***
<br><br>[$updateBotInlineQuery](/API_docs/constructors/updateBotInlineQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'query' => [string](/API_docs/types/string.html), 'geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'peer_type' => [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html), 'offset' => [string](/API_docs/types/string.html), \];<a name="updateBotInlineQuery"></a>  

***
<br><br>[$updateBotInlineSend](/API_docs/constructors/updateBotInlineSend.html) = \['user_id' => [long](/API_docs/types/long.html), 'query' => [string](/API_docs/types/string.html), 'geo' => [GeoPoint](/API_docs/types/GeoPoint.html), 'id' => [string](/API_docs/types/string.html), 'msg_id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), \];<a name="updateBotInlineSend"></a>  

***
<br><br>[$updateBotMenuButton](/API_docs/constructors/updateBotMenuButton.html) = \['bot_id' => [long](/API_docs/types/long.html), 'button' => [BotMenuButton](/API_docs/types/BotMenuButton.html), \];<a name="updateBotMenuButton"></a>  

***
<br><br>[$updateBotPrecheckoutQuery](/API_docs/constructors/updateBotPrecheckoutQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'payload' => [bytes](/API_docs/types/bytes.html), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), 'shipping_option_id' => [string](/API_docs/types/string.html), 'currency' => [string](/API_docs/types/string.html), 'total_amount' => [long](/API_docs/types/long.html), \];<a name="updateBotPrecheckoutQuery"></a>  

***
<br><br>[$updateBotShippingQuery](/API_docs/constructors/updateBotShippingQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'payload' => [bytes](/API_docs/types/bytes.html), 'shipping_address' => [PostAddress](/API_docs/types/PostAddress.html), \];<a name="updateBotShippingQuery"></a>  

***
<br><br>[$updateBotStopped](/API_docs/constructors/updateBotStopped.html) = \['user_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'stopped' => [Bool](/API_docs/types/Bool.html), 'qts' => [int](/API_docs/types/int.html), \];<a name="updateBotStopped"></a>  

***
<br><br>[$updateBotWebhookJSON](/API_docs/constructors/updateBotWebhookJSON.html) = \['data' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="updateBotWebhookJSON"></a>  

***
<br><br>[$updateBotWebhookJSONQuery](/API_docs/constructors/updateBotWebhookJSONQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'data' => [DataJSON](/API_docs/types/DataJSON.html), 'timeout' => [int](/API_docs/types/int.html), \];<a name="updateBotWebhookJSONQuery"></a>  

***
<br><br>[$updateChannel](/API_docs/constructors/updateChannel.html) = \['channel_id' => [long](/API_docs/types/long.html), \];<a name="updateChannel"></a>  

***
<br><br>[$updateChannelAvailableMessages](/API_docs/constructors/updateChannelAvailableMessages.html) = \['channel_id' => [long](/API_docs/types/long.html), 'available_min_id' => [int](/API_docs/types/int.html), \];<a name="updateChannelAvailableMessages"></a>  

***
<br><br>[$updateChannelMessageForwards](/API_docs/constructors/updateChannelMessageForwards.html) = \['channel_id' => [long](/API_docs/types/long.html), 'id' => [int](/API_docs/types/int.html), 'forwards' => [int](/API_docs/types/int.html), \];<a name="updateChannelMessageForwards"></a>  

***
<br><br>[$updateChannelMessageViews](/API_docs/constructors/updateChannelMessageViews.html) = \['channel_id' => [long](/API_docs/types/long.html), 'id' => [int](/API_docs/types/int.html), 'views' => [int](/API_docs/types/int.html), \];<a name="updateChannelMessageViews"></a>  

***
<br><br>[$updateChannelParticipant](/API_docs/constructors/updateChannelParticipant.html) = \['channel_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'actor_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.html), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'qts' => [int](/API_docs/types/int.html), \];<a name="updateChannelParticipant"></a>  

***
<br><br>[$updateChannelReadMessagesContents](/API_docs/constructors/updateChannelReadMessagesContents.html) = \['channel_id' => [long](/API_docs/types/long.html), 'messages' => \[[int](/API_docs/types/int.html)\], \];<a name="updateChannelReadMessagesContents"></a>  

***
<br><br>[$updateChannelTooLong](/API_docs/constructors/updateChannelTooLong.html) = \['channel_id' => [long](/API_docs/types/long.html), 'pts' => [int](/API_docs/types/int.html), \];<a name="updateChannelTooLong"></a>  

***
<br><br>[$updateChannelUserTyping](/API_docs/constructors/updateChannelUserTyping.html) = \['channel_id' => [long](/API_docs/types/long.html), 'top_msg_id' => [int](/API_docs/types/int.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.html), \];<a name="updateChannelUserTyping"></a>  

***
<br><br>[$updateChannelWebPage](/API_docs/constructors/updateChannelWebPage.html) = \['channel_id' => [long](/API_docs/types/long.html), 'webpage' => [WebPage](/API_docs/types/WebPage.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateChannelWebPage"></a>  

***
<br><br>[$updateChat](/API_docs/constructors/updateChat.html) = \['chat_id' => [long](/API_docs/types/long.html), \];<a name="updateChat"></a>  

***
<br><br>[$updateChatDefaultBannedRights](/API_docs/constructors/updateChatDefaultBannedRights.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.html), 'version' => [int](/API_docs/types/int.html), \];<a name="updateChatDefaultBannedRights"></a>  

***
<br><br>[$updateChatParticipant](/API_docs/constructors/updateChatParticipant.html) = \['chat_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'actor_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'prev_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.html), 'new_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.html), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html), 'qts' => [int](/API_docs/types/int.html), \];<a name="updateChatParticipant"></a>  

***
<br><br>[$updateChatParticipantAdd](/API_docs/constructors/updateChatParticipantAdd.html) = \['chat_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'inviter_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'version' => [int](/API_docs/types/int.html), \];<a name="updateChatParticipantAdd"></a>  

***
<br><br>[$updateChatParticipantAdmin](/API_docs/constructors/updateChatParticipantAdmin.html) = \['chat_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'is_admin' => [Bool](/API_docs/types/Bool.html), 'version' => [int](/API_docs/types/int.html), \];<a name="updateChatParticipantAdmin"></a>  

***
<br><br>[$updateChatParticipantDelete](/API_docs/constructors/updateChatParticipantDelete.html) = \['chat_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'version' => [int](/API_docs/types/int.html), \];<a name="updateChatParticipantDelete"></a>  

***
<br><br>[$updateChatParticipants](/API_docs/constructors/updateChatParticipants.html) = \['participants' => [ChatParticipants](/API_docs/types/ChatParticipants.html), \];<a name="updateChatParticipants"></a>  

***
<br><br>[$updateChatUserTyping](/API_docs/constructors/updateChatUserTyping.html) = \['chat_id' => [long](/API_docs/types/long.html), 'from_id' => [Peer](/API_docs/types/Peer.html), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.html), \];<a name="updateChatUserTyping"></a>  

***
<br><br>[$updateConfig](/API_docs/constructors/updateConfig.html) = \[\];<a name="updateConfig"></a>  

***
<br><br>[$updateContactsReset](/API_docs/constructors/updateContactsReset.html) = \[\];<a name="updateContactsReset"></a>  

***
<br><br>[$updateDcOptions](/API_docs/constructors/updateDcOptions.html) = \['dc_options' => \[[DcOption](/API_docs/types/DcOption.html)\], \];<a name="updateDcOptions"></a>  

***
<br><br>[$updateDeleteChannelMessages](/API_docs/constructors/updateDeleteChannelMessages.html) = \['channel_id' => [long](/API_docs/types/long.html), 'messages' => \[[int](/API_docs/types/int.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateDeleteChannelMessages"></a>  

***
<br><br>[$updateDeleteMessages](/API_docs/constructors/updateDeleteMessages.html) = \['messages' => \[[int](/API_docs/types/int.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateDeleteMessages"></a>  

***
<br><br>[$updateDeleteScheduledMessages](/API_docs/constructors/updateDeleteScheduledMessages.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'messages' => \[[int](/API_docs/types/int.html)\], \];<a name="updateDeleteScheduledMessages"></a>  

***
<br><br>[$updateDialogFilter](/API_docs/constructors/updateDialogFilter.html) = \['id' => [int](/API_docs/types/int.html), 'filter' => [DialogFilter](/API_docs/types/DialogFilter.html), \];<a name="updateDialogFilter"></a>  

***
<br><br>[$updateDialogFilterOrder](/API_docs/constructors/updateDialogFilterOrder.html) = \['order' => \[[int](/API_docs/types/int.html)\], \];<a name="updateDialogFilterOrder"></a>  

***
<br><br>[$updateDialogFilters](/API_docs/constructors/updateDialogFilters.html) = \[\];<a name="updateDialogFilters"></a>  

***
<br><br>[$updateDialogPinned](/API_docs/constructors/updateDialogPinned.html) = \['pinned' => [Bool](/API_docs/types/Bool.html), 'folder_id' => [int](/API_docs/types/int.html), 'peer' => [DialogPeer](/API_docs/types/DialogPeer.html), \];<a name="updateDialogPinned"></a>  

***
<br><br>[$updateDialogUnreadMark](/API_docs/constructors/updateDialogUnreadMark.html) = \['unread' => [Bool](/API_docs/types/Bool.html), 'peer' => [DialogPeer](/API_docs/types/DialogPeer.html), \];<a name="updateDialogUnreadMark"></a>  

***
<br><br>[$updateDraftMessage](/API_docs/constructors/updateDraftMessage.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'draft' => [DraftMessage](/API_docs/types/DraftMessage.html), \];<a name="updateDraftMessage"></a>  

***
<br><br>[$updateEditChannelMessage](/API_docs/constructors/updateEditChannelMessage.html) = \['message' => [Message](/API_docs/types/Message.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateEditChannelMessage"></a>  

***
<br><br>[$updateEditMessage](/API_docs/constructors/updateEditMessage.html) = \['message' => [Message](/API_docs/types/Message.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateEditMessage"></a>  

***
<br><br>[$updateEncryptedChatTyping](/API_docs/constructors/updateEncryptedChatTyping.html) = \['chat_id' => [int](/API_docs/types/int.html), \];<a name="updateEncryptedChatTyping"></a>  

***
<br><br>[$updateEncryptedMessagesRead](/API_docs/constructors/updateEncryptedMessagesRead.html) = \['chat_id' => [int](/API_docs/types/int.html), 'max_date' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), \];<a name="updateEncryptedMessagesRead"></a>  

***
<br><br>[$updateEncryption](/API_docs/constructors/updateEncryption.html) = \['chat' => [EncryptedChat](/API_docs/types/EncryptedChat.html), 'date' => [int](/API_docs/types/int.html), \];<a name="updateEncryption"></a>  

***
<br><br>[$updateFavedStickers](/API_docs/constructors/updateFavedStickers.html) = \[\];<a name="updateFavedStickers"></a>  

***
<br><br>[$updateFolderPeers](/API_docs/constructors/updateFolderPeers.html) = \['folder_peers' => \[[FolderPeer](/API_docs/types/FolderPeer.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateFolderPeers"></a>  

***
<br><br>[$updateGeoLiveViewed](/API_docs/constructors/updateGeoLiveViewed.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'msg_id' => [int](/API_docs/types/int.html), \];<a name="updateGeoLiveViewed"></a>  

***
<br><br>[$updateGroupCall](/API_docs/constructors/updateGroupCall.html) = \['chat_id' => [long](/API_docs/types/long.html), 'call' => [GroupCall](/API_docs/types/GroupCall.html), \];<a name="updateGroupCall"></a>  

***
<br><br>[$updateGroupCallConnection](/API_docs/constructors/updateGroupCallConnection.html) = \['presentation' => [Bool](/API_docs/types/Bool.html), 'params' => [DataJSON](/API_docs/types/DataJSON.html), \];<a name="updateGroupCallConnection"></a>  

***
<br><br>[$updateGroupCallParticipants](/API_docs/constructors/updateGroupCallParticipants.html) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.html), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html)\], 'version' => [int](/API_docs/types/int.html), \];<a name="updateGroupCallParticipants"></a>  

***
<br><br>[$updateInlineBotCallbackQuery](/API_docs/constructors/updateInlineBotCallbackQuery.html) = \['query_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'msg_id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), 'chat_instance' => [long](/API_docs/types/long.html), 'data' => [bytes](/API_docs/types/bytes.html), 'game_short_name' => [string](/API_docs/types/string.html), \];<a name="updateInlineBotCallbackQuery"></a>  

***
<br><br>[$updateLangPack](/API_docs/constructors/updateLangPack.html) = \['difference' => [LangPackDifference](/API_docs/types/LangPackDifference.html), \];<a name="updateLangPack"></a>  

***
<br><br>[$updateLangPackTooLong](/API_docs/constructors/updateLangPackTooLong.html) = \['lang_code' => [string](/API_docs/types/string.html), \];<a name="updateLangPackTooLong"></a>  

***
<br><br>[$updateLoginToken](/API_docs/constructors/updateLoginToken.html) = \[\];<a name="updateLoginToken"></a>  

***
<br><br>[$updateMessageID](/API_docs/constructors/updateMessageID.html) = \['id' => [int](/API_docs/types/int.html), \];<a name="updateMessageID"></a>  

***
<br><br>[$updateMessagePoll](/API_docs/constructors/updateMessagePoll.html) = \['poll_id' => [long](/API_docs/types/long.html), 'poll' => [Poll](/API_docs/types/Poll.html), 'results' => [PollResults](/API_docs/types/PollResults.html), \];<a name="updateMessagePoll"></a>  

***
<br><br>[$updateMessagePollVote](/API_docs/constructors/updateMessagePollVote.html) = \['poll_id' => [long](/API_docs/types/long.html), 'user_id' => [long](/API_docs/types/long.html), 'options' => \[[bytes](/API_docs/types/bytes.html)\], 'qts' => [int](/API_docs/types/int.html), \];<a name="updateMessagePollVote"></a>  

***
<br><br>[$updateMessageReactions](/API_docs/constructors/updateMessageReactions.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'msg_id' => [int](/API_docs/types/int.html), 'reactions' => [MessageReactions](/API_docs/types/MessageReactions.html), \];<a name="updateMessageReactions"></a>  

***
<br><br>[$updateNewChannelMessage](/API_docs/constructors/updateNewChannelMessage.html) = \['message' => [Message](/API_docs/types/Message.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateNewChannelMessage"></a>  

***
<br><br>[$updateNewEncryptedMessage](/API_docs/constructors/updateNewEncryptedMessage.html) = \['message' => [EncryptedMessage](/API_docs/types/EncryptedMessage.html), 'qts' => [int](/API_docs/types/int.html), \];<a name="updateNewEncryptedMessage"></a>  

***
<br><br>[$updateNewMessage](/API_docs/constructors/updateNewMessage.html) = \['message' => [Message](/API_docs/types/Message.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateNewMessage"></a>  

***
<br><br>[$updateNewScheduledMessage](/API_docs/constructors/updateNewScheduledMessage.html) = \['message' => [Message](/API_docs/types/Message.html), \];<a name="updateNewScheduledMessage"></a>  

***
<br><br>[$updateNewStickerSet](/API_docs/constructors/updateNewStickerSet.html) = \['stickerset' => [messages.StickerSet](/API_docs/types/messages.StickerSet.html), \];<a name="updateNewStickerSet"></a>  

***
<br><br>[$updateNotifySettings](/API_docs/constructors/updateNotifySettings.html) = \['peer' => [NotifyPeer](/API_docs/types/NotifyPeer.html), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html), \];<a name="updateNotifySettings"></a>  

***
<br><br>[$updatePeerBlocked](/API_docs/constructors/updatePeerBlocked.html) = \['peer_id' => [Peer](/API_docs/types/Peer.html), 'blocked' => [Bool](/API_docs/types/Bool.html), \];<a name="updatePeerBlocked"></a>  

***
<br><br>[$updatePeerHistoryTTL](/API_docs/constructors/updatePeerHistoryTTL.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="updatePeerHistoryTTL"></a>  

***
<br><br>[$updatePeerLocated](/API_docs/constructors/updatePeerLocated.html) = \['peers' => \[[PeerLocated](/API_docs/types/PeerLocated.html)\], \];<a name="updatePeerLocated"></a>  

***
<br><br>[$updatePeerSettings](/API_docs/constructors/updatePeerSettings.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'settings' => [PeerSettings](/API_docs/types/PeerSettings.html), \];<a name="updatePeerSettings"></a>  

***
<br><br>[$updatePendingJoinRequests](/API_docs/constructors/updatePendingJoinRequests.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'requests_pending' => [int](/API_docs/types/int.html), 'recent_requesters' => \[[long](/API_docs/types/long.html)\], \];<a name="updatePendingJoinRequests"></a>  

***
<br><br>[$updatePhoneCall](/API_docs/constructors/updatePhoneCall.html) = \['phone_call' => [PhoneCall](/API_docs/types/PhoneCall.html), \];<a name="updatePhoneCall"></a>  

***
<br><br>[$updatePhoneCallSignalingData](/API_docs/constructors/updatePhoneCallSignalingData.html) = \['phone_call_id' => [long](/API_docs/types/long.html), 'data' => [bytes](/API_docs/types/bytes.html), \];<a name="updatePhoneCallSignalingData"></a>  

***
<br><br>[$updatePinnedChannelMessages](/API_docs/constructors/updatePinnedChannelMessages.html) = \['pinned' => [Bool](/API_docs/types/Bool.html), 'channel_id' => [long](/API_docs/types/long.html), 'messages' => \[[int](/API_docs/types/int.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updatePinnedChannelMessages"></a>  

***
<br><br>[$updatePinnedDialogs](/API_docs/constructors/updatePinnedDialogs.html) = \['folder_id' => [int](/API_docs/types/int.html), 'order' => \[[DialogPeer](/API_docs/types/DialogPeer.html)\], \];<a name="updatePinnedDialogs"></a>  

***
<br><br>[$updatePinnedMessages](/API_docs/constructors/updatePinnedMessages.html) = \['pinned' => [Bool](/API_docs/types/Bool.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'messages' => \[[int](/API_docs/types/int.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updatePinnedMessages"></a>  

***
<br><br>[$updatePrivacy](/API_docs/constructors/updatePrivacy.html) = \['key' => [PrivacyKey](/API_docs/types/PrivacyKey.html), 'rules' => \[[PrivacyRule](/API_docs/types/PrivacyRule.html)\], \];<a name="updatePrivacy"></a>  

***
<br><br>[$updatePtsChanged](/API_docs/constructors/updatePtsChanged.html) = \[\];<a name="updatePtsChanged"></a>  

***
<br><br>[$updateReadChannelDiscussionInbox](/API_docs/constructors/updateReadChannelDiscussionInbox.html) = \['channel_id' => [long](/API_docs/types/long.html), 'top_msg_id' => [int](/API_docs/types/int.html), 'read_max_id' => [int](/API_docs/types/int.html), 'broadcast_id' => [long](/API_docs/types/long.html), 'broadcast_post' => [int](/API_docs/types/int.html), \];<a name="updateReadChannelDiscussionInbox"></a>  

***
<br><br>[$updateReadChannelDiscussionOutbox](/API_docs/constructors/updateReadChannelDiscussionOutbox.html) = \['channel_id' => [long](/API_docs/types/long.html), 'top_msg_id' => [int](/API_docs/types/int.html), 'read_max_id' => [int](/API_docs/types/int.html), \];<a name="updateReadChannelDiscussionOutbox"></a>  

***
<br><br>[$updateReadChannelInbox](/API_docs/constructors/updateReadChannelInbox.html) = \['folder_id' => [int](/API_docs/types/int.html), 'channel_id' => [long](/API_docs/types/long.html), 'max_id' => [int](/API_docs/types/int.html), 'still_unread_count' => [int](/API_docs/types/int.html), 'pts' => [int](/API_docs/types/int.html), \];<a name="updateReadChannelInbox"></a>  

***
<br><br>[$updateReadChannelOutbox](/API_docs/constructors/updateReadChannelOutbox.html) = \['channel_id' => [long](/API_docs/types/long.html), 'max_id' => [int](/API_docs/types/int.html), \];<a name="updateReadChannelOutbox"></a>  

***
<br><br>[$updateReadFeaturedStickers](/API_docs/constructors/updateReadFeaturedStickers.html) = \[\];<a name="updateReadFeaturedStickers"></a>  

***
<br><br>[$updateReadHistoryInbox](/API_docs/constructors/updateReadHistoryInbox.html) = \['folder_id' => [int](/API_docs/types/int.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'max_id' => [int](/API_docs/types/int.html), 'still_unread_count' => [int](/API_docs/types/int.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateReadHistoryInbox"></a>  

***
<br><br>[$updateReadHistoryOutbox](/API_docs/constructors/updateReadHistoryOutbox.html) = \['peer' => [Peer](/API_docs/types/Peer.html), 'max_id' => [int](/API_docs/types/int.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateReadHistoryOutbox"></a>  

***
<br><br>[$updateReadMessagesContents](/API_docs/constructors/updateReadMessagesContents.html) = \['messages' => \[[int](/API_docs/types/int.html)\], 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateReadMessagesContents"></a>  

***
<br><br>[$updateRecentStickers](/API_docs/constructors/updateRecentStickers.html) = \[\];<a name="updateRecentStickers"></a>  

***
<br><br>[$updateSavedGifs](/API_docs/constructors/updateSavedGifs.html) = \[\];<a name="updateSavedGifs"></a>  

***
<br><br>[$updateSavedRingtones](/API_docs/constructors/updateSavedRingtones.html) = \[\];<a name="updateSavedRingtones"></a>  

***
<br><br>[$updateServiceNotification](/API_docs/constructors/updateServiceNotification.html) = \['popup' => [Bool](/API_docs/types/Bool.html), 'inbox_date' => [int](/API_docs/types/int.html), 'type' => [string](/API_docs/types/string.html), 'message' => [string](/API_docs/types/string.html), 'media' => [MessageMedia](/API_docs/types/MessageMedia.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \];<a name="updateServiceNotification"></a>  

***
<br><br>[$updateShort](/API_docs/constructors/updateShort.html) = \['update' => [Update](/API_docs/types/Update.html), 'date' => [int](/API_docs/types/int.html), \];<a name="updateShort"></a>  

***
<br><br>[$updateShortChatMessage](/API_docs/constructors/updateShortChatMessage.html) = \['out' => [Bool](/API_docs/types/Bool.html), 'mentioned' => [Bool](/API_docs/types/Bool.html), 'media_unread' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'from_id' => [long](/API_docs/types/long.html), 'chat_id' => [long](/API_docs/types/long.html), 'message' => [string](/API_docs/types/string.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.html), 'via_bot_id' => [long](/API_docs/types/long.html), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="updateShortChatMessage"></a>  

***
<br><br>[$updateShortMessage](/API_docs/constructors/updateShortMessage.html) = \['out' => [Bool](/API_docs/types/Bool.html), 'mentioned' => [Bool](/API_docs/types/Bool.html), 'media_unread' => [Bool](/API_docs/types/Bool.html), 'silent' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'user_id' => [long](/API_docs/types/long.html), 'message' => [string](/API_docs/types/string.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.html), 'via_bot_id' => [long](/API_docs/types/long.html), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="updateShortMessage"></a>  

***
<br><br>[$updateShortSentMessage](/API_docs/constructors/updateShortSentMessage.html) = \['out' => [Bool](/API_docs/types/Bool.html), 'id' => [int](/API_docs/types/int.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'media' => [MessageMedia](/API_docs/types/MessageMedia.html), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.html)\], 'ttl_period' => [int](/API_docs/types/int.html), \];<a name="updateShortSentMessage"></a>  

***
<br><br>[$updateStickerSets](/API_docs/constructors/updateStickerSets.html) = \[\];<a name="updateStickerSets"></a>  

***
<br><br>[$updateStickerSetsOrder](/API_docs/constructors/updateStickerSetsOrder.html) = \['masks' => [Bool](/API_docs/types/Bool.html), 'order' => \[[long](/API_docs/types/long.html)\], \];<a name="updateStickerSetsOrder"></a>  

***
<br><br>[$updateTheme](/API_docs/constructors/updateTheme.html) = \['theme' => [Theme](/API_docs/types/Theme.html), \];<a name="updateTheme"></a>  

***
<br><br>[$updateTranscribedAudio](/API_docs/constructors/updateTranscribedAudio.html) = \['pending' => [Bool](/API_docs/types/Bool.html), 'peer' => [Peer](/API_docs/types/Peer.html), 'msg_id' => [int](/API_docs/types/int.html), 'transcription_id' => [long](/API_docs/types/long.html), 'text' => [string](/API_docs/types/string.html), \];<a name="updateTranscribedAudio"></a>  

***
<br><br>[$updateUserName](/API_docs/constructors/updateUserName.html) = \['user_id' => [long](/API_docs/types/long.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'username' => [string](/API_docs/types/string.html), \];<a name="updateUserName"></a>  

***
<br><br>[$updateUserPhone](/API_docs/constructors/updateUserPhone.html) = \['user_id' => [long](/API_docs/types/long.html), 'phone' => [string](/API_docs/types/string.html), \];<a name="updateUserPhone"></a>  

***
<br><br>[$updateUserPhoto](/API_docs/constructors/updateUserPhoto.html) = \['user_id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), 'photo' => [UserProfilePhoto](/API_docs/types/UserProfilePhoto.html), 'previous' => [Bool](/API_docs/types/Bool.html), \];<a name="updateUserPhoto"></a>  

***
<br><br>[$updateUserStatus](/API_docs/constructors/updateUserStatus.html) = \['user_id' => [long](/API_docs/types/long.html), 'status' => [UserStatus](/API_docs/types/UserStatus.html), \];<a name="updateUserStatus"></a>  

***
<br><br>[$updateUserTyping](/API_docs/constructors/updateUserTyping.html) = \['user_id' => [long](/API_docs/types/long.html), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.html), \];<a name="updateUserTyping"></a>  

***
<br><br>[$updateWebPage](/API_docs/constructors/updateWebPage.html) = \['webpage' => [WebPage](/API_docs/types/WebPage.html), 'pts' => [int](/API_docs/types/int.html), 'pts_count' => [int](/API_docs/types/int.html), \];<a name="updateWebPage"></a>  

***
<br><br>[$updateWebViewResultSent](/API_docs/constructors/updateWebViewResultSent.html) = \['query_id' => [long](/API_docs/types/long.html), \];<a name="updateWebViewResultSent"></a>  

***
<br><br>[$updates](/API_docs/constructors/updates.html) = \['updates' => \[[Update](/API_docs/types/Update.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'date' => [int](/API_docs/types/int.html), 'seq' => [int](/API_docs/types/int.html), \];<a name="updates"></a>  

***
<br><br>[$updates.channelDifference](/API_docs/constructors/updates.channelDifference.html) = \['final' => [Bool](/API_docs/types/Bool.html), 'pts' => [int](/API_docs/types/int.html), 'timeout' => [int](/API_docs/types/int.html), 'new_messages' => \[[Message](/API_docs/types/Message.html)\], 'other_updates' => \[[Update](/API_docs/types/Update.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="updates.channelDifference"></a>  

***
<br><br>[$updates.channelDifferenceEmpty](/API_docs/constructors/updates.channelDifferenceEmpty.html) = \['final' => [Bool](/API_docs/types/Bool.html), 'pts' => [int](/API_docs/types/int.html), 'timeout' => [int](/API_docs/types/int.html), \];<a name="updates.channelDifferenceEmpty"></a>  

***
<br><br>[$updates.channelDifferenceTooLong](/API_docs/constructors/updates.channelDifferenceTooLong.html) = \['final' => [Bool](/API_docs/types/Bool.html), 'timeout' => [int](/API_docs/types/int.html), 'dialog' => [Dialog](/API_docs/types/Dialog.html), 'messages' => \[[Message](/API_docs/types/Message.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="updates.channelDifferenceTooLong"></a>  

***
<br><br>[$updates.difference](/API_docs/constructors/updates.difference.html) = \['new_messages' => \[[Message](/API_docs/types/Message.html)\], 'new_encrypted_messages' => \[[EncryptedMessage](/API_docs/types/EncryptedMessage.html)\], 'other_updates' => \[[Update](/API_docs/types/Update.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'state' => [updates.State](/API_docs/types/updates.State.html), \];<a name="updates.difference"></a>  

***
<br><br>[$updates.differenceEmpty](/API_docs/constructors/updates.differenceEmpty.html) = \['date' => [int](/API_docs/types/int.html), 'seq' => [int](/API_docs/types/int.html), \];<a name="updates.differenceEmpty"></a>  

***
<br><br>[$updates.differenceSlice](/API_docs/constructors/updates.differenceSlice.html) = \['new_messages' => \[[Message](/API_docs/types/Message.html)\], 'new_encrypted_messages' => \[[EncryptedMessage](/API_docs/types/EncryptedMessage.html)\], 'other_updates' => \[[Update](/API_docs/types/Update.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'intermediate_state' => [updates.State](/API_docs/types/updates.State.html), \];<a name="updates.differenceSlice"></a>  

***
<br><br>[$updates.differenceTooLong](/API_docs/constructors/updates.differenceTooLong.html) = \['pts' => [int](/API_docs/types/int.html), \];<a name="updates.differenceTooLong"></a>  

***
<br><br>[$updates.state](/API_docs/constructors/updates.state.html) = \['pts' => [int](/API_docs/types/int.html), 'qts' => [int](/API_docs/types/int.html), 'date' => [int](/API_docs/types/int.html), 'seq' => [int](/API_docs/types/int.html), 'unread_count' => [int](/API_docs/types/int.html), \];<a name="updates.state"></a>  

***
<br><br>[$updatesCombined](/API_docs/constructors/updatesCombined.html) = \['updates' => \[[Update](/API_docs/types/Update.html)\], 'users' => \[[User](/API_docs/types/User.html)\], 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'date' => [int](/API_docs/types/int.html), 'seq_start' => [int](/API_docs/types/int.html), 'seq' => [int](/API_docs/types/int.html), \];<a name="updatesCombined"></a>  

***
<br><br>[$updatesTooLong](/API_docs/constructors/updatesTooLong.html) = \[\];<a name="updatesTooLong"></a>  

***
<br><br>[$upload.cdnFile](/API_docs/constructors/upload.cdnFile.html) = \['bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="upload.cdnFile"></a>  

***
<br><br>[$upload.cdnFileReuploadNeeded](/API_docs/constructors/upload.cdnFileReuploadNeeded.html) = \['request_token' => [bytes](/API_docs/types/bytes.html), \];<a name="upload.cdnFileReuploadNeeded"></a>  

***
<br><br>[$upload.file](/API_docs/constructors/upload.file.html) = \['type' => [storage.FileType](/API_docs/types/storage.FileType.html), 'mtime' => [int](/API_docs/types/int.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="upload.file"></a>  

***
<br><br>[$upload.fileCdnRedirect](/API_docs/constructors/upload.fileCdnRedirect.html) = \['dc_id' => [int](/API_docs/types/int.html), 'file_token' => [bytes](/API_docs/types/bytes.html), 'encryption_key' => [bytes](/API_docs/types/bytes.html), 'encryption_iv' => [bytes](/API_docs/types/bytes.html), 'file_hashes' => \[[FileHash](/API_docs/types/FileHash.html)\], \];<a name="upload.fileCdnRedirect"></a>  

***
<br><br>[$upload.webFile](/API_docs/constructors/upload.webFile.html) = \['size' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'file_type' => [storage.FileType](/API_docs/types/storage.FileType.html), 'mtime' => [int](/API_docs/types/int.html), 'bytes' => [bytes](/API_docs/types/bytes.html), \];<a name="upload.webFile"></a>  

***
<br><br>[$urlAuthResultAccepted](/API_docs/constructors/urlAuthResultAccepted.html) = \['url' => [string](/API_docs/types/string.html), \];<a name="urlAuthResultAccepted"></a>  

***
<br><br>[$urlAuthResultDefault](/API_docs/constructors/urlAuthResultDefault.html) = \[\];<a name="urlAuthResultDefault"></a>  

***
<br><br>[$urlAuthResultRequest](/API_docs/constructors/urlAuthResultRequest.html) = \['request_write_access' => [Bool](/API_docs/types/Bool.html), 'bot' => [User](/API_docs/types/User.html), 'domain' => [string](/API_docs/types/string.html), \];<a name="urlAuthResultRequest"></a>  

***
<br><br>[$user](/API_docs/constructors/user.html) = \['self' => [Bool](/API_docs/types/Bool.html), 'contact' => [Bool](/API_docs/types/Bool.html), 'mutual_contact' => [Bool](/API_docs/types/Bool.html), 'deleted' => [Bool](/API_docs/types/Bool.html), 'bot' => [Bool](/API_docs/types/Bool.html), 'bot_chat_history' => [Bool](/API_docs/types/Bool.html), 'bot_nochats' => [Bool](/API_docs/types/Bool.html), 'verified' => [Bool](/API_docs/types/Bool.html), 'restricted' => [Bool](/API_docs/types/Bool.html), 'min' => [Bool](/API_docs/types/Bool.html), 'bot_inline_geo' => [Bool](/API_docs/types/Bool.html), 'support' => [Bool](/API_docs/types/Bool.html), 'scam' => [Bool](/API_docs/types/Bool.html), 'apply_min_photo' => [Bool](/API_docs/types/Bool.html), 'fake' => [Bool](/API_docs/types/Bool.html), 'bot_attach_menu' => [Bool](/API_docs/types/Bool.html), 'premium' => [Bool](/API_docs/types/Bool.html), 'attach_menu_enabled' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'access_hash' => [long](/API_docs/types/long.html), 'first_name' => [string](/API_docs/types/string.html), 'last_name' => [string](/API_docs/types/string.html), 'username' => [string](/API_docs/types/string.html), 'phone' => [string](/API_docs/types/string.html), 'photo' => [UserProfilePhoto](/API_docs/types/UserProfilePhoto.html), 'status' => [UserStatus](/API_docs/types/UserStatus.html), 'bot_info_version' => [int](/API_docs/types/int.html), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.html)\], 'bot_inline_placeholder' => [string](/API_docs/types/string.html), 'lang_code' => [string](/API_docs/types/string.html), \];<a name="user"></a>  

***
<br><br>[$userEmpty](/API_docs/constructors/userEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="userEmpty"></a>  

***
<br><br>[$userFull](/API_docs/constructors/userFull.html) = \['blocked' => [Bool](/API_docs/types/Bool.html), 'phone_calls_available' => [Bool](/API_docs/types/Bool.html), 'phone_calls_private' => [Bool](/API_docs/types/Bool.html), 'can_pin_message' => [Bool](/API_docs/types/Bool.html), 'has_scheduled' => [Bool](/API_docs/types/Bool.html), 'video_calls_available' => [Bool](/API_docs/types/Bool.html), 'id' => [long](/API_docs/types/long.html), 'about' => [string](/API_docs/types/string.html), 'settings' => [PeerSettings](/API_docs/types/PeerSettings.html), 'profile_photo' => [Photo](/API_docs/types/Photo.html), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html), 'bot_info' => [BotInfo](/API_docs/types/BotInfo.html), 'pinned_msg_id' => [int](/API_docs/types/int.html), 'common_chats_count' => [int](/API_docs/types/int.html), 'folder_id' => [int](/API_docs/types/int.html), 'ttl_period' => [int](/API_docs/types/int.html), 'theme_emoticon' => [string](/API_docs/types/string.html), 'private_forward_name' => [string](/API_docs/types/string.html), 'bot_group_admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), 'bot_broadcast_admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.html), \];<a name="userFull"></a>  

***
<br><br>[$userProfilePhoto](/API_docs/constructors/userProfilePhoto.html) = \['has_video' => [Bool](/API_docs/types/Bool.html), 'photo_id' => [long](/API_docs/types/long.html), 'stripped_thumb' => [bytes](/API_docs/types/bytes.html), 'dc_id' => [int](/API_docs/types/int.html), \];<a name="userProfilePhoto"></a>  

***
<br><br>[$userProfilePhotoEmpty](/API_docs/constructors/userProfilePhotoEmpty.html) = \[\];<a name="userProfilePhotoEmpty"></a>  

***
<br><br>[$userStatusEmpty](/API_docs/constructors/userStatusEmpty.html) = \[\];<a name="userStatusEmpty"></a>  

***
<br><br>[$userStatusLastMonth](/API_docs/constructors/userStatusLastMonth.html) = \[\];<a name="userStatusLastMonth"></a>  

***
<br><br>[$userStatusLastWeek](/API_docs/constructors/userStatusLastWeek.html) = \[\];<a name="userStatusLastWeek"></a>  

***
<br><br>[$userStatusOffline](/API_docs/constructors/userStatusOffline.html) = \['was_online' => [int](/API_docs/types/int.html), \];<a name="userStatusOffline"></a>  

***
<br><br>[$userStatusOnline](/API_docs/constructors/userStatusOnline.html) = \['expires' => [int](/API_docs/types/int.html), \];<a name="userStatusOnline"></a>  

***
<br><br>[$userStatusRecently](/API_docs/constructors/userStatusRecently.html) = \[\];<a name="userStatusRecently"></a>  

***
<br><br>[$users.userFull](/API_docs/constructors/users.userFull.html) = \['full_user' => [UserFull](/API_docs/types/UserFull.html), 'chats' => \[[Chat](/API_docs/types/Chat.html)\], 'users' => \[[User](/API_docs/types/User.html)\], \];<a name="users.userFull"></a>  

***
<br><br>[$videoSize](/API_docs/constructors/videoSize.html) = \['type' => [string](/API_docs/types/string.html), 'w' => [int](/API_docs/types/int.html), 'h' => [int](/API_docs/types/int.html), 'size' => [int](/API_docs/types/int.html), 'video_start_ts' => [double](/API_docs/types/double.html), \];<a name="videoSize"></a>  

***
<br><br>[$wallPaper](/API_docs/constructors/wallPaper.html) = \['id' => [long](/API_docs/types/long.html), 'creator' => [Bool](/API_docs/types/Bool.html), 'default' => [Bool](/API_docs/types/Bool.html), 'pattern' => [Bool](/API_docs/types/Bool.html), 'dark' => [Bool](/API_docs/types/Bool.html), 'access_hash' => [long](/API_docs/types/long.html), 'slug' => [string](/API_docs/types/string.html), 'document' => [Document](/API_docs/types/Document.html), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \];<a name="wallPaper"></a>  

***
<br><br>[$wallPaperNoFile](/API_docs/constructors/wallPaperNoFile.html) = \['id' => [long](/API_docs/types/long.html), 'default' => [Bool](/API_docs/types/Bool.html), 'dark' => [Bool](/API_docs/types/Bool.html), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \];<a name="wallPaperNoFile"></a>  

***
<br><br>[$wallPaperSettings](/API_docs/constructors/wallPaperSettings.html) = \['blur' => [Bool](/API_docs/types/Bool.html), 'motion' => [Bool](/API_docs/types/Bool.html), 'background_color' => [int](/API_docs/types/int.html), 'second_background_color' => [int](/API_docs/types/int.html), 'third_background_color' => [int](/API_docs/types/int.html), 'fourth_background_color' => [int](/API_docs/types/int.html), 'intensity' => [int](/API_docs/types/int.html), 'rotation' => [int](/API_docs/types/int.html), \];<a name="wallPaperSettings"></a>  

***
<br><br>[$webAuthorization](/API_docs/constructors/webAuthorization.html) = \['hash' => [long](/API_docs/types/long.html), 'bot_id' => [long](/API_docs/types/long.html), 'domain' => [string](/API_docs/types/string.html), 'browser' => [string](/API_docs/types/string.html), 'platform' => [string](/API_docs/types/string.html), 'date_created' => [int](/API_docs/types/int.html), 'date_active' => [int](/API_docs/types/int.html), 'ip' => [string](/API_docs/types/string.html), 'region' => [string](/API_docs/types/string.html), \];<a name="webAuthorization"></a>  

***
<br><br>[$webDocument](/API_docs/constructors/webDocument.html) = \['url' => [string](/API_docs/types/string.html), 'access_hash' => [long](/API_docs/types/long.html), 'size' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], \];<a name="webDocument"></a>  

***
<br><br>[$webDocumentNoProxy](/API_docs/constructors/webDocumentNoProxy.html) = \['url' => [string](/API_docs/types/string.html), 'size' => [int](/API_docs/types/int.html), 'mime_type' => [string](/API_docs/types/string.html), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.html)\], \];<a name="webDocumentNoProxy"></a>  

***
<br><br>[$webPage](/API_docs/constructors/webPage.html) = \['id' => [long](/API_docs/types/long.html), 'url' => [string](/API_docs/types/string.html), 'display_url' => [string](/API_docs/types/string.html), 'hash' => [int](/API_docs/types/int.html), 'type' => [string](/API_docs/types/string.html), 'site_name' => [string](/API_docs/types/string.html), 'title' => [string](/API_docs/types/string.html), 'description' => [string](/API_docs/types/string.html), 'photo' => [Photo](/API_docs/types/Photo.html), 'embed_url' => [string](/API_docs/types/string.html), 'embed_type' => [string](/API_docs/types/string.html), 'embed_width' => [int](/API_docs/types/int.html), 'embed_height' => [int](/API_docs/types/int.html), 'duration' => [int](/API_docs/types/int.html), 'author' => [string](/API_docs/types/string.html), 'document' => [Document](/API_docs/types/Document.html), 'cached_page' => [Page](/API_docs/types/Page.html), 'attributes' => \[[WebPageAttribute](/API_docs/types/WebPageAttribute.html)\], \];<a name="webPage"></a>  

***
<br><br>[$webPageAttributeTheme](/API_docs/constructors/webPageAttributeTheme.html) = \['documents' => \[[Document](/API_docs/types/Document.html)\], 'settings' => [ThemeSettings](/API_docs/types/ThemeSettings.html), \];<a name="webPageAttributeTheme"></a>  

***
<br><br>[$webPageEmpty](/API_docs/constructors/webPageEmpty.html) = \['id' => [long](/API_docs/types/long.html), \];<a name="webPageEmpty"></a>  

***
<br><br>[$webPageNotModified](/API_docs/constructors/webPageNotModified.html) = \['cached_page_views' => [int](/API_docs/types/int.html), \];<a name="webPageNotModified"></a>  

***
<br><br>[$webPagePending](/API_docs/constructors/webPagePending.html) = \['id' => [long](/API_docs/types/long.html), 'date' => [int](/API_docs/types/int.html), \];<a name="webPagePending"></a>  

***
<br><br>[$webViewMessageSent](/API_docs/constructors/webViewMessageSent.html) = \['msg_id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), \];<a name="webViewMessageSent"></a>  

***
<br><br>[$webViewResultUrl](/API_docs/constructors/webViewResultUrl.html) = \['query_id' => [long](/API_docs/types/long.html), 'url' => [string](/API_docs/types/string.html), \];<a name="webViewResultUrl"></a>  



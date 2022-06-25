---
title: Methods (API)
description: List of methods
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Methods  
[Back to API documentation index](..)

[Go to the new description-version method index](index.html)

$MadelineProto->[logout](https://docs.madelineproto.xyz/logout.html)();

$MadelineProto->[phoneLogin](https://docs.madelineproto.xyz/phoneLogin.html)($number);

$MadelineProto->[completePhoneLogin](https://docs.madelineproto.xyz/completePhoneLogin.html)($code);

$MadelineProto->[complete2FALogin](https://docs.madelineproto.xyz/complete2FAlogin.html)($password);

$MadelineProto->[botLogin](https://docs.madelineproto.xyz/botLogin.html)($token);


$MadelineProto->[getDialogs](https://docs.madelineproto.xyz/getDialogs.html)();

$MadelineProto->[getPwrChat](https://docs.madelineproto.xyz/getPwrChat.html)($id);

$MadelineProto->[getInfo](https://docs.madelineproto.xyz/getInfo.html)($id);

$MadelineProto->[getFullInfo](https://docs.madelineproto.xyz/getFullInfo.html)($id);

$MadelineProto->[getSelf](https://docs.madelineproto.xyz/getSelf.html)();


$MadelineProto->[requestCall](https://docs.madelineproto.xyz/requestCall.html)($id);

$MadelineProto->[requestSecretChat](https://docs.madelineproto.xyz/requestSecretChat.html)($id);

***
<br><br>
$MadelineProto->[account->acceptAuthorization](/API_docs/methods/account.acceptAuthorization.html)(\[bot_id: [long](/API_docs/types/long.html), scope: [string](/API_docs/types/string.html), public_key: [string](/API_docs/types/string.html), value_hashes: \[[SecureValueHash](/API_docs/types/SecureValueHash.html)\], credentials: [SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.acceptAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->cancelPasswordEmail](/API_docs/methods/account.cancelPasswordEmail.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.cancelPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->changeAuthorizationSettings](/API_docs/methods/account.changeAuthorizationSettings.html)(\[hash: [long](/API_docs/types/long.html), encrypted_requests_disabled: [Bool](/API_docs/types/Bool.html), call_requests_disabled: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.changeAuthorizationSettings"></a>  

***
<br><br>
$MadelineProto->[account->changePhone](/API_docs/methods/account.changePhone.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), phone_code: [string](/API_docs/types/string.html), \]) === [$User](/API_docs/types/User.html)<a name="account.changePhone"></a>  

***
<br><br>
$MadelineProto->[account->checkUsername](/API_docs/methods/account.checkUsername.html)(\[username: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.checkUsername"></a>  

***
<br><br>
$MadelineProto->[account->confirmPasswordEmail](/API_docs/methods/account.confirmPasswordEmail.html)(\[code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.confirmPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->confirmPhone](/API_docs/methods/account.confirmPhone.html)(\[phone_code_hash: [string](/API_docs/types/string.html), phone_code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.confirmPhone"></a>  

***
<br><br>
$MadelineProto->[account->createTheme](/API_docs/methods/account.createTheme.html)(\[slug: [string](/API_docs/types/string.html), title: [string](/API_docs/types/string.html), document: [InputDocument](/API_docs/types/InputDocument.html), settings: \[[InputThemeSettings](/API_docs/types/InputThemeSettings.html)\], \]) === [$Theme](/API_docs/types/Theme.html)<a name="account.createTheme"></a>  

***
<br><br>
$MadelineProto->[account->declinePasswordReset](/API_docs/methods/account.declinePasswordReset.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.declinePasswordReset"></a>  

***
<br><br>
$MadelineProto->[account->deleteAccount](/API_docs/methods/account.deleteAccount.html)(\[reason: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.deleteAccount"></a>  

***
<br><br>
$MadelineProto->[account->deleteSecureValue](/API_docs/methods/account.deleteSecureValue.html)(\[types: \[[SecureValueType](/API_docs/types/SecureValueType.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.deleteSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->finishTakeoutSession](/API_docs/methods/account.finishTakeoutSession.html)(\[success: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.finishTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->getAccountTTL](/API_docs/methods/account.getAccountTTL.html)(\[\]) === [$AccountDaysTTL](/API_docs/types/AccountDaysTTL.html)<a name="account.getAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->getAllSecureValues](/API_docs/methods/account.getAllSecureValues.html)(\[\]) === [$Vector\_of\_SecureValue](/API_docs/types/SecureValue.html)<a name="account.getAllSecureValues"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizationForm](/API_docs/methods/account.getAuthorizationForm.html)(\[bot_id: [long](/API_docs/types/long.html), scope: [string](/API_docs/types/string.html), public_key: [string](/API_docs/types/string.html), \]) === [$account.AuthorizationForm](/API_docs/types/account.AuthorizationForm.html)<a name="account.getAuthorizationForm"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizations](/API_docs/methods/account.getAuthorizations.html)(\[\]) === [$account.Authorizations](/API_docs/types/account.Authorizations.html)<a name="account.getAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->getAutoDownloadSettings](/API_docs/methods/account.getAutoDownloadSettings.html)(\[\]) === [$account.AutoDownloadSettings](/API_docs/types/account.AutoDownloadSettings.html)<a name="account.getAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->getChatThemes](/API_docs/methods/account.getChatThemes.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$account.Themes](/API_docs/types/account.Themes.html)<a name="account.getChatThemes"></a>  

***
<br><br>
$MadelineProto->[account->getContactSignUpNotification](/API_docs/methods/account.getContactSignUpNotification.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.getContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->getContentSettings](/API_docs/methods/account.getContentSettings.html)(\[\]) === [$account.ContentSettings](/API_docs/types/account.ContentSettings.html)<a name="account.getContentSettings"></a>  

***
<br><br>
$MadelineProto->[account->getGlobalPrivacySettings](/API_docs/methods/account.getGlobalPrivacySettings.html)(\[\]) === [$GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)<a name="account.getGlobalPrivacySettings"></a>  

***
<br><br>
$MadelineProto->[account->getMultiWallPapers](/API_docs/methods/account.getMultiWallPapers.html)(\[wallpapers: \[[InputWallPaper](/API_docs/types/InputWallPaper.html)\], \]) === [$Vector\_of\_WallPaper](/API_docs/types/WallPaper.html)<a name="account.getMultiWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->getNotifyExceptions](/API_docs/methods/account.getNotifyExceptions.html)(\[compare_sound: [Bool](/API_docs/types/Bool.html), peer: [InputNotifyPeer](/API_docs/types/InputNotifyPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="account.getNotifyExceptions"></a>  

***
<br><br>
$MadelineProto->[account->getNotifySettings](/API_docs/methods/account.getNotifySettings.html)(\[peer: [InputNotifyPeer](/API_docs/types/InputNotifyPeer.html), \]) === [$PeerNotifySettings](/API_docs/types/PeerNotifySettings.html)<a name="account.getNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->getPassword](/API_docs/methods/account.getPassword.html)(\[\]) === [$account.Password](/API_docs/types/account.Password.html)<a name="account.getPassword"></a>  

***
<br><br>
$MadelineProto->[account->getPasswordSettings](/API_docs/methods/account.getPasswordSettings.html)(\[password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), \]) === [$account.PasswordSettings](/API_docs/types/account.PasswordSettings.html)<a name="account.getPasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->getPrivacy](/API_docs/methods/account.getPrivacy.html)(\[key: [InputPrivacyKey](/API_docs/types/InputPrivacyKey.html), \]) === [$account.PrivacyRules](/API_docs/types/account.PrivacyRules.html)<a name="account.getPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->getSavedRingtones](/API_docs/methods/account.getSavedRingtones.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$account.SavedRingtones](/API_docs/types/account.SavedRingtones.html)<a name="account.getSavedRingtones"></a>  

***
<br><br>
$MadelineProto->[account->getSecureValue](/API_docs/methods/account.getSecureValue.html)(\[types: \[[SecureValueType](/API_docs/types/SecureValueType.html)\], \]) === [$Vector\_of\_SecureValue](/API_docs/types/SecureValue.html)<a name="account.getSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->getTheme](/API_docs/methods/account.getTheme.html)(\[format: [string](/API_docs/types/string.html), theme: [InputTheme](/API_docs/types/InputTheme.html), document_id: [long](/API_docs/types/long.html), \]) === [$Theme](/API_docs/types/Theme.html)<a name="account.getTheme"></a>  

***
<br><br>
$MadelineProto->[account->getThemes](/API_docs/methods/account.getThemes.html)(\[format: [string](/API_docs/types/string.html), hash: [long](/API_docs/types/long.html), \]) === [$account.Themes](/API_docs/types/account.Themes.html)<a name="account.getThemes"></a>  

***
<br><br>
$MadelineProto->[account->getTmpPassword](/API_docs/methods/account.getTmpPassword.html)(\[password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), period: [int](/API_docs/types/int.html), \]) === [$account.TmpPassword](/API_docs/types/account.TmpPassword.html)<a name="account.getTmpPassword"></a>  

***
<br><br>
$MadelineProto->[account->getWallPaper](/API_docs/methods/account.getWallPaper.html)(\[wallpaper: [InputWallPaper](/API_docs/types/InputWallPaper.html), \]) === [$WallPaper](/API_docs/types/WallPaper.html)<a name="account.getWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->getWallPapers](/API_docs/methods/account.getWallPapers.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$account.WallPapers](/API_docs/types/account.WallPapers.html)<a name="account.getWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->getWebAuthorizations](/API_docs/methods/account.getWebAuthorizations.html)(\[\]) === [$account.WebAuthorizations](/API_docs/types/account.WebAuthorizations.html)<a name="account.getWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->initTakeoutSession](/API_docs/methods/account.initTakeoutSession.html)(\[contacts: [Bool](/API_docs/types/Bool.html), message_users: [Bool](/API_docs/types/Bool.html), message_chats: [Bool](/API_docs/types/Bool.html), message_megagroups: [Bool](/API_docs/types/Bool.html), message_channels: [Bool](/API_docs/types/Bool.html), files: [Bool](/API_docs/types/Bool.html), file_max_size: [long](/API_docs/types/long.html), \]) === [$account.Takeout](/API_docs/types/account.Takeout.html)<a name="account.initTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->installTheme](/API_docs/methods/account.installTheme.html)(\[dark: [Bool](/API_docs/types/Bool.html), theme: [InputTheme](/API_docs/types/InputTheme.html), format: [string](/API_docs/types/string.html), base_theme: [BaseTheme](/API_docs/types/BaseTheme.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.installTheme"></a>  

***
<br><br>
$MadelineProto->[account->installWallPaper](/API_docs/methods/account.installWallPaper.html)(\[wallpaper: [InputWallPaper](/API_docs/types/InputWallPaper.html), settings: [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.installWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->registerDevice](/API_docs/methods/account.registerDevice.html)(\[no_muted: [Bool](/API_docs/types/Bool.html), token_type: [int](/API_docs/types/int.html), token: [string](/API_docs/types/string.html), app_sandbox: [Bool](/API_docs/types/Bool.html), secret: [bytes](/API_docs/types/bytes.html), other_uids: \[[long](/API_docs/types/long.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.registerDevice"></a>  

***
<br><br>
$MadelineProto->[account->reportPeer](/API_docs/methods/account.reportPeer.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), reason: [ReportReason](/API_docs/types/ReportReason.html), message: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.reportPeer"></a>  

***
<br><br>
$MadelineProto->[account->reportProfilePhoto](/API_docs/methods/account.reportProfilePhoto.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), photo_id: [InputPhoto](/API_docs/types/InputPhoto.html), reason: [ReportReason](/API_docs/types/ReportReason.html), message: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.reportProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[account->resendPasswordEmail](/API_docs/methods/account.resendPasswordEmail.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resendPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->resetAuthorization](/API_docs/methods/account.resetAuthorization.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resetAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetNotifySettings](/API_docs/methods/account.resetNotifySettings.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resetNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->resetPassword](/API_docs/methods/account.resetPassword.html)(\[\]) === [$account.ResetPasswordResult](/API_docs/types/account.ResetPasswordResult.html)<a name="account.resetPassword"></a>  

***
<br><br>
$MadelineProto->[account->resetWallPapers](/API_docs/methods/account.resetWallPapers.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resetWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorization](/API_docs/methods/account.resetWebAuthorization.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resetWebAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorizations](/API_docs/methods/account.resetWebAuthorizations.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="account.resetWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->saveAutoDownloadSettings](/API_docs/methods/account.saveAutoDownloadSettings.html)(\[low: [Bool](/API_docs/types/Bool.html), high: [Bool](/API_docs/types/Bool.html), settings: [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.saveAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->saveRingtone](/API_docs/methods/account.saveRingtone.html)(\[id: [InputDocument](/API_docs/types/InputDocument.html), unsave: [Bool](/API_docs/types/Bool.html), \]) === [$account.SavedRingtone](/API_docs/types/account.SavedRingtone.html)<a name="account.saveRingtone"></a>  

***
<br><br>
$MadelineProto->[account->saveSecureValue](/API_docs/methods/account.saveSecureValue.html)(\[value: [InputSecureValue](/API_docs/types/InputSecureValue.html), secure_secret_id: [long](/API_docs/types/long.html), \]) === [$SecureValue](/API_docs/types/SecureValue.html)<a name="account.saveSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->saveTheme](/API_docs/methods/account.saveTheme.html)(\[theme: [InputTheme](/API_docs/types/InputTheme.html), unsave: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.saveTheme"></a>  

***
<br><br>
$MadelineProto->[account->saveWallPaper](/API_docs/methods/account.saveWallPaper.html)(\[wallpaper: [InputWallPaper](/API_docs/types/InputWallPaper.html), unsave: [Bool](/API_docs/types/Bool.html), settings: [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.saveWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->sendChangePhoneCode](/API_docs/methods/account.sendChangePhoneCode.html)(\[phone_number: [string](/API_docs/types/string.html), settings: [CodeSettings](/API_docs/types/CodeSettings.html), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.html)<a name="account.sendChangePhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendConfirmPhoneCode](/API_docs/methods/account.sendConfirmPhoneCode.html)(\[hash: [string](/API_docs/types/string.html), settings: [CodeSettings](/API_docs/types/CodeSettings.html), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.html)<a name="account.sendConfirmPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyEmailCode](/API_docs/methods/account.sendVerifyEmailCode.html)(\[email: [string](/API_docs/types/string.html), \]) === [$account.SentEmailCode](/API_docs/types/account.SentEmailCode.html)<a name="account.sendVerifyEmailCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyPhoneCode](/API_docs/methods/account.sendVerifyPhoneCode.html)(\[phone_number: [string](/API_docs/types/string.html), settings: [CodeSettings](/API_docs/types/CodeSettings.html), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.html)<a name="account.sendVerifyPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->setAccountTTL](/API_docs/methods/account.setAccountTTL.html)(\[ttl: [AccountDaysTTL](/API_docs/types/AccountDaysTTL.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.setAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->setAuthorizationTTL](/API_docs/methods/account.setAuthorizationTTL.html)(\[authorization_ttl_days: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.setAuthorizationTTL"></a>  

***
<br><br>
$MadelineProto->[account->setContactSignUpNotification](/API_docs/methods/account.setContactSignUpNotification.html)(\[silent: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.setContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->setContentSettings](/API_docs/methods/account.setContentSettings.html)(\[sensitive_enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.setContentSettings"></a>  

***
<br><br>
$MadelineProto->[account->setGlobalPrivacySettings](/API_docs/methods/account.setGlobalPrivacySettings.html)(\[settings: [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html), \]) === [$GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)<a name="account.setGlobalPrivacySettings"></a>  

***
<br><br>
$MadelineProto->[account->setPrivacy](/API_docs/methods/account.setPrivacy.html)(\[key: [InputPrivacyKey](/API_docs/types/InputPrivacyKey.html), rules: \[[InputPrivacyRule](/API_docs/types/InputPrivacyRule.html)\], \]) === [$account.PrivacyRules](/API_docs/types/account.PrivacyRules.html)<a name="account.setPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->unregisterDevice](/API_docs/methods/account.unregisterDevice.html)(\[token_type: [int](/API_docs/types/int.html), token: [string](/API_docs/types/string.html), other_uids: \[[long](/API_docs/types/long.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.unregisterDevice"></a>  

***
<br><br>
$MadelineProto->[account->updateDeviceLocked](/API_docs/methods/account.updateDeviceLocked.html)(\[period: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.updateDeviceLocked"></a>  

***
<br><br>
$MadelineProto->[account->updateNotifySettings](/API_docs/methods/account.updateNotifySettings.html)(\[peer: [InputNotifyPeer](/API_docs/types/InputNotifyPeer.html), settings: [InputPeerNotifySettings](/API_docs/types/InputPeerNotifySettings.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.updateNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->updatePasswordSettings](/API_docs/methods/account.updatePasswordSettings.html)(\[password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), new_settings: [account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.updatePasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->updateProfile](/API_docs/methods/account.updateProfile.html)(\[first_name: [string](/API_docs/types/string.html), last_name: [string](/API_docs/types/string.html), about: [string](/API_docs/types/string.html), \]) === [$User](/API_docs/types/User.html)<a name="account.updateProfile"></a>  

***
<br><br>
$MadelineProto->[account->updateStatus](/API_docs/methods/account.updateStatus.html)(\[offline: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.updateStatus"></a>  

***
<br><br>
$MadelineProto->[account->updateTheme](/API_docs/methods/account.updateTheme.html)(\[format: [string](/API_docs/types/string.html), theme: [InputTheme](/API_docs/types/InputTheme.html), slug: [string](/API_docs/types/string.html), title: [string](/API_docs/types/string.html), document: [InputDocument](/API_docs/types/InputDocument.html), settings: \[[InputThemeSettings](/API_docs/types/InputThemeSettings.html)\], \]) === [$Theme](/API_docs/types/Theme.html)<a name="account.updateTheme"></a>  

***
<br><br>
$MadelineProto->[account->updateUsername](/API_docs/methods/account.updateUsername.html)(\[username: [string](/API_docs/types/string.html), \]) === [$User](/API_docs/types/User.html)<a name="account.updateUsername"></a>  

***
<br><br>
$MadelineProto->[account->uploadRingtone](/API_docs/methods/account.uploadRingtone.html)(\[file: [InputFile](/API_docs/types/InputFile.html), file_name: [string](/API_docs/types/string.html), mime_type: [string](/API_docs/types/string.html), \]) === [$Document](/API_docs/types/Document.html)<a name="account.uploadRingtone"></a>  

***
<br><br>
$MadelineProto->[account->uploadTheme](/API_docs/methods/account.uploadTheme.html)(\[file: [InputFile](/API_docs/types/InputFile.html), thumb: [InputFile](/API_docs/types/InputFile.html), file_name: [string](/API_docs/types/string.html), mime_type: [string](/API_docs/types/string.html), \]) === [$Document](/API_docs/types/Document.html)<a name="account.uploadTheme"></a>  

***
<br><br>
$MadelineProto->[account->uploadWallPaper](/API_docs/methods/account.uploadWallPaper.html)(\[file: [InputFile](/API_docs/types/InputFile.html), mime_type: [string](/API_docs/types/string.html), settings: [WallPaperSettings](/API_docs/types/WallPaperSettings.html), \]) === [$WallPaper](/API_docs/types/WallPaper.html)<a name="account.uploadWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->verifyEmail](/API_docs/methods/account.verifyEmail.html)(\[email: [string](/API_docs/types/string.html), code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.verifyEmail"></a>  

***
<br><br>
$MadelineProto->[account->verifyPhone](/API_docs/methods/account.verifyPhone.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), phone_code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="account.verifyPhone"></a>  

***
<br><br>
$MadelineProto->[auth->acceptLoginToken](/API_docs/methods/auth.acceptLoginToken.html)(\[token: [bytes](/API_docs/types/bytes.html), \]) === [$Authorization](/API_docs/types/Authorization.html)<a name="auth.acceptLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->bindTempAuthKey](/API_docs/methods/auth.bindTempAuthKey.html)(\[perm_auth_key_id: [long](/API_docs/types/long.html), nonce: [long](/API_docs/types/long.html), expires_at: [int](/API_docs/types/int.html), encrypted_message: [bytes](/API_docs/types/bytes.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="auth.bindTempAuthKey"></a>  

***
<br><br>
$MadelineProto->[auth->cancelCode](/API_docs/methods/auth.cancelCode.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="auth.cancelCode"></a>  

***
<br><br>
$MadelineProto->[auth->checkPassword](/API_docs/methods/auth.checkPassword.html)(\[password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.checkPassword"></a>  

***
<br><br>
$MadelineProto->[auth->checkRecoveryPassword](/API_docs/methods/auth.checkRecoveryPassword.html)(\[code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="auth.checkRecoveryPassword"></a>  

***
<br><br>
$MadelineProto->[auth->dropTempAuthKeys](/API_docs/methods/auth.dropTempAuthKeys.html)(\[except_auth_keys: \[[long](/API_docs/types/long.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="auth.dropTempAuthKeys"></a>  

***
<br><br>
$MadelineProto->[auth->exportAuthorization](/API_docs/methods/auth.exportAuthorization.html)(\[dc_id: [int](/API_docs/types/int.html), \]) === [$auth.ExportedAuthorization](/API_docs/types/auth.ExportedAuthorization.html)<a name="auth.exportAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->exportLoginToken](/API_docs/methods/auth.exportLoginToken.html)(\[api_id: [int](/API_docs/types/int.html), api_hash: [string](/API_docs/types/string.html), except_ids: \[[long](/API_docs/types/long.html)\], \]) === [$auth.LoginToken](/API_docs/types/auth.LoginToken.html)<a name="auth.exportLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->importAuthorization](/API_docs/methods/auth.importAuthorization.html)(\[id: [long](/API_docs/types/long.html), bytes: [bytes](/API_docs/types/bytes.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.importAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importBotAuthorization](/API_docs/methods/auth.importBotAuthorization.html)(\[api_id: [int](/API_docs/types/int.html), api_hash: [string](/API_docs/types/string.html), bot_auth_token: [string](/API_docs/types/string.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.importBotAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importLoginToken](/API_docs/methods/auth.importLoginToken.html)(\[token: [bytes](/API_docs/types/bytes.html), \]) === [$auth.LoginToken](/API_docs/types/auth.LoginToken.html)<a name="auth.importLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->logOut](/API_docs/methods/auth.logOut.html)(\[\]) === [$auth.LoggedOut](/API_docs/types/auth.LoggedOut.html)<a name="auth.logOut"></a>  

***
<br><br>
$MadelineProto->[auth->recoverPassword](/API_docs/methods/auth.recoverPassword.html)(\[code: [string](/API_docs/types/string.html), new_settings: [account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.recoverPassword"></a>  

***
<br><br>
$MadelineProto->[auth->requestPasswordRecovery](/API_docs/methods/auth.requestPasswordRecovery.html)(\[\]) === [$auth.PasswordRecovery](/API_docs/types/auth.PasswordRecovery.html)<a name="auth.requestPasswordRecovery"></a>  

***
<br><br>
$MadelineProto->[auth->resendCode](/API_docs/methods/auth.resendCode.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.html)<a name="auth.resendCode"></a>  

***
<br><br>
$MadelineProto->[auth->resetAuthorizations](/API_docs/methods/auth.resetAuthorizations.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="auth.resetAuthorizations"></a>  

***
<br><br>
$MadelineProto->[auth->sendCode](/API_docs/methods/auth.sendCode.html)(\[phone_number: [string](/API_docs/types/string.html), api_id: [int](/API_docs/types/int.html), api_hash: [string](/API_docs/types/string.html), settings: [CodeSettings](/API_docs/types/CodeSettings.html), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.html)<a name="auth.sendCode"></a>  

***
<br><br>
$MadelineProto->[auth->signIn](/API_docs/methods/auth.signIn.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), phone_code: [string](/API_docs/types/string.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.signIn"></a>  

***
<br><br>
$MadelineProto->[auth->signUp](/API_docs/methods/auth.signUp.html)(\[phone_number: [string](/API_docs/types/string.html), phone_code_hash: [string](/API_docs/types/string.html), first_name: [string](/API_docs/types/string.html), last_name: [string](/API_docs/types/string.html), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.html)<a name="auth.signUp"></a>  

***
<br><br>
$MadelineProto->[bots->answerWebhookJSONQuery](/API_docs/methods/bots.answerWebhookJSONQuery.html)(\[query_id: [long](/API_docs/types/long.html), data: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.answerWebhookJSONQuery"></a>  

***
<br><br>
$MadelineProto->[bots->getBotCommands](/API_docs/methods/bots.getBotCommands.html)(\[scope: [BotCommandScope](/API_docs/types/BotCommandScope.html), lang_code: [string](/API_docs/types/string.html), \]) === [$Vector\_of\_BotCommand](/API_docs/types/BotCommand.html)<a name="bots.getBotCommands"></a>  

***
<br><br>
$MadelineProto->[bots->getBotMenuButton](/API_docs/methods/bots.getBotMenuButton.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$BotMenuButton](/API_docs/types/BotMenuButton.html)<a name="bots.getBotMenuButton"></a>  

***
<br><br>
$MadelineProto->[bots->resetBotCommands](/API_docs/methods/bots.resetBotCommands.html)(\[scope: [BotCommandScope](/API_docs/types/BotCommandScope.html), lang_code: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.resetBotCommands"></a>  

***
<br><br>
$MadelineProto->[bots->sendCustomRequest](/API_docs/methods/bots.sendCustomRequest.html)(\[custom_method: [string](/API_docs/types/string.html), params: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$DataJSON](/API_docs/types/DataJSON.html)<a name="bots.sendCustomRequest"></a>  

***
<br><br>
$MadelineProto->[bots->setBotBroadcastDefaultAdminRights](/API_docs/methods/bots.setBotBroadcastDefaultAdminRights.html)(\[admin_rights: [ChatAdminRights](/API_docs/types/ChatAdminRights.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.setBotBroadcastDefaultAdminRights"></a>  

***
<br><br>
$MadelineProto->[bots->setBotCommands](/API_docs/methods/bots.setBotCommands.html)(\[scope: [BotCommandScope](/API_docs/types/BotCommandScope.html), lang_code: [string](/API_docs/types/string.html), commands: \[[BotCommand](/API_docs/types/BotCommand.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.setBotCommands"></a>  

***
<br><br>
$MadelineProto->[bots->setBotGroupDefaultAdminRights](/API_docs/methods/bots.setBotGroupDefaultAdminRights.html)(\[admin_rights: [ChatAdminRights](/API_docs/types/ChatAdminRights.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.setBotGroupDefaultAdminRights"></a>  

***
<br><br>
$MadelineProto->[bots->setBotMenuButton](/API_docs/methods/bots.setBotMenuButton.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), button: [BotMenuButton](/API_docs/types/BotMenuButton.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="bots.setBotMenuButton"></a>  

***
<br><br>
$MadelineProto->[channels->checkUsername](/API_docs/methods/channels.checkUsername.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), username: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.checkUsername"></a>  

***
<br><br>
$MadelineProto->[channels->convertToGigagroup](/API_docs/methods/channels.convertToGigagroup.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.convertToGigagroup"></a>  

***
<br><br>
$MadelineProto->[channels->createChannel](/API_docs/methods/channels.createChannel.html)(\[broadcast: [Bool](/API_docs/types/Bool.html), megagroup: [Bool](/API_docs/types/Bool.html), for_import: [Bool](/API_docs/types/Bool.html), title: [string](/API_docs/types/string.html), about: [string](/API_docs/types/string.html), geo_point: [InputGeoPoint](/API_docs/types/InputGeoPoint.html), address: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.createChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteChannel](/API_docs/methods/channels.deleteChannel.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.deleteChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteHistory](/API_docs/methods/channels.deleteHistory.html)(\[for_everyone: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), max_id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[channels->deleteMessages](/API_docs/methods/channels.deleteMessages.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)<a name="channels.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[channels->deleteParticipantHistory](/API_docs/methods/channels.deleteParticipantHistory.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), participant: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)<a name="channels.deleteParticipantHistory"></a>  

***
<br><br>
$MadelineProto->[channels->editAdmin](/API_docs/methods/channels.editAdmin.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), user_id: [InputUser](/API_docs/types/InputUser.html), admin_rights: [ChatAdminRights](/API_docs/types/ChatAdminRights.html), rank: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.editAdmin"></a>  

***
<br><br>
$MadelineProto->[channels->editBanned](/API_docs/methods/channels.editBanned.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), participant: [InputPeer](/API_docs/types/InputPeer.html), banned_rights: [ChatBannedRights](/API_docs/types/ChatBannedRights.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.editBanned"></a>  

***
<br><br>
$MadelineProto->[channels->editCreator](/API_docs/methods/channels.editCreator.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), user_id: [InputUser](/API_docs/types/InputUser.html), password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.editCreator"></a>  

***
<br><br>
$MadelineProto->[channels->editLocation](/API_docs/methods/channels.editLocation.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), geo_point: [InputGeoPoint](/API_docs/types/InputGeoPoint.html), address: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.editLocation"></a>  

***
<br><br>
$MadelineProto->[channels->editPhoto](/API_docs/methods/channels.editPhoto.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), photo: [InputChatPhoto](/API_docs/types/InputChatPhoto.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.editPhoto"></a>  

***
<br><br>
$MadelineProto->[channels->editTitle](/API_docs/methods/channels.editTitle.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), title: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.editTitle"></a>  

***
<br><br>
$MadelineProto->[channels->exportMessageLink](/API_docs/methods/channels.exportMessageLink.html)(\[grouped: [Bool](/API_docs/types/Bool.html), thread: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), id: [int](/API_docs/types/int.html), \]) === [$ExportedMessageLink](/API_docs/types/ExportedMessageLink.html)<a name="channels.exportMessageLink"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminLog](/API_docs/methods/channels.getAdminLog.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), q: [string](/API_docs/types/string.html), events_filter: [ChannelAdminLogEventsFilter](/API_docs/types/ChannelAdminLogEventsFilter.html), admins: \[[InputUser](/API_docs/types/InputUser.html)\], max_id: [long](/API_docs/types/long.html), min_id: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$channels.AdminLogResults](/API_docs/types/channels.AdminLogResults.html)<a name="channels.getAdminLog"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminedPublicChannels](/API_docs/methods/channels.getAdminedPublicChannels.html)(\[by_location: [Bool](/API_docs/types/Bool.html), check_limit: [Bool](/API_docs/types/Bool.html), \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="channels.getAdminedPublicChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getChannels](/API_docs/methods/channels.getChannels.html)(\[id: \[[InputChannel](/API_docs/types/InputChannel.html)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="channels.getChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getFullChannel](/API_docs/methods/channels.getFullChannel.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$messages.ChatFull](/API_docs/types/messages.ChatFull.html)<a name="channels.getFullChannel"></a>  

***
<br><br>
$MadelineProto->[channels->getGroupsForDiscussion](/API_docs/methods/channels.getGroupsForDiscussion.html)(\[\]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="channels.getGroupsForDiscussion"></a>  

***
<br><br>
$MadelineProto->[channels->getInactiveChannels](/API_docs/methods/channels.getInactiveChannels.html)(\[\]) === [$messages.InactiveChats](/API_docs/types/messages.InactiveChats.html)<a name="channels.getInactiveChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getLeftChannels](/API_docs/methods/channels.getLeftChannels.html)(\[offset: [int](/API_docs/types/int.html), \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="channels.getLeftChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getMessages](/API_docs/methods/channels.getMessages.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), id: \[[InputMessage](/API_docs/types/InputMessage.html)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="channels.getMessages"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipant](/API_docs/methods/channels.getParticipant.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), participant: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$channels.ChannelParticipant](/API_docs/types/channels.ChannelParticipant.html)<a name="channels.getParticipant"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipants](/API_docs/methods/channels.getParticipants.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), filter: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.html), offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$channels.ChannelParticipants](/API_docs/types/channels.ChannelParticipants.html)<a name="channels.getParticipants"></a>  

***
<br><br>
$MadelineProto->[channels->getSendAs](/API_docs/methods/channels.getSendAs.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$channels.SendAsPeers](/API_docs/types/channels.SendAsPeers.html)<a name="channels.getSendAs"></a>  

***
<br><br>
$MadelineProto->[channels->getSponsoredMessages](/API_docs/methods/channels.getSponsoredMessages.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$messages.SponsoredMessages](/API_docs/types/messages.SponsoredMessages.html)<a name="channels.getSponsoredMessages"></a>  

***
<br><br>
$MadelineProto->[channels->inviteToChannel](/API_docs/methods/channels.inviteToChannel.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), users: \[[InputUser](/API_docs/types/InputUser.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.inviteToChannel"></a>  

***
<br><br>
$MadelineProto->[channels->joinChannel](/API_docs/methods/channels.joinChannel.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.joinChannel"></a>  

***
<br><br>
$MadelineProto->[channels->leaveChannel](/API_docs/methods/channels.leaveChannel.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.leaveChannel"></a>  

***
<br><br>
$MadelineProto->[channels->readHistory](/API_docs/methods/channels.readHistory.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), max_id: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.readHistory"></a>  

***
<br><br>
$MadelineProto->[channels->readMessageContents](/API_docs/methods/channels.readMessageContents.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[channels->reportSpam](/API_docs/methods/channels.reportSpam.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), participant: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.reportSpam"></a>  

***
<br><br>
$MadelineProto->[channels->setDiscussionGroup](/API_docs/methods/channels.setDiscussionGroup.html)(\[broadcast: [InputChannel](/API_docs/types/InputChannel.html), group: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.setDiscussionGroup"></a>  

***
<br><br>
$MadelineProto->[channels->setStickers](/API_docs/methods/channels.setStickers.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.setStickers"></a>  

***
<br><br>
$MadelineProto->[channels->toggleJoinRequest](/API_docs/methods/channels.toggleJoinRequest.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.toggleJoinRequest"></a>  

***
<br><br>
$MadelineProto->[channels->toggleJoinToSend](/API_docs/methods/channels.toggleJoinToSend.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.toggleJoinToSend"></a>  

***
<br><br>
$MadelineProto->[channels->togglePreHistoryHidden](/API_docs/methods/channels.togglePreHistoryHidden.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.togglePreHistoryHidden"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSignatures](/API_docs/methods/channels.toggleSignatures.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.toggleSignatures"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSlowMode](/API_docs/methods/channels.toggleSlowMode.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), seconds: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="channels.toggleSlowMode"></a>  

***
<br><br>
$MadelineProto->[channels->updateUsername](/API_docs/methods/channels.updateUsername.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), username: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.updateUsername"></a>  

***
<br><br>
$MadelineProto->[channels->viewSponsoredMessage](/API_docs/methods/channels.viewSponsoredMessage.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="channels.viewSponsoredMessage"></a>  

***
<br><br>
$MadelineProto->[contacts->acceptContact](/API_docs/methods/contacts.acceptContact.html)(\[id: [InputUser](/API_docs/types/InputUser.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="contacts.acceptContact"></a>  

***
<br><br>
$MadelineProto->[contacts->addContact](/API_docs/methods/contacts.addContact.html)(\[add_phone_privacy_exception: [Bool](/API_docs/types/Bool.html), id: [InputUser](/API_docs/types/InputUser.html), first_name: [string](/API_docs/types/string.html), last_name: [string](/API_docs/types/string.html), phone: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="contacts.addContact"></a>  

***
<br><br>
$MadelineProto->[contacts->block](/API_docs/methods/contacts.block.html)(\[id: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.block"></a>  

***
<br><br>
$MadelineProto->[contacts->blockFromReplies](/API_docs/methods/contacts.blockFromReplies.html)(\[delete_message: [Bool](/API_docs/types/Bool.html), delete_history: [Bool](/API_docs/types/Bool.html), report_spam: [Bool](/API_docs/types/Bool.html), msg_id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="contacts.blockFromReplies"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteByPhones](/API_docs/methods/contacts.deleteByPhones.html)(\[phones: \[[string](/API_docs/types/string.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.deleteByPhones"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteContacts](/API_docs/methods/contacts.deleteContacts.html)(\[id: \[[InputUser](/API_docs/types/InputUser.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="contacts.deleteContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getBlocked](/API_docs/methods/contacts.getBlocked.html)(\[offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$contacts.Blocked](/API_docs/types/contacts.Blocked.html)<a name="contacts.getBlocked"></a>  

***
<br><br>
$MadelineProto->[contacts->getContactIDs](/API_docs/methods/contacts.getContactIDs.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$Vector\_of\_int](/API_docs/types/int.html)<a name="contacts.getContactIDs"></a>  

***
<br><br>
$MadelineProto->[contacts->getContacts](/API_docs/methods/contacts.getContacts.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$contacts.Contacts](/API_docs/types/contacts.Contacts.html)<a name="contacts.getContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getLocated](/API_docs/methods/contacts.getLocated.html)(\[background: [Bool](/API_docs/types/Bool.html), geo_point: [InputGeoPoint](/API_docs/types/InputGeoPoint.html), self_expires: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="contacts.getLocated"></a>  

***
<br><br>
$MadelineProto->[contacts->getSaved](/API_docs/methods/contacts.getSaved.html)(\[\]) === [$Vector\_of\_SavedContact](/API_docs/types/SavedContact.html)<a name="contacts.getSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->getStatuses](/API_docs/methods/contacts.getStatuses.html)(\[\]) === [$Vector\_of\_ContactStatus](/API_docs/types/ContactStatus.html)<a name="contacts.getStatuses"></a>  

***
<br><br>
$MadelineProto->[contacts->getTopPeers](/API_docs/methods/contacts.getTopPeers.html)(\[correspondents: [Bool](/API_docs/types/Bool.html), bots_pm: [Bool](/API_docs/types/Bool.html), bots_inline: [Bool](/API_docs/types/Bool.html), phone_calls: [Bool](/API_docs/types/Bool.html), forward_users: [Bool](/API_docs/types/Bool.html), forward_chats: [Bool](/API_docs/types/Bool.html), groups: [Bool](/API_docs/types/Bool.html), channels: [Bool](/API_docs/types/Bool.html), offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$contacts.TopPeers](/API_docs/types/contacts.TopPeers.html)<a name="contacts.getTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->importContacts](/API_docs/methods/contacts.importContacts.html)(\[contacts: \[[InputContact](/API_docs/types/InputContact.html)\], \]) === [$contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.html)<a name="contacts.importContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->resetSaved](/API_docs/methods/contacts.resetSaved.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.resetSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->resetTopPeerRating](/API_docs/methods/contacts.resetTopPeerRating.html)(\[category: [TopPeerCategory](/API_docs/types/TopPeerCategory.html), peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.resetTopPeerRating"></a>  

***
<br><br>
$MadelineProto->[contacts->resolvePhone](/API_docs/methods/contacts.resolvePhone.html)(\[phone: [string](/API_docs/types/string.html), \]) === [$contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)<a name="contacts.resolvePhone"></a>  

***
<br><br>
$MadelineProto->[contacts->resolveUsername](/API_docs/methods/contacts.resolveUsername.html)(\[username: [string](/API_docs/types/string.html), \]) === [$contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)<a name="contacts.resolveUsername"></a>  

***
<br><br>
$MadelineProto->[contacts->search](/API_docs/methods/contacts.search.html)(\[q: [string](/API_docs/types/string.html), limit: [int](/API_docs/types/int.html), \]) === [$contacts.Found](/API_docs/types/contacts.Found.html)<a name="contacts.search"></a>  

***
<br><br>
$MadelineProto->[contacts->toggleTopPeers](/API_docs/methods/contacts.toggleTopPeers.html)(\[enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.toggleTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->unblock](/API_docs/methods/contacts.unblock.html)(\[id: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="contacts.unblock"></a>  

***
<br><br>
$MadelineProto->[folders->deleteFolder](/API_docs/methods/folders.deleteFolder.html)(\[folder_id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="folders.deleteFolder"></a>  

***
<br><br>
$MadelineProto->[folders->editPeerFolders](/API_docs/methods/folders.editPeerFolders.html)(\[folder_peers: \[[InputFolderPeer](/API_docs/types/InputFolderPeer.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="folders.editPeerFolders"></a>  

***
<br><br>
$MadelineProto->[help->acceptTermsOfService](/API_docs/methods/help.acceptTermsOfService.html)(\[id: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="help.acceptTermsOfService"></a>  

***
<br><br>
$MadelineProto->[help->dismissSuggestion](/API_docs/methods/help.dismissSuggestion.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), suggestion: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="help.dismissSuggestion"></a>  

***
<br><br>
$MadelineProto->[help->editUserInfo](/API_docs/methods/help.editUserInfo.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), message: [string](/API_docs/types/string.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \]) === [$help.UserInfo](/API_docs/types/help.UserInfo.html)<a name="help.editUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->getAppChangelog](/API_docs/methods/help.getAppChangelog.html)(\[prev_app_version: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="help.getAppChangelog"></a>  

***
<br><br>
$MadelineProto->[help->getAppConfig](/API_docs/methods/help.getAppConfig.html)(\[\]) === [$JSONValue](/API_docs/types/JSONValue.html)<a name="help.getAppConfig"></a>  

***
<br><br>
$MadelineProto->[help->getAppUpdate](/API_docs/methods/help.getAppUpdate.html)(\[source: [string](/API_docs/types/string.html), \]) === [$help.AppUpdate](/API_docs/types/help.AppUpdate.html)<a name="help.getAppUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getCdnConfig](/API_docs/methods/help.getCdnConfig.html)(\[\]) === [$CdnConfig](/API_docs/types/CdnConfig.html)<a name="help.getCdnConfig"></a>  

***
<br><br>
$MadelineProto->[help->getConfig](/API_docs/methods/help.getConfig.html)(\[\]) === [$Config](/API_docs/types/Config.html)<a name="help.getConfig"></a>  

***
<br><br>
$MadelineProto->[help->getCountriesList](/API_docs/methods/help.getCountriesList.html)(\[lang_code: [string](/API_docs/types/string.html), hash: [int](/API_docs/types/int.html), \]) === [$help.CountriesList](/API_docs/types/help.CountriesList.html)<a name="help.getCountriesList"></a>  

***
<br><br>
$MadelineProto->[help->getDeepLinkInfo](/API_docs/methods/help.getDeepLinkInfo.html)(\[path: [string](/API_docs/types/string.html), \]) === [$help.DeepLinkInfo](/API_docs/types/help.DeepLinkInfo.html)<a name="help.getDeepLinkInfo"></a>  

***
<br><br>
$MadelineProto->[help->getInviteText](/API_docs/methods/help.getInviteText.html)(\[\]) === [$help.InviteText](/API_docs/types/help.InviteText.html)<a name="help.getInviteText"></a>  

***
<br><br>
$MadelineProto->[help->getNearestDc](/API_docs/methods/help.getNearestDc.html)(\[\]) === [$NearestDc](/API_docs/types/NearestDc.html)<a name="help.getNearestDc"></a>  

***
<br><br>
$MadelineProto->[help->getPassportConfig](/API_docs/methods/help.getPassportConfig.html)(\[hash: [int](/API_docs/types/int.html), \]) === [$help.PassportConfig](/API_docs/types/help.PassportConfig.html)<a name="help.getPassportConfig"></a>  

***
<br><br>
$MadelineProto->[help->getPremiumPromo](/API_docs/methods/help.getPremiumPromo.html)(\[\]) === [$help.PremiumPromo](/API_docs/types/help.PremiumPromo.html)<a name="help.getPremiumPromo"></a>  

***
<br><br>
$MadelineProto->[help->getPromoData](/API_docs/methods/help.getPromoData.html)(\[\]) === [$help.PromoData](/API_docs/types/help.PromoData.html)<a name="help.getPromoData"></a>  

***
<br><br>
$MadelineProto->[help->getRecentMeUrls](/API_docs/methods/help.getRecentMeUrls.html)(\[referer: [string](/API_docs/types/string.html), \]) === [$help.RecentMeUrls](/API_docs/types/help.RecentMeUrls.html)<a name="help.getRecentMeUrls"></a>  

***
<br><br>
$MadelineProto->[help->getSupport](/API_docs/methods/help.getSupport.html)(\[\]) === [$help.Support](/API_docs/types/help.Support.html)<a name="help.getSupport"></a>  

***
<br><br>
$MadelineProto->[help->getSupportName](/API_docs/methods/help.getSupportName.html)(\[\]) === [$help.SupportName](/API_docs/types/help.SupportName.html)<a name="help.getSupportName"></a>  

***
<br><br>
$MadelineProto->[help->getTermsOfServiceUpdate](/API_docs/methods/help.getTermsOfServiceUpdate.html)(\[\]) === [$help.TermsOfServiceUpdate](/API_docs/types/help.TermsOfServiceUpdate.html)<a name="help.getTermsOfServiceUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getUserInfo](/API_docs/methods/help.getUserInfo.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$help.UserInfo](/API_docs/types/help.UserInfo.html)<a name="help.getUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->hidePromoData](/API_docs/methods/help.hidePromoData.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="help.hidePromoData"></a>  

***
<br><br>
$MadelineProto->[help->saveAppLog](/API_docs/methods/help.saveAppLog.html)(\[events: \[[InputAppEvent](/API_docs/types/InputAppEvent.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="help.saveAppLog"></a>  

***
<br><br>
$MadelineProto->[help->setBotUpdatesStatus](/API_docs/methods/help.setBotUpdatesStatus.html)(\[pending_updates_count: [int](/API_docs/types/int.html), message: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="help.setBotUpdatesStatus"></a>  

***
<br><br>
$MadelineProto->[initConnection](/API_docs/methods/initConnection.html)(\[api_id: [int](/API_docs/types/int.html), device_model: [string](/API_docs/types/string.html), system_version: [string](/API_docs/types/string.html), app_version: [string](/API_docs/types/string.html), system_lang_code: [string](/API_docs/types/string.html), lang_pack: [string](/API_docs/types/string.html), lang_code: [string](/API_docs/types/string.html), proxy: [InputClientProxy](/API_docs/types/InputClientProxy.html), params: [JSONValue](/API_docs/types/JSONValue.html), query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="initConnection"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsg](/API_docs/methods/invokeAfterMsg.html)(\[msg_id: [long](/API_docs/types/long.html), query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeAfterMsg"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsgs](/API_docs/methods/invokeAfterMsgs.html)(\[msg_ids: \[[long](/API_docs/types/long.html)\], query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeAfterMsgs"></a>  

***
<br><br>
$MadelineProto->[invokeWithLayer](/API_docs/methods/invokeWithLayer.html)(\[layer: [int](/API_docs/types/int.html), query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeWithLayer"></a>  

***
<br><br>
$MadelineProto->[invokeWithMessagesRange](/API_docs/methods/invokeWithMessagesRange.html)(\[range: [MessageRange](/API_docs/types/MessageRange.html), query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeWithMessagesRange"></a>  

***
<br><br>
$MadelineProto->[invokeWithTakeout](/API_docs/methods/invokeWithTakeout.html)(\[takeout_id: [long](/API_docs/types/long.html), query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeWithTakeout"></a>  

***
<br><br>
$MadelineProto->[invokeWithoutUpdates](/API_docs/methods/invokeWithoutUpdates.html)(\[query: [!X](/API_docs/types/!X.html), \]) === [$X](/API_docs/types/X.html)<a name="invokeWithoutUpdates"></a>  

***
<br><br>
$MadelineProto->[langpack->getDifference](/API_docs/methods/langpack.getDifference.html)(\[lang_pack: [string](/API_docs/types/string.html), lang_code: [string](/API_docs/types/string.html), from_version: [int](/API_docs/types/int.html), \]) === [$LangPackDifference](/API_docs/types/LangPackDifference.html)<a name="langpack.getDifference"></a>  

***
<br><br>
$MadelineProto->[langpack->getLangPack](/API_docs/methods/langpack.getLangPack.html)(\[lang_pack: [string](/API_docs/types/string.html), lang_code: [string](/API_docs/types/string.html), \]) === [$LangPackDifference](/API_docs/types/LangPackDifference.html)<a name="langpack.getLangPack"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguage](/API_docs/methods/langpack.getLanguage.html)(\[lang_pack: [string](/API_docs/types/string.html), lang_code: [string](/API_docs/types/string.html), \]) === [$LangPackLanguage](/API_docs/types/LangPackLanguage.html)<a name="langpack.getLanguage"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguages](/API_docs/methods/langpack.getLanguages.html)(\[lang_pack: [string](/API_docs/types/string.html), \]) === [$Vector\_of\_LangPackLanguage](/API_docs/types/LangPackLanguage.html)<a name="langpack.getLanguages"></a>  

***
<br><br>
$MadelineProto->[langpack->getStrings](/API_docs/methods/langpack.getStrings.html)(\[lang_pack: [string](/API_docs/types/string.html), lang_code: [string](/API_docs/types/string.html), keys: \[[string](/API_docs/types/string.html)\], \]) === [$Vector\_of\_LangPackString](/API_docs/types/LangPackString.html)<a name="langpack.getStrings"></a>  

***
<br><br>
$MadelineProto->[messages->acceptEncryption](/API_docs/methods/messages.acceptEncryption.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), g_b: [bytes](/API_docs/types/bytes.html), key_fingerprint: [long](/API_docs/types/long.html), \]) === [$EncryptedChat](/API_docs/types/EncryptedChat.html)<a name="messages.acceptEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->acceptUrlAuth](/API_docs/methods/messages.acceptUrlAuth.html)(\[write_allowed: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), button_id: [int](/API_docs/types/int.html), url: [string](/API_docs/types/string.html), \]) === [$UrlAuthResult](/API_docs/types/UrlAuthResult.html)<a name="messages.acceptUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->addChatUser](/API_docs/methods/messages.addChatUser.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), user_id: [InputUser](/API_docs/types/InputUser.html), fwd_limit: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.addChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->checkChatInvite](/API_docs/methods/messages.checkChatInvite.html)(\[hash: [string](/API_docs/types/string.html), \]) === [$ChatInvite](/API_docs/types/ChatInvite.html)<a name="messages.checkChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->checkHistoryImport](/API_docs/methods/messages.checkHistoryImport.html)(\[import_head: [string](/API_docs/types/string.html), \]) === [$messages.HistoryImportParsed](/API_docs/types/messages.HistoryImportParsed.html)<a name="messages.checkHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->checkHistoryImportPeer](/API_docs/methods/messages.checkHistoryImportPeer.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.CheckedHistoryImportPeer](/API_docs/types/messages.CheckedHistoryImportPeer.html)<a name="messages.checkHistoryImportPeer"></a>  

***
<br><br>
$MadelineProto->[messages->clearAllDrafts](/API_docs/methods/messages.clearAllDrafts.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.clearAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->clearRecentStickers](/API_docs/methods/messages.clearRecentStickers.html)(\[attached: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.clearRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->createChat](/API_docs/methods/messages.createChat.html)(\[users: \[[InputUser](/API_docs/types/InputUser.html)\], title: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.createChat"></a>  

***
<br><br>
$MadelineProto->[messages->deleteChat](/API_docs/methods/messages.deleteChat.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.deleteChat"></a>  

***
<br><br>
$MadelineProto->[messages->deleteChatUser](/API_docs/methods/messages.deleteChatUser.html)(\[revoke_history: [Bool](/API_docs/types/Bool.html), chat_id: [InputPeer](/API_docs/types/InputPeer.html), user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.deleteChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->deleteExportedChatInvite](/API_docs/methods/messages.deleteExportedChatInvite.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), link: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.deleteExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->deleteHistory](/API_docs/methods/messages.deleteHistory.html)(\[just_clear: [Bool](/API_docs/types/Bool.html), revoke: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), max_id: [int](/API_docs/types/int.html), min_date: [int](/API_docs/types/int.html), max_date: [int](/API_docs/types/int.html), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)<a name="messages.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[messages->deleteMessages](/API_docs/methods/messages.deleteMessages.html)(\[revoke: [Bool](/API_docs/types/Bool.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)<a name="messages.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[messages->deletePhoneCallHistory](/API_docs/methods/messages.deletePhoneCallHistory.html)(\[revoke: [Bool](/API_docs/types/Bool.html), \]) === [$messages.AffectedFoundMessages](/API_docs/types/messages.AffectedFoundMessages.html)<a name="messages.deletePhoneCallHistory"></a>  

***
<br><br>
$MadelineProto->[messages->deleteRevokedExportedChatInvites](/API_docs/methods/messages.deleteRevokedExportedChatInvites.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), admin_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.deleteRevokedExportedChatInvites"></a>  

***
<br><br>
$MadelineProto->[messages->deleteScheduledMessages](/API_docs/methods/messages.deleteScheduledMessages.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.deleteScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->discardEncryption](/API_docs/methods/messages.discardEncryption.html)(\[delete_history: [Bool](/API_docs/types/Bool.html), chat_id: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.discardEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAbout](/API_docs/methods/messages.editChatAbout.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), about: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.editChatAbout"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAdmin](/API_docs/methods/messages.editChatAdmin.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), user_id: [InputUser](/API_docs/types/InputUser.html), is_admin: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.editChatAdmin"></a>  

***
<br><br>
$MadelineProto->[messages->editChatDefaultBannedRights](/API_docs/methods/messages.editChatDefaultBannedRights.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), banned_rights: [ChatBannedRights](/API_docs/types/ChatBannedRights.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.editChatDefaultBannedRights"></a>  

***
<br><br>
$MadelineProto->[messages->editChatPhoto](/API_docs/methods/messages.editChatPhoto.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), photo: [InputChatPhoto](/API_docs/types/InputChatPhoto.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.editChatPhoto"></a>  

***
<br><br>
$MadelineProto->[messages->editChatTitle](/API_docs/methods/messages.editChatTitle.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), title: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.editChatTitle"></a>  

***
<br><br>
$MadelineProto->[messages->editExportedChatInvite](/API_docs/methods/messages.editExportedChatInvite.html)(\[revoked: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), link: [string](/API_docs/types/string.html), expire_date: [int](/API_docs/types/int.html), usage_limit: [int](/API_docs/types/int.html), request_needed: [Bool](/API_docs/types/Bool.html), title: [string](/API_docs/types/string.html), \]) === [$messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)<a name="messages.editExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->editInlineBotMessage](/API_docs/methods/messages.editInlineBotMessage.html)(\[no_webpage: [Bool](/API_docs/types/Bool.html), id: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), message: [string](/API_docs/types/string.html), media: [InputMedia](/API_docs/types/InputMedia.html), reply_markup: [ReplyMarkup](/API_docs/types/ReplyMarkup.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.editInlineBotMessage"></a>  

***
<br><br>
$MadelineProto->[messages->editMessage](/API_docs/methods/messages.editMessage.html)(\[no_webpage: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), message: [string](/API_docs/types/string.html), media: [InputMedia](/API_docs/types/InputMedia.html), reply_markup: [ReplyMarkup](/API_docs/types/ReplyMarkup.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], schedule_date: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.editMessage"></a>  

***
<br><br>
$MadelineProto->[messages->exportChatInvite](/API_docs/methods/messages.exportChatInvite.html)(\[legacy_revoke_permanent: [Bool](/API_docs/types/Bool.html), request_needed: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), expire_date: [int](/API_docs/types/int.html), usage_limit: [int](/API_docs/types/int.html), title: [string](/API_docs/types/string.html), \]) === [$ExportedChatInvite](/API_docs/types/ExportedChatInvite.html)<a name="messages.exportChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->faveSticker](/API_docs/methods/messages.faveSticker.html)(\[id: [InputDocument](/API_docs/types/InputDocument.html), unfave: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.faveSticker"></a>  

***
<br><br>
$MadelineProto->[messages->forwardMessages](/API_docs/methods/messages.forwardMessages.html)(\[silent: [Bool](/API_docs/types/Bool.html), background: [Bool](/API_docs/types/Bool.html), with_my_score: [Bool](/API_docs/types/Bool.html), drop_author: [Bool](/API_docs/types/Bool.html), drop_media_captions: [Bool](/API_docs/types/Bool.html), noforwards: [Bool](/API_docs/types/Bool.html), from_peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], to_peer: [InputPeer](/API_docs/types/InputPeer.html), schedule_date: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.forwardMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getAdminsWithInvites](/API_docs/methods/messages.getAdminsWithInvites.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.ChatAdminsWithInvites](/API_docs/types/messages.ChatAdminsWithInvites.html)<a name="messages.getAdminsWithInvites"></a>  

***
<br><br>
$MadelineProto->[messages->getAllChats](/API_docs/methods/messages.getAllChats.html)(\[except_ids: \[[long](/API_docs/types/long.html)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="messages.getAllChats"></a>  

***
<br><br>
$MadelineProto->[messages->getAllDrafts](/API_docs/methods/messages.getAllDrafts.html)(\[\]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.getAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->getAllStickers](/API_docs/methods/messages.getAllStickers.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$messages.AllStickers](/API_docs/types/messages.AllStickers.html)<a name="messages.getAllStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getArchivedStickers](/API_docs/methods/messages.getArchivedStickers.html)(\[masks: [Bool](/API_docs/types/Bool.html), offset_id: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.ArchivedStickers](/API_docs/types/messages.ArchivedStickers.html)<a name="messages.getArchivedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getAttachMenuBot](/API_docs/methods/messages.getAttachMenuBot.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), \]) === [$AttachMenuBotsBot](/API_docs/types/AttachMenuBotsBot.html)<a name="messages.getAttachMenuBot"></a>  

***
<br><br>
$MadelineProto->[messages->getAttachMenuBots](/API_docs/methods/messages.getAttachMenuBots.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$AttachMenuBots](/API_docs/types/AttachMenuBots.html)<a name="messages.getAttachMenuBots"></a>  

***
<br><br>
$MadelineProto->[messages->getAttachedStickers](/API_docs/methods/messages.getAttachedStickers.html)(\[media: [InputStickeredMedia](/API_docs/types/InputStickeredMedia.html), \]) === [$Vector\_of\_StickerSetCovered](/API_docs/types/StickerSetCovered.html)<a name="messages.getAttachedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getAvailableReactions](/API_docs/methods/messages.getAvailableReactions.html)(\[hash: [int](/API_docs/types/int.html), \]) === [$messages.AvailableReactions](/API_docs/types/messages.AvailableReactions.html)<a name="messages.getAvailableReactions"></a>  

***
<br><br>
$MadelineProto->[messages->getBotCallbackAnswer](/API_docs/methods/messages.getBotCallbackAnswer.html)(\[game: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), data: [bytes](/API_docs/types/bytes.html), password: [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html), \]) === [$messages.BotCallbackAnswer](/API_docs/types/messages.BotCallbackAnswer.html)<a name="messages.getBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->getChatInviteImporters](/API_docs/methods/messages.getChatInviteImporters.html)(\[requested: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), link: [string](/API_docs/types/string.html), q: [string](/API_docs/types/string.html), offset_date: [int](/API_docs/types/int.html), offset_user: [InputUser](/API_docs/types/InputUser.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.ChatInviteImporters](/API_docs/types/messages.ChatInviteImporters.html)<a name="messages.getChatInviteImporters"></a>  

***
<br><br>
$MadelineProto->[messages->getChats](/API_docs/methods/messages.getChats.html)(\[id: \[[long](/API_docs/types/long.html)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="messages.getChats"></a>  

***
<br><br>
$MadelineProto->[messages->getCommonChats](/API_docs/methods/messages.getCommonChats.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), max_id: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.Chats](/API_docs/types/messages.Chats.html)<a name="messages.getCommonChats"></a>  

***
<br><br>
$MadelineProto->[messages->getDhConfig](/API_docs/methods/messages.getDhConfig.html)(\[version: [int](/API_docs/types/int.html), random_length: [int](/API_docs/types/int.html), \]) === [$messages.DhConfig](/API_docs/types/messages.DhConfig.html)<a name="messages.getDhConfig"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogFilters](/API_docs/methods/messages.getDialogFilters.html)(\[\]) === [$Vector\_of\_DialogFilter](/API_docs/types/DialogFilter.html)<a name="messages.getDialogFilters"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogUnreadMarks](/API_docs/methods/messages.getDialogUnreadMarks.html)(\[\]) === [$Vector\_of\_DialogPeer](/API_docs/types/DialogPeer.html)<a name="messages.getDialogUnreadMarks"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogs](/API_docs/methods/messages.getDialogs.html)(\[exclude_pinned: [Bool](/API_docs/types/Bool.html), folder_id: [int](/API_docs/types/int.html), offset_date: [int](/API_docs/types/int.html), offset_id: [int](/API_docs/types/int.html), offset_peer: [InputPeer](/API_docs/types/InputPeer.html), limit: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Dialogs](/API_docs/types/messages.Dialogs.html)<a name="messages.getDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getDiscussionMessage](/API_docs/methods/messages.getDiscussionMessage.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), \]) === [$messages.DiscussionMessage](/API_docs/types/messages.DiscussionMessage.html)<a name="messages.getDiscussionMessage"></a>  

***
<br><br>
$MadelineProto->[messages->getDocumentByHash](/API_docs/methods/messages.getDocumentByHash.html)(\[sha256: [bytes](/API_docs/types/bytes.html), size: [long](/API_docs/types/long.html), mime_type: [string](/API_docs/types/string.html), \]) === [$Document](/API_docs/types/Document.html)<a name="messages.getDocumentByHash"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywords](/API_docs/methods/messages.getEmojiKeywords.html)(\[lang_code: [string](/API_docs/types/string.html), \]) === [$EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.html)<a name="messages.getEmojiKeywords"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsDifference](/API_docs/methods/messages.getEmojiKeywordsDifference.html)(\[lang_code: [string](/API_docs/types/string.html), from_version: [int](/API_docs/types/int.html), \]) === [$EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.html)<a name="messages.getEmojiKeywordsDifference"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsLanguages](/API_docs/methods/messages.getEmojiKeywordsLanguages.html)(\[lang_codes: \[[string](/API_docs/types/string.html)\], \]) === [$Vector\_of\_EmojiLanguage](/API_docs/types/EmojiLanguage.html)<a name="messages.getEmojiKeywordsLanguages"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiURL](/API_docs/methods/messages.getEmojiURL.html)(\[lang_code: [string](/API_docs/types/string.html), \]) === [$EmojiURL](/API_docs/types/EmojiURL.html)<a name="messages.getEmojiURL"></a>  

***
<br><br>
$MadelineProto->[messages->getExportedChatInvite](/API_docs/methods/messages.getExportedChatInvite.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), link: [string](/API_docs/types/string.html), \]) === [$messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)<a name="messages.getExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->getExportedChatInvites](/API_docs/methods/messages.getExportedChatInvites.html)(\[revoked: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), admin_id: [InputUser](/API_docs/types/InputUser.html), offset_date: [int](/API_docs/types/int.html), offset_link: [string](/API_docs/types/string.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.html)<a name="messages.getExportedChatInvites"></a>  

***
<br><br>
$MadelineProto->[messages->getFavedStickers](/API_docs/methods/messages.getFavedStickers.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$messages.FavedStickers](/API_docs/types/messages.FavedStickers.html)<a name="messages.getFavedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFeaturedStickers](/API_docs/methods/messages.getFeaturedStickers.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.html)<a name="messages.getFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFullChat](/API_docs/methods/messages.getFullChat.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.ChatFull](/API_docs/types/messages.ChatFull.html)<a name="messages.getFullChat"></a>  

***
<br><br>
$MadelineProto->[messages->getGameHighScores](/API_docs/methods/messages.getGameHighScores.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$messages.HighScores](/API_docs/types/messages.HighScores.html)<a name="messages.getGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getHistory](/API_docs/methods/messages.getHistory.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), offset_id: [int](/API_docs/types/int.html), offset_date: [int](/API_docs/types/int.html), add_offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), max_id: [int](/API_docs/types/int.html), min_id: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineBotResults](/API_docs/methods/messages.getInlineBotResults.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), peer: [InputPeer](/API_docs/types/InputPeer.html), geo_point: [InputGeoPoint](/API_docs/types/InputGeoPoint.html), query: [string](/API_docs/types/string.html), offset: [string](/API_docs/types/string.html), \]) === [$messages.BotResults](/API_docs/types/messages.BotResults.html)<a name="messages.getInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineGameHighScores](/API_docs/methods/messages.getInlineGameHighScores.html)(\[id: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$messages.HighScores](/API_docs/types/messages.HighScores.html)<a name="messages.getInlineGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getMaskStickers](/API_docs/methods/messages.getMaskStickers.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$messages.AllStickers](/API_docs/types/messages.AllStickers.html)<a name="messages.getMaskStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageEditData](/API_docs/methods/messages.getMessageEditData.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), \]) === [$messages.MessageEditData](/API_docs/types/messages.MessageEditData.html)<a name="messages.getMessageEditData"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageReactionsList](/API_docs/methods/messages.getMessageReactionsList.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), reaction: [string](/API_docs/types/string.html), offset: [string](/API_docs/types/string.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.MessageReactionsList](/API_docs/types/messages.MessageReactionsList.html)<a name="messages.getMessageReactionsList"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageReadParticipants](/API_docs/methods/messages.getMessageReadParticipants.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), \]) === [$Vector\_of\_long](/API_docs/types/long.html)<a name="messages.getMessageReadParticipants"></a>  

***
<br><br>
$MadelineProto->[messages->getMessages](/API_docs/methods/messages.getMessages.html)(\[id: \[[InputMessage](/API_docs/types/InputMessage.html)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getMessagesReactions](/API_docs/methods/messages.getMessagesReactions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.getMessagesReactions"></a>  

***
<br><br>
$MadelineProto->[messages->getMessagesViews](/API_docs/methods/messages.getMessagesViews.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], increment: [Bool](/API_docs/types/Bool.html), \]) === [$messages.MessageViews](/API_docs/types/messages.MessageViews.html)<a name="messages.getMessagesViews"></a>  

***
<br><br>
$MadelineProto->[messages->getOldFeaturedStickers](/API_docs/methods/messages.getOldFeaturedStickers.html)(\[offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.html)<a name="messages.getOldFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getOnlines](/API_docs/methods/messages.getOnlines.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$ChatOnlines](/API_docs/types/ChatOnlines.html)<a name="messages.getOnlines"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerDialogs](/API_docs/methods/messages.getPeerDialogs.html)(\[peers: \[[InputDialogPeer](/API_docs/types/InputDialogPeer.html)\], \]) === [$messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.html)<a name="messages.getPeerDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerSettings](/API_docs/methods/messages.getPeerSettings.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.PeerSettings](/API_docs/types/messages.PeerSettings.html)<a name="messages.getPeerSettings"></a>  

***
<br><br>
$MadelineProto->[messages->getPinnedDialogs](/API_docs/methods/messages.getPinnedDialogs.html)(\[folder_id: [int](/API_docs/types/int.html), \]) === [$messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.html)<a name="messages.getPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPollResults](/API_docs/methods/messages.getPollResults.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.getPollResults"></a>  

***
<br><br>
$MadelineProto->[messages->getPollVotes](/API_docs/methods/messages.getPollVotes.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), option: [bytes](/API_docs/types/bytes.html), offset: [string](/API_docs/types/string.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.VotesList](/API_docs/types/messages.VotesList.html)<a name="messages.getPollVotes"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentLocations](/API_docs/methods/messages.getRecentLocations.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), limit: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getRecentLocations"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentStickers](/API_docs/methods/messages.getRecentStickers.html)(\[attached: [Bool](/API_docs/types/Bool.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.RecentStickers](/API_docs/types/messages.RecentStickers.html)<a name="messages.getRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getReplies](/API_docs/methods/messages.getReplies.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), offset_id: [int](/API_docs/types/int.html), offset_date: [int](/API_docs/types/int.html), add_offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), max_id: [int](/API_docs/types/int.html), min_id: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getReplies"></a>  

***
<br><br>
$MadelineProto->[messages->getSavedGifs](/API_docs/methods/messages.getSavedGifs.html)(\[hash: [long](/API_docs/types/long.html), \]) === [$messages.SavedGifs](/API_docs/types/messages.SavedGifs.html)<a name="messages.getSavedGifs"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledHistory](/API_docs/methods/messages.getScheduledHistory.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getScheduledHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledMessages](/API_docs/methods/messages.getScheduledMessages.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchCounters](/API_docs/methods/messages.getSearchCounters.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), filters: \[[MessagesFilter](/API_docs/types/MessagesFilter.html)\], \]) === [$Vector\_of\_messages.SearchCounter](/API_docs/types/messages.SearchCounter.html)<a name="messages.getSearchCounters"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchResultsCalendar](/API_docs/methods/messages.getSearchResultsCalendar.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), filter: [MessagesFilter](/API_docs/types/MessagesFilter.html), offset_id: [int](/API_docs/types/int.html), offset_date: [int](/API_docs/types/int.html), \]) === [$messages.SearchResultsCalendar](/API_docs/types/messages.SearchResultsCalendar.html)<a name="messages.getSearchResultsCalendar"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchResultsPositions](/API_docs/methods/messages.getSearchResultsPositions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), filter: [MessagesFilter](/API_docs/types/MessagesFilter.html), offset_id: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.SearchResultsPositions](/API_docs/types/messages.SearchResultsPositions.html)<a name="messages.getSearchResultsPositions"></a>  

***
<br><br>
$MadelineProto->[messages->getSplitRanges](/API_docs/methods/messages.getSplitRanges.html)(\[\]) === [$Vector\_of\_MessageRange](/API_docs/types/MessageRange.html)<a name="messages.getSplitRanges"></a>  

***
<br><br>
$MadelineProto->[messages->getStickerSet](/API_docs/methods/messages.getStickerSet.html)(\[stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), hash: [int](/API_docs/types/int.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="messages.getStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->getStickers](/API_docs/methods/messages.getStickers.html)(\[emoticon: [string](/API_docs/types/string.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Stickers](/API_docs/types/messages.Stickers.html)<a name="messages.getStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getSuggestedDialogFilters](/API_docs/methods/messages.getSuggestedDialogFilters.html)(\[\]) === [$Vector\_of\_DialogFilterSuggested](/API_docs/types/DialogFilterSuggested.html)<a name="messages.getSuggestedDialogFilters"></a>  

***
<br><br>
$MadelineProto->[messages->getUnreadMentions](/API_docs/methods/messages.getUnreadMentions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), offset_id: [int](/API_docs/types/int.html), add_offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), max_id: [int](/API_docs/types/int.html), min_id: [int](/API_docs/types/int.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getUnreadMentions"></a>  

***
<br><br>
$MadelineProto->[messages->getUnreadReactions](/API_docs/methods/messages.getUnreadReactions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), offset_id: [int](/API_docs/types/int.html), add_offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), max_id: [int](/API_docs/types/int.html), min_id: [int](/API_docs/types/int.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.getUnreadReactions"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPage](/API_docs/methods/messages.getWebPage.html)(\[url: [string](/API_docs/types/string.html), hash: [int](/API_docs/types/int.html), \]) === [$WebPage](/API_docs/types/WebPage.html)<a name="messages.getWebPage"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPagePreview](/API_docs/methods/messages.getWebPagePreview.html)(\[message: [string](/API_docs/types/string.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \]) === [$MessageMedia](/API_docs/types/MessageMedia.html)<a name="messages.getWebPagePreview"></a>  

***
<br><br>
$MadelineProto->[messages->hideAllChatJoinRequests](/API_docs/methods/messages.hideAllChatJoinRequests.html)(\[approved: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), link: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.hideAllChatJoinRequests"></a>  

***
<br><br>
$MadelineProto->[messages->hideChatJoinRequest](/API_docs/methods/messages.hideChatJoinRequest.html)(\[approved: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), user_id: [InputUser](/API_docs/types/InputUser.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.hideChatJoinRequest"></a>  

***
<br><br>
$MadelineProto->[messages->hidePeerSettingsBar](/API_docs/methods/messages.hidePeerSettingsBar.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.hidePeerSettingsBar"></a>  

***
<br><br>
$MadelineProto->[messages->importChatInvite](/API_docs/methods/messages.importChatInvite.html)(\[hash: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.importChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->initHistoryImport](/API_docs/methods/messages.initHistoryImport.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), file: [InputFile](/API_docs/types/InputFile.html), media_count: [int](/API_docs/types/int.html), \]) === [$messages.HistoryImport](/API_docs/types/messages.HistoryImport.html)<a name="messages.initHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->installStickerSet](/API_docs/methods/messages.installStickerSet.html)(\[stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), archived: [Bool](/API_docs/types/Bool.html), \]) === [$messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.html)<a name="messages.installStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->markDialogUnread](/API_docs/methods/messages.markDialogUnread.html)(\[unread: [Bool](/API_docs/types/Bool.html), peer: [InputDialogPeer](/API_docs/types/InputDialogPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.markDialogUnread"></a>  

***
<br><br>
$MadelineProto->[messages->migrateChat](/API_docs/methods/messages.migrateChat.html)(\[chat_id: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.migrateChat"></a>  

***
<br><br>
$MadelineProto->[messages->prolongWebView](/API_docs/methods/messages.prolongWebView.html)(\[silent: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), bot: [InputUser](/API_docs/types/InputUser.html), query_id: [long](/API_docs/types/long.html), reply_to_msg_id: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.prolongWebView"></a>  

***
<br><br>
$MadelineProto->[messages->rateTranscribedAudio](/API_docs/methods/messages.rateTranscribedAudio.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), transcription_id: [long](/API_docs/types/long.html), good: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.rateTranscribedAudio"></a>  

***
<br><br>
$MadelineProto->[messages->readDiscussion](/API_docs/methods/messages.readDiscussion.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), read_max_id: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.readDiscussion"></a>  

***
<br><br>
$MadelineProto->[messages->readEncryptedHistory](/API_docs/methods/messages.readEncryptedHistory.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), max_date: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.readEncryptedHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readFeaturedStickers](/API_docs/methods/messages.readFeaturedStickers.html)(\[id: \[[long](/API_docs/types/long.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.readFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->readHistory](/API_docs/methods/messages.readHistory.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), max_id: [int](/API_docs/types/int.html), \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)<a name="messages.readHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readMentions](/API_docs/methods/messages.readMentions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)<a name="messages.readMentions"></a>  

***
<br><br>
$MadelineProto->[messages->readMessageContents](/API_docs/methods/messages.readMessageContents.html)(\[id: \[[int](/API_docs/types/int.html)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)<a name="messages.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[messages->readReactions](/API_docs/methods/messages.readReactions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)<a name="messages.readReactions"></a>  

***
<br><br>
$MadelineProto->[messages->receivedMessages](/API_docs/methods/messages.receivedMessages.html)(\[max_id: [int](/API_docs/types/int.html), \]) === [$Vector\_of\_ReceivedNotifyMessage](/API_docs/types/ReceivedNotifyMessage.html)<a name="messages.receivedMessages"></a>  

***
<br><br>
$MadelineProto->[messages->receivedQueue](/API_docs/methods/messages.receivedQueue.html)(\[max_qts: [int](/API_docs/types/int.html), \]) === [$Vector\_of\_long](/API_docs/types/long.html)<a name="messages.receivedQueue"></a>  

***
<br><br>
$MadelineProto->[messages->reorderPinnedDialogs](/API_docs/methods/messages.reorderPinnedDialogs.html)(\[force: [Bool](/API_docs/types/Bool.html), folder_id: [int](/API_docs/types/int.html), order: \[[InputDialogPeer](/API_docs/types/InputDialogPeer.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.reorderPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->reorderStickerSets](/API_docs/methods/messages.reorderStickerSets.html)(\[masks: [Bool](/API_docs/types/Bool.html), order: \[[long](/API_docs/types/long.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.reorderStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->report](/API_docs/methods/messages.report.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], reason: [ReportReason](/API_docs/types/ReportReason.html), message: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.report"></a>  

***
<br><br>
$MadelineProto->[messages->reportEncryptedSpam](/API_docs/methods/messages.reportEncryptedSpam.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.reportEncryptedSpam"></a>  

***
<br><br>
$MadelineProto->[messages->reportSpam](/API_docs/methods/messages.reportSpam.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.reportSpam"></a>  

***
<br><br>
$MadelineProto->[messages->requestEncryption](/API_docs/methods/messages.requestEncryption.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), g_a: [bytes](/API_docs/types/bytes.html), \]) === [$EncryptedChat](/API_docs/types/EncryptedChat.html)<a name="messages.requestEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->requestSimpleWebView](/API_docs/methods/messages.requestSimpleWebView.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), url: [string](/API_docs/types/string.html), theme_params: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$SimpleWebViewResult](/API_docs/types/SimpleWebViewResult.html)<a name="messages.requestSimpleWebView"></a>  

***
<br><br>
$MadelineProto->[messages->requestUrlAuth](/API_docs/methods/messages.requestUrlAuth.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), button_id: [int](/API_docs/types/int.html), url: [string](/API_docs/types/string.html), \]) === [$UrlAuthResult](/API_docs/types/UrlAuthResult.html)<a name="messages.requestUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->requestWebView](/API_docs/methods/messages.requestWebView.html)(\[from_bot_menu: [Bool](/API_docs/types/Bool.html), silent: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), bot: [InputUser](/API_docs/types/InputUser.html), url: [string](/API_docs/types/string.html), start_param: [string](/API_docs/types/string.html), theme_params: [DataJSON](/API_docs/types/DataJSON.html), reply_to_msg_id: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$WebViewResult](/API_docs/types/WebViewResult.html)<a name="messages.requestWebView"></a>  

***
<br><br>
$MadelineProto->[messages->saveDefaultSendAs](/API_docs/methods/messages.saveDefaultSendAs.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.saveDefaultSendAs"></a>  

***
<br><br>
$MadelineProto->[messages->saveDraft](/API_docs/methods/messages.saveDraft.html)(\[no_webpage: [Bool](/API_docs/types/Bool.html), reply_to_msg_id: [int](/API_docs/types/int.html), peer: [InputPeer](/API_docs/types/InputPeer.html), message: [string](/API_docs/types/string.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.saveDraft"></a>  

***
<br><br>
$MadelineProto->[messages->saveGif](/API_docs/methods/messages.saveGif.html)(\[id: [InputDocument](/API_docs/types/InputDocument.html), unsave: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.saveGif"></a>  

***
<br><br>
$MadelineProto->[messages->saveRecentSticker](/API_docs/methods/messages.saveRecentSticker.html)(\[attached: [Bool](/API_docs/types/Bool.html), id: [InputDocument](/API_docs/types/InputDocument.html), unsave: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.saveRecentSticker"></a>  

***
<br><br>
$MadelineProto->[messages->search](/API_docs/methods/messages.search.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), q: [string](/API_docs/types/string.html), from_id: [InputPeer](/API_docs/types/InputPeer.html), top_msg_id: [int](/API_docs/types/int.html), filter: [MessagesFilter](/API_docs/types/MessagesFilter.html), min_date: [int](/API_docs/types/int.html), max_date: [int](/API_docs/types/int.html), offset_id: [int](/API_docs/types/int.html), add_offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), max_id: [int](/API_docs/types/int.html), min_id: [int](/API_docs/types/int.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.search"></a>  

***
<br><br>
$MadelineProto->[messages->searchGlobal](/API_docs/methods/messages.searchGlobal.html)(\[folder_id: [int](/API_docs/types/int.html), q: [string](/API_docs/types/string.html), filter: [MessagesFilter](/API_docs/types/MessagesFilter.html), min_date: [int](/API_docs/types/int.html), max_date: [int](/API_docs/types/int.html), offset_rate: [int](/API_docs/types/int.html), offset_peer: [InputPeer](/API_docs/types/InputPeer.html), offset_id: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.searchGlobal"></a>  

***
<br><br>
$MadelineProto->[messages->searchSentMedia](/API_docs/methods/messages.searchSentMedia.html)(\[q: [string](/API_docs/types/string.html), filter: [MessagesFilter](/API_docs/types/MessagesFilter.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="messages.searchSentMedia"></a>  

***
<br><br>
$MadelineProto->[messages->searchStickerSets](/API_docs/methods/messages.searchStickerSets.html)(\[exclude_featured: [Bool](/API_docs/types/Bool.html), q: [string](/API_docs/types/string.html), hash: [long](/API_docs/types/long.html), \]) === [$messages.FoundStickerSets](/API_docs/types/messages.FoundStickerSets.html)<a name="messages.searchStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncrypted](/API_docs/methods/messages.sendEncrypted.html)(\[silent: [Bool](/API_docs/types/Bool.html), peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), data: [bytes](/API_docs/types/bytes.html), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.html)<a name="messages.sendEncrypted"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedFile](/API_docs/methods/messages.sendEncryptedFile.html)(\[silent: [Bool](/API_docs/types/Bool.html), peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), data: [bytes](/API_docs/types/bytes.html), file: [InputEncryptedFile](/API_docs/types/InputEncryptedFile.html), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.html)<a name="messages.sendEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedService](/API_docs/methods/messages.sendEncryptedService.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), data: [bytes](/API_docs/types/bytes.html), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.html)<a name="messages.sendEncryptedService"></a>  

***
<br><br>
$MadelineProto->[messages->sendInlineBotResult](/API_docs/methods/messages.sendInlineBotResult.html)(\[silent: [Bool](/API_docs/types/Bool.html), background: [Bool](/API_docs/types/Bool.html), clear_draft: [Bool](/API_docs/types/Bool.html), hide_via: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), reply_to_msg_id: [int](/API_docs/types/int.html), query_id: [long](/API_docs/types/long.html), id: [string](/API_docs/types/string.html), schedule_date: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendInlineBotResult"></a>  

***
<br><br>
$MadelineProto->[messages->sendMedia](/API_docs/methods/messages.sendMedia.html)(\[silent: [Bool](/API_docs/types/Bool.html), background: [Bool](/API_docs/types/Bool.html), clear_draft: [Bool](/API_docs/types/Bool.html), noforwards: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), reply_to_msg_id: [int](/API_docs/types/int.html), media: [InputMedia](/API_docs/types/InputMedia.html), message: [string](/API_docs/types/string.html), reply_markup: [ReplyMarkup](/API_docs/types/ReplyMarkup.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], schedule_date: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendMessage](/API_docs/methods/messages.sendMessage.html)(\[no_webpage: [Bool](/API_docs/types/Bool.html), silent: [Bool](/API_docs/types/Bool.html), background: [Bool](/API_docs/types/Bool.html), clear_draft: [Bool](/API_docs/types/Bool.html), noforwards: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), reply_to_msg_id: [int](/API_docs/types/int.html), message: [string](/API_docs/types/string.html), reply_markup: [ReplyMarkup](/API_docs/types/ReplyMarkup.html), entities: \[[MessageEntity](/API_docs/types/MessageEntity.html)\], schedule_date: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendMessage"></a>  

***
<br><br>
$MadelineProto->[messages->sendMultiMedia](/API_docs/methods/messages.sendMultiMedia.html)(\[silent: [Bool](/API_docs/types/Bool.html), background: [Bool](/API_docs/types/Bool.html), clear_draft: [Bool](/API_docs/types/Bool.html), noforwards: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), reply_to_msg_id: [int](/API_docs/types/int.html), multi_media: \[[InputSingleMedia](/API_docs/types/InputSingleMedia.html)\], schedule_date: [int](/API_docs/types/int.html), send_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendMultiMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendReaction](/API_docs/methods/messages.sendReaction.html)(\[big: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), reaction: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendReaction"></a>  

***
<br><br>
$MadelineProto->[messages->sendScheduledMessages](/API_docs/methods/messages.sendScheduledMessages.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), id: \[[int](/API_docs/types/int.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->sendScreenshotNotification](/API_docs/methods/messages.sendScreenshotNotification.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), reply_to_msg_id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendScreenshotNotification"></a>  

***
<br><br>
$MadelineProto->[messages->sendVote](/API_docs/methods/messages.sendVote.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), options: \[[bytes](/API_docs/types/bytes.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendVote"></a>  

***
<br><br>
$MadelineProto->[messages->sendWebViewData](/API_docs/methods/messages.sendWebViewData.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), button_text: [string](/API_docs/types/string.html), data: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.sendWebViewData"></a>  

***
<br><br>
$MadelineProto->[messages->sendWebViewResultMessage](/API_docs/methods/messages.sendWebViewResultMessage.html)(\[bot_query_id: [string](/API_docs/types/string.html), result: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.html), \]) === [$WebViewMessageSent](/API_docs/types/WebViewMessageSent.html)<a name="messages.sendWebViewResultMessage"></a>  

***
<br><br>
$MadelineProto->[messages->setBotCallbackAnswer](/API_docs/methods/messages.setBotCallbackAnswer.html)(\[alert: [Bool](/API_docs/types/Bool.html), query_id: [long](/API_docs/types/long.html), message: [string](/API_docs/types/string.html), url: [string](/API_docs/types/string.html), cache_time: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->setBotPrecheckoutResults](/API_docs/methods/messages.setBotPrecheckoutResults.html)(\[success: [Bool](/API_docs/types/Bool.html), query_id: [long](/API_docs/types/long.html), error: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setBotPrecheckoutResults"></a>  

***
<br><br>
$MadelineProto->[messages->setBotShippingResults](/API_docs/methods/messages.setBotShippingResults.html)(\[query_id: [long](/API_docs/types/long.html), error: [string](/API_docs/types/string.html), shipping_options: \[[ShippingOption](/API_docs/types/ShippingOption.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setBotShippingResults"></a>  

***
<br><br>
$MadelineProto->[messages->setChatAvailableReactions](/API_docs/methods/messages.setChatAvailableReactions.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), available_reactions: \[[string](/API_docs/types/string.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.setChatAvailableReactions"></a>  

***
<br><br>
$MadelineProto->[messages->setChatTheme](/API_docs/methods/messages.setChatTheme.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), emoticon: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.setChatTheme"></a>  

***
<br><br>
$MadelineProto->[messages->setDefaultReaction](/API_docs/methods/messages.setDefaultReaction.html)(\[reaction: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setDefaultReaction"></a>  

***
<br><br>
$MadelineProto->[messages->setEncryptedTyping](/API_docs/methods/messages.setEncryptedTyping.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), typing: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setEncryptedTyping"></a>  

***
<br><br>
$MadelineProto->[messages->setGameScore](/API_docs/methods/messages.setGameScore.html)(\[edit_message: [Bool](/API_docs/types/Bool.html), force: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), user_id: [InputUser](/API_docs/types/InputUser.html), score: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.setGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setHistoryTTL](/API_docs/methods/messages.setHistoryTTL.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), period: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.setHistoryTTL"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineBotResults](/API_docs/methods/messages.setInlineBotResults.html)(\[gallery: [Bool](/API_docs/types/Bool.html), private: [Bool](/API_docs/types/Bool.html), query_id: [long](/API_docs/types/long.html), results: \[[InputBotInlineResult](/API_docs/types/InputBotInlineResult.html)\], cache_time: [int](/API_docs/types/int.html), next_offset: [string](/API_docs/types/string.html), switch_pm: [InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineGameScore](/API_docs/methods/messages.setInlineGameScore.html)(\[edit_message: [Bool](/API_docs/types/Bool.html), force: [Bool](/API_docs/types/Bool.html), id: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html), user_id: [InputUser](/API_docs/types/InputUser.html), score: [int](/API_docs/types/int.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setInlineGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setTyping](/API_docs/methods/messages.setTyping.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), top_msg_id: [int](/API_docs/types/int.html), action: [SendMessageAction](/API_docs/types/SendMessageAction.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.setTyping"></a>  

***
<br><br>
$MadelineProto->[messages->startBot](/API_docs/methods/messages.startBot.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), peer: [InputPeer](/API_docs/types/InputPeer.html), start_param: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.startBot"></a>  

***
<br><br>
$MadelineProto->[messages->startHistoryImport](/API_docs/methods/messages.startHistoryImport.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), import_id: [long](/API_docs/types/long.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.startHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->toggleBotInAttachMenu](/API_docs/methods/messages.toggleBotInAttachMenu.html)(\[bot: [InputUser](/API_docs/types/InputUser.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.toggleBotInAttachMenu"></a>  

***
<br><br>
$MadelineProto->[messages->toggleDialogPin](/API_docs/methods/messages.toggleDialogPin.html)(\[pinned: [Bool](/API_docs/types/Bool.html), peer: [InputDialogPeer](/API_docs/types/InputDialogPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.toggleDialogPin"></a>  

***
<br><br>
$MadelineProto->[messages->toggleNoForwards](/API_docs/methods/messages.toggleNoForwards.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), enabled: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.toggleNoForwards"></a>  

***
<br><br>
$MadelineProto->[messages->toggleStickerSets](/API_docs/methods/messages.toggleStickerSets.html)(\[uninstall: [Bool](/API_docs/types/Bool.html), archive: [Bool](/API_docs/types/Bool.html), unarchive: [Bool](/API_docs/types/Bool.html), stickersets: \[[InputStickerSet](/API_docs/types/InputStickerSet.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.toggleStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->transcribeAudio](/API_docs/methods/messages.transcribeAudio.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), \]) === [$messages.TranscribedAudio](/API_docs/types/messages.TranscribedAudio.html)<a name="messages.transcribeAudio"></a>  

***
<br><br>
$MadelineProto->[messages->translateText](/API_docs/methods/messages.translateText.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), text: [string](/API_docs/types/string.html), from_lang: [string](/API_docs/types/string.html), to_lang: [string](/API_docs/types/string.html), \]) === [$messages.TranslatedText](/API_docs/types/messages.TranslatedText.html)<a name="messages.translateText"></a>  

***
<br><br>
$MadelineProto->[messages->uninstallStickerSet](/API_docs/methods/messages.uninstallStickerSet.html)(\[stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.uninstallStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->unpinAllMessages](/API_docs/methods/messages.unpinAllMessages.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)<a name="messages.unpinAllMessages"></a>  

***
<br><br>
$MadelineProto->[messages->updateDialogFilter](/API_docs/methods/messages.updateDialogFilter.html)(\[id: [int](/API_docs/types/int.html), filter: [DialogFilter](/API_docs/types/DialogFilter.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.updateDialogFilter"></a>  

***
<br><br>
$MadelineProto->[messages->updateDialogFiltersOrder](/API_docs/methods/messages.updateDialogFiltersOrder.html)(\[order: \[[int](/API_docs/types/int.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="messages.updateDialogFiltersOrder"></a>  

***
<br><br>
$MadelineProto->[messages->updatePinnedMessage](/API_docs/methods/messages.updatePinnedMessage.html)(\[silent: [Bool](/API_docs/types/Bool.html), unpin: [Bool](/API_docs/types/Bool.html), pm_oneside: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), id: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="messages.updatePinnedMessage"></a>  

***
<br><br>
$MadelineProto->[messages->uploadEncryptedFile](/API_docs/methods/messages.uploadEncryptedFile.html)(\[peer: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html), file: [InputEncryptedFile](/API_docs/types/InputEncryptedFile.html), \]) === [$EncryptedFile](/API_docs/types/EncryptedFile.html)<a name="messages.uploadEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->uploadImportedMedia](/API_docs/methods/messages.uploadImportedMedia.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), import_id: [long](/API_docs/types/long.html), file_name: [string](/API_docs/types/string.html), media: [InputMedia](/API_docs/types/InputMedia.html), \]) === [$MessageMedia](/API_docs/types/MessageMedia.html)<a name="messages.uploadImportedMedia"></a>  

***
<br><br>
$MadelineProto->[messages->uploadMedia](/API_docs/methods/messages.uploadMedia.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), media: [InputMedia](/API_docs/types/InputMedia.html), \]) === [$MessageMedia](/API_docs/types/MessageMedia.html)<a name="messages.uploadMedia"></a>  

***
<br><br>
$MadelineProto->[payments->assignAppStoreTransaction](/API_docs/methods/payments.assignAppStoreTransaction.html)(\[restore: [Bool](/API_docs/types/Bool.html), transaction_id: [string](/API_docs/types/string.html), receipt: [bytes](/API_docs/types/bytes.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="payments.assignAppStoreTransaction"></a>  

***
<br><br>
$MadelineProto->[payments->assignPlayMarketTransaction](/API_docs/methods/payments.assignPlayMarketTransaction.html)(\[purchase_token: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="payments.assignPlayMarketTransaction"></a>  

***
<br><br>
$MadelineProto->[payments->canPurchasePremium](/API_docs/methods/payments.canPurchasePremium.html)(\[\]) === [$Bool](/API_docs/types/Bool.html)<a name="payments.canPurchasePremium"></a>  

***
<br><br>
$MadelineProto->[payments->clearSavedInfo](/API_docs/methods/payments.clearSavedInfo.html)(\[credentials: [Bool](/API_docs/types/Bool.html), info: [Bool](/API_docs/types/Bool.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="payments.clearSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->exportInvoice](/API_docs/methods/payments.exportInvoice.html)(\[invoice_media: [InputMedia](/API_docs/types/InputMedia.html), \]) === [$payments.ExportedInvoice](/API_docs/types/payments.ExportedInvoice.html)<a name="payments.exportInvoice"></a>  

***
<br><br>
$MadelineProto->[payments->getBankCardData](/API_docs/methods/payments.getBankCardData.html)(\[number: [string](/API_docs/types/string.html), \]) === [$payments.BankCardData](/API_docs/types/payments.BankCardData.html)<a name="payments.getBankCardData"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentForm](/API_docs/methods/payments.getPaymentForm.html)(\[invoice: [InputInvoice](/API_docs/types/InputInvoice.html), theme_params: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)<a name="payments.getPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentReceipt](/API_docs/methods/payments.getPaymentReceipt.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), msg_id: [int](/API_docs/types/int.html), \]) === [$payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.html)<a name="payments.getPaymentReceipt"></a>  

***
<br><br>
$MadelineProto->[payments->getSavedInfo](/API_docs/methods/payments.getSavedInfo.html)(\[\]) === [$payments.SavedInfo](/API_docs/types/payments.SavedInfo.html)<a name="payments.getSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->requestRecurringPayment](/API_docs/methods/payments.requestRecurringPayment.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), recurring_init_charge: [string](/API_docs/types/string.html), invoice_media: [InputMedia](/API_docs/types/InputMedia.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="payments.requestRecurringPayment"></a>  

***
<br><br>
$MadelineProto->[payments->restorePlayMarketReceipt](/API_docs/methods/payments.restorePlayMarketReceipt.html)(\[receipt: [bytes](/API_docs/types/bytes.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="payments.restorePlayMarketReceipt"></a>  

***
<br><br>
$MadelineProto->[payments->sendPaymentForm](/API_docs/methods/payments.sendPaymentForm.html)(\[form_id: [long](/API_docs/types/long.html), invoice: [InputInvoice](/API_docs/types/InputInvoice.html), requested_info_id: [string](/API_docs/types/string.html), shipping_option_id: [string](/API_docs/types/string.html), credentials: [InputPaymentCredentials](/API_docs/types/InputPaymentCredentials.html), tip_amount: [long](/API_docs/types/long.html), \]) === [$payments.PaymentResult](/API_docs/types/payments.PaymentResult.html)<a name="payments.sendPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->validateRequestedInfo](/API_docs/methods/payments.validateRequestedInfo.html)(\[save: [Bool](/API_docs/types/Bool.html), invoice: [InputInvoice](/API_docs/types/InputInvoice.html), info: [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html), \]) === [$payments.ValidatedRequestedInfo](/API_docs/types/payments.ValidatedRequestedInfo.html)<a name="payments.validateRequestedInfo"></a>  

***
<br><br>
$MadelineProto->[phone->acceptCall](/API_docs/methods/phone.acceptCall.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), g_b: [bytes](/API_docs/types/bytes.html), protocol: [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)<a name="phone.acceptCall"></a>  

***
<br><br>
$MadelineProto->[phone->checkGroupCall](/API_docs/methods/phone.checkGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), sources: \[[int](/API_docs/types/int.html)\], \]) === [$Vector\_of\_int](/API_docs/types/int.html)<a name="phone.checkGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->confirmCall](/API_docs/methods/phone.confirmCall.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), g_a: [bytes](/API_docs/types/bytes.html), key_fingerprint: [long](/API_docs/types/long.html), protocol: [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)<a name="phone.confirmCall"></a>  

***
<br><br>
$MadelineProto->[phone->createGroupCall](/API_docs/methods/phone.createGroupCall.html)(\[rtmp_stream: [Bool](/API_docs/types/Bool.html), peer: [InputPeer](/API_docs/types/InputPeer.html), title: [string](/API_docs/types/string.html), schedule_date: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.createGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->discardCall](/API_docs/methods/phone.discardCall.html)(\[video: [Bool](/API_docs/types/Bool.html), peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), duration: [int](/API_docs/types/int.html), reason: [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html), connection_id: [long](/API_docs/types/long.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.discardCall"></a>  

***
<br><br>
$MadelineProto->[phone->discardGroupCall](/API_docs/methods/phone.discardGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.discardGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->editGroupCallParticipant](/API_docs/methods/phone.editGroupCallParticipant.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), participant: [InputPeer](/API_docs/types/InputPeer.html), muted: [Bool](/API_docs/types/Bool.html), volume: [int](/API_docs/types/int.html), raise_hand: [Bool](/API_docs/types/Bool.html), video_stopped: [Bool](/API_docs/types/Bool.html), video_paused: [Bool](/API_docs/types/Bool.html), presentation_paused: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.editGroupCallParticipant"></a>  

***
<br><br>
$MadelineProto->[phone->editGroupCallTitle](/API_docs/methods/phone.editGroupCallTitle.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), title: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.editGroupCallTitle"></a>  

***
<br><br>
$MadelineProto->[phone->exportGroupCallInvite](/API_docs/methods/phone.exportGroupCallInvite.html)(\[can_self_unmute: [Bool](/API_docs/types/Bool.html), call: [InputGroupCall](/API_docs/types/InputGroupCall.html), \]) === [$phone.ExportedGroupCallInvite](/API_docs/types/phone.ExportedGroupCallInvite.html)<a name="phone.exportGroupCallInvite"></a>  

***
<br><br>
$MadelineProto->[phone->getCallConfig](/API_docs/methods/phone.getCallConfig.html)(\[\]) === [$DataJSON](/API_docs/types/DataJSON.html)<a name="phone.getCallConfig"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCall](/API_docs/methods/phone.getGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), limit: [int](/API_docs/types/int.html), \]) === [$phone.GroupCall](/API_docs/types/phone.GroupCall.html)<a name="phone.getGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCallJoinAs](/API_docs/methods/phone.getGroupCallJoinAs.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.html)<a name="phone.getGroupCallJoinAs"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCallStreamChannels](/API_docs/methods/phone.getGroupCallStreamChannels.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), \]) === [$phone.GroupCallStreamChannels](/API_docs/types/phone.GroupCallStreamChannels.html)<a name="phone.getGroupCallStreamChannels"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCallStreamRtmpUrl](/API_docs/methods/phone.getGroupCallStreamRtmpUrl.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), revoke: [Bool](/API_docs/types/Bool.html), \]) === [$phone.GroupCallStreamRtmpUrl](/API_docs/types/phone.GroupCallStreamRtmpUrl.html)<a name="phone.getGroupCallStreamRtmpUrl"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupParticipants](/API_docs/methods/phone.getGroupParticipants.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), ids: \[[InputPeer](/API_docs/types/InputPeer.html)\], sources: \[[int](/API_docs/types/int.html)\], offset: [string](/API_docs/types/string.html), limit: [int](/API_docs/types/int.html), \]) === [$phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.html)<a name="phone.getGroupParticipants"></a>  

***
<br><br>
$MadelineProto->[phone->inviteToGroupCall](/API_docs/methods/phone.inviteToGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), users: \[[InputUser](/API_docs/types/InputUser.html)\], \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.inviteToGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->joinGroupCall](/API_docs/methods/phone.joinGroupCall.html)(\[muted: [Bool](/API_docs/types/Bool.html), video_stopped: [Bool](/API_docs/types/Bool.html), call: [InputGroupCall](/API_docs/types/InputGroupCall.html), join_as: [InputPeer](/API_docs/types/InputPeer.html), invite_hash: [string](/API_docs/types/string.html), params: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.joinGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->joinGroupCallPresentation](/API_docs/methods/phone.joinGroupCallPresentation.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), params: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.joinGroupCallPresentation"></a>  

***
<br><br>
$MadelineProto->[phone->leaveGroupCall](/API_docs/methods/phone.leaveGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), source: [int](/API_docs/types/int.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.leaveGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->leaveGroupCallPresentation](/API_docs/methods/phone.leaveGroupCallPresentation.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.leaveGroupCallPresentation"></a>  

***
<br><br>
$MadelineProto->[phone->receivedCall](/API_docs/methods/phone.receivedCall.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="phone.receivedCall"></a>  

***
<br><br>
$MadelineProto->[phone->requestCall](/API_docs/methods/phone.requestCall.html)(\[video: [Bool](/API_docs/types/Bool.html), user_id: [InputUser](/API_docs/types/InputUser.html), g_a_hash: [bytes](/API_docs/types/bytes.html), protocol: [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.html)<a name="phone.requestCall"></a>  

***
<br><br>
$MadelineProto->[phone->saveCallDebug](/API_docs/methods/phone.saveCallDebug.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), debug: [DataJSON](/API_docs/types/DataJSON.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="phone.saveCallDebug"></a>  

***
<br><br>
$MadelineProto->[phone->saveCallLog](/API_docs/methods/phone.saveCallLog.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), file: [InputFile](/API_docs/types/InputFile.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="phone.saveCallLog"></a>  

***
<br><br>
$MadelineProto->[phone->saveDefaultGroupCallJoinAs](/API_docs/methods/phone.saveDefaultGroupCallJoinAs.html)(\[peer: [InputPeer](/API_docs/types/InputPeer.html), join_as: [InputPeer](/API_docs/types/InputPeer.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="phone.saveDefaultGroupCallJoinAs"></a>  

***
<br><br>
$MadelineProto->[phone->sendSignalingData](/API_docs/methods/phone.sendSignalingData.html)(\[peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), data: [bytes](/API_docs/types/bytes.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="phone.sendSignalingData"></a>  

***
<br><br>
$MadelineProto->[phone->setCallRating](/API_docs/methods/phone.setCallRating.html)(\[user_initiative: [Bool](/API_docs/types/Bool.html), peer: [InputPhoneCall](/API_docs/types/InputPhoneCall.html), rating: [int](/API_docs/types/int.html), comment: [string](/API_docs/types/string.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.setCallRating"></a>  

***
<br><br>
$MadelineProto->[phone->startScheduledGroupCall](/API_docs/methods/phone.startScheduledGroupCall.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.startScheduledGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallRecord](/API_docs/methods/phone.toggleGroupCallRecord.html)(\[start: [Bool](/API_docs/types/Bool.html), video: [Bool](/API_docs/types/Bool.html), call: [InputGroupCall](/API_docs/types/InputGroupCall.html), title: [string](/API_docs/types/string.html), video_portrait: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.toggleGroupCallRecord"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallSettings](/API_docs/methods/phone.toggleGroupCallSettings.html)(\[reset_invite_hash: [Bool](/API_docs/types/Bool.html), call: [InputGroupCall](/API_docs/types/InputGroupCall.html), join_muted: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.toggleGroupCallSettings"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallStartSubscription](/API_docs/methods/phone.toggleGroupCallStartSubscription.html)(\[call: [InputGroupCall](/API_docs/types/InputGroupCall.html), subscribed: [Bool](/API_docs/types/Bool.html), \]) === [$Updates](/API_docs/types/Updates.html)<a name="phone.toggleGroupCallStartSubscription"></a>  

***
<br><br>
$MadelineProto->[photos->deletePhotos](/API_docs/methods/photos.deletePhotos.html)(\[id: \[[InputPhoto](/API_docs/types/InputPhoto.html)\], \]) === [$Vector\_of\_long](/API_docs/types/long.html)<a name="photos.deletePhotos"></a>  

***
<br><br>
$MadelineProto->[photos->getUserPhotos](/API_docs/methods/photos.getUserPhotos.html)(\[user_id: [InputUser](/API_docs/types/InputUser.html), offset: [int](/API_docs/types/int.html), max_id: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$photos.Photos](/API_docs/types/photos.Photos.html)<a name="photos.getUserPhotos"></a>  

***
<br><br>
$MadelineProto->[photos->updateProfilePhoto](/API_docs/methods/photos.updateProfilePhoto.html)(\[id: [InputPhoto](/API_docs/types/InputPhoto.html), \]) === [$photos.Photo](/API_docs/types/photos.Photo.html)<a name="photos.updateProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[photos->uploadProfilePhoto](/API_docs/methods/photos.uploadProfilePhoto.html)(\[file: [InputFile](/API_docs/types/InputFile.html), video: [InputFile](/API_docs/types/InputFile.html), video_start_ts: [double](/API_docs/types/double.html), \]) === [$photos.Photo](/API_docs/types/photos.Photo.html)<a name="photos.uploadProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[stats->getBroadcastStats](/API_docs/methods/stats.getBroadcastStats.html)(\[dark: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$stats.BroadcastStats](/API_docs/types/stats.BroadcastStats.html)<a name="stats.getBroadcastStats"></a>  

***
<br><br>
$MadelineProto->[stats->getMegagroupStats](/API_docs/methods/stats.getMegagroupStats.html)(\[dark: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), \]) === [$stats.MegagroupStats](/API_docs/types/stats.MegagroupStats.html)<a name="stats.getMegagroupStats"></a>  

***
<br><br>
$MadelineProto->[stats->getMessagePublicForwards](/API_docs/methods/stats.getMessagePublicForwards.html)(\[channel: [InputChannel](/API_docs/types/InputChannel.html), msg_id: [int](/API_docs/types/int.html), offset_rate: [int](/API_docs/types/int.html), offset_peer: [InputPeer](/API_docs/types/InputPeer.html), offset_id: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$messages.Messages](/API_docs/types/messages.Messages.html)<a name="stats.getMessagePublicForwards"></a>  

***
<br><br>
$MadelineProto->[stats->getMessageStats](/API_docs/methods/stats.getMessageStats.html)(\[dark: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), msg_id: [int](/API_docs/types/int.html), \]) === [$stats.MessageStats](/API_docs/types/stats.MessageStats.html)<a name="stats.getMessageStats"></a>  

***
<br><br>
$MadelineProto->[stats->loadAsyncGraph](/API_docs/methods/stats.loadAsyncGraph.html)(\[token: [string](/API_docs/types/string.html), x: [long](/API_docs/types/long.html), \]) === [$StatsGraph](/API_docs/types/StatsGraph.html)<a name="stats.loadAsyncGraph"></a>  

***
<br><br>
$MadelineProto->[stickers->addStickerToSet](/API_docs/methods/stickers.addStickerToSet.html)(\[stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), sticker: [InputStickerSetItem](/API_docs/types/InputStickerSetItem.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="stickers.addStickerToSet"></a>  

***
<br><br>
$MadelineProto->[stickers->changeStickerPosition](/API_docs/methods/stickers.changeStickerPosition.html)(\[sticker: [InputDocument](/API_docs/types/InputDocument.html), position: [int](/API_docs/types/int.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="stickers.changeStickerPosition"></a>  

***
<br><br>
$MadelineProto->[stickers->checkShortName](/API_docs/methods/stickers.checkShortName.html)(\[short_name: [string](/API_docs/types/string.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="stickers.checkShortName"></a>  

***
<br><br>
$MadelineProto->[stickers->createStickerSet](/API_docs/methods/stickers.createStickerSet.html)(\[masks: [Bool](/API_docs/types/Bool.html), animated: [Bool](/API_docs/types/Bool.html), videos: [Bool](/API_docs/types/Bool.html), user_id: [InputUser](/API_docs/types/InputUser.html), title: [string](/API_docs/types/string.html), short_name: [string](/API_docs/types/string.html), thumb: [InputDocument](/API_docs/types/InputDocument.html), stickers: \[[InputStickerSetItem](/API_docs/types/InputStickerSetItem.html)\], software: [string](/API_docs/types/string.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="stickers.createStickerSet"></a>  

***
<br><br>
$MadelineProto->[stickers->removeStickerFromSet](/API_docs/methods/stickers.removeStickerFromSet.html)(\[sticker: [InputDocument](/API_docs/types/InputDocument.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="stickers.removeStickerFromSet"></a>  

***
<br><br>
$MadelineProto->[stickers->setStickerSetThumb](/API_docs/methods/stickers.setStickerSetThumb.html)(\[stickerset: [InputStickerSet](/API_docs/types/InputStickerSet.html), thumb: [InputDocument](/API_docs/types/InputDocument.html), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.html)<a name="stickers.setStickerSetThumb"></a>  

***
<br><br>
$MadelineProto->[stickers->suggestShortName](/API_docs/methods/stickers.suggestShortName.html)(\[title: [string](/API_docs/types/string.html), \]) === [$stickers.SuggestedShortName](/API_docs/types/stickers.SuggestedShortName.html)<a name="stickers.suggestShortName"></a>  

***
<br><br>
$MadelineProto->[updates->getChannelDifference](/API_docs/methods/updates.getChannelDifference.html)(\[force: [Bool](/API_docs/types/Bool.html), channel: [InputChannel](/API_docs/types/InputChannel.html), filter: [ChannelMessagesFilter](/API_docs/types/ChannelMessagesFilter.html), pts: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)<a name="updates.getChannelDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getDifference](/API_docs/methods/updates.getDifference.html)(\[pts: [int](/API_docs/types/int.html), pts_total_limit: [int](/API_docs/types/int.html), date: [int](/API_docs/types/int.html), qts: [int](/API_docs/types/int.html), \]) === [$updates.Difference](/API_docs/types/updates.Difference.html)<a name="updates.getDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getState](/API_docs/methods/updates.getState.html)(\[\]) === [$updates.State](/API_docs/types/updates.State.html)<a name="updates.getState"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFile](/API_docs/methods/upload.getCdnFile.html)(\[file_token: [bytes](/API_docs/types/bytes.html), offset: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$upload.CdnFile](/API_docs/types/upload.CdnFile.html)<a name="upload.getCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFileHashes](/API_docs/methods/upload.getCdnFileHashes.html)(\[file_token: [bytes](/API_docs/types/bytes.html), offset: [long](/API_docs/types/long.html), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.html)<a name="upload.getCdnFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getFile](/API_docs/methods/upload.getFile.html)(\[precise: [Bool](/API_docs/types/Bool.html), cdn_supported: [Bool](/API_docs/types/Bool.html), location: [InputFileLocation](/API_docs/types/InputFileLocation.html), offset: [long](/API_docs/types/long.html), limit: [int](/API_docs/types/int.html), \]) === [$upload.File](/API_docs/types/upload.File.html)<a name="upload.getFile"></a>  

***
<br><br>
$MadelineProto->[upload->getFileHashes](/API_docs/methods/upload.getFileHashes.html)(\[location: [InputFileLocation](/API_docs/types/InputFileLocation.html), offset: [long](/API_docs/types/long.html), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.html)<a name="upload.getFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getWebFile](/API_docs/methods/upload.getWebFile.html)(\[location: [InputWebFileLocation](/API_docs/types/InputWebFileLocation.html), offset: [int](/API_docs/types/int.html), limit: [int](/API_docs/types/int.html), \]) === [$upload.WebFile](/API_docs/types/upload.WebFile.html)<a name="upload.getWebFile"></a>  

***
<br><br>
$MadelineProto->[upload->reuploadCdnFile](/API_docs/methods/upload.reuploadCdnFile.html)(\[file_token: [bytes](/API_docs/types/bytes.html), request_token: [bytes](/API_docs/types/bytes.html), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.html)<a name="upload.reuploadCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->saveBigFilePart](/API_docs/methods/upload.saveBigFilePart.html)(\[file_id: [long](/API_docs/types/long.html), file_part: [int](/API_docs/types/int.html), file_total_parts: [int](/API_docs/types/int.html), bytes: [bytes](/API_docs/types/bytes.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="upload.saveBigFilePart"></a>  

***
<br><br>
$MadelineProto->[upload->saveFilePart](/API_docs/methods/upload.saveFilePart.html)(\[file_id: [long](/API_docs/types/long.html), file_part: [int](/API_docs/types/int.html), bytes: [bytes](/API_docs/types/bytes.html), \]) === [$Bool](/API_docs/types/Bool.html)<a name="upload.saveFilePart"></a>  

***
<br><br>
$MadelineProto->[users->getFullUser](/API_docs/methods/users.getFullUser.html)(\[id: [InputUser](/API_docs/types/InputUser.html), \]) === [$users.UserFull](/API_docs/types/users.UserFull.html)<a name="users.getFullUser"></a>  

***
<br><br>
$MadelineProto->[users->getUsers](/API_docs/methods/users.getUsers.html)(\[id: \[[InputUser](/API_docs/types/InputUser.html)\], \]) === [$Vector\_of\_User](/API_docs/types/User.html)<a name="users.getUsers"></a>  

***
<br><br>
$MadelineProto->[users->setSecureValueErrors](/API_docs/methods/users.setSecureValueErrors.html)(\[id: [InputUser](/API_docs/types/InputUser.html), errors: \[[SecureValueError](/API_docs/types/SecureValueError.html)\], \]) === [$Bool](/API_docs/types/Bool.html)<a name="users.setSecureValueErrors"></a>  



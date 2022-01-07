---
title: Methods (API)
description: List of methods
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Methods  
[Back to API documentation index](..)

[Go to the new description-version method index](index.md)

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
$MadelineProto->[account->acceptAuthorization](/API_docs/methods/account.acceptAuthorization.md)(\['bot_id' => [long](/API_docs/types/long.md), 'scope' => [string](/API_docs/types/string.md), 'public_key' => [string](/API_docs/types/string.md), 'value_hashes' => \[[SecureValueHash](/API_docs/types/SecureValueHash.md)\], 'credentials' => [SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.acceptAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->cancelPasswordEmail](/API_docs/methods/account.cancelPasswordEmail.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.cancelPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->changeAuthorizationSettings](/API_docs/methods/account.changeAuthorizationSettings.md)(\['hash' => [long](/API_docs/types/long.md), 'encrypted_requests_disabled' => [Bool](/API_docs/types/Bool.md), 'call_requests_disabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.changeAuthorizationSettings"></a>  

***
<br><br>
$MadelineProto->[account->changePhone](/API_docs/methods/account.changePhone.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), 'phone_code' => [string](/API_docs/types/string.md), \]) === [$User](/API_docs/types/User.md)<a name="account.changePhone"></a>  

***
<br><br>
$MadelineProto->[account->checkUsername](/API_docs/methods/account.checkUsername.md)(\['username' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.checkUsername"></a>  

***
<br><br>
$MadelineProto->[account->confirmPasswordEmail](/API_docs/methods/account.confirmPasswordEmail.md)(\['code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.confirmPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->confirmPhone](/API_docs/methods/account.confirmPhone.md)(\['phone_code_hash' => [string](/API_docs/types/string.md), 'phone_code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.confirmPhone"></a>  

***
<br><br>
$MadelineProto->[account->createTheme](/API_docs/methods/account.createTheme.md)(\['slug' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'document' => [InputDocument](/API_docs/types/InputDocument.md), 'settings' => \[[InputThemeSettings](/API_docs/types/InputThemeSettings.md)\], \]) === [$Theme](/API_docs/types/Theme.md)<a name="account.createTheme"></a>  

***
<br><br>
$MadelineProto->[account->declinePasswordReset](/API_docs/methods/account.declinePasswordReset.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.declinePasswordReset"></a>  

***
<br><br>
$MadelineProto->[account->deleteAccount](/API_docs/methods/account.deleteAccount.md)(\['reason' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.deleteAccount"></a>  

***
<br><br>
$MadelineProto->[account->deleteSecureValue](/API_docs/methods/account.deleteSecureValue.md)(\['types' => \[[SecureValueType](/API_docs/types/SecureValueType.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.deleteSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->finishTakeoutSession](/API_docs/methods/account.finishTakeoutSession.md)(\['success' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.finishTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->getAccountTTL](/API_docs/methods/account.getAccountTTL.md)(\[\]) === [$AccountDaysTTL](/API_docs/types/AccountDaysTTL.md)<a name="account.getAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->getAllSecureValues](/API_docs/methods/account.getAllSecureValues.md)(\[\]) === [$Vector\_of\_SecureValue](/API_docs/types/SecureValue.md)<a name="account.getAllSecureValues"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizationForm](/API_docs/methods/account.getAuthorizationForm.md)(\['bot_id' => [long](/API_docs/types/long.md), 'scope' => [string](/API_docs/types/string.md), 'public_key' => [string](/API_docs/types/string.md), \]) === [$account.AuthorizationForm](/API_docs/types/account.AuthorizationForm.md)<a name="account.getAuthorizationForm"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizations](/API_docs/methods/account.getAuthorizations.md)(\[\]) === [$account.Authorizations](/API_docs/types/account.Authorizations.md)<a name="account.getAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->getAutoDownloadSettings](/API_docs/methods/account.getAutoDownloadSettings.md)(\[\]) === [$account.AutoDownloadSettings](/API_docs/types/account.AutoDownloadSettings.md)<a name="account.getAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->getChatThemes](/API_docs/methods/account.getChatThemes.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$account.Themes](/API_docs/types/account.Themes.md)<a name="account.getChatThemes"></a>  

***
<br><br>
$MadelineProto->[account->getContactSignUpNotification](/API_docs/methods/account.getContactSignUpNotification.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.getContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->getContentSettings](/API_docs/methods/account.getContentSettings.md)(\[\]) === [$account.ContentSettings](/API_docs/types/account.ContentSettings.md)<a name="account.getContentSettings"></a>  

***
<br><br>
$MadelineProto->[account->getGlobalPrivacySettings](/API_docs/methods/account.getGlobalPrivacySettings.md)(\[\]) === [$GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.md)<a name="account.getGlobalPrivacySettings"></a>  

***
<br><br>
$MadelineProto->[account->getMultiWallPapers](/API_docs/methods/account.getMultiWallPapers.md)(\['wallpapers' => \[[InputWallPaper](/API_docs/types/InputWallPaper.md)\], \]) === [$Vector\_of\_WallPaper](/API_docs/types/WallPaper.md)<a name="account.getMultiWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->getNotifyExceptions](/API_docs/methods/account.getNotifyExceptions.md)(\['compare_sound' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputNotifyPeer](/API_docs/types/InputNotifyPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="account.getNotifyExceptions"></a>  

***
<br><br>
$MadelineProto->[account->getNotifySettings](/API_docs/methods/account.getNotifySettings.md)(\['peer' => [InputNotifyPeer](/API_docs/types/InputNotifyPeer.md), \]) === [$PeerNotifySettings](/API_docs/types/PeerNotifySettings.md)<a name="account.getNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->getPassword](/API_docs/methods/account.getPassword.md)(\[\]) === [$account.Password](/API_docs/types/account.Password.md)<a name="account.getPassword"></a>  

***
<br><br>
$MadelineProto->[account->getPasswordSettings](/API_docs/methods/account.getPasswordSettings.md)(\['password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), \]) === [$account.PasswordSettings](/API_docs/types/account.PasswordSettings.md)<a name="account.getPasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->getPrivacy](/API_docs/methods/account.getPrivacy.md)(\['key' => [InputPrivacyKey](/API_docs/types/InputPrivacyKey.md), \]) === [$account.PrivacyRules](/API_docs/types/account.PrivacyRules.md)<a name="account.getPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->getSecureValue](/API_docs/methods/account.getSecureValue.md)(\['types' => \[[SecureValueType](/API_docs/types/SecureValueType.md)\], \]) === [$Vector\_of\_SecureValue](/API_docs/types/SecureValue.md)<a name="account.getSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->getTheme](/API_docs/methods/account.getTheme.md)(\['format' => [string](/API_docs/types/string.md), 'theme' => [InputTheme](/API_docs/types/InputTheme.md), 'document_id' => [long](/API_docs/types/long.md), \]) === [$Theme](/API_docs/types/Theme.md)<a name="account.getTheme"></a>  

***
<br><br>
$MadelineProto->[account->getThemes](/API_docs/methods/account.getThemes.md)(\['format' => [string](/API_docs/types/string.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$account.Themes](/API_docs/types/account.Themes.md)<a name="account.getThemes"></a>  

***
<br><br>
$MadelineProto->[account->getTmpPassword](/API_docs/methods/account.getTmpPassword.md)(\['password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), 'period' => [int](/API_docs/types/int.md), \]) === [$account.TmpPassword](/API_docs/types/account.TmpPassword.md)<a name="account.getTmpPassword"></a>  

***
<br><br>
$MadelineProto->[account->getWallPaper](/API_docs/methods/account.getWallPaper.md)(\['wallpaper' => [InputWallPaper](/API_docs/types/InputWallPaper.md), \]) === [$WallPaper](/API_docs/types/WallPaper.md)<a name="account.getWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->getWallPapers](/API_docs/methods/account.getWallPapers.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$account.WallPapers](/API_docs/types/account.WallPapers.md)<a name="account.getWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->getWebAuthorizations](/API_docs/methods/account.getWebAuthorizations.md)(\[\]) === [$account.WebAuthorizations](/API_docs/types/account.WebAuthorizations.md)<a name="account.getWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->initTakeoutSession](/API_docs/methods/account.initTakeoutSession.md)(\['contacts' => [Bool](/API_docs/types/Bool.md), 'message_users' => [Bool](/API_docs/types/Bool.md), 'message_chats' => [Bool](/API_docs/types/Bool.md), 'message_megagroups' => [Bool](/API_docs/types/Bool.md), 'message_channels' => [Bool](/API_docs/types/Bool.md), 'files' => [Bool](/API_docs/types/Bool.md), 'file_max_size' => [int](/API_docs/types/int.md), \]) === [$account.Takeout](/API_docs/types/account.Takeout.md)<a name="account.initTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->installTheme](/API_docs/methods/account.installTheme.md)(\['dark' => [Bool](/API_docs/types/Bool.md), 'theme' => [InputTheme](/API_docs/types/InputTheme.md), 'format' => [string](/API_docs/types/string.md), 'base_theme' => [BaseTheme](/API_docs/types/BaseTheme.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.installTheme"></a>  

***
<br><br>
$MadelineProto->[account->installWallPaper](/API_docs/methods/account.installWallPaper.md)(\['wallpaper' => [InputWallPaper](/API_docs/types/InputWallPaper.md), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.installWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->registerDevice](/API_docs/methods/account.registerDevice.md)(\['no_muted' => [Bool](/API_docs/types/Bool.md), 'token_type' => [int](/API_docs/types/int.md), 'token' => [string](/API_docs/types/string.md), 'app_sandbox' => [Bool](/API_docs/types/Bool.md), 'secret' => [bytes](/API_docs/types/bytes.md), 'other_uids' => \[[long](/API_docs/types/long.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.registerDevice"></a>  

***
<br><br>
$MadelineProto->[account->reportPeer](/API_docs/methods/account.reportPeer.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reason' => [ReportReason](/API_docs/types/ReportReason.md), 'message' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.reportPeer"></a>  

***
<br><br>
$MadelineProto->[account->reportProfilePhoto](/API_docs/methods/account.reportProfilePhoto.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'photo_id' => [InputPhoto](/API_docs/types/InputPhoto.md), 'reason' => [ReportReason](/API_docs/types/ReportReason.md), 'message' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.reportProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[account->resendPasswordEmail](/API_docs/methods/account.resendPasswordEmail.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resendPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->resetAuthorization](/API_docs/methods/account.resetAuthorization.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resetAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetNotifySettings](/API_docs/methods/account.resetNotifySettings.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resetNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->resetPassword](/API_docs/methods/account.resetPassword.md)(\[\]) === [$account.ResetPasswordResult](/API_docs/types/account.ResetPasswordResult.md)<a name="account.resetPassword"></a>  

***
<br><br>
$MadelineProto->[account->resetWallPapers](/API_docs/methods/account.resetWallPapers.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resetWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorization](/API_docs/methods/account.resetWebAuthorization.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resetWebAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorizations](/API_docs/methods/account.resetWebAuthorizations.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="account.resetWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->saveAutoDownloadSettings](/API_docs/methods/account.saveAutoDownloadSettings.md)(\['low' => [Bool](/API_docs/types/Bool.md), 'high' => [Bool](/API_docs/types/Bool.md), 'settings' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.saveAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->saveSecureValue](/API_docs/methods/account.saveSecureValue.md)(\['value' => [InputSecureValue](/API_docs/types/InputSecureValue.md), 'secure_secret_id' => [long](/API_docs/types/long.md), \]) === [$SecureValue](/API_docs/types/SecureValue.md)<a name="account.saveSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->saveTheme](/API_docs/methods/account.saveTheme.md)(\['theme' => [InputTheme](/API_docs/types/InputTheme.md), 'unsave' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.saveTheme"></a>  

***
<br><br>
$MadelineProto->[account->saveWallPaper](/API_docs/methods/account.saveWallPaper.md)(\['wallpaper' => [InputWallPaper](/API_docs/types/InputWallPaper.md), 'unsave' => [Bool](/API_docs/types/Bool.md), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.saveWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->sendChangePhoneCode](/API_docs/methods/account.sendChangePhoneCode.md)(\['phone_number' => [string](/API_docs/types/string.md), 'settings' => [CodeSettings](/API_docs/types/CodeSettings.md), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.md)<a name="account.sendChangePhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendConfirmPhoneCode](/API_docs/methods/account.sendConfirmPhoneCode.md)(\['hash' => [string](/API_docs/types/string.md), 'settings' => [CodeSettings](/API_docs/types/CodeSettings.md), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.md)<a name="account.sendConfirmPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyEmailCode](/API_docs/methods/account.sendVerifyEmailCode.md)(\['email' => [string](/API_docs/types/string.md), \]) === [$account.SentEmailCode](/API_docs/types/account.SentEmailCode.md)<a name="account.sendVerifyEmailCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyPhoneCode](/API_docs/methods/account.sendVerifyPhoneCode.md)(\['phone_number' => [string](/API_docs/types/string.md), 'settings' => [CodeSettings](/API_docs/types/CodeSettings.md), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.md)<a name="account.sendVerifyPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->setAccountTTL](/API_docs/methods/account.setAccountTTL.md)(\['ttl' => [AccountDaysTTL](/API_docs/types/AccountDaysTTL.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.setAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->setAuthorizationTTL](/API_docs/methods/account.setAuthorizationTTL.md)(\['authorization_ttl_days' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.setAuthorizationTTL"></a>  

***
<br><br>
$MadelineProto->[account->setContactSignUpNotification](/API_docs/methods/account.setContactSignUpNotification.md)(\['silent' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.setContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->setContentSettings](/API_docs/methods/account.setContentSettings.md)(\['sensitive_enabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.setContentSettings"></a>  

***
<br><br>
$MadelineProto->[account->setGlobalPrivacySettings](/API_docs/methods/account.setGlobalPrivacySettings.md)(\['settings' => [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.md), \]) === [$GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.md)<a name="account.setGlobalPrivacySettings"></a>  

***
<br><br>
$MadelineProto->[account->setPrivacy](/API_docs/methods/account.setPrivacy.md)(\['key' => [InputPrivacyKey](/API_docs/types/InputPrivacyKey.md), 'rules' => \[[InputPrivacyRule](/API_docs/types/InputPrivacyRule.md)\], \]) === [$account.PrivacyRules](/API_docs/types/account.PrivacyRules.md)<a name="account.setPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->unregisterDevice](/API_docs/methods/account.unregisterDevice.md)(\['token_type' => [int](/API_docs/types/int.md), 'token' => [string](/API_docs/types/string.md), 'other_uids' => \[[long](/API_docs/types/long.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.unregisterDevice"></a>  

***
<br><br>
$MadelineProto->[account->updateDeviceLocked](/API_docs/methods/account.updateDeviceLocked.md)(\['period' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.updateDeviceLocked"></a>  

***
<br><br>
$MadelineProto->[account->updateNotifySettings](/API_docs/methods/account.updateNotifySettings.md)(\['peer' => [InputNotifyPeer](/API_docs/types/InputNotifyPeer.md), 'settings' => [InputPeerNotifySettings](/API_docs/types/InputPeerNotifySettings.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.updateNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->updatePasswordSettings](/API_docs/methods/account.updatePasswordSettings.md)(\['password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), 'new_settings' => [account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.updatePasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->updateProfile](/API_docs/methods/account.updateProfile.md)(\['first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'about' => [string](/API_docs/types/string.md), \]) === [$User](/API_docs/types/User.md)<a name="account.updateProfile"></a>  

***
<br><br>
$MadelineProto->[account->updateStatus](/API_docs/methods/account.updateStatus.md)(\['offline' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.updateStatus"></a>  

***
<br><br>
$MadelineProto->[account->updateTheme](/API_docs/methods/account.updateTheme.md)(\['format' => [string](/API_docs/types/string.md), 'theme' => [InputTheme](/API_docs/types/InputTheme.md), 'slug' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'document' => [InputDocument](/API_docs/types/InputDocument.md), 'settings' => \[[InputThemeSettings](/API_docs/types/InputThemeSettings.md)\], \]) === [$Theme](/API_docs/types/Theme.md)<a name="account.updateTheme"></a>  

***
<br><br>
$MadelineProto->[account->updateUsername](/API_docs/methods/account.updateUsername.md)(\['username' => [string](/API_docs/types/string.md), \]) === [$User](/API_docs/types/User.md)<a name="account.updateUsername"></a>  

***
<br><br>
$MadelineProto->[account->uploadTheme](/API_docs/methods/account.uploadTheme.md)(\['file' => [InputFile](/API_docs/types/InputFile.md), 'thumb' => [InputFile](/API_docs/types/InputFile.md), 'file_name' => [string](/API_docs/types/string.md), 'mime_type' => [string](/API_docs/types/string.md), \]) === [$Document](/API_docs/types/Document.md)<a name="account.uploadTheme"></a>  

***
<br><br>
$MadelineProto->[account->uploadWallPaper](/API_docs/methods/account.uploadWallPaper.md)(\['file' => [InputFile](/API_docs/types/InputFile.md), 'mime_type' => [string](/API_docs/types/string.md), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \]) === [$WallPaper](/API_docs/types/WallPaper.md)<a name="account.uploadWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->verifyEmail](/API_docs/methods/account.verifyEmail.md)(\['email' => [string](/API_docs/types/string.md), 'code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.verifyEmail"></a>  

***
<br><br>
$MadelineProto->[account->verifyPhone](/API_docs/methods/account.verifyPhone.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), 'phone_code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="account.verifyPhone"></a>  

***
<br><br>
$MadelineProto->[auth->acceptLoginToken](/API_docs/methods/auth.acceptLoginToken.md)(\['token' => [bytes](/API_docs/types/bytes.md), \]) === [$Authorization](/API_docs/types/Authorization.md)<a name="auth.acceptLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->bindTempAuthKey](/API_docs/methods/auth.bindTempAuthKey.md)(\['perm_auth_key_id' => [long](/API_docs/types/long.md), 'nonce' => [long](/API_docs/types/long.md), 'expires_at' => [int](/API_docs/types/int.md), 'encrypted_message' => [bytes](/API_docs/types/bytes.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="auth.bindTempAuthKey"></a>  

***
<br><br>
$MadelineProto->[auth->cancelCode](/API_docs/methods/auth.cancelCode.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="auth.cancelCode"></a>  

***
<br><br>
$MadelineProto->[auth->checkPassword](/API_docs/methods/auth.checkPassword.md)(\['password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.checkPassword"></a>  

***
<br><br>
$MadelineProto->[auth->checkRecoveryPassword](/API_docs/methods/auth.checkRecoveryPassword.md)(\['code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="auth.checkRecoveryPassword"></a>  

***
<br><br>
$MadelineProto->[auth->dropTempAuthKeys](/API_docs/methods/auth.dropTempAuthKeys.md)(\['except_auth_keys' => \[[long](/API_docs/types/long.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="auth.dropTempAuthKeys"></a>  

***
<br><br>
$MadelineProto->[auth->exportAuthorization](/API_docs/methods/auth.exportAuthorization.md)(\['dc_id' => [int](/API_docs/types/int.md), \]) === [$auth.ExportedAuthorization](/API_docs/types/auth.ExportedAuthorization.md)<a name="auth.exportAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->exportLoginToken](/API_docs/methods/auth.exportLoginToken.md)(\['api_id' => [int](/API_docs/types/int.md), 'api_hash' => [string](/API_docs/types/string.md), 'except_ids' => \[[long](/API_docs/types/long.md)\], \]) === [$auth.LoginToken](/API_docs/types/auth.LoginToken.md)<a name="auth.exportLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->importAuthorization](/API_docs/methods/auth.importAuthorization.md)(\['id' => [long](/API_docs/types/long.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.importAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importBotAuthorization](/API_docs/methods/auth.importBotAuthorization.md)(\['api_id' => [int](/API_docs/types/int.md), 'api_hash' => [string](/API_docs/types/string.md), 'bot_auth_token' => [string](/API_docs/types/string.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.importBotAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importLoginToken](/API_docs/methods/auth.importLoginToken.md)(\['token' => [bytes](/API_docs/types/bytes.md), \]) === [$auth.LoginToken](/API_docs/types/auth.LoginToken.md)<a name="auth.importLoginToken"></a>  

***
<br><br>
$MadelineProto->[auth->logOut](/API_docs/methods/auth.logOut.md)(\[\]) === [$auth.LoggedOut](/API_docs/types/auth.LoggedOut.md)<a name="auth.logOut"></a>  

***
<br><br>
$MadelineProto->[auth->recoverPassword](/API_docs/methods/auth.recoverPassword.md)(\['code' => [string](/API_docs/types/string.md), 'new_settings' => [account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.recoverPassword"></a>  

***
<br><br>
$MadelineProto->[auth->requestPasswordRecovery](/API_docs/methods/auth.requestPasswordRecovery.md)(\[\]) === [$auth.PasswordRecovery](/API_docs/types/auth.PasswordRecovery.md)<a name="auth.requestPasswordRecovery"></a>  

***
<br><br>
$MadelineProto->[auth->resendCode](/API_docs/methods/auth.resendCode.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.md)<a name="auth.resendCode"></a>  

***
<br><br>
$MadelineProto->[auth->resetAuthorizations](/API_docs/methods/auth.resetAuthorizations.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="auth.resetAuthorizations"></a>  

***
<br><br>
$MadelineProto->[auth->sendCode](/API_docs/methods/auth.sendCode.md)(\['phone_number' => [string](/API_docs/types/string.md), 'api_id' => [int](/API_docs/types/int.md), 'api_hash' => [string](/API_docs/types/string.md), 'settings' => [CodeSettings](/API_docs/types/CodeSettings.md), \]) === [$auth.SentCode](/API_docs/types/auth.SentCode.md)<a name="auth.sendCode"></a>  

***
<br><br>
$MadelineProto->[auth->signIn](/API_docs/methods/auth.signIn.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), 'phone_code' => [string](/API_docs/types/string.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.signIn"></a>  

***
<br><br>
$MadelineProto->[auth->signUp](/API_docs/methods/auth.signUp.md)(\['phone_number' => [string](/API_docs/types/string.md), 'phone_code_hash' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), \]) === [$auth.Authorization](/API_docs/types/auth.Authorization.md)<a name="auth.signUp"></a>  

***
<br><br>
$MadelineProto->[bots->answerWebhookJSONQuery](/API_docs/methods/bots.answerWebhookJSONQuery.md)(\['query_id' => [long](/API_docs/types/long.md), 'data' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="bots.answerWebhookJSONQuery"></a>  

***
<br><br>
$MadelineProto->[bots->getBotCommands](/API_docs/methods/bots.getBotCommands.md)(\['scope' => [BotCommandScope](/API_docs/types/BotCommandScope.md), 'lang_code' => [string](/API_docs/types/string.md), \]) === [$Vector\_of\_BotCommand](/API_docs/types/BotCommand.md)<a name="bots.getBotCommands"></a>  

***
<br><br>
$MadelineProto->[bots->resetBotCommands](/API_docs/methods/bots.resetBotCommands.md)(\['scope' => [BotCommandScope](/API_docs/types/BotCommandScope.md), 'lang_code' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="bots.resetBotCommands"></a>  

***
<br><br>
$MadelineProto->[bots->sendCustomRequest](/API_docs/methods/bots.sendCustomRequest.md)(\['custom_method' => [string](/API_docs/types/string.md), 'params' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$DataJSON](/API_docs/types/DataJSON.md)<a name="bots.sendCustomRequest"></a>  

***
<br><br>
$MadelineProto->[bots->setBotCommands](/API_docs/methods/bots.setBotCommands.md)(\['scope' => [BotCommandScope](/API_docs/types/BotCommandScope.md), 'lang_code' => [string](/API_docs/types/string.md), 'commands' => \[[BotCommand](/API_docs/types/BotCommand.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="bots.setBotCommands"></a>  

***
<br><br>
$MadelineProto->[channels->checkUsername](/API_docs/methods/channels.checkUsername.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'username' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.checkUsername"></a>  

***
<br><br>
$MadelineProto->[channels->convertToGigagroup](/API_docs/methods/channels.convertToGigagroup.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.convertToGigagroup"></a>  

***
<br><br>
$MadelineProto->[channels->createChannel](/API_docs/methods/channels.createChannel.md)(\['broadcast' => [Bool](/API_docs/types/Bool.md), 'megagroup' => [Bool](/API_docs/types/Bool.md), 'for_import' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), 'about' => [string](/API_docs/types/string.md), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'address' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.createChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteChannel](/API_docs/methods/channels.deleteChannel.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.deleteChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteHistory](/API_docs/methods/channels.deleteHistory.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'max_id' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[channels->deleteMessages](/API_docs/methods/channels.deleteMessages.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.md)<a name="channels.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[channels->deleteParticipantHistory](/API_docs/methods/channels.deleteParticipantHistory.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'participant' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.md)<a name="channels.deleteParticipantHistory"></a>  

***
<br><br>
$MadelineProto->[channels->editAdmin](/API_docs/methods/channels.editAdmin.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.md), 'rank' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.editAdmin"></a>  

***
<br><br>
$MadelineProto->[channels->editBanned](/API_docs/methods/channels.editBanned.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'participant' => [InputPeer](/API_docs/types/InputPeer.md), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.editBanned"></a>  

***
<br><br>
$MadelineProto->[channels->editCreator](/API_docs/methods/channels.editCreator.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.editCreator"></a>  

***
<br><br>
$MadelineProto->[channels->editLocation](/API_docs/methods/channels.editLocation.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'address' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.editLocation"></a>  

***
<br><br>
$MadelineProto->[channels->editPhoto](/API_docs/methods/channels.editPhoto.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'photo' => [InputChatPhoto](/API_docs/types/InputChatPhoto.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.editPhoto"></a>  

***
<br><br>
$MadelineProto->[channels->editTitle](/API_docs/methods/channels.editTitle.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'title' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.editTitle"></a>  

***
<br><br>
$MadelineProto->[channels->exportMessageLink](/API_docs/methods/channels.exportMessageLink.md)(\['grouped' => [Bool](/API_docs/types/Bool.md), 'thread' => [Bool](/API_docs/types/Bool.md), 'channel' => [InputChannel](/API_docs/types/InputChannel.md), 'id' => [int](/API_docs/types/int.md), \]) === [$ExportedMessageLink](/API_docs/types/ExportedMessageLink.md)<a name="channels.exportMessageLink"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminLog](/API_docs/methods/channels.getAdminLog.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'q' => [string](/API_docs/types/string.md), 'events_filter' => [ChannelAdminLogEventsFilter](/API_docs/types/ChannelAdminLogEventsFilter.md), 'admins' => \[[InputUser](/API_docs/types/InputUser.md)\], 'max_id' => [long](/API_docs/types/long.md), 'min_id' => [long](/API_docs/types/long.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$channels.AdminLogResults](/API_docs/types/channels.AdminLogResults.md)<a name="channels.getAdminLog"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminedPublicChannels](/API_docs/methods/channels.getAdminedPublicChannels.md)(\['by_location' => [Bool](/API_docs/types/Bool.md), 'check_limit' => [Bool](/API_docs/types/Bool.md), \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="channels.getAdminedPublicChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getChannels](/API_docs/methods/channels.getChannels.md)(\['id' => \[[InputChannel](/API_docs/types/InputChannel.md)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="channels.getChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getFullChannel](/API_docs/methods/channels.getFullChannel.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$messages.ChatFull](/API_docs/types/messages.ChatFull.md)<a name="channels.getFullChannel"></a>  

***
<br><br>
$MadelineProto->[channels->getGroupsForDiscussion](/API_docs/methods/channels.getGroupsForDiscussion.md)(\[\]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="channels.getGroupsForDiscussion"></a>  

***
<br><br>
$MadelineProto->[channels->getInactiveChannels](/API_docs/methods/channels.getInactiveChannels.md)(\[\]) === [$messages.InactiveChats](/API_docs/types/messages.InactiveChats.md)<a name="channels.getInactiveChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getLeftChannels](/API_docs/methods/channels.getLeftChannels.md)(\['offset' => [int](/API_docs/types/int.md), \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="channels.getLeftChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getMessages](/API_docs/methods/channels.getMessages.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'id' => \[[InputMessage](/API_docs/types/InputMessage.md)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="channels.getMessages"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipant](/API_docs/methods/channels.getParticipant.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'participant' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$channels.ChannelParticipant](/API_docs/types/channels.ChannelParticipant.md)<a name="channels.getParticipant"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipants](/API_docs/methods/channels.getParticipants.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'filter' => [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.md), 'offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$channels.ChannelParticipants](/API_docs/types/channels.ChannelParticipants.md)<a name="channels.getParticipants"></a>  

***
<br><br>
$MadelineProto->[channels->getSendAs](/API_docs/methods/channels.getSendAs.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$channels.SendAsPeers](/API_docs/types/channels.SendAsPeers.md)<a name="channels.getSendAs"></a>  

***
<br><br>
$MadelineProto->[channels->getSponsoredMessages](/API_docs/methods/channels.getSponsoredMessages.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$messages.SponsoredMessages](/API_docs/types/messages.SponsoredMessages.md)<a name="channels.getSponsoredMessages"></a>  

***
<br><br>
$MadelineProto->[channels->inviteToChannel](/API_docs/methods/channels.inviteToChannel.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'users' => \[[InputUser](/API_docs/types/InputUser.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.inviteToChannel"></a>  

***
<br><br>
$MadelineProto->[channels->joinChannel](/API_docs/methods/channels.joinChannel.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.joinChannel"></a>  

***
<br><br>
$MadelineProto->[channels->leaveChannel](/API_docs/methods/channels.leaveChannel.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.leaveChannel"></a>  

***
<br><br>
$MadelineProto->[channels->readHistory](/API_docs/methods/channels.readHistory.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'max_id' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.readHistory"></a>  

***
<br><br>
$MadelineProto->[channels->readMessageContents](/API_docs/methods/channels.readMessageContents.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[channels->reportSpam](/API_docs/methods/channels.reportSpam.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'participant' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.reportSpam"></a>  

***
<br><br>
$MadelineProto->[channels->setDiscussionGroup](/API_docs/methods/channels.setDiscussionGroup.md)(\['broadcast' => [InputChannel](/API_docs/types/InputChannel.md), 'group' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.setDiscussionGroup"></a>  

***
<br><br>
$MadelineProto->[channels->setStickers](/API_docs/methods/channels.setStickers.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.setStickers"></a>  

***
<br><br>
$MadelineProto->[channels->togglePreHistoryHidden](/API_docs/methods/channels.togglePreHistoryHidden.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'enabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.togglePreHistoryHidden"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSignatures](/API_docs/methods/channels.toggleSignatures.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'enabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.toggleSignatures"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSlowMode](/API_docs/methods/channels.toggleSlowMode.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'seconds' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="channels.toggleSlowMode"></a>  

***
<br><br>
$MadelineProto->[channels->updateUsername](/API_docs/methods/channels.updateUsername.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'username' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.updateUsername"></a>  

***
<br><br>
$MadelineProto->[channels->viewSponsoredMessage](/API_docs/methods/channels.viewSponsoredMessage.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="channels.viewSponsoredMessage"></a>  

***
<br><br>
$MadelineProto->[contacts->acceptContact](/API_docs/methods/contacts.acceptContact.md)(\['id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="contacts.acceptContact"></a>  

***
<br><br>
$MadelineProto->[contacts->addContact](/API_docs/methods/contacts.addContact.md)(\['add_phone_privacy_exception' => [Bool](/API_docs/types/Bool.md), 'id' => [InputUser](/API_docs/types/InputUser.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'phone' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="contacts.addContact"></a>  

***
<br><br>
$MadelineProto->[contacts->block](/API_docs/methods/contacts.block.md)(\['id' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.block"></a>  

***
<br><br>
$MadelineProto->[contacts->blockFromReplies](/API_docs/methods/contacts.blockFromReplies.md)(\['delete_message' => [Bool](/API_docs/types/Bool.md), 'delete_history' => [Bool](/API_docs/types/Bool.md), 'report_spam' => [Bool](/API_docs/types/Bool.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="contacts.blockFromReplies"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteByPhones](/API_docs/methods/contacts.deleteByPhones.md)(\['phones' => \[[string](/API_docs/types/string.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.deleteByPhones"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteContacts](/API_docs/methods/contacts.deleteContacts.md)(\['id' => \[[InputUser](/API_docs/types/InputUser.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="contacts.deleteContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getBlocked](/API_docs/methods/contacts.getBlocked.md)(\['offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$contacts.Blocked](/API_docs/types/contacts.Blocked.md)<a name="contacts.getBlocked"></a>  

***
<br><br>
$MadelineProto->[contacts->getContactIDs](/API_docs/methods/contacts.getContactIDs.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$Vector\_of\_int](/API_docs/types/int.md)<a name="contacts.getContactIDs"></a>  

***
<br><br>
$MadelineProto->[contacts->getContacts](/API_docs/methods/contacts.getContacts.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$contacts.Contacts](/API_docs/types/contacts.Contacts.md)<a name="contacts.getContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getLocated](/API_docs/methods/contacts.getLocated.md)(\['background' => [Bool](/API_docs/types/Bool.md), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'self_expires' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="contacts.getLocated"></a>  

***
<br><br>
$MadelineProto->[contacts->getSaved](/API_docs/methods/contacts.getSaved.md)(\[\]) === [$Vector\_of\_SavedContact](/API_docs/types/SavedContact.md)<a name="contacts.getSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->getStatuses](/API_docs/methods/contacts.getStatuses.md)(\[\]) === [$Vector\_of\_ContactStatus](/API_docs/types/ContactStatus.md)<a name="contacts.getStatuses"></a>  

***
<br><br>
$MadelineProto->[contacts->getTopPeers](/API_docs/methods/contacts.getTopPeers.md)(\['correspondents' => [Bool](/API_docs/types/Bool.md), 'bots_pm' => [Bool](/API_docs/types/Bool.md), 'bots_inline' => [Bool](/API_docs/types/Bool.md), 'phone_calls' => [Bool](/API_docs/types/Bool.md), 'forward_users' => [Bool](/API_docs/types/Bool.md), 'forward_chats' => [Bool](/API_docs/types/Bool.md), 'groups' => [Bool](/API_docs/types/Bool.md), 'channels' => [Bool](/API_docs/types/Bool.md), 'offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$contacts.TopPeers](/API_docs/types/contacts.TopPeers.md)<a name="contacts.getTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->importContacts](/API_docs/methods/contacts.importContacts.md)(\['contacts' => \[[InputContact](/API_docs/types/InputContact.md)\], \]) === [$contacts.ImportedContacts](/API_docs/types/contacts.ImportedContacts.md)<a name="contacts.importContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->resetSaved](/API_docs/methods/contacts.resetSaved.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.resetSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->resetTopPeerRating](/API_docs/methods/contacts.resetTopPeerRating.md)(\['category' => [TopPeerCategory](/API_docs/types/TopPeerCategory.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.resetTopPeerRating"></a>  

***
<br><br>
$MadelineProto->[contacts->resolveUsername](/API_docs/methods/contacts.resolveUsername.md)(\['username' => [string](/API_docs/types/string.md), \]) === [$contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.md)<a name="contacts.resolveUsername"></a>  

***
<br><br>
$MadelineProto->[contacts->search](/API_docs/methods/contacts.search.md)(\['q' => [string](/API_docs/types/string.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$contacts.Found](/API_docs/types/contacts.Found.md)<a name="contacts.search"></a>  

***
<br><br>
$MadelineProto->[contacts->toggleTopPeers](/API_docs/methods/contacts.toggleTopPeers.md)(\['enabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.toggleTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->unblock](/API_docs/methods/contacts.unblock.md)(\['id' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="contacts.unblock"></a>  

***
<br><br>
$MadelineProto->[folders->deleteFolder](/API_docs/methods/folders.deleteFolder.md)(\['folder_id' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="folders.deleteFolder"></a>  

***
<br><br>
$MadelineProto->[folders->editPeerFolders](/API_docs/methods/folders.editPeerFolders.md)(\['folder_peers' => \[[InputFolderPeer](/API_docs/types/InputFolderPeer.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="folders.editPeerFolders"></a>  

***
<br><br>
$MadelineProto->[help->acceptTermsOfService](/API_docs/methods/help.acceptTermsOfService.md)(\['id' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="help.acceptTermsOfService"></a>  

***
<br><br>
$MadelineProto->[help->dismissSuggestion](/API_docs/methods/help.dismissSuggestion.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'suggestion' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="help.dismissSuggestion"></a>  

***
<br><br>
$MadelineProto->[help->editUserInfo](/API_docs/methods/help.editUserInfo.md)(\['user_id' => [InputUser](/API_docs/types/InputUser.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \]) === [$help.UserInfo](/API_docs/types/help.UserInfo.md)<a name="help.editUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->getAppChangelog](/API_docs/methods/help.getAppChangelog.md)(\['prev_app_version' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="help.getAppChangelog"></a>  

***
<br><br>
$MadelineProto->[help->getAppConfig](/API_docs/methods/help.getAppConfig.md)(\[\]) === [$JSONValue](/API_docs/types/JSONValue.md)<a name="help.getAppConfig"></a>  

***
<br><br>
$MadelineProto->[help->getAppUpdate](/API_docs/methods/help.getAppUpdate.md)(\['source' => [string](/API_docs/types/string.md), \]) === [$help.AppUpdate](/API_docs/types/help.AppUpdate.md)<a name="help.getAppUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getCdnConfig](/API_docs/methods/help.getCdnConfig.md)(\[\]) === [$CdnConfig](/API_docs/types/CdnConfig.md)<a name="help.getCdnConfig"></a>  

***
<br><br>
$MadelineProto->[help->getConfig](/API_docs/methods/help.getConfig.md)(\[\]) === [$Config](/API_docs/types/Config.md)<a name="help.getConfig"></a>  

***
<br><br>
$MadelineProto->[help->getCountriesList](/API_docs/methods/help.getCountriesList.md)(\['lang_code' => [string](/API_docs/types/string.md), 'hash' => [int](/API_docs/types/int.md), \]) === [$help.CountriesList](/API_docs/types/help.CountriesList.md)<a name="help.getCountriesList"></a>  

***
<br><br>
$MadelineProto->[help->getDeepLinkInfo](/API_docs/methods/help.getDeepLinkInfo.md)(\['path' => [string](/API_docs/types/string.md), \]) === [$help.DeepLinkInfo](/API_docs/types/help.DeepLinkInfo.md)<a name="help.getDeepLinkInfo"></a>  

***
<br><br>
$MadelineProto->[help->getInviteText](/API_docs/methods/help.getInviteText.md)(\[\]) === [$help.InviteText](/API_docs/types/help.InviteText.md)<a name="help.getInviteText"></a>  

***
<br><br>
$MadelineProto->[help->getNearestDc](/API_docs/methods/help.getNearestDc.md)(\[\]) === [$NearestDc](/API_docs/types/NearestDc.md)<a name="help.getNearestDc"></a>  

***
<br><br>
$MadelineProto->[help->getPassportConfig](/API_docs/methods/help.getPassportConfig.md)(\['hash' => [int](/API_docs/types/int.md), \]) === [$help.PassportConfig](/API_docs/types/help.PassportConfig.md)<a name="help.getPassportConfig"></a>  

***
<br><br>
$MadelineProto->[help->getPromoData](/API_docs/methods/help.getPromoData.md)(\[\]) === [$help.PromoData](/API_docs/types/help.PromoData.md)<a name="help.getPromoData"></a>  

***
<br><br>
$MadelineProto->[help->getRecentMeUrls](/API_docs/methods/help.getRecentMeUrls.md)(\['referer' => [string](/API_docs/types/string.md), \]) === [$help.RecentMeUrls](/API_docs/types/help.RecentMeUrls.md)<a name="help.getRecentMeUrls"></a>  

***
<br><br>
$MadelineProto->[help->getSupport](/API_docs/methods/help.getSupport.md)(\[\]) === [$help.Support](/API_docs/types/help.Support.md)<a name="help.getSupport"></a>  

***
<br><br>
$MadelineProto->[help->getSupportName](/API_docs/methods/help.getSupportName.md)(\[\]) === [$help.SupportName](/API_docs/types/help.SupportName.md)<a name="help.getSupportName"></a>  

***
<br><br>
$MadelineProto->[help->getTermsOfServiceUpdate](/API_docs/methods/help.getTermsOfServiceUpdate.md)(\[\]) === [$help.TermsOfServiceUpdate](/API_docs/types/help.TermsOfServiceUpdate.md)<a name="help.getTermsOfServiceUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getUserInfo](/API_docs/methods/help.getUserInfo.md)(\['user_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$help.UserInfo](/API_docs/types/help.UserInfo.md)<a name="help.getUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->hidePromoData](/API_docs/methods/help.hidePromoData.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="help.hidePromoData"></a>  

***
<br><br>
$MadelineProto->[help->saveAppLog](/API_docs/methods/help.saveAppLog.md)(\['events' => \[[InputAppEvent](/API_docs/types/InputAppEvent.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="help.saveAppLog"></a>  

***
<br><br>
$MadelineProto->[help->setBotUpdatesStatus](/API_docs/methods/help.setBotUpdatesStatus.md)(\['pending_updates_count' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="help.setBotUpdatesStatus"></a>  

***
<br><br>
$MadelineProto->[initConnection](/API_docs/methods/initConnection.md)(\['api_id' => [int](/API_docs/types/int.md), 'device_model' => [string](/API_docs/types/string.md), 'system_version' => [string](/API_docs/types/string.md), 'app_version' => [string](/API_docs/types/string.md), 'system_lang_code' => [string](/API_docs/types/string.md), 'lang_pack' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), 'proxy' => [InputClientProxy](/API_docs/types/InputClientProxy.md), 'params' => [JSONValue](/API_docs/types/JSONValue.md), 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="initConnection"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsg](/API_docs/methods/invokeAfterMsg.md)(\['msg_id' => [long](/API_docs/types/long.md), 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeAfterMsg"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsgs](/API_docs/methods/invokeAfterMsgs.md)(\['msg_ids' => \[[long](/API_docs/types/long.md)\], 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeAfterMsgs"></a>  

***
<br><br>
$MadelineProto->[invokeWithLayer](/API_docs/methods/invokeWithLayer.md)(\['layer' => [int](/API_docs/types/int.md), 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeWithLayer"></a>  

***
<br><br>
$MadelineProto->[invokeWithMessagesRange](/API_docs/methods/invokeWithMessagesRange.md)(\['range' => [MessageRange](/API_docs/types/MessageRange.md), 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeWithMessagesRange"></a>  

***
<br><br>
$MadelineProto->[invokeWithTakeout](/API_docs/methods/invokeWithTakeout.md)(\['takeout_id' => [long](/API_docs/types/long.md), 'query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeWithTakeout"></a>  

***
<br><br>
$MadelineProto->[invokeWithoutUpdates](/API_docs/methods/invokeWithoutUpdates.md)(\['query' => [!X](/API_docs/types/!X.md), \]) === [$X](/API_docs/types/X.md)<a name="invokeWithoutUpdates"></a>  

***
<br><br>
$MadelineProto->[langpack->getDifference](/API_docs/methods/langpack.getDifference.md)(\['lang_pack' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), 'from_version' => [int](/API_docs/types/int.md), \]) === [$LangPackDifference](/API_docs/types/LangPackDifference.md)<a name="langpack.getDifference"></a>  

***
<br><br>
$MadelineProto->[langpack->getLangPack](/API_docs/methods/langpack.getLangPack.md)(\['lang_pack' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), \]) === [$LangPackDifference](/API_docs/types/LangPackDifference.md)<a name="langpack.getLangPack"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguage](/API_docs/methods/langpack.getLanguage.md)(\['lang_pack' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), \]) === [$LangPackLanguage](/API_docs/types/LangPackLanguage.md)<a name="langpack.getLanguage"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguages](/API_docs/methods/langpack.getLanguages.md)(\['lang_pack' => [string](/API_docs/types/string.md), \]) === [$Vector\_of\_LangPackLanguage](/API_docs/types/LangPackLanguage.md)<a name="langpack.getLanguages"></a>  

***
<br><br>
$MadelineProto->[langpack->getStrings](/API_docs/methods/langpack.getStrings.md)(\['lang_pack' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), 'keys' => \[[string](/API_docs/types/string.md)\], \]) === [$Vector\_of\_LangPackString](/API_docs/types/LangPackString.md)<a name="langpack.getStrings"></a>  

***
<br><br>
$MadelineProto->[messages->acceptEncryption](/API_docs/methods/messages.acceptEncryption.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'g_b' => [bytes](/API_docs/types/bytes.md), 'key_fingerprint' => [long](/API_docs/types/long.md), \]) === [$EncryptedChat](/API_docs/types/EncryptedChat.md)<a name="messages.acceptEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->acceptUrlAuth](/API_docs/methods/messages.acceptUrlAuth.md)(\['write_allowed' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'button_id' => [int](/API_docs/types/int.md), 'url' => [string](/API_docs/types/string.md), \]) === [$UrlAuthResult](/API_docs/types/UrlAuthResult.md)<a name="messages.acceptUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->addChatUser](/API_docs/methods/messages.addChatUser.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'fwd_limit' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.addChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->checkChatInvite](/API_docs/methods/messages.checkChatInvite.md)(\['hash' => [string](/API_docs/types/string.md), \]) === [$ChatInvite](/API_docs/types/ChatInvite.md)<a name="messages.checkChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->checkHistoryImport](/API_docs/methods/messages.checkHistoryImport.md)(\['import_head' => [string](/API_docs/types/string.md), \]) === [$messages.HistoryImportParsed](/API_docs/types/messages.HistoryImportParsed.md)<a name="messages.checkHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->checkHistoryImportPeer](/API_docs/methods/messages.checkHistoryImportPeer.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.CheckedHistoryImportPeer](/API_docs/types/messages.CheckedHistoryImportPeer.md)<a name="messages.checkHistoryImportPeer"></a>  

***
<br><br>
$MadelineProto->[messages->clearAllDrafts](/API_docs/methods/messages.clearAllDrafts.md)(\[\]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.clearAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->clearRecentStickers](/API_docs/methods/messages.clearRecentStickers.md)(\['attached' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.clearRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->createChat](/API_docs/methods/messages.createChat.md)(\['users' => \[[InputUser](/API_docs/types/InputUser.md)\], 'title' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.createChat"></a>  

***
<br><br>
$MadelineProto->[messages->deleteChat](/API_docs/methods/messages.deleteChat.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.deleteChat"></a>  

***
<br><br>
$MadelineProto->[messages->deleteChatUser](/API_docs/methods/messages.deleteChatUser.md)(\['revoke_history' => [Bool](/API_docs/types/Bool.md), 'chat_id' => [InputPeer](/API_docs/types/InputPeer.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.deleteChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->deleteExportedChatInvite](/API_docs/methods/messages.deleteExportedChatInvite.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'link' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.deleteExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->deleteHistory](/API_docs/methods/messages.deleteHistory.md)(\['just_clear' => [Bool](/API_docs/types/Bool.md), 'revoke' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'max_id' => [int](/API_docs/types/int.md), 'min_date' => [int](/API_docs/types/int.md), 'max_date' => [int](/API_docs/types/int.md), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.md)<a name="messages.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[messages->deleteMessages](/API_docs/methods/messages.deleteMessages.md)(\['revoke' => [Bool](/API_docs/types/Bool.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.md)<a name="messages.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[messages->deletePhoneCallHistory](/API_docs/methods/messages.deletePhoneCallHistory.md)(\['revoke' => [Bool](/API_docs/types/Bool.md), \]) === [$messages.AffectedFoundMessages](/API_docs/types/messages.AffectedFoundMessages.md)<a name="messages.deletePhoneCallHistory"></a>  

***
<br><br>
$MadelineProto->[messages->deleteRevokedExportedChatInvites](/API_docs/methods/messages.deleteRevokedExportedChatInvites.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'admin_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.deleteRevokedExportedChatInvites"></a>  

***
<br><br>
$MadelineProto->[messages->deleteScheduledMessages](/API_docs/methods/messages.deleteScheduledMessages.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.deleteScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->discardEncryption](/API_docs/methods/messages.discardEncryption.md)(\['delete_history' => [Bool](/API_docs/types/Bool.md), 'chat_id' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.discardEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAbout](/API_docs/methods/messages.editChatAbout.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'about' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.editChatAbout"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAdmin](/API_docs/methods/messages.editChatAdmin.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'is_admin' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.editChatAdmin"></a>  

***
<br><br>
$MadelineProto->[messages->editChatDefaultBannedRights](/API_docs/methods/messages.editChatDefaultBannedRights.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.editChatDefaultBannedRights"></a>  

***
<br><br>
$MadelineProto->[messages->editChatPhoto](/API_docs/methods/messages.editChatPhoto.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), 'photo' => [InputChatPhoto](/API_docs/types/InputChatPhoto.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.editChatPhoto"></a>  

***
<br><br>
$MadelineProto->[messages->editChatTitle](/API_docs/methods/messages.editChatTitle.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), 'title' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.editChatTitle"></a>  

***
<br><br>
$MadelineProto->[messages->editExportedChatInvite](/API_docs/methods/messages.editExportedChatInvite.md)(\['revoked' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'link' => [string](/API_docs/types/string.md), 'expire_date' => [int](/API_docs/types/int.md), 'usage_limit' => [int](/API_docs/types/int.md), 'request_needed' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), \]) === [$messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.md)<a name="messages.editExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->editInlineBotMessage](/API_docs/methods/messages.editInlineBotMessage.md)(\['no_webpage' => [Bool](/API_docs/types/Bool.md), 'id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.md), 'message' => [string](/API_docs/types/string.md), 'media' => [InputMedia](/API_docs/types/InputMedia.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.editInlineBotMessage"></a>  

***
<br><br>
$MadelineProto->[messages->editMessage](/API_docs/methods/messages.editMessage.md)(\['no_webpage' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), 'media' => [InputMedia](/API_docs/types/InputMedia.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'schedule_date' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.editMessage"></a>  

***
<br><br>
$MadelineProto->[messages->exportChatInvite](/API_docs/methods/messages.exportChatInvite.md)(\['legacy_revoke_permanent' => [Bool](/API_docs/types/Bool.md), 'request_needed' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'expire_date' => [int](/API_docs/types/int.md), 'usage_limit' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), \]) === [$ExportedChatInvite](/API_docs/types/ExportedChatInvite.md)<a name="messages.exportChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->faveSticker](/API_docs/methods/messages.faveSticker.md)(\['id' => [InputDocument](/API_docs/types/InputDocument.md), 'unfave' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.faveSticker"></a>  

***
<br><br>
$MadelineProto->[messages->forwardMessages](/API_docs/methods/messages.forwardMessages.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'background' => [Bool](/API_docs/types/Bool.md), 'with_my_score' => [Bool](/API_docs/types/Bool.md), 'drop_author' => [Bool](/API_docs/types/Bool.md), 'drop_media_captions' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'from_peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], 'to_peer' => [InputPeer](/API_docs/types/InputPeer.md), 'schedule_date' => [int](/API_docs/types/int.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.forwardMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getAdminsWithInvites](/API_docs/methods/messages.getAdminsWithInvites.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.ChatAdminsWithInvites](/API_docs/types/messages.ChatAdminsWithInvites.md)<a name="messages.getAdminsWithInvites"></a>  

***
<br><br>
$MadelineProto->[messages->getAllChats](/API_docs/methods/messages.getAllChats.md)(\['except_ids' => \[[long](/API_docs/types/long.md)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="messages.getAllChats"></a>  

***
<br><br>
$MadelineProto->[messages->getAllDrafts](/API_docs/methods/messages.getAllDrafts.md)(\[\]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.getAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->getAllStickers](/API_docs/methods/messages.getAllStickers.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$messages.AllStickers](/API_docs/types/messages.AllStickers.md)<a name="messages.getAllStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getArchivedStickers](/API_docs/methods/messages.getArchivedStickers.md)(\['masks' => [Bool](/API_docs/types/Bool.md), 'offset_id' => [long](/API_docs/types/long.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.ArchivedStickers](/API_docs/types/messages.ArchivedStickers.md)<a name="messages.getArchivedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getAttachedStickers](/API_docs/methods/messages.getAttachedStickers.md)(\['media' => [InputStickeredMedia](/API_docs/types/InputStickeredMedia.md), \]) === [$Vector\_of\_StickerSetCovered](/API_docs/types/StickerSetCovered.md)<a name="messages.getAttachedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getAvailableReactions](/API_docs/methods/messages.getAvailableReactions.md)(\['hash' => [int](/API_docs/types/int.md), \]) === [$messages.AvailableReactions](/API_docs/types/messages.AvailableReactions.md)<a name="messages.getAvailableReactions"></a>  

***
<br><br>
$MadelineProto->[messages->getBotCallbackAnswer](/API_docs/methods/messages.getBotCallbackAnswer.md)(\['game' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'data' => [bytes](/API_docs/types/bytes.md), 'password' => [InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.md), \]) === [$messages.BotCallbackAnswer](/API_docs/types/messages.BotCallbackAnswer.md)<a name="messages.getBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->getChatInviteImporters](/API_docs/methods/messages.getChatInviteImporters.md)(\['requested' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'link' => [string](/API_docs/types/string.md), 'q' => [string](/API_docs/types/string.md), 'offset_date' => [int](/API_docs/types/int.md), 'offset_user' => [InputUser](/API_docs/types/InputUser.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.ChatInviteImporters](/API_docs/types/messages.ChatInviteImporters.md)<a name="messages.getChatInviteImporters"></a>  

***
<br><br>
$MadelineProto->[messages->getChats](/API_docs/methods/messages.getChats.md)(\['id' => \[[long](/API_docs/types/long.md)\], \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="messages.getChats"></a>  

***
<br><br>
$MadelineProto->[messages->getCommonChats](/API_docs/methods/messages.getCommonChats.md)(\['user_id' => [InputUser](/API_docs/types/InputUser.md), 'max_id' => [long](/API_docs/types/long.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.Chats](/API_docs/types/messages.Chats.md)<a name="messages.getCommonChats"></a>  

***
<br><br>
$MadelineProto->[messages->getDhConfig](/API_docs/methods/messages.getDhConfig.md)(\['version' => [int](/API_docs/types/int.md), 'random_length' => [int](/API_docs/types/int.md), \]) === [$messages.DhConfig](/API_docs/types/messages.DhConfig.md)<a name="messages.getDhConfig"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogFilters](/API_docs/methods/messages.getDialogFilters.md)(\[\]) === [$Vector\_of\_DialogFilter](/API_docs/types/DialogFilter.md)<a name="messages.getDialogFilters"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogUnreadMarks](/API_docs/methods/messages.getDialogUnreadMarks.md)(\[\]) === [$Vector\_of\_DialogPeer](/API_docs/types/DialogPeer.md)<a name="messages.getDialogUnreadMarks"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogs](/API_docs/methods/messages.getDialogs.md)(\['exclude_pinned' => [Bool](/API_docs/types/Bool.md), 'folder_id' => [int](/API_docs/types/int.md), 'offset_date' => [int](/API_docs/types/int.md), 'offset_id' => [int](/API_docs/types/int.md), 'offset_peer' => [InputPeer](/API_docs/types/InputPeer.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Dialogs](/API_docs/types/messages.Dialogs.md)<a name="messages.getDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getDiscussionMessage](/API_docs/methods/messages.getDiscussionMessage.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$messages.DiscussionMessage](/API_docs/types/messages.DiscussionMessage.md)<a name="messages.getDiscussionMessage"></a>  

***
<br><br>
$MadelineProto->[messages->getDocumentByHash](/API_docs/methods/messages.getDocumentByHash.md)(\['sha256' => [bytes](/API_docs/types/bytes.md), 'size' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), \]) === [$Document](/API_docs/types/Document.md)<a name="messages.getDocumentByHash"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywords](/API_docs/methods/messages.getEmojiKeywords.md)(\['lang_code' => [string](/API_docs/types/string.md), \]) === [$EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.md)<a name="messages.getEmojiKeywords"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsDifference](/API_docs/methods/messages.getEmojiKeywordsDifference.md)(\['lang_code' => [string](/API_docs/types/string.md), 'from_version' => [int](/API_docs/types/int.md), \]) === [$EmojiKeywordsDifference](/API_docs/types/EmojiKeywordsDifference.md)<a name="messages.getEmojiKeywordsDifference"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsLanguages](/API_docs/methods/messages.getEmojiKeywordsLanguages.md)(\['lang_codes' => \[[string](/API_docs/types/string.md)\], \]) === [$Vector\_of\_EmojiLanguage](/API_docs/types/EmojiLanguage.md)<a name="messages.getEmojiKeywordsLanguages"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiURL](/API_docs/methods/messages.getEmojiURL.md)(\['lang_code' => [string](/API_docs/types/string.md), \]) === [$EmojiURL](/API_docs/types/EmojiURL.md)<a name="messages.getEmojiURL"></a>  

***
<br><br>
$MadelineProto->[messages->getExportedChatInvite](/API_docs/methods/messages.getExportedChatInvite.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'link' => [string](/API_docs/types/string.md), \]) === [$messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.md)<a name="messages.getExportedChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->getExportedChatInvites](/API_docs/methods/messages.getExportedChatInvites.md)(\['revoked' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'admin_id' => [InputUser](/API_docs/types/InputUser.md), 'offset_date' => [int](/API_docs/types/int.md), 'offset_link' => [string](/API_docs/types/string.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.md)<a name="messages.getExportedChatInvites"></a>  

***
<br><br>
$MadelineProto->[messages->getFavedStickers](/API_docs/methods/messages.getFavedStickers.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$messages.FavedStickers](/API_docs/types/messages.FavedStickers.md)<a name="messages.getFavedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFeaturedStickers](/API_docs/methods/messages.getFeaturedStickers.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.md)<a name="messages.getFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFullChat](/API_docs/methods/messages.getFullChat.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.ChatFull](/API_docs/types/messages.ChatFull.md)<a name="messages.getFullChat"></a>  

***
<br><br>
$MadelineProto->[messages->getGameHighScores](/API_docs/methods/messages.getGameHighScores.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$messages.HighScores](/API_docs/types/messages.HighScores.md)<a name="messages.getGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getHistory](/API_docs/methods/messages.getHistory.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'offset_id' => [int](/API_docs/types/int.md), 'offset_date' => [int](/API_docs/types/int.md), 'add_offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'max_id' => [int](/API_docs/types/int.md), 'min_id' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineBotResults](/API_docs/methods/messages.getInlineBotResults.md)(\['bot' => [InputUser](/API_docs/types/InputUser.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'query' => [string](/API_docs/types/string.md), 'offset' => [string](/API_docs/types/string.md), \]) === [$messages.BotResults](/API_docs/types/messages.BotResults.md)<a name="messages.getInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineGameHighScores](/API_docs/methods/messages.getInlineGameHighScores.md)(\['id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$messages.HighScores](/API_docs/types/messages.HighScores.md)<a name="messages.getInlineGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getMaskStickers](/API_docs/methods/messages.getMaskStickers.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$messages.AllStickers](/API_docs/types/messages.AllStickers.md)<a name="messages.getMaskStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageEditData](/API_docs/methods/messages.getMessageEditData.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), \]) === [$messages.MessageEditData](/API_docs/types/messages.MessageEditData.md)<a name="messages.getMessageEditData"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageReactionsList](/API_docs/methods/messages.getMessageReactionsList.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), 'reaction' => [string](/API_docs/types/string.md), 'offset' => [string](/API_docs/types/string.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.MessageReactionsList](/API_docs/types/messages.MessageReactionsList.md)<a name="messages.getMessageReactionsList"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageReadParticipants](/API_docs/methods/messages.getMessageReadParticipants.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$Vector\_of\_long](/API_docs/types/long.md)<a name="messages.getMessageReadParticipants"></a>  

***
<br><br>
$MadelineProto->[messages->getMessages](/API_docs/methods/messages.getMessages.md)(\['id' => \[[InputMessage](/API_docs/types/InputMessage.md)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getMessagesReactions](/API_docs/methods/messages.getMessagesReactions.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.getMessagesReactions"></a>  

***
<br><br>
$MadelineProto->[messages->getMessagesViews](/API_docs/methods/messages.getMessagesViews.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], 'increment' => [Bool](/API_docs/types/Bool.md), \]) === [$messages.MessageViews](/API_docs/types/messages.MessageViews.md)<a name="messages.getMessagesViews"></a>  

***
<br><br>
$MadelineProto->[messages->getOldFeaturedStickers](/API_docs/methods/messages.getOldFeaturedStickers.md)(\['offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.md)<a name="messages.getOldFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getOnlines](/API_docs/methods/messages.getOnlines.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$ChatOnlines](/API_docs/types/ChatOnlines.md)<a name="messages.getOnlines"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerDialogs](/API_docs/methods/messages.getPeerDialogs.md)(\['peers' => \[[InputDialogPeer](/API_docs/types/InputDialogPeer.md)\], \]) === [$messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.md)<a name="messages.getPeerDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerSettings](/API_docs/methods/messages.getPeerSettings.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.PeerSettings](/API_docs/types/messages.PeerSettings.md)<a name="messages.getPeerSettings"></a>  

***
<br><br>
$MadelineProto->[messages->getPinnedDialogs](/API_docs/methods/messages.getPinnedDialogs.md)(\['folder_id' => [int](/API_docs/types/int.md), \]) === [$messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.md)<a name="messages.getPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPollResults](/API_docs/methods/messages.getPollResults.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.getPollResults"></a>  

***
<br><br>
$MadelineProto->[messages->getPollVotes](/API_docs/methods/messages.getPollVotes.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), 'option' => [bytes](/API_docs/types/bytes.md), 'offset' => [string](/API_docs/types/string.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.VotesList](/API_docs/types/messages.VotesList.md)<a name="messages.getPollVotes"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentLocations](/API_docs/methods/messages.getRecentLocations.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getRecentLocations"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentStickers](/API_docs/methods/messages.getRecentStickers.md)(\['attached' => [Bool](/API_docs/types/Bool.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.RecentStickers](/API_docs/types/messages.RecentStickers.md)<a name="messages.getRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getReplies](/API_docs/methods/messages.getReplies.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'offset_id' => [int](/API_docs/types/int.md), 'offset_date' => [int](/API_docs/types/int.md), 'add_offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'max_id' => [int](/API_docs/types/int.md), 'min_id' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getReplies"></a>  

***
<br><br>
$MadelineProto->[messages->getSavedGifs](/API_docs/methods/messages.getSavedGifs.md)(\['hash' => [long](/API_docs/types/long.md), \]) === [$messages.SavedGifs](/API_docs/types/messages.SavedGifs.md)<a name="messages.getSavedGifs"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledHistory](/API_docs/methods/messages.getScheduledHistory.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getScheduledHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledMessages](/API_docs/methods/messages.getScheduledMessages.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchCounters](/API_docs/methods/messages.getSearchCounters.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'filters' => \[[MessagesFilter](/API_docs/types/MessagesFilter.md)\], \]) === [$Vector\_of\_messages.SearchCounter](/API_docs/types/messages.SearchCounter.md)<a name="messages.getSearchCounters"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchResultsCalendar](/API_docs/methods/messages.getSearchResultsCalendar.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.md), 'offset_id' => [int](/API_docs/types/int.md), 'offset_date' => [int](/API_docs/types/int.md), \]) === [$messages.SearchResultsCalendar](/API_docs/types/messages.SearchResultsCalendar.md)<a name="messages.getSearchResultsCalendar"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchResultsPositions](/API_docs/methods/messages.getSearchResultsPositions.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.md), 'offset_id' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.SearchResultsPositions](/API_docs/types/messages.SearchResultsPositions.md)<a name="messages.getSearchResultsPositions"></a>  

***
<br><br>
$MadelineProto->[messages->getSplitRanges](/API_docs/methods/messages.getSplitRanges.md)(\[\]) === [$Vector\_of\_MessageRange](/API_docs/types/MessageRange.md)<a name="messages.getSplitRanges"></a>  

***
<br><br>
$MadelineProto->[messages->getStickerSet](/API_docs/methods/messages.getStickerSet.md)(\['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'hash' => [int](/API_docs/types/int.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="messages.getStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->getStickers](/API_docs/methods/messages.getStickers.md)(\['emoticon' => [string](/API_docs/types/string.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Stickers](/API_docs/types/messages.Stickers.md)<a name="messages.getStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getSuggestedDialogFilters](/API_docs/methods/messages.getSuggestedDialogFilters.md)(\[\]) === [$Vector\_of\_DialogFilterSuggested](/API_docs/types/DialogFilterSuggested.md)<a name="messages.getSuggestedDialogFilters"></a>  

***
<br><br>
$MadelineProto->[messages->getUnreadMentions](/API_docs/methods/messages.getUnreadMentions.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'offset_id' => [int](/API_docs/types/int.md), 'add_offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'max_id' => [int](/API_docs/types/int.md), 'min_id' => [int](/API_docs/types/int.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.getUnreadMentions"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPage](/API_docs/methods/messages.getWebPage.md)(\['url' => [string](/API_docs/types/string.md), 'hash' => [int](/API_docs/types/int.md), \]) === [$WebPage](/API_docs/types/WebPage.md)<a name="messages.getWebPage"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPagePreview](/API_docs/methods/messages.getWebPagePreview.md)(\['message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \]) === [$MessageMedia](/API_docs/types/MessageMedia.md)<a name="messages.getWebPagePreview"></a>  

***
<br><br>
$MadelineProto->[messages->hideAllChatJoinRequests](/API_docs/methods/messages.hideAllChatJoinRequests.md)(\['approved' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'link' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.hideAllChatJoinRequests"></a>  

***
<br><br>
$MadelineProto->[messages->hideChatJoinRequest](/API_docs/methods/messages.hideChatJoinRequest.md)(\['approved' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.hideChatJoinRequest"></a>  

***
<br><br>
$MadelineProto->[messages->hidePeerSettingsBar](/API_docs/methods/messages.hidePeerSettingsBar.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.hidePeerSettingsBar"></a>  

***
<br><br>
$MadelineProto->[messages->importChatInvite](/API_docs/methods/messages.importChatInvite.md)(\['hash' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.importChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->initHistoryImport](/API_docs/methods/messages.initHistoryImport.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'file' => [InputFile](/API_docs/types/InputFile.md), 'media_count' => [int](/API_docs/types/int.md), \]) === [$messages.HistoryImport](/API_docs/types/messages.HistoryImport.md)<a name="messages.initHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->installStickerSet](/API_docs/methods/messages.installStickerSet.md)(\['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'archived' => [Bool](/API_docs/types/Bool.md), \]) === [$messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.md)<a name="messages.installStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->markDialogUnread](/API_docs/methods/messages.markDialogUnread.md)(\['unread' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputDialogPeer](/API_docs/types/InputDialogPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.markDialogUnread"></a>  

***
<br><br>
$MadelineProto->[messages->migrateChat](/API_docs/methods/messages.migrateChat.md)(\['chat_id' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.migrateChat"></a>  

***
<br><br>
$MadelineProto->[messages->readDiscussion](/API_docs/methods/messages.readDiscussion.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'read_max_id' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.readDiscussion"></a>  

***
<br><br>
$MadelineProto->[messages->readEncryptedHistory](/API_docs/methods/messages.readEncryptedHistory.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'max_date' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.readEncryptedHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readFeaturedStickers](/API_docs/methods/messages.readFeaturedStickers.md)(\['id' => \[[long](/API_docs/types/long.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.readFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->readHistory](/API_docs/methods/messages.readHistory.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'max_id' => [int](/API_docs/types/int.md), \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.md)<a name="messages.readHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readMentions](/API_docs/methods/messages.readMentions.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.md)<a name="messages.readMentions"></a>  

***
<br><br>
$MadelineProto->[messages->readMessageContents](/API_docs/methods/messages.readMessageContents.md)(\['id' => \[[int](/API_docs/types/int.md)\], \]) === [$messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.md)<a name="messages.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[messages->receivedMessages](/API_docs/methods/messages.receivedMessages.md)(\['max_id' => [int](/API_docs/types/int.md), \]) === [$Vector\_of\_ReceivedNotifyMessage](/API_docs/types/ReceivedNotifyMessage.md)<a name="messages.receivedMessages"></a>  

***
<br><br>
$MadelineProto->[messages->receivedQueue](/API_docs/methods/messages.receivedQueue.md)(\['max_qts' => [int](/API_docs/types/int.md), \]) === [$Vector\_of\_long](/API_docs/types/long.md)<a name="messages.receivedQueue"></a>  

***
<br><br>
$MadelineProto->[messages->reorderPinnedDialogs](/API_docs/methods/messages.reorderPinnedDialogs.md)(\['force' => [Bool](/API_docs/types/Bool.md), 'folder_id' => [int](/API_docs/types/int.md), 'order' => \[[InputDialogPeer](/API_docs/types/InputDialogPeer.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.reorderPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->reorderStickerSets](/API_docs/methods/messages.reorderStickerSets.md)(\['masks' => [Bool](/API_docs/types/Bool.md), 'order' => \[[long](/API_docs/types/long.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.reorderStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->report](/API_docs/methods/messages.report.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], 'reason' => [ReportReason](/API_docs/types/ReportReason.md), 'message' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.report"></a>  

***
<br><br>
$MadelineProto->[messages->reportEncryptedSpam](/API_docs/methods/messages.reportEncryptedSpam.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.reportEncryptedSpam"></a>  

***
<br><br>
$MadelineProto->[messages->reportSpam](/API_docs/methods/messages.reportSpam.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.reportSpam"></a>  

***
<br><br>
$MadelineProto->[messages->requestEncryption](/API_docs/methods/messages.requestEncryption.md)(\['user_id' => [InputUser](/API_docs/types/InputUser.md), 'g_a' => [bytes](/API_docs/types/bytes.md), \]) === [$EncryptedChat](/API_docs/types/EncryptedChat.md)<a name="messages.requestEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->requestUrlAuth](/API_docs/methods/messages.requestUrlAuth.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'button_id' => [int](/API_docs/types/int.md), 'url' => [string](/API_docs/types/string.md), \]) === [$UrlAuthResult](/API_docs/types/UrlAuthResult.md)<a name="messages.requestUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->saveDefaultSendAs](/API_docs/methods/messages.saveDefaultSendAs.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.saveDefaultSendAs"></a>  

***
<br><br>
$MadelineProto->[messages->saveDraft](/API_docs/methods/messages.saveDraft.md)(\['no_webpage' => [Bool](/API_docs/types/Bool.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.saveDraft"></a>  

***
<br><br>
$MadelineProto->[messages->saveGif](/API_docs/methods/messages.saveGif.md)(\['id' => [InputDocument](/API_docs/types/InputDocument.md), 'unsave' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.saveGif"></a>  

***
<br><br>
$MadelineProto->[messages->saveRecentSticker](/API_docs/methods/messages.saveRecentSticker.md)(\['attached' => [Bool](/API_docs/types/Bool.md), 'id' => [InputDocument](/API_docs/types/InputDocument.md), 'unsave' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.saveRecentSticker"></a>  

***
<br><br>
$MadelineProto->[messages->search](/API_docs/methods/messages.search.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'q' => [string](/API_docs/types/string.md), 'from_id' => [InputPeer](/API_docs/types/InputPeer.md), 'top_msg_id' => [int](/API_docs/types/int.md), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.md), 'min_date' => [int](/API_docs/types/int.md), 'max_date' => [int](/API_docs/types/int.md), 'offset_id' => [int](/API_docs/types/int.md), 'add_offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'max_id' => [int](/API_docs/types/int.md), 'min_id' => [int](/API_docs/types/int.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.search"></a>  

***
<br><br>
$MadelineProto->[messages->searchGlobal](/API_docs/methods/messages.searchGlobal.md)(\['folder_id' => [int](/API_docs/types/int.md), 'q' => [string](/API_docs/types/string.md), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.md), 'min_date' => [int](/API_docs/types/int.md), 'max_date' => [int](/API_docs/types/int.md), 'offset_rate' => [int](/API_docs/types/int.md), 'offset_peer' => [InputPeer](/API_docs/types/InputPeer.md), 'offset_id' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="messages.searchGlobal"></a>  

***
<br><br>
$MadelineProto->[messages->searchStickerSets](/API_docs/methods/messages.searchStickerSets.md)(\['exclude_featured' => [Bool](/API_docs/types/Bool.md), 'q' => [string](/API_docs/types/string.md), 'hash' => [long](/API_docs/types/long.md), \]) === [$messages.FoundStickerSets](/API_docs/types/messages.FoundStickerSets.md)<a name="messages.searchStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncrypted](/API_docs/methods/messages.sendEncrypted.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'data' => [bytes](/API_docs/types/bytes.md), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.md)<a name="messages.sendEncrypted"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedFile](/API_docs/methods/messages.sendEncryptedFile.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'data' => [bytes](/API_docs/types/bytes.md), 'file' => [InputEncryptedFile](/API_docs/types/InputEncryptedFile.md), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.md)<a name="messages.sendEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedService](/API_docs/methods/messages.sendEncryptedService.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'data' => [bytes](/API_docs/types/bytes.md), \]) === [$messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.md)<a name="messages.sendEncryptedService"></a>  

***
<br><br>
$MadelineProto->[messages->sendInlineBotResult](/API_docs/methods/messages.sendInlineBotResult.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'background' => [Bool](/API_docs/types/Bool.md), 'clear_draft' => [Bool](/API_docs/types/Bool.md), 'hide_via' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'query_id' => [long](/API_docs/types/long.md), 'id' => [string](/API_docs/types/string.md), 'schedule_date' => [int](/API_docs/types/int.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendInlineBotResult"></a>  

***
<br><br>
$MadelineProto->[messages->sendMedia](/API_docs/methods/messages.sendMedia.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'background' => [Bool](/API_docs/types/Bool.md), 'clear_draft' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'media' => [InputMedia](/API_docs/types/InputMedia.md), 'message' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'schedule_date' => [int](/API_docs/types/int.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendMessage](/API_docs/methods/messages.sendMessage.md)(\['no_webpage' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'background' => [Bool](/API_docs/types/Bool.md), 'clear_draft' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'schedule_date' => [int](/API_docs/types/int.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendMessage"></a>  

***
<br><br>
$MadelineProto->[messages->sendMultiMedia](/API_docs/methods/messages.sendMultiMedia.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'background' => [Bool](/API_docs/types/Bool.md), 'clear_draft' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'multi_media' => \[[InputSingleMedia](/API_docs/types/InputSingleMedia.md)\], 'schedule_date' => [int](/API_docs/types/int.md), 'send_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendMultiMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendReaction](/API_docs/methods/messages.sendReaction.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'reaction' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendReaction"></a>  

***
<br><br>
$MadelineProto->[messages->sendScheduledMessages](/API_docs/methods/messages.sendScheduledMessages.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => \[[int](/API_docs/types/int.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->sendScreenshotNotification](/API_docs/methods/messages.sendScreenshotNotification.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendScreenshotNotification"></a>  

***
<br><br>
$MadelineProto->[messages->sendVote](/API_docs/methods/messages.sendVote.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'options' => \[[bytes](/API_docs/types/bytes.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.sendVote"></a>  

***
<br><br>
$MadelineProto->[messages->setBotCallbackAnswer](/API_docs/methods/messages.setBotCallbackAnswer.md)(\['alert' => [Bool](/API_docs/types/Bool.md), 'query_id' => [long](/API_docs/types/long.md), 'message' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'cache_time' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->setBotPrecheckoutResults](/API_docs/methods/messages.setBotPrecheckoutResults.md)(\['success' => [Bool](/API_docs/types/Bool.md), 'query_id' => [long](/API_docs/types/long.md), 'error' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setBotPrecheckoutResults"></a>  

***
<br><br>
$MadelineProto->[messages->setBotShippingResults](/API_docs/methods/messages.setBotShippingResults.md)(\['query_id' => [long](/API_docs/types/long.md), 'error' => [string](/API_docs/types/string.md), 'shipping_options' => \[[ShippingOption](/API_docs/types/ShippingOption.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setBotShippingResults"></a>  

***
<br><br>
$MadelineProto->[messages->setChatAvailableReactions](/API_docs/methods/messages.setChatAvailableReactions.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'available_reactions' => \[[string](/API_docs/types/string.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.setChatAvailableReactions"></a>  

***
<br><br>
$MadelineProto->[messages->setChatTheme](/API_docs/methods/messages.setChatTheme.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'emoticon' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.setChatTheme"></a>  

***
<br><br>
$MadelineProto->[messages->setDefaultReaction](/API_docs/methods/messages.setDefaultReaction.md)(\['reaction' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setDefaultReaction"></a>  

***
<br><br>
$MadelineProto->[messages->setEncryptedTyping](/API_docs/methods/messages.setEncryptedTyping.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'typing' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setEncryptedTyping"></a>  

***
<br><br>
$MadelineProto->[messages->setGameScore](/API_docs/methods/messages.setGameScore.md)(\['edit_message' => [Bool](/API_docs/types/Bool.md), 'force' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'score' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.setGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setHistoryTTL](/API_docs/methods/messages.setHistoryTTL.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'period' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.setHistoryTTL"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineBotResults](/API_docs/methods/messages.setInlineBotResults.md)(\['gallery' => [Bool](/API_docs/types/Bool.md), 'private' => [Bool](/API_docs/types/Bool.md), 'query_id' => [long](/API_docs/types/long.md), 'results' => \[[InputBotInlineResult](/API_docs/types/InputBotInlineResult.md)\], 'cache_time' => [int](/API_docs/types/int.md), 'next_offset' => [string](/API_docs/types/string.md), 'switch_pm' => [InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineGameScore](/API_docs/methods/messages.setInlineGameScore.md)(\['edit_message' => [Bool](/API_docs/types/Bool.md), 'force' => [Bool](/API_docs/types/Bool.md), 'id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'score' => [int](/API_docs/types/int.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setInlineGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setTyping](/API_docs/methods/messages.setTyping.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'top_msg_id' => [int](/API_docs/types/int.md), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.setTyping"></a>  

***
<br><br>
$MadelineProto->[messages->startBot](/API_docs/methods/messages.startBot.md)(\['bot' => [InputUser](/API_docs/types/InputUser.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'start_param' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.startBot"></a>  

***
<br><br>
$MadelineProto->[messages->startHistoryImport](/API_docs/methods/messages.startHistoryImport.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'import_id' => [long](/API_docs/types/long.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.startHistoryImport"></a>  

***
<br><br>
$MadelineProto->[messages->toggleDialogPin](/API_docs/methods/messages.toggleDialogPin.md)(\['pinned' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputDialogPeer](/API_docs/types/InputDialogPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.toggleDialogPin"></a>  

***
<br><br>
$MadelineProto->[messages->toggleNoForwards](/API_docs/methods/messages.toggleNoForwards.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'enabled' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.toggleNoForwards"></a>  

***
<br><br>
$MadelineProto->[messages->toggleStickerSets](/API_docs/methods/messages.toggleStickerSets.md)(\['uninstall' => [Bool](/API_docs/types/Bool.md), 'archive' => [Bool](/API_docs/types/Bool.md), 'unarchive' => [Bool](/API_docs/types/Bool.md), 'stickersets' => \[[InputStickerSet](/API_docs/types/InputStickerSet.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.toggleStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->uninstallStickerSet](/API_docs/methods/messages.uninstallStickerSet.md)(\['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.uninstallStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->unpinAllMessages](/API_docs/methods/messages.unpinAllMessages.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.md)<a name="messages.unpinAllMessages"></a>  

***
<br><br>
$MadelineProto->[messages->updateDialogFilter](/API_docs/methods/messages.updateDialogFilter.md)(\['id' => [int](/API_docs/types/int.md), 'filter' => [DialogFilter](/API_docs/types/DialogFilter.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.updateDialogFilter"></a>  

***
<br><br>
$MadelineProto->[messages->updateDialogFiltersOrder](/API_docs/methods/messages.updateDialogFiltersOrder.md)(\['order' => \[[int](/API_docs/types/int.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="messages.updateDialogFiltersOrder"></a>  

***
<br><br>
$MadelineProto->[messages->updatePinnedMessage](/API_docs/methods/messages.updatePinnedMessage.md)(\['silent' => [Bool](/API_docs/types/Bool.md), 'unpin' => [Bool](/API_docs/types/Bool.md), 'pm_oneside' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'id' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="messages.updatePinnedMessage"></a>  

***
<br><br>
$MadelineProto->[messages->uploadEncryptedFile](/API_docs/methods/messages.uploadEncryptedFile.md)(\['peer' => [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md), 'file' => [InputEncryptedFile](/API_docs/types/InputEncryptedFile.md), \]) === [$EncryptedFile](/API_docs/types/EncryptedFile.md)<a name="messages.uploadEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->uploadImportedMedia](/API_docs/methods/messages.uploadImportedMedia.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'import_id' => [long](/API_docs/types/long.md), 'file_name' => [string](/API_docs/types/string.md), 'media' => [InputMedia](/API_docs/types/InputMedia.md), \]) === [$MessageMedia](/API_docs/types/MessageMedia.md)<a name="messages.uploadImportedMedia"></a>  

***
<br><br>
$MadelineProto->[messages->uploadMedia](/API_docs/methods/messages.uploadMedia.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'media' => [InputMedia](/API_docs/types/InputMedia.md), \]) === [$MessageMedia](/API_docs/types/MessageMedia.md)<a name="messages.uploadMedia"></a>  

***
<br><br>
$MadelineProto->[payments->clearSavedInfo](/API_docs/methods/payments.clearSavedInfo.md)(\['credentials' => [Bool](/API_docs/types/Bool.md), 'info' => [Bool](/API_docs/types/Bool.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="payments.clearSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->getBankCardData](/API_docs/methods/payments.getBankCardData.md)(\['number' => [string](/API_docs/types/string.md), \]) === [$payments.BankCardData](/API_docs/types/payments.BankCardData.md)<a name="payments.getBankCardData"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentForm](/API_docs/methods/payments.getPaymentForm.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'theme_params' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$payments.PaymentForm](/API_docs/types/payments.PaymentForm.md)<a name="payments.getPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentReceipt](/API_docs/methods/payments.getPaymentReceipt.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.md)<a name="payments.getPaymentReceipt"></a>  

***
<br><br>
$MadelineProto->[payments->getSavedInfo](/API_docs/methods/payments.getSavedInfo.md)(\[\]) === [$payments.SavedInfo](/API_docs/types/payments.SavedInfo.md)<a name="payments.getSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->sendPaymentForm](/API_docs/methods/payments.sendPaymentForm.md)(\['form_id' => [long](/API_docs/types/long.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'requested_info_id' => [string](/API_docs/types/string.md), 'shipping_option_id' => [string](/API_docs/types/string.md), 'credentials' => [InputPaymentCredentials](/API_docs/types/InputPaymentCredentials.md), 'tip_amount' => [long](/API_docs/types/long.md), \]) === [$payments.PaymentResult](/API_docs/types/payments.PaymentResult.md)<a name="payments.sendPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->validateRequestedInfo](/API_docs/methods/payments.validateRequestedInfo.md)(\['save' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), \]) === [$payments.ValidatedRequestedInfo](/API_docs/types/payments.ValidatedRequestedInfo.md)<a name="payments.validateRequestedInfo"></a>  

***
<br><br>
$MadelineProto->[phone->acceptCall](/API_docs/methods/phone.acceptCall.md)(\['peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'g_b' => [bytes](/API_docs/types/bytes.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.md)<a name="phone.acceptCall"></a>  

***
<br><br>
$MadelineProto->[phone->checkGroupCall](/API_docs/methods/phone.checkGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'sources' => \[[int](/API_docs/types/int.md)\], \]) === [$Vector\_of\_int](/API_docs/types/int.md)<a name="phone.checkGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->confirmCall](/API_docs/methods/phone.confirmCall.md)(\['peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'g_a' => [bytes](/API_docs/types/bytes.md), 'key_fingerprint' => [long](/API_docs/types/long.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.md)<a name="phone.confirmCall"></a>  

***
<br><br>
$MadelineProto->[phone->createGroupCall](/API_docs/methods/phone.createGroupCall.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'title' => [string](/API_docs/types/string.md), 'schedule_date' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.createGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->discardCall](/API_docs/methods/phone.discardCall.md)(\['video' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'duration' => [int](/API_docs/types/int.md), 'reason' => [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.md), 'connection_id' => [long](/API_docs/types/long.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.discardCall"></a>  

***
<br><br>
$MadelineProto->[phone->discardGroupCall](/API_docs/methods/phone.discardGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.discardGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->editGroupCallParticipant](/API_docs/methods/phone.editGroupCallParticipant.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'participant' => [InputPeer](/API_docs/types/InputPeer.md), 'muted' => [Bool](/API_docs/types/Bool.md), 'volume' => [int](/API_docs/types/int.md), 'raise_hand' => [Bool](/API_docs/types/Bool.md), 'video_stopped' => [Bool](/API_docs/types/Bool.md), 'video_paused' => [Bool](/API_docs/types/Bool.md), 'presentation_paused' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.editGroupCallParticipant"></a>  

***
<br><br>
$MadelineProto->[phone->editGroupCallTitle](/API_docs/methods/phone.editGroupCallTitle.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'title' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.editGroupCallTitle"></a>  

***
<br><br>
$MadelineProto->[phone->exportGroupCallInvite](/API_docs/methods/phone.exportGroupCallInvite.md)(\['can_self_unmute' => [Bool](/API_docs/types/Bool.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \]) === [$phone.ExportedGroupCallInvite](/API_docs/types/phone.ExportedGroupCallInvite.md)<a name="phone.exportGroupCallInvite"></a>  

***
<br><br>
$MadelineProto->[phone->getCallConfig](/API_docs/methods/phone.getCallConfig.md)(\[\]) === [$DataJSON](/API_docs/types/DataJSON.md)<a name="phone.getCallConfig"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCall](/API_docs/methods/phone.getGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$phone.GroupCall](/API_docs/types/phone.GroupCall.md)<a name="phone.getGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupCallJoinAs](/API_docs/methods/phone.getGroupCallJoinAs.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.md)<a name="phone.getGroupCallJoinAs"></a>  

***
<br><br>
$MadelineProto->[phone->getGroupParticipants](/API_docs/methods/phone.getGroupParticipants.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'ids' => \[[InputPeer](/API_docs/types/InputPeer.md)\], 'sources' => \[[int](/API_docs/types/int.md)\], 'offset' => [string](/API_docs/types/string.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.md)<a name="phone.getGroupParticipants"></a>  

***
<br><br>
$MadelineProto->[phone->inviteToGroupCall](/API_docs/methods/phone.inviteToGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'users' => \[[InputUser](/API_docs/types/InputUser.md)\], \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.inviteToGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->joinGroupCall](/API_docs/methods/phone.joinGroupCall.md)(\['muted' => [Bool](/API_docs/types/Bool.md), 'video_stopped' => [Bool](/API_docs/types/Bool.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'join_as' => [InputPeer](/API_docs/types/InputPeer.md), 'invite_hash' => [string](/API_docs/types/string.md), 'params' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.joinGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->joinGroupCallPresentation](/API_docs/methods/phone.joinGroupCallPresentation.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'params' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.joinGroupCallPresentation"></a>  

***
<br><br>
$MadelineProto->[phone->leaveGroupCall](/API_docs/methods/phone.leaveGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'source' => [int](/API_docs/types/int.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.leaveGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->leaveGroupCallPresentation](/API_docs/methods/phone.leaveGroupCallPresentation.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.leaveGroupCallPresentation"></a>  

***
<br><br>
$MadelineProto->[phone->receivedCall](/API_docs/methods/phone.receivedCall.md)(\['peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="phone.receivedCall"></a>  

***
<br><br>
$MadelineProto->[phone->requestCall](/API_docs/methods/phone.requestCall.md)(\['video' => [Bool](/API_docs/types/Bool.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'g_a_hash' => [bytes](/API_docs/types/bytes.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](/API_docs/types/phone.PhoneCall.md)<a name="phone.requestCall"></a>  

***
<br><br>
$MadelineProto->[phone->saveCallDebug](/API_docs/methods/phone.saveCallDebug.md)(\['peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'debug' => [DataJSON](/API_docs/types/DataJSON.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="phone.saveCallDebug"></a>  

***
<br><br>
$MadelineProto->[phone->saveDefaultGroupCallJoinAs](/API_docs/methods/phone.saveDefaultGroupCallJoinAs.md)(\['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'join_as' => [InputPeer](/API_docs/types/InputPeer.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="phone.saveDefaultGroupCallJoinAs"></a>  

***
<br><br>
$MadelineProto->[phone->sendSignalingData](/API_docs/methods/phone.sendSignalingData.md)(\['peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'data' => [bytes](/API_docs/types/bytes.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="phone.sendSignalingData"></a>  

***
<br><br>
$MadelineProto->[phone->setCallRating](/API_docs/methods/phone.setCallRating.md)(\['user_initiative' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPhoneCall](/API_docs/types/InputPhoneCall.md), 'rating' => [int](/API_docs/types/int.md), 'comment' => [string](/API_docs/types/string.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.setCallRating"></a>  

***
<br><br>
$MadelineProto->[phone->startScheduledGroupCall](/API_docs/methods/phone.startScheduledGroupCall.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.startScheduledGroupCall"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallRecord](/API_docs/methods/phone.toggleGroupCallRecord.md)(\['start' => [Bool](/API_docs/types/Bool.md), 'video' => [Bool](/API_docs/types/Bool.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'title' => [string](/API_docs/types/string.md), 'video_portrait' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.toggleGroupCallRecord"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallSettings](/API_docs/methods/phone.toggleGroupCallSettings.md)(\['reset_invite_hash' => [Bool](/API_docs/types/Bool.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'join_muted' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.toggleGroupCallSettings"></a>  

***
<br><br>
$MadelineProto->[phone->toggleGroupCallStartSubscription](/API_docs/methods/phone.toggleGroupCallStartSubscription.md)(\['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'subscribed' => [Bool](/API_docs/types/Bool.md), \]) === [$Updates](/API_docs/types/Updates.md)<a name="phone.toggleGroupCallStartSubscription"></a>  

***
<br><br>
$MadelineProto->[photos->deletePhotos](/API_docs/methods/photos.deletePhotos.md)(\['id' => \[[InputPhoto](/API_docs/types/InputPhoto.md)\], \]) === [$Vector\_of\_long](/API_docs/types/long.md)<a name="photos.deletePhotos"></a>  

***
<br><br>
$MadelineProto->[photos->getUserPhotos](/API_docs/methods/photos.getUserPhotos.md)(\['user_id' => [InputUser](/API_docs/types/InputUser.md), 'offset' => [int](/API_docs/types/int.md), 'max_id' => [long](/API_docs/types/long.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$photos.Photos](/API_docs/types/photos.Photos.md)<a name="photos.getUserPhotos"></a>  

***
<br><br>
$MadelineProto->[photos->updateProfilePhoto](/API_docs/methods/photos.updateProfilePhoto.md)(\['id' => [InputPhoto](/API_docs/types/InputPhoto.md), \]) === [$photos.Photo](/API_docs/types/photos.Photo.md)<a name="photos.updateProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[photos->uploadProfilePhoto](/API_docs/methods/photos.uploadProfilePhoto.md)(\['file' => [InputFile](/API_docs/types/InputFile.md), 'video' => [InputFile](/API_docs/types/InputFile.md), 'video_start_ts' => [double](/API_docs/types/double.md), \]) === [$photos.Photo](/API_docs/types/photos.Photo.md)<a name="photos.uploadProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[stats->getBroadcastStats](/API_docs/methods/stats.getBroadcastStats.md)(\['dark' => [Bool](/API_docs/types/Bool.md), 'channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$stats.BroadcastStats](/API_docs/types/stats.BroadcastStats.md)<a name="stats.getBroadcastStats"></a>  

***
<br><br>
$MadelineProto->[stats->getMegagroupStats](/API_docs/methods/stats.getMegagroupStats.md)(\['dark' => [Bool](/API_docs/types/Bool.md), 'channel' => [InputChannel](/API_docs/types/InputChannel.md), \]) === [$stats.MegagroupStats](/API_docs/types/stats.MegagroupStats.md)<a name="stats.getMegagroupStats"></a>  

***
<br><br>
$MadelineProto->[stats->getMessagePublicForwards](/API_docs/methods/stats.getMessagePublicForwards.md)(\['channel' => [InputChannel](/API_docs/types/InputChannel.md), 'msg_id' => [int](/API_docs/types/int.md), 'offset_rate' => [int](/API_docs/types/int.md), 'offset_peer' => [InputPeer](/API_docs/types/InputPeer.md), 'offset_id' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$messages.Messages](/API_docs/types/messages.Messages.md)<a name="stats.getMessagePublicForwards"></a>  

***
<br><br>
$MadelineProto->[stats->getMessageStats](/API_docs/methods/stats.getMessageStats.md)(\['dark' => [Bool](/API_docs/types/Bool.md), 'channel' => [InputChannel](/API_docs/types/InputChannel.md), 'msg_id' => [int](/API_docs/types/int.md), \]) === [$stats.MessageStats](/API_docs/types/stats.MessageStats.md)<a name="stats.getMessageStats"></a>  

***
<br><br>
$MadelineProto->[stats->loadAsyncGraph](/API_docs/methods/stats.loadAsyncGraph.md)(\['token' => [string](/API_docs/types/string.md), 'x' => [long](/API_docs/types/long.md), \]) === [$StatsGraph](/API_docs/types/StatsGraph.md)<a name="stats.loadAsyncGraph"></a>  

***
<br><br>
$MadelineProto->[stickers->addStickerToSet](/API_docs/methods/stickers.addStickerToSet.md)(\['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'sticker' => [InputStickerSetItem](/API_docs/types/InputStickerSetItem.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="stickers.addStickerToSet"></a>  

***
<br><br>
$MadelineProto->[stickers->changeStickerPosition](/API_docs/methods/stickers.changeStickerPosition.md)(\['sticker' => [InputDocument](/API_docs/types/InputDocument.md), 'position' => [int](/API_docs/types/int.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="stickers.changeStickerPosition"></a>  

***
<br><br>
$MadelineProto->[stickers->checkShortName](/API_docs/methods/stickers.checkShortName.md)(\['short_name' => [string](/API_docs/types/string.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="stickers.checkShortName"></a>  

***
<br><br>
$MadelineProto->[stickers->createStickerSet](/API_docs/methods/stickers.createStickerSet.md)(\['masks' => [Bool](/API_docs/types/Bool.md), 'animated' => [Bool](/API_docs/types/Bool.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), 'title' => [string](/API_docs/types/string.md), 'short_name' => [string](/API_docs/types/string.md), 'thumb' => [InputDocument](/API_docs/types/InputDocument.md), 'stickers' => \[[InputStickerSetItem](/API_docs/types/InputStickerSetItem.md)\], 'software' => [string](/API_docs/types/string.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="stickers.createStickerSet"></a>  

***
<br><br>
$MadelineProto->[stickers->removeStickerFromSet](/API_docs/methods/stickers.removeStickerFromSet.md)(\['sticker' => [InputDocument](/API_docs/types/InputDocument.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="stickers.removeStickerFromSet"></a>  

***
<br><br>
$MadelineProto->[stickers->setStickerSetThumb](/API_docs/methods/stickers.setStickerSetThumb.md)(\['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'thumb' => [InputDocument](/API_docs/types/InputDocument.md), \]) === [$messages.StickerSet](/API_docs/types/messages.StickerSet.md)<a name="stickers.setStickerSetThumb"></a>  

***
<br><br>
$MadelineProto->[stickers->suggestShortName](/API_docs/methods/stickers.suggestShortName.md)(\['title' => [string](/API_docs/types/string.md), \]) === [$stickers.SuggestedShortName](/API_docs/types/stickers.SuggestedShortName.md)<a name="stickers.suggestShortName"></a>  

***
<br><br>
$MadelineProto->[updates->getChannelDifference](/API_docs/methods/updates.getChannelDifference.md)(\['force' => [Bool](/API_docs/types/Bool.md), 'channel' => [InputChannel](/API_docs/types/InputChannel.md), 'filter' => [ChannelMessagesFilter](/API_docs/types/ChannelMessagesFilter.md), 'pts' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.md)<a name="updates.getChannelDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getDifference](/API_docs/methods/updates.getDifference.md)(\['pts' => [int](/API_docs/types/int.md), 'pts_total_limit' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'qts' => [int](/API_docs/types/int.md), \]) === [$updates.Difference](/API_docs/types/updates.Difference.md)<a name="updates.getDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getState](/API_docs/methods/updates.getState.md)(\[\]) === [$updates.State](/API_docs/types/updates.State.md)<a name="updates.getState"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFile](/API_docs/methods/upload.getCdnFile.md)(\['file_token' => [bytes](/API_docs/types/bytes.md), 'offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$upload.CdnFile](/API_docs/types/upload.CdnFile.md)<a name="upload.getCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFileHashes](/API_docs/methods/upload.getCdnFileHashes.md)(\['file_token' => [bytes](/API_docs/types/bytes.md), 'offset' => [int](/API_docs/types/int.md), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.md)<a name="upload.getCdnFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getFile](/API_docs/methods/upload.getFile.md)(\['precise' => [Bool](/API_docs/types/Bool.md), 'cdn_supported' => [Bool](/API_docs/types/Bool.md), 'location' => [InputFileLocation](/API_docs/types/InputFileLocation.md), 'offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$upload.File](/API_docs/types/upload.File.md)<a name="upload.getFile"></a>  

***
<br><br>
$MadelineProto->[upload->getFileHashes](/API_docs/methods/upload.getFileHashes.md)(\['location' => [InputFileLocation](/API_docs/types/InputFileLocation.md), 'offset' => [int](/API_docs/types/int.md), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.md)<a name="upload.getFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getWebFile](/API_docs/methods/upload.getWebFile.md)(\['location' => [InputWebFileLocation](/API_docs/types/InputWebFileLocation.md), 'offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), \]) === [$upload.WebFile](/API_docs/types/upload.WebFile.md)<a name="upload.getWebFile"></a>  

***
<br><br>
$MadelineProto->[upload->reuploadCdnFile](/API_docs/methods/upload.reuploadCdnFile.md)(\['file_token' => [bytes](/API_docs/types/bytes.md), 'request_token' => [bytes](/API_docs/types/bytes.md), \]) === [$Vector\_of\_FileHash](/API_docs/types/FileHash.md)<a name="upload.reuploadCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->saveBigFilePart](/API_docs/methods/upload.saveBigFilePart.md)(\['file_id' => [long](/API_docs/types/long.md), 'file_part' => [int](/API_docs/types/int.md), 'file_total_parts' => [int](/API_docs/types/int.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="upload.saveBigFilePart"></a>  

***
<br><br>
$MadelineProto->[upload->saveFilePart](/API_docs/methods/upload.saveFilePart.md)(\['file_id' => [long](/API_docs/types/long.md), 'file_part' => [int](/API_docs/types/int.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \]) === [$Bool](/API_docs/types/Bool.md)<a name="upload.saveFilePart"></a>  

***
<br><br>
$MadelineProto->[users->getFullUser](/API_docs/methods/users.getFullUser.md)(\['id' => [InputUser](/API_docs/types/InputUser.md), \]) === [$users.UserFull](/API_docs/types/users.UserFull.md)<a name="users.getFullUser"></a>  

***
<br><br>
$MadelineProto->[users->getUsers](/API_docs/methods/users.getUsers.md)(\['id' => \[[InputUser](/API_docs/types/InputUser.md)\], \]) === [$Vector\_of\_User](/API_docs/types/User.md)<a name="users.getUsers"></a>  

***
<br><br>
$MadelineProto->[users->setSecureValueErrors](/API_docs/methods/users.setSecureValueErrors.md)(\['id' => [InputUser](/API_docs/types/InputUser.md), 'errors' => \[[SecureValueError](/API_docs/types/SecureValueError.md)\], \]) === [$Bool](/API_docs/types/Bool.md)<a name="users.setSecureValueErrors"></a>  



---
title: "danog\\MadelineProto\\Namespace\\Account: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Account`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`registerDevice(bool $app_sandbox, bool $no_muted = false, int $token_type = 0, string $token = '', string $secret = '', list<int> $other_uids = []): bool`](#registerdevice-bool-app_sandbox-bool-no_muted-false-int-token_type-0-string-token-string-secret-list-int-other_uids-bool)
* [`unregisterDevice(int $token_type = 0, string $token = '', list<int> $other_uids = []): bool`](#unregisterdevice-int-token_type-0-string-token-list-int-other_uids-bool)
* [`updateNotifySettings(array|int|string $peer, array{_: \"inputPeerNotifySettings", show_previews?: bool, silent?: bool, mute_until?: int, sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title?: string, data?: string}|array{_: \"notificationSoundRingtone", id?: int}} $settings): bool`](#updatenotifysettings-array-int-string-peer-array-_-inputpeernotifysettings-show_previews-bool-silent-bool-mute_until-int-sound-array-_-notificationsounddefault-array-_-notificationsoundnone-array-_-notificationsoundlocal-title-string-data-string-array-_-notificationsoundringtone-id-int-settings-bool)
* [`getNotifySettings(array|int|string $peer): array{_: \"peerNotifySettings", show_previews?: bool, silent?: bool, mute_until: int, ios_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: int}, android_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: int}, other_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: \int}} @see https://docs.madelineproto.xyz/API_docs/types/PeerNotifySettings.ht}}`](#getnotifysettings-array-int-string-peer-array-_-peernotifysettings-show_previews-bool-silent-bool-mute_until-int-ios_sound-array-_-notificationsounddefault-array-_-notificationsoundnone-array-_-notificationsoundlocal-title-string-data-string-array-_-notificationsoundringtone-id-int-android_sound-array-_-notificationsounddefault-array-_-notificationsoundnone-array-_-notificationsoundlocal-title-string-data-string-array-_-notificationsoundringtone-id-int-other_sound-array-_-notificationsounddefault-array-_-notificationsoundnone-array-_-notificationsoundlocal-title-string-data-string-array-_-notificationsoundringtone-id-int-see-https-docs-madelineproto-xyz-api_docs-types-peernotifysettings-ht)
* [`resetNotifySettings(): bool`](#resetnotifysettings-bool)
* [`updateProfile(string $first_name = '', string $last_name = '', string $about = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`](#updateprofile-string-first_name-string-last_name-string-about-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-user-html)
* [`updateStatus(bool $offline): bool`](#updatestatus-bool-offline-bool)
* [`getWallPapers(list<int> $hash = []): array{_: \"account.wallPapersNotModified"}|array{_: \"account.wallPapers", hash: list<int>, wallpapers: \list<array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}>} @see https://docs.madelineproto.xyz/API_docs/types/account.WallPapers.htm}`](#getwallpapers-list-int-hash-array-_-account-wallpapersnotmodified-array-_-account-wallpapers-hash-list-int-wallpapers-list-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-see-https-docs-madelineproto-xyz-api_docs-types-account-wallpapers-htm)
* [`reportPeer(array|int|string $peer, array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"} $reason, string $message = ''): bool`](#reportpeer-array-int-string-peer-array-_-inputreportreasonspam-array-_-inputreportreasonviolence-array-_-inputreportreasonpornography-array-_-inputreportreasonchildabuse-array-_-inputreportreasonother-array-_-inputreportreasoncopyright-array-_-inputreportreasongeoirrelevant-array-_-inputreportreasonfake-array-_-inputreportreasonillegaldrugs-array-_-inputreportreasonpersonaldetails-reason-string-message-bool)
* [`checkUsername(string $username = ''): bool`](#checkusername-string-username-bool)
* [`updateUsername(string $username = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`](#updateusername-string-username-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-user-html)
* [`getPrivacy(array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"} $key): array{_: \"account.privacyRules", rules: list<array{_: \"privacyValueAllowContacts"}|array{_: \"privacyValueAllowAll"}|array{_: \"privacyValueAllowUsers", users: list<int>}|array{_: \"privacyValueDisallowContacts"}|array{_: \"privacyValueDisallowAll"}|array{_: \"privacyValueDisallowUsers", users: list<int>}|array{_: \"privacyValueAllowChatParticipants", chats: list<int>}|array{_: \"privacyValueDisallowChatParticipants", chats: list<int>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.htm}`](#getprivacy-array-_-inputprivacykeystatustimestamp-array-_-inputprivacykeychatinvite-array-_-inputprivacykeyphonecall-array-_-inputprivacykeyphonep2p-array-_-inputprivacykeyforwards-array-_-inputprivacykeyprofilephoto-array-_-inputprivacykeyphonenumber-array-_-inputprivacykeyaddedbyphone-array-_-inputprivacykeyvoicemessages-key-array-_-account-privacyrules-rules-list-array-_-privacyvalueallowcontacts-array-_-privacyvalueallowall-array-_-privacyvalueallowusers-users-list-int-array-_-privacyvaluedisallowcontacts-array-_-privacyvaluedisallowall-array-_-privacyvaluedisallowusers-users-list-int-array-_-privacyvalueallowchatparticipants-chats-list-int-array-_-privacyvaluedisallowchatparticipants-chats-list-int-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-account-privacyrules-htm)
* [`setPrivacy(array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"} $key, list<array{_: \"inputPrivacyValueAllowContacts"}|array{_: \"inputPrivacyValueAllowAll"}|array{_: \"inputPrivacyValueAllowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueDisallowContacts"}|array{_: \"inputPrivacyValueDisallowAll"}|array{_: \"inputPrivacyValueDisallowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueAllowChatParticipants", chats?: list<int>}|array{_: \"inputPrivacyValueDisallowChatParticipants", chats?: list<int>}> $rules = []): array{_: \"account.privacyRules", rules: list<array{_: \"privacyValueAllowContacts"}|array{_: \"privacyValueAllowAll"}|array{_: \"privacyValueAllowUsers", users: list<int>}|array{_: \"privacyValueDisallowContacts"}|array{_: \"privacyValueDisallowAll"}|array{_: \"privacyValueDisallowUsers", users: list<int>}|array{_: \"privacyValueAllowChatParticipants", chats: list<int>}|array{_: \"privacyValueDisallowChatParticipants", chats: list<int>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.htm}`](#setprivacy-array-_-inputprivacykeystatustimestamp-array-_-inputprivacykeychatinvite-array-_-inputprivacykeyphonecall-array-_-inputprivacykeyphonep2p-array-_-inputprivacykeyforwards-array-_-inputprivacykeyprofilephoto-array-_-inputprivacykeyphonenumber-array-_-inputprivacykeyaddedbyphone-array-_-inputprivacykeyvoicemessages-key-list-array-_-inputprivacyvalueallowcontacts-array-_-inputprivacyvalueallowall-array-_-inputprivacyvalueallowusers-users-list-array-int-string-array-_-inputprivacyvaluedisallowcontacts-array-_-inputprivacyvaluedisallowall-array-_-inputprivacyvaluedisallowusers-users-list-array-int-string-array-_-inputprivacyvalueallowchatparticipants-chats-list-int-array-_-inputprivacyvaluedisallowchatparticipants-chats-list-int-rules-array-_-account-privacyrules-rules-list-array-_-privacyvalueallowcontacts-array-_-privacyvalueallowall-array-_-privacyvalueallowusers-users-list-int-array-_-privacyvaluedisallowcontacts-array-_-privacyvaluedisallowall-array-_-privacyvaluedisallowusers-users-list-int-array-_-privacyvalueallowchatparticipants-chats-list-int-array-_-privacyvaluedisallowchatparticipants-chats-list-int-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-account-privacyrules-htm)
* [`deleteAccount(string $reason = '', string|array $password = []): bool`](#deleteaccount-string-reason-string-array-password-bool)
* [`getAccountTTL(): array{_: \"accountDaysTTL", days: \int} @see https://docs.madelineproto.xyz/API_docs/types/AccountDaysTTL.htm}`](#getaccountttl-array-_-accountdaysttl-days-int-see-https-docs-madelineproto-xyz-api_docs-types-accountdaysttl-htm)
* [`setAccountTTL(array{_: \"accountDaysTTL", days?: int} $ttl): bool`](#setaccountttl-array-_-accountdaysttl-days-int-ttl-bool)
* [`sendChangePhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $phone_number = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`](#sendchangephonecode-array-_-codesettings-allow_flashcall-bool-current_number-bool-allow_app_hash-bool-allow_missed_call-bool-allow_firebase-bool-logout_tokens-list-string-token-string-app_sandbox-bool-settings-string-phone_number-array-_-auth-sentcode-type-array-_-auth-sentcodetypeapp-length-int-array-_-auth-sentcodetypesms-length-int-array-_-auth-sentcodetypecall-length-int-array-_-auth-sentcodetypeflashcall-pattern-string-array-_-auth-sentcodetypemissedcall-prefix-string-length-int-array-_-auth-sentcodetypeemailcode-apple_signin_allowed-bool-google_signin_allowed-bool-email_pattern-string-length-int-reset_available_period-int-reset_pending_date-int-array-_-auth-sentcodetypesetupemailrequired-apple_signin_allowed-bool-google_signin_allowed-bool-array-_-auth-sentcodetypefragmentsms-url-string-length-int-array-_-auth-sentcodetypefirebasesms-nonce-string-receipt-string-push_timeout-int-length-int-phone_code_hash-string-next_type-array-_-auth-codetypesms-array-_-auth-codetypecall-array-_-auth-codetypeflashcall-array-_-auth-codetypemissedcall-array-_-auth-codetypefragmentsms-timeout-int-array-_-auth-sentcodesuccess-authorization-array-_-auth-authorization-user-array-int-string-setup_password_required-bool-otherwise_relogin_days-int-tmp_sessions-int-future_auth_token-string-array-_-auth-authorizationsignuprequired-terms_of_service-array-_-help-termsofservice-id-mixed-popup-bool-text-string-entities-list-array-_-messageentityunknown-offset-int-length-int-array-_-messageentitymention-offset-int-length-int-array-_-messageentityhashtag-offset-int-length-int-array-_-messageentitybotcommand-offset-int-length-int-array-_-messageentityurl-offset-int-length-int-array-_-messageentityemail-offset-int-length-int-array-_-messageentitybold-offset-int-length-int-array-_-messageentityitalic-offset-int-length-int-array-_-messageentitycode-offset-int-length-int-array-_-messageentitypre-offset-int-length-int-language-string-array-_-messageentitytexturl-offset-int-length-int-url-string-array-_-messageentitymentionname-offset-int-length-int-user_id-int-array-_-inputmessageentitymentionname-user_id-array-int-string-offset-int-length-int-array-_-messageentityphone-offset-int-length-int-array-_-messageentitycashtag-offset-int-length-int-array-_-messageentityunderline-offset-int-length-int-array-_-messageentitystrike-offset-int-length-int-array-_-messageentityblockquote-offset-int-length-int-array-_-messageentitybankcard-offset-int-length-int-array-_-messageentityspoiler-offset-int-length-int-array-_-messageentitycustomemoji-offset-int-length-int-document_id-int-min_age_confirm-int-see-https-docs-madelineproto-xyz-api_docs-types-auth-sentcode-h)
* [`changePhone(string $phone_number = '', string $phone_code_hash = '', string $phone_code = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`](#changephone-string-phone_number-string-phone_code_hash-string-phone_code-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-user-html)
* [`updateDeviceLocked(int $period = 0): bool`](#updatedevicelocked-int-period-0-bool)
* [`getAuthorizations(): array{_: \"account.authorizations", authorization_ttl_days: int, authorizations: \list<array{_: "authorization", current: bool, official_app: bool, password_pending: bool, encrypted_requests_disabled: bool, call_requests_disabled: bool, hash: list<int>, device_model: string, platform: string, system_version: string, api_id: int, app_name: string, app_version: string, date_created: int, date_active: int, ip: string, country: string, region: string}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Authorizations.htm}`](#getauthorizations-array-_-account-authorizations-authorization_ttl_days-int-authorizations-list-array-_-authorization-current-bool-official_app-bool-password_pending-bool-encrypted_requests_disabled-bool-call_requests_disabled-bool-hash-list-int-device_model-string-platform-string-system_version-string-api_id-int-app_name-string-app_version-string-date_created-int-date_active-int-ip-string-country-string-region-string-see-https-docs-madelineproto-xyz-api_docs-types-account-authorizations-htm)
* [`resetAuthorization(list<int> $hash = []): bool`](#resetauthorization-list-int-hash-bool)
* [`getPassword(): array{_: \"account.password", new_algo: array{_: \"passwordKdfAlgoUnknown"}|array{_: \"passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", salt1: string, salt2: string, g: int, p: string}, new_secure_algo: array{_: \"securePasswordKdfAlgoUnknown"}|array{_: \"securePasswordKdfAlgoPBKDF2HMACSHA512iter100000", salt: string}|array{_: \"securePasswordKdfAlgoSHA512", salt: string}, has_recovery: bool, has_secure_values: bool, has_password: bool, current_algo?: array{_: \"passwordKdfAlgoUnknown"}|array{_: \"passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", salt1: string, salt2: string, g: int, p: string}, srp_B: string, srp_id: int, hint: string, email_unconfirmed_pattern: string, secure_random: string, pending_reset_date: int, login_email_pattern: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.Password.htm}`](#getpassword-array-_-account-password-new_algo-array-_-passwordkdfalgounknown-array-_-passwordkdfalgosha256sha256pbkdf2hmacsha512iter100000sha256modpow-salt1-string-salt2-string-g-int-p-string-new_secure_algo-array-_-securepasswordkdfalgounknown-array-_-securepasswordkdfalgopbkdf2hmacsha512iter100000-salt-string-array-_-securepasswordkdfalgosha512-salt-string-has_recovery-bool-has_secure_values-bool-has_password-bool-current_algo-array-_-passwordkdfalgounknown-array-_-passwordkdfalgosha256sha256pbkdf2hmacsha512iter100000sha256modpow-salt1-string-salt2-string-g-int-p-string-srp_b-string-srp_id-int-hint-string-email_unconfirmed_pattern-string-secure_random-string-pending_reset_date-int-login_email_pattern-string-see-https-docs-madelineproto-xyz-api_docs-types-account-password-htm)
* [`sendConfirmPhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $hash = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`](#sendconfirmphonecode-array-_-codesettings-allow_flashcall-bool-current_number-bool-allow_app_hash-bool-allow_missed_call-bool-allow_firebase-bool-logout_tokens-list-string-token-string-app_sandbox-bool-settings-string-hash-array-_-auth-sentcode-type-array-_-auth-sentcodetypeapp-length-int-array-_-auth-sentcodetypesms-length-int-array-_-auth-sentcodetypecall-length-int-array-_-auth-sentcodetypeflashcall-pattern-string-array-_-auth-sentcodetypemissedcall-prefix-string-length-int-array-_-auth-sentcodetypeemailcode-apple_signin_allowed-bool-google_signin_allowed-bool-email_pattern-string-length-int-reset_available_period-int-reset_pending_date-int-array-_-auth-sentcodetypesetupemailrequired-apple_signin_allowed-bool-google_signin_allowed-bool-array-_-auth-sentcodetypefragmentsms-url-string-length-int-array-_-auth-sentcodetypefirebasesms-nonce-string-receipt-string-push_timeout-int-length-int-phone_code_hash-string-next_type-array-_-auth-codetypesms-array-_-auth-codetypecall-array-_-auth-codetypeflashcall-array-_-auth-codetypemissedcall-array-_-auth-codetypefragmentsms-timeout-int-array-_-auth-sentcodesuccess-authorization-array-_-auth-authorization-user-array-int-string-setup_password_required-bool-otherwise_relogin_days-int-tmp_sessions-int-future_auth_token-string-array-_-auth-authorizationsignuprequired-terms_of_service-array-_-help-termsofservice-id-mixed-popup-bool-text-string-entities-list-array-_-messageentityunknown-offset-int-length-int-array-_-messageentitymention-offset-int-length-int-array-_-messageentityhashtag-offset-int-length-int-array-_-messageentitybotcommand-offset-int-length-int-array-_-messageentityurl-offset-int-length-int-array-_-messageentityemail-offset-int-length-int-array-_-messageentitybold-offset-int-length-int-array-_-messageentityitalic-offset-int-length-int-array-_-messageentitycode-offset-int-length-int-array-_-messageentitypre-offset-int-length-int-language-string-array-_-messageentitytexturl-offset-int-length-int-url-string-array-_-messageentitymentionname-offset-int-length-int-user_id-int-array-_-inputmessageentitymentionname-user_id-array-int-string-offset-int-length-int-array-_-messageentityphone-offset-int-length-int-array-_-messageentitycashtag-offset-int-length-int-array-_-messageentityunderline-offset-int-length-int-array-_-messageentitystrike-offset-int-length-int-array-_-messageentityblockquote-offset-int-length-int-array-_-messageentitybankcard-offset-int-length-int-array-_-messageentityspoiler-offset-int-length-int-array-_-messageentitycustomemoji-offset-int-length-int-document_id-int-min_age_confirm-int-see-https-docs-madelineproto-xyz-api_docs-types-auth-sentcode-h)
* [`confirmPhone(string $phone_code_hash = '', string $phone_code = ''): bool`](#confirmphone-string-phone_code_hash-string-phone_code-bool)
* [`getTmpPassword(string|array $password, int $period = 0): array{_: \"account.tmpPassword", tmp_password: string, valid_until: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.TmpPassword.htm}`](#gettmppassword-string-array-password-int-period-0-array-_-account-tmppassword-tmp_password-string-valid_until-int-see-https-docs-madelineproto-xyz-api_docs-types-account-tmppassword-htm)
* [`getWebAuthorizations(): array{_: \"account.webAuthorizations", authorizations: list<array{_: \"webAuthorization", hash: list<int>, bot_id: int, domain: string, browser: string, platform: string, date_created: int, date_active: int, ip: string, region: string}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.WebAuthorizations.htm}`](#getwebauthorizations-array-_-account-webauthorizations-authorizations-list-array-_-webauthorization-hash-list-int-bot_id-int-domain-string-browser-string-platform-string-date_created-int-date_active-int-ip-string-region-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-account-webauthorizations-htm)
* [`resetWebAuthorization(list<int> $hash = []): bool`](#resetwebauthorization-list-int-hash-bool)
* [`resetWebAuthorizations(): bool`](#resetwebauthorizations-bool)
* [`getAllSecureValues(): \list<array{_: "secureValue", type: array{_: "secureValueTypePersonalDetails"}|array{_: "secureValueTypePassport"}|array{_: "secureValueTypeDriverLicense"}|array{_: "secureValueTypeIdentityCard"}|array{_: "secureValueTypeInternalPassport"}|array{_: "secureValueTypeAddress"}|array{_: "secureValueTypeUtilityBill"}|array{_: "secureValueTypeBankStatement"}|array{_: "secureValueTypeRentalAgreement"}|array{_: "secureValueTypePassportRegistration"}|array{_: "secureValueTypeTemporaryRegistration"}|array{_: "secureValueTypePhone"}|array{_: "secureValueTypeEmail"}, data?: array{_: "secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: "securePlainPhone", phone: string}|array{_: "securePlainEmail", email: string}, hash: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html`](#getallsecurevalues-list-array-_-securevalue-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data-array-_-securedata-data-string-data_hash-string-secret-string-front_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-reverse_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-selfie-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-translation-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-files-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-plain_data-array-_-secureplainphone-phone-string-array-_-secureplainemail-email-string-hash-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-securevalue-html)
* [`getSecureValue(list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}> $types = []): \list<array{_: "secureValue", type: array{_: "secureValueTypePersonalDetails"}|array{_: "secureValueTypePassport"}|array{_: "secureValueTypeDriverLicense"}|array{_: "secureValueTypeIdentityCard"}|array{_: "secureValueTypeInternalPassport"}|array{_: "secureValueTypeAddress"}|array{_: "secureValueTypeUtilityBill"}|array{_: "secureValueTypeBankStatement"}|array{_: "secureValueTypeRentalAgreement"}|array{_: "secureValueTypePassportRegistration"}|array{_: "secureValueTypeTemporaryRegistration"}|array{_: "secureValueTypePhone"}|array{_: "secureValueTypeEmail"}, data?: array{_: "secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: "securePlainPhone", phone: string}|array{_: "securePlainEmail", email: string}, hash: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html`](#getsecurevalue-list-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-types-list-array-_-securevalue-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data-array-_-securedata-data-string-data_hash-string-secret-string-front_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-reverse_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-selfie-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-translation-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-files-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-plain_data-array-_-secureplainphone-phone-string-array-_-secureplainemail-email-string-hash-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-securevalue-html)
* [`saveSecureValue(array{_: \"inputSecureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data?: string, data_hash?: string, secret?: string}, front_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, reverse_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, selfie?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, translation?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, files?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, plain_data?: array{_: \"securePlainPhone", phone?: string}|array{_: \"securePlainEmail", email?: string}} $value, int $secure_secret_id = 0): array{_: \"secureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: \"securePlainPhone", phone: string}|array{_: \"securePlainEmail", email: string}, hash: \string} @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.htm}`](#savesecurevalue-array-_-inputsecurevalue-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data-array-_-securedata-data-string-data_hash-string-secret-string-front_side-array-_-inputsecurefileuploaded-id-int-parts-int-md5_checksum-string-file_hash-string-secret-string-array-_-inputsecurefile-id-int-access_hash-int-reverse_side-array-_-inputsecurefileuploaded-id-int-parts-int-md5_checksum-string-file_hash-string-secret-string-array-_-inputsecurefile-id-int-access_hash-int-selfie-array-_-inputsecurefileuploaded-id-int-parts-int-md5_checksum-string-file_hash-string-secret-string-array-_-inputsecurefile-id-int-access_hash-int-translation-list-array-_-inputsecurefileuploaded-id-int-parts-int-md5_checksum-string-file_hash-string-secret-string-array-_-inputsecurefile-id-int-access_hash-int-files-list-array-_-inputsecurefileuploaded-id-int-parts-int-md5_checksum-string-file_hash-string-secret-string-array-_-inputsecurefile-id-int-access_hash-int-plain_data-array-_-secureplainphone-phone-string-array-_-secureplainemail-email-string-value-int-secure_secret_id-0-array-_-securevalue-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data-array-_-securedata-data-string-data_hash-string-secret-string-front_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-reverse_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-selfie-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-translation-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-files-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-plain_data-array-_-secureplainphone-phone-string-array-_-secureplainemail-email-string-hash-string-see-https-docs-madelineproto-xyz-api_docs-types-securevalue-htm)
* [`deleteSecureValue(list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}> $types = []): bool`](#deletesecurevalue-list-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-types-bool)
* [`getAuthorizationForm(int $bot_id = 0, string $scope = '', string $public_key = ''): array{_: \"account.authorizationForm", required_types: list<array{_: \"secureRequiredType", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, native_names: bool, selfie_required: bool, translation_required: bool}>, values: list<array{_: \"secureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: \"securePlainPhone", phone: string}|array{_: \"securePlainEmail", email: string}, hash: string}>, errors: list<array{_: \"secureValueErrorData", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data_hash: string, field: string, text: string}|array{_: \"secureValueErrorFrontSide", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorReverseSide", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorSelfie", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorFile", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorFiles", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: list<string>, text: string}|array{_: \"secureValueError", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, hash: string, text: string}|array{_: \"secureValueErrorTranslationFile", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorTranslationFiles", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: list<string>, text: string}>, users: list<array|int|string>, privacy_policy_url: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.AuthorizationForm.htm}`](#getauthorizationform-int-bot_id-0-string-scope-string-public_key-array-_-account-authorizationform-required_types-list-array-_-securerequiredtype-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-native_names-bool-selfie_required-bool-translation_required-bool-values-list-array-_-securevalue-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data-array-_-securedata-data-string-data_hash-string-secret-string-front_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-reverse_side-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-selfie-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-translation-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-files-list-array-_-securefileempty-array-_-securefile-id-int-access_hash-int-size-int-dc_id-int-date-int-file_hash-string-secret-string-plain_data-array-_-secureplainphone-phone-string-array-_-secureplainemail-email-string-hash-string-errors-list-array-_-securevalueerrordata-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-data_hash-string-field-string-text-string-array-_-securevalueerrorfrontside-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-string-text-string-array-_-securevalueerrorreverseside-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-string-text-string-array-_-securevalueerrorselfie-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-string-text-string-array-_-securevalueerrorfile-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-string-text-string-array-_-securevalueerrorfiles-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-list-string-text-string-array-_-securevalueerror-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-hash-string-text-string-array-_-securevalueerrortranslationfile-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-string-text-string-array-_-securevalueerrortranslationfiles-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-file_hash-list-string-text-string-users-list-array-int-string-privacy_policy_url-string-see-https-docs-madelineproto-xyz-api_docs-types-account-authorizationform-htm)
* [`acceptAuthorization(array{_: \"secureCredentialsEncrypted", data?: string, hash?: string, secret?: string} $credentials, int $bot_id = 0, string $scope = '', string $public_key = '', list<array{_: \"secureValueHash", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, hash?: string}> $value_hashes = []): bool`](#acceptauthorization-array-_-securecredentialsencrypted-data-string-hash-string-secret-string-credentials-int-bot_id-0-string-scope-string-public_key-list-array-_-securevaluehash-type-array-_-securevaluetypepersonaldetails-array-_-securevaluetypepassport-array-_-securevaluetypedriverlicense-array-_-securevaluetypeidentitycard-array-_-securevaluetypeinternalpassport-array-_-securevaluetypeaddress-array-_-securevaluetypeutilitybill-array-_-securevaluetypebankstatement-array-_-securevaluetyperentalagreement-array-_-securevaluetypepassportregistration-array-_-securevaluetypetemporaryregistration-array-_-securevaluetypephone-array-_-securevaluetypeemail-hash-string-value_hashes-bool)
* [`sendVerifyPhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $phone_number = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`](#sendverifyphonecode-array-_-codesettings-allow_flashcall-bool-current_number-bool-allow_app_hash-bool-allow_missed_call-bool-allow_firebase-bool-logout_tokens-list-string-token-string-app_sandbox-bool-settings-string-phone_number-array-_-auth-sentcode-type-array-_-auth-sentcodetypeapp-length-int-array-_-auth-sentcodetypesms-length-int-array-_-auth-sentcodetypecall-length-int-array-_-auth-sentcodetypeflashcall-pattern-string-array-_-auth-sentcodetypemissedcall-prefix-string-length-int-array-_-auth-sentcodetypeemailcode-apple_signin_allowed-bool-google_signin_allowed-bool-email_pattern-string-length-int-reset_available_period-int-reset_pending_date-int-array-_-auth-sentcodetypesetupemailrequired-apple_signin_allowed-bool-google_signin_allowed-bool-array-_-auth-sentcodetypefragmentsms-url-string-length-int-array-_-auth-sentcodetypefirebasesms-nonce-string-receipt-string-push_timeout-int-length-int-phone_code_hash-string-next_type-array-_-auth-codetypesms-array-_-auth-codetypecall-array-_-auth-codetypeflashcall-array-_-auth-codetypemissedcall-array-_-auth-codetypefragmentsms-timeout-int-array-_-auth-sentcodesuccess-authorization-array-_-auth-authorization-user-array-int-string-setup_password_required-bool-otherwise_relogin_days-int-tmp_sessions-int-future_auth_token-string-array-_-auth-authorizationsignuprequired-terms_of_service-array-_-help-termsofservice-id-mixed-popup-bool-text-string-entities-list-array-_-messageentityunknown-offset-int-length-int-array-_-messageentitymention-offset-int-length-int-array-_-messageentityhashtag-offset-int-length-int-array-_-messageentitybotcommand-offset-int-length-int-array-_-messageentityurl-offset-int-length-int-array-_-messageentityemail-offset-int-length-int-array-_-messageentitybold-offset-int-length-int-array-_-messageentityitalic-offset-int-length-int-array-_-messageentitycode-offset-int-length-int-array-_-messageentitypre-offset-int-length-int-language-string-array-_-messageentitytexturl-offset-int-length-int-url-string-array-_-messageentitymentionname-offset-int-length-int-user_id-int-array-_-inputmessageentitymentionname-user_id-array-int-string-offset-int-length-int-array-_-messageentityphone-offset-int-length-int-array-_-messageentitycashtag-offset-int-length-int-array-_-messageentityunderline-offset-int-length-int-array-_-messageentitystrike-offset-int-length-int-array-_-messageentityblockquote-offset-int-length-int-array-_-messageentitybankcard-offset-int-length-int-array-_-messageentityspoiler-offset-int-length-int-array-_-messageentitycustomemoji-offset-int-length-int-document_id-int-min_age_confirm-int-see-https-docs-madelineproto-xyz-api_docs-types-auth-sentcode-h)
* [`verifyPhone(string $phone_number = '', string $phone_code_hash = '', string $phone_code = ''): bool`](#verifyphone-string-phone_number-string-phone_code_hash-string-phone_code-bool)
* [`sendVerifyEmailCode(array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"} $purpose, string $email = ''): array{_: \"account.sentEmailCode", email_pattern: string, length: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.SentEmailCode.htm}`](#sendverifyemailcode-array-_-emailverifypurposeloginsetup-phone_number-string-phone_code_hash-string-array-_-emailverifypurposeloginchange-array-_-emailverifypurposepassport-purpose-string-email-array-_-account-sentemailcode-email_pattern-string-length-int-see-https-docs-madelineproto-xyz-api_docs-types-account-sentemailcode-htm)
* [`verifyEmail(array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"} $purpose, array{_: \"emailVerificationCode", code?: string}|array{_: \"emailVerificationGoogle", token?: string}|array{_: \"emailVerificationApple", token?: string} $verification): array{_: \"account.emailVerified", email: string}|array{_: \"account.emailVerifiedLogin", sent_code: array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: int}}}, email: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.EmailVerified.htm}`](#verifyemail-array-_-emailverifypurposeloginsetup-phone_number-string-phone_code_hash-string-array-_-emailverifypurposeloginchange-array-_-emailverifypurposepassport-purpose-array-_-emailverificationcode-code-string-array-_-emailverificationgoogle-token-string-array-_-emailverificationapple-token-string-verification-array-_-account-emailverified-email-string-array-_-account-emailverifiedlogin-sent_code-array-_-auth-sentcode-type-array-_-auth-sentcodetypeapp-length-int-array-_-auth-sentcodetypesms-length-int-array-_-auth-sentcodetypecall-length-int-array-_-auth-sentcodetypeflashcall-pattern-string-array-_-auth-sentcodetypemissedcall-prefix-string-length-int-array-_-auth-sentcodetypeemailcode-apple_signin_allowed-bool-google_signin_allowed-bool-email_pattern-string-length-int-reset_available_period-int-reset_pending_date-int-array-_-auth-sentcodetypesetupemailrequired-apple_signin_allowed-bool-google_signin_allowed-bool-array-_-auth-sentcodetypefragmentsms-url-string-length-int-array-_-auth-sentcodetypefirebasesms-nonce-string-receipt-string-push_timeout-int-length-int-phone_code_hash-string-next_type-array-_-auth-codetypesms-array-_-auth-codetypecall-array-_-auth-codetypeflashcall-array-_-auth-codetypemissedcall-array-_-auth-codetypefragmentsms-timeout-int-array-_-auth-sentcodesuccess-authorization-array-_-auth-authorization-user-array-int-string-setup_password_required-bool-otherwise_relogin_days-int-tmp_sessions-int-future_auth_token-string-array-_-auth-authorizationsignuprequired-terms_of_service-array-_-help-termsofservice-id-mixed-popup-bool-text-string-entities-list-array-_-messageentityunknown-offset-int-length-int-array-_-messageentitymention-offset-int-length-int-array-_-messageentityhashtag-offset-int-length-int-array-_-messageentitybotcommand-offset-int-length-int-array-_-messageentityurl-offset-int-length-int-array-_-messageentityemail-offset-int-length-int-array-_-messageentitybold-offset-int-length-int-array-_-messageentityitalic-offset-int-length-int-array-_-messageentitycode-offset-int-length-int-array-_-messageentitypre-offset-int-length-int-language-string-array-_-messageentitytexturl-offset-int-length-int-url-string-array-_-messageentitymentionname-offset-int-length-int-user_id-int-array-_-inputmessageentitymentionname-user_id-array-int-string-offset-int-length-int-array-_-messageentityphone-offset-int-length-int-array-_-messageentitycashtag-offset-int-length-int-array-_-messageentityunderline-offset-int-length-int-array-_-messageentitystrike-offset-int-length-int-array-_-messageentityblockquote-offset-int-length-int-array-_-messageentitybankcard-offset-int-length-int-array-_-messageentityspoiler-offset-int-length-int-array-_-messageentitycustomemoji-offset-int-length-int-document_id-int-min_age_confirm-int-email-string-see-https-docs-madelineproto-xyz-api_docs-types-account-emailverified-htm)
* [`initTakeoutSession(bool $contacts = false, bool $message_users = false, bool $message_chats = false, bool $message_megagroups = false, bool $message_channels = false, bool $files = false, int $file_max_size = 0): array{_: \"account.takeout", id: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.Takeout.htm}`](#inittakeoutsession-bool-contacts-false-bool-message_users-false-bool-message_chats-false-bool-message_megagroups-false-bool-message_channels-false-bool-files-false-int-file_max_size-0-array-_-account-takeout-id-int-see-https-docs-madelineproto-xyz-api_docs-types-account-takeout-htm)
* [`finishTakeoutSession(bool $success = false): bool`](#finishtakeoutsession-bool-success-false-bool)
* [`confirmPasswordEmail(string $code = ''): bool`](#confirmpasswordemail-string-code-bool)
* [`resendPasswordEmail(): bool`](#resendpasswordemail-bool)
* [`cancelPasswordEmail(): bool`](#cancelpasswordemail-bool)
* [`getContactSignUpNotification(): bool`](#getcontactsignupnotification-bool)
* [`setContactSignUpNotification(bool $silent): bool`](#setcontactsignupnotification-bool-silent-bool)
* [`getNotifyExceptions(bool $compare_sound = false, array|int|string $peer = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#getnotifyexceptions-bool-compare_sound-false-array-int-string-peer-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper): array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: \int}} @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.ht}}`](#getwallpaper-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-see-https-docs-madelineproto-xyz-api_docs-types-wallpaper-ht)
* [`uploadWallPaper(mixed $file, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings, bool $for_chat = false, string $mime_type = ''): array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: \int}} @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.ht}}`](#uploadwallpaper-mixed-file-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-settings-bool-for_chat-false-string-mime_type-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-see-https-docs-madelineproto-xyz-api_docs-types-wallpaper-ht)
* [`saveWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper, bool $unsave, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings): bool`](#savewallpaper-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpaper-bool-unsave-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-settings-bool)
* [`installWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings): bool`](#installwallpaper-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpaper-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-settings-bool)
* [`resetWallPapers(): bool`](#resetwallpapers-bool)
* [`getAutoDownloadSettings(): array{_: \"account.autoDownloadSettings", low: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int}, medium: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int}, high: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: \int}} @see https://docs.madelineproto.xyz/API_docs/types/account.AutoDownloadSettings.ht}}`](#getautodownloadsettings-array-_-account-autodownloadsettings-low-array-_-autodownloadsettings-disabled-bool-video_preload_large-bool-audio_preload_next-bool-phonecalls_less_data-bool-photo_size_max-int-video_size_max-int-file_size_max-int-video_upload_maxbitrate-int-medium-array-_-autodownloadsettings-disabled-bool-video_preload_large-bool-audio_preload_next-bool-phonecalls_less_data-bool-photo_size_max-int-video_size_max-int-file_size_max-int-video_upload_maxbitrate-int-high-array-_-autodownloadsettings-disabled-bool-video_preload_large-bool-audio_preload_next-bool-phonecalls_less_data-bool-photo_size_max-int-video_size_max-int-file_size_max-int-video_upload_maxbitrate-int-see-https-docs-madelineproto-xyz-api_docs-types-account-autodownloadsettings-ht)
* [`saveAutoDownloadSettings(array{_: \"autoDownloadSettings", disabled?: bool, video_preload_large?: bool, audio_preload_next?: bool, phonecalls_less_data?: bool, photo_size_max?: int, video_size_max?: int, file_size_max?: int, video_upload_maxbitrate?: int} $settings, bool $low = false, bool $high = false): bool`](#saveautodownloadsettings-array-_-autodownloadsettings-disabled-bool-video_preload_large-bool-audio_preload_next-bool-phonecalls_less_data-bool-photo_size_max-int-video_size_max-int-file_size_max-int-video_upload_maxbitrate-int-settings-bool-low-false-bool-high-false-bool)
* [`uploadTheme(mixed $file, mixed $thumb = [], string $file_name = '', string $mime_type = ''): array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>} @see https://docs.madelineproto.xyz/API_docs/types/Document.htm}`](#uploadtheme-mixed-file-mixed-thumb-string-file_name-string-mime_type-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-see-https-docs-madelineproto-xyz-api_docs-types-document-htm)
* [`createTheme(string $slug = '', string $title = '', array $document = [], list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}> $settings = []): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`](#createtheme-string-slug-string-title-array-document-list-array-_-inputthemesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpaper_settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-settings-array-_-theme-creator-bool-default-bool-for_chat-bool-id-int-access_hash-int-slug-string-title-string-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-settings-list-array-_-themesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-emoticon-string-installs_count-int-see-https-docs-madelineproto-xyz-api_docs-types-theme-htm)
* [`updateTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, string $format = '', string $slug = '', string $title = '', array $document = [], list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}> $settings = []): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`](#updatetheme-array-_-inputtheme-id-int-access_hash-int-array-_-inputthemeslug-slug-string-theme-string-format-string-slug-string-title-array-document-list-array-_-inputthemesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpaper_settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-settings-array-_-theme-creator-bool-default-bool-for_chat-bool-id-int-access_hash-int-slug-string-title-string-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-settings-list-array-_-themesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-emoticon-string-installs_count-int-see-https-docs-madelineproto-xyz-api_docs-types-theme-htm)
* [`saveTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, bool $unsave): bool`](#savetheme-array-_-inputtheme-id-int-access_hash-int-array-_-inputthemeslug-slug-string-theme-bool-unsave-bool)
* [`installTheme(bool $dark = false, array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme = [], string $format = '', array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"} $base_theme = []): bool`](#installtheme-bool-dark-false-array-_-inputtheme-id-int-access_hash-int-array-_-inputthemeslug-slug-string-theme-string-format-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-base_theme-bool)
* [`getTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, string $format = ''): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`](#gettheme-array-_-inputtheme-id-int-access_hash-int-array-_-inputthemeslug-slug-string-theme-string-format-array-_-theme-creator-bool-default-bool-for_chat-bool-id-int-access_hash-int-slug-string-title-string-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-settings-list-array-_-themesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-emoticon-string-installs_count-int-see-https-docs-madelineproto-xyz-api_docs-types-theme-htm)
* [`getThemes(string $format = '', list<int> $hash = []): array{_: \"account.themesNotModified"}|array{_: \"account.themes", hash: list<int>, themes: \list<array{_: "theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: "themeSettings", base_theme: array{_: "baseThemeClassic"}|array{_: "baseThemeDay"}|array{_: "baseThemeNight"}|array{_: "baseThemeTinted"}|array{_: "baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.htm}`](#getthemes-string-format-list-int-hash-array-_-account-themesnotmodified-array-_-account-themes-hash-list-int-themes-list-array-_-theme-creator-bool-default-bool-for_chat-bool-id-int-access_hash-int-slug-string-title-string-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-settings-list-array-_-themesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-emoticon-string-installs_count-int-see-https-docs-madelineproto-xyz-api_docs-types-account-themes-htm)
* [`setContentSettings(bool $sensitive_enabled = false): bool`](#setcontentsettings-bool-sensitive_enabled-false-bool)
* [`getContentSettings(): array{_: \"account.contentSettings", sensitive_enabled: bool, sensitive_can_change: \bool} @see https://docs.madelineproto.xyz/API_docs/types/account.ContentSettings.htm}`](#getcontentsettings-array-_-account-contentsettings-sensitive_enabled-bool-sensitive_can_change-bool-see-https-docs-madelineproto-xyz-api_docs-types-account-contentsettings-htm)
* [`getMultiWallPapers(list<array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}> $wallpapers = []): \list<array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.html`](#getmultiwallpapers-list-array-_-inputwallpaper-id-int-access_hash-int-array-_-inputwallpaperslug-slug-string-array-_-inputwallpapernofile-id-int-wallpapers-list-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-of-see-https-docs-madelineproto-xyz-api_docs-types-wallpaper-html)
* [`getGlobalPrivacySettings(): array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: \bool} @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.htm}`](#getglobalprivacysettings-array-_-globalprivacysettings-archive_and_mute_new_noncontact_peers-bool-see-https-docs-madelineproto-xyz-api_docs-types-globalprivacysettings-htm)
* [`setGlobalPrivacySettings(array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: bool} $settings): array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: \bool} @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.htm}`](#setglobalprivacysettings-array-_-globalprivacysettings-archive_and_mute_new_noncontact_peers-bool-settings-array-_-globalprivacysettings-archive_and_mute_new_noncontact_peers-bool-see-https-docs-madelineproto-xyz-api_docs-types-globalprivacysettings-htm)
* [`reportProfilePhoto(array|int|string $peer, array $photo_id, array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"} $reason, string $message = ''): bool`](#reportprofilephoto-array-int-string-peer-array-photo_id-array-_-inputreportreasonspam-array-_-inputreportreasonviolence-array-_-inputreportreasonpornography-array-_-inputreportreasonchildabuse-array-_-inputreportreasonother-array-_-inputreportreasoncopyright-array-_-inputreportreasongeoirrelevant-array-_-inputreportreasonfake-array-_-inputreportreasonillegaldrugs-array-_-inputreportreasonpersonaldetails-reason-string-message-bool)
* [`resetPassword(): array{_: \"account.resetPasswordFailedWait", retry_date: int}|array{_: \"account.resetPasswordRequestedWait", until_date: int}|array{_: \"account.resetPasswordOk"} @see https://docs.madelineproto.xyz/API_docs/types/account.ResetPasswordResult.htm}`](#resetpassword-array-_-account-resetpasswordfailedwait-retry_date-int-array-_-account-resetpasswordrequestedwait-until_date-int-array-_-account-resetpasswordok-see-https-docs-madelineproto-xyz-api_docs-types-account-resetpasswordresult-htm)
* [`declinePasswordReset(): bool`](#declinepasswordreset-bool)
* [`getChatThemes(list<int> $hash = []): array{_: \"account.themesNotModified"}|array{_: \"account.themes", hash: list<int>, themes: \list<array{_: "theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: "themeSettings", base_theme: array{_: "baseThemeClassic"}|array{_: "baseThemeDay"}|array{_: "baseThemeNight"}|array{_: "baseThemeTinted"}|array{_: "baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.htm}`](#getchatthemes-list-int-hash-array-_-account-themesnotmodified-array-_-account-themes-hash-list-int-themes-list-array-_-theme-creator-bool-default-bool-for_chat-bool-id-int-access_hash-int-slug-string-title-string-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-settings-list-array-_-themesettings-base_theme-array-_-basethemeclassic-array-_-basethemeday-array-_-basethemenight-array-_-basethemetinted-array-_-basethemearctic-message_colors_animated-bool-accent_color-int-outbox_accent_color-int-message_colors-list-int-wallpaper-array-_-wallpaper-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-id-int-creator-bool-default-bool-pattern-bool-dark-bool-access_hash-int-slug-string-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-array-_-wallpapernofile-id-int-default-bool-dark-bool-settings-array-_-wallpapersettings-blur-bool-motion-bool-background_color-int-second_background_color-int-third_background_color-int-fourth_background_color-int-intensity-int-rotation-int-emoticon-string-installs_count-int-see-https-docs-madelineproto-xyz-api_docs-types-account-themes-htm)
* [`setAuthorizationTTL(int $authorization_ttl_days = 0): bool`](#setauthorizationttl-int-authorization_ttl_days-0-bool)
* [`changeAuthorizationSettings(list<int> $hash = [], bool $encrypted_requests_disabled = false, bool $call_requests_disabled = false): bool`](#changeauthorizationsettings-list-int-hash-bool-encrypted_requests_disabled-false-bool-call_requests_disabled-false-bool)
* [`getSavedRingtones(list<int> $hash = []): array{_: \"account.savedRingtonesNotModified"}|array{_: \"account.savedRingtones", hash: list<int>, ringtones: \list<array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}>} @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtones.htm}`](#getsavedringtones-list-int-hash-array-_-account-savedringtonesnotmodified-array-_-account-savedringtones-hash-list-int-ringtones-list-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-see-https-docs-madelineproto-xyz-api_docs-types-account-savedringtones-htm)
* [`saveRingtone(array $id, bool $unsave): array{_: \"account.savedRingtone"}|array{_: \"account.savedRingtoneConverted", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>}} @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtone.ht}}`](#saveringtone-array-id-bool-unsave-array-_-account-savedringtone-array-_-account-savedringtoneconverted-document-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-see-https-docs-madelineproto-xyz-api_docs-types-account-savedringtone-ht)
* [`uploadRingtone(mixed $file, string $file_name = '', string $mime_type = ''): array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>} @see https://docs.madelineproto.xyz/API_docs/types/Document.htm}`](#uploadringtone-mixed-file-string-file_name-string-mime_type-array-_-documentempty-id-array-array-_-document-id-array-access_hash-array-file_reference-array-date-array-mime_type-array-size-array-thumbs-list-array-video_thumbs-list-array-dc_id-array-attributes-list-array-see-https-docs-madelineproto-xyz-api_docs-types-document-htm)
* [`updateEmojiStatus(array{_: \"emojiStatusEmpty"}|array{_: \"emojiStatus", document_id?: int}|array{_: \"emojiStatusUntil", document_id?: int, until?: int} $emoji_status): bool`](#updateemojistatus-array-_-emojistatusempty-array-_-emojistatus-document_id-int-array-_-emojistatusuntil-document_id-int-until-int-emoji_status-bool)
* [`getDefaultEmojiStatuses(list<int> $hash = []): array{_: \"account.emojiStatusesNotModified"}|array{_: \"account.emojiStatuses", hash: list<int>, statuses: \list<array{_: "emojiStatusEmpty"}|array{_: "emojiStatus", document_id: int}|array{_: "emojiStatusUntil", document_id: int, until: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.htm}`](#getdefaultemojistatuses-list-int-hash-array-_-account-emojistatusesnotmodified-array-_-account-emojistatuses-hash-list-int-statuses-list-array-_-emojistatusempty-array-_-emojistatus-document_id-int-array-_-emojistatusuntil-document_id-int-until-int-see-https-docs-madelineproto-xyz-api_docs-types-account-emojistatuses-htm)
* [`getRecentEmojiStatuses(list<int> $hash = []): array{_: \"account.emojiStatusesNotModified"}|array{_: \"account.emojiStatuses", hash: list<int>, statuses: \list<array{_: "emojiStatusEmpty"}|array{_: "emojiStatus", document_id: int}|array{_: "emojiStatusUntil", document_id: int, until: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.htm}`](#getrecentemojistatuses-list-int-hash-array-_-account-emojistatusesnotmodified-array-_-account-emojistatuses-hash-list-int-statuses-list-array-_-emojistatusempty-array-_-emojistatus-document_id-int-array-_-emojistatusuntil-document_id-int-until-int-see-https-docs-madelineproto-xyz-api_docs-types-account-emojistatuses-htm)
* [`clearRecentEmojiStatuses(): bool`](#clearrecentemojistatuses-bool)
* [`reorderUsernames(list<string> $order = []): bool`](#reorderusernames-list-string-order-bool)
* [`toggleUsername(bool $active, string $username = ''): bool`](#toggleusername-bool-active-string-username-bool)
* [`getDefaultProfilePhotoEmojis(list<int> $hash = []): array{_: \"emojiListNotModified"}|array{_: \"emojiList", hash: list<int>, document_id: \list<int>} @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.htm}`](#getdefaultprofilephotoemojis-list-int-hash-array-_-emojilistnotmodified-array-_-emojilist-hash-list-int-document_id-list-int-see-https-docs-madelineproto-xyz-api_docs-types-emojilist-htm)
* [`getDefaultGroupPhotoEmojis(list<int> $hash = []): array{_: \"emojiListNotModified"}|array{_: \"emojiList", hash: list<int>, document_id: \list<int>} @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.htm}`](#getdefaultgroupphotoemojis-list-int-hash-array-_-emojilistnotmodified-array-_-emojilist-hash-list-int-document_id-list-int-see-https-docs-madelineproto-xyz-api_docs-types-emojilist-htm)
* [`getAutoSaveSettings(): array{_: \"account.autoSaveSettings", users_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, chats_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, broadcasts_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, exceptions: list<array{_: \"autoSaveException", peer: array|int|string, settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.AutoSaveSettings.htm}`](#getautosavesettings-array-_-account-autosavesettings-users_settings-array-_-autosavesettings-photos-bool-videos-bool-video_max_size-int-chats_settings-array-_-autosavesettings-photos-bool-videos-bool-video_max_size-int-broadcasts_settings-array-_-autosavesettings-photos-bool-videos-bool-video_max_size-int-exceptions-list-array-_-autosaveexception-peer-array-int-string-settings-array-_-autosavesettings-photos-bool-videos-bool-video_max_size-int-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-account-autosavesettings-htm)
* [`saveAutoSaveSettings(array{_: \"autoSaveSettings", photos?: bool, videos?: bool, video_max_size?: int} $settings, bool $users = false, bool $chats = false, bool $broadcasts = false, array|int|string $peer = []): bool`](#saveautosavesettings-array-_-autosavesettings-photos-bool-videos-bool-video_max_size-int-settings-bool-users-false-bool-chats-false-bool-broadcasts-false-array-int-string-peer-bool)
* [`deleteAutoSaveExceptions(): bool`](#deleteautosaveexceptions-bool)

## Methods:
### `registerDevice(bool $app_sandbox, bool $no_muted = false, int $token_type = 0, string $token = '', string $secret = '', list<int> $other_uids = []): bool`

Register device to receive [PUSH notifications](https://core.telegram.org/api/push-updates)


Parameters:

* `$app_sandbox`: `bool` If [(boolTrue)](https://docs.madelineproto.xyz/API_docs/constructors/boolTrue.html) is transmitted, a sandbox-certificate will be used during transmission.  
* `$no_muted`: `bool` Avoid receiving (silent and invisible background) notifications. Useful to save battery.  
* `$token_type`: `int` Device token type, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values.  
* `$token`: `string` Device token, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values.  
* `$secret`: `string` For FCM and APNS VoIP, optional encryption key used to encrypt push notifications  
* `$other_uids`: `list<int>` List of user identifiers of other users currently using the client  



### `unregisterDevice(int $token_type = 0, string $token = '', list<int> $other_uids = []): bool`

Deletes a device by its token, stops sending PUSH-notifications to it.


Parameters:

* `$token_type`: `int` Device token type, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values.  
* `$token`: `string` Device token, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values.  
* `$other_uids`: `list<int>` List of user identifiers of other users currently using the client  



### `updateNotifySettings(array|int|string $peer, array{_: \"inputPeerNotifySettings", show_previews?: bool, silent?: bool, mute_until?: int, sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title?: string, data?: string}|array{_: \"notificationSoundRingtone", id?: int}} $settings): bool`

Edits notification settings from a given user/group, from all users/all groups.


Parameters:

* `$peer`: `array|int|string` Notification source @see https://docs.madelineproto.xyz/API_docs/types/InputNotifyPeer.html  
* `$settings`: `array{_: \"inputPeerNotifySettings", show_previews?: bool, silent?: bool, mute_until?: int, sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title?: string, data?: string}|array{_: \"notificationSoundRingtone", id?: int}}` Notification settings @see https://docs.madelineproto.xyz/API_docs/types/InputPeerNotifySettings.html  



### `getNotifySettings(array|int|string $peer): array{_: \"peerNotifySettings", show_previews?: bool, silent?: bool, mute_until: int, ios_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: int}, android_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: int}, other_sound?: array{_: \"notificationSoundDefault"}|array{_: \"notificationSoundNone"}|array{_: \"notificationSoundLocal", title: string, data: string}|array{_: \"notificationSoundRingtone", id: \int}} @see https://docs.madelineproto.xyz/API_docs/types/PeerNotifySettings.ht}}`

Gets current notification settings for a given user/group, from all users/all groups.


Parameters:

* `$peer`: `array|int|string` Notification source @see https://docs.madelineproto.xyz/API_docs/types/InputNotifyPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/PeerNotifySettings.html


### `resetNotifySettings(): bool`

Resets all notification settings from users and groups.



### `updateProfile(string $first_name = '', string $last_name = '', string $about = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`

Updates user profile.


Parameters:

* `$first_name`: `string` New user first name  
* `$last_name`: `string` New user last name  
* `$about`: `string` New bio  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/User.html


### `updateStatus(bool $offline): bool`

Updates online user status.


Parameters:

* `$offline`: `bool` If [(boolTrue)](https://docs.madelineproto.xyz/API_docs/constructors/boolTrue.html) is transmitted, user status will change to [(userStatusOffline)](https://docs.madelineproto.xyz/API_docs/constructors/userStatusOffline.html).  



### `getWallPapers(list<int> $hash = []): array{_: \"account.wallPapersNotModified"}|array{_: \"account.wallPapers", hash: list<int>, wallpapers: \list<array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}>} @see https://docs.madelineproto.xyz/API_docs/types/account.WallPapers.htm}`

Returns a list of available [wallpapers](https://core.telegram.org/api/wallpapers).


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.WallPapers.html


### `reportPeer(array|int|string $peer, array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"} $reason, string $message = ''): bool`

Report a peer for violation of telegram's Terms of Service


Parameters:

* `$peer`: `array|int|string` The peer to report @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$reason`: `array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"}` The reason why this peer is being reported @see https://docs.madelineproto.xyz/API_docs/types/ReportReason.html  
* `$message`: `string` Comment for report moderation  



### `checkUsername(string $username = ''): bool`

Validates a username and checks availability.


Parameters:

* `$username`: `string` username<br>Accepted characters: A-z (case-insensitive), 0-9 and underscores.<br>Length: 5-32 characters.  



### `updateUsername(string $username = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`

Changes username for the current user.


Parameters:

* `$username`: `string` username or empty string if username is to be removed<br>Accepted characters: a-z (case-insensitive), 0-9 and underscores.<br>Length: 5-32 characters.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/User.html


### `getPrivacy(array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"} $key): array{_: \"account.privacyRules", rules: list<array{_: \"privacyValueAllowContacts"}|array{_: \"privacyValueAllowAll"}|array{_: \"privacyValueAllowUsers", users: list<int>}|array{_: \"privacyValueDisallowContacts"}|array{_: \"privacyValueDisallowAll"}|array{_: \"privacyValueDisallowUsers", users: list<int>}|array{_: \"privacyValueAllowChatParticipants", chats: list<int>}|array{_: \"privacyValueDisallowChatParticipants", chats: list<int>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.htm}`

Get privacy settings of current account


Parameters:

* `$key`: `array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"}` Peer category whose privacy settings should be fetched @see https://docs.madelineproto.xyz/API_docs/types/InputPrivacyKey.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.html


### `setPrivacy(array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"} $key, list<array{_: \"inputPrivacyValueAllowContacts"}|array{_: \"inputPrivacyValueAllowAll"}|array{_: \"inputPrivacyValueAllowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueDisallowContacts"}|array{_: \"inputPrivacyValueDisallowAll"}|array{_: \"inputPrivacyValueDisallowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueAllowChatParticipants", chats?: list<int>}|array{_: \"inputPrivacyValueDisallowChatParticipants", chats?: list<int>}> $rules = []): array{_: \"account.privacyRules", rules: list<array{_: \"privacyValueAllowContacts"}|array{_: \"privacyValueAllowAll"}|array{_: \"privacyValueAllowUsers", users: list<int>}|array{_: \"privacyValueDisallowContacts"}|array{_: \"privacyValueDisallowAll"}|array{_: \"privacyValueDisallowUsers", users: list<int>}|array{_: \"privacyValueAllowChatParticipants", chats: list<int>}|array{_: \"privacyValueDisallowChatParticipants", chats: list<int>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.htm}`

Change privacy settings of current account


Parameters:

* `$key`: `array{_: \"inputPrivacyKeyStatusTimestamp"}|array{_: \"inputPrivacyKeyChatInvite"}|array{_: \"inputPrivacyKeyPhoneCall"}|array{_: \"inputPrivacyKeyPhoneP2P"}|array{_: \"inputPrivacyKeyForwards"}|array{_: \"inputPrivacyKeyProfilePhoto"}|array{_: \"inputPrivacyKeyPhoneNumber"}|array{_: \"inputPrivacyKeyAddedByPhone"}|array{_: \"inputPrivacyKeyVoiceMessages"}` Peers to which the privacy rules apply @see https://docs.madelineproto.xyz/API_docs/types/InputPrivacyKey.html  
* `$rules`: `list<array{_: \"inputPrivacyValueAllowContacts"}|array{_: \"inputPrivacyValueAllowAll"}|array{_: \"inputPrivacyValueAllowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueDisallowContacts"}|array{_: \"inputPrivacyValueDisallowAll"}|array{_: \"inputPrivacyValueDisallowUsers", users?: list<array|int|string>}|array{_: \"inputPrivacyValueAllowChatParticipants", chats?: list<int>}|array{_: \"inputPrivacyValueDisallowChatParticipants", chats?: list<int>}>` Array of New privacy rules @see https://docs.madelineproto.xyz/API_docs/types/InputPrivacyRule.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.PrivacyRules.html


### `deleteAccount(string $reason = '', string|array $password = []): bool`

Delete the user's account from the telegram servers.
Can also be used to delete the account of a user that provided the login code, but forgot the 2FA password and no recovery method is configured, see [here »](https://core.telegram.org/api/srp#password-recovery) for more info on password recovery, and [here »](https://core.telegram.org/api/account-deletion) for more info on account deletion.

Parameters:

* `$reason`: `string` Why is the account being deleted, can be empty  
* `$password`: `string|array` [2FA password](https://core.telegram.org/api/srp): this field can be omitted even for accounts with 2FA enabled: in this case account account deletion will be delayed by 7 days [as specified in the docs »](https://core.telegram.org/api/account-deletion) @see https://docs.madelineproto.xyz/API_docs/types/InputCheckPasswordSRP.html  



### `getAccountTTL(): array{_: \"accountDaysTTL", days: \int} @see https://docs.madelineproto.xyz/API_docs/types/AccountDaysTTL.htm}`

Get days to live of account


Return value: @see https://docs.madelineproto.xyz/API_docs/types/AccountDaysTTL.html


### `setAccountTTL(array{_: \"accountDaysTTL", days?: int} $ttl): bool`

Set account self-destruction period


Parameters:

* `$ttl`: `array{_: \"accountDaysTTL", days?: int}` Time to live in days @see https://docs.madelineproto.xyz/API_docs/types/AccountDaysTTL.html  



### `sendChangePhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $phone_number = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`

Verify a new phone number to associate to the current account


Parameters:

* `$settings`: `array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool}` Phone code settings @see https://docs.madelineproto.xyz/API_docs/types/CodeSettings.html  
* `$phone_number`: `string` New phone number  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.html


### `changePhone(string $phone_number = '', string $phone_code_hash = '', string $phone_code = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`

Change the phone number of the current account


Parameters:

* `$phone_number`: `string` New phone number  
* `$phone_code_hash`: `string` Phone code hash received when calling [account.sendChangePhoneCode](https://docs.madelineproto.xyz/API_docs/methods/account.sendChangePhoneCode.html)  
* `$phone_code`: `string` Phone code received when calling [account.sendChangePhoneCode](https://docs.madelineproto.xyz/API_docs/methods/account.sendChangePhoneCode.html)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/User.html


### `updateDeviceLocked(int $period = 0): bool`

When client-side passcode lock feature is enabled, will not show message texts in incoming [PUSH notifications](https://core.telegram.org/api/push-updates).


Parameters:

* `$period`: `int` Inactivity period after which to start hiding message texts in [PUSH notifications](https://core.telegram.org/api/push-updates).  



### `getAuthorizations(): array{_: \"account.authorizations", authorization_ttl_days: int, authorizations: \list<array{_: "authorization", current: bool, official_app: bool, password_pending: bool, encrypted_requests_disabled: bool, call_requests_disabled: bool, hash: list<int>, device_model: string, platform: string, system_version: string, api_id: int, app_name: string, app_version: string, date_created: int, date_active: int, ip: string, country: string, region: string}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Authorizations.htm}`

Get logged-in sessions


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.Authorizations.html


### `resetAuthorization(list<int> $hash = []): bool`

Log out an active [authorized session](https://core.telegram.org/api/auth) by its hash


Parameters:

* `$hash`: `list<int>` Session hash  



### `getPassword(): array{_: \"account.password", new_algo: array{_: \"passwordKdfAlgoUnknown"}|array{_: \"passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", salt1: string, salt2: string, g: int, p: string}, new_secure_algo: array{_: \"securePasswordKdfAlgoUnknown"}|array{_: \"securePasswordKdfAlgoPBKDF2HMACSHA512iter100000", salt: string}|array{_: \"securePasswordKdfAlgoSHA512", salt: string}, has_recovery: bool, has_secure_values: bool, has_password: bool, current_algo?: array{_: \"passwordKdfAlgoUnknown"}|array{_: \"passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", salt1: string, salt2: string, g: int, p: string}, srp_B: string, srp_id: int, hint: string, email_unconfirmed_pattern: string, secure_random: string, pending_reset_date: int, login_email_pattern: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.Password.htm}`

Obtain configuration for two-factor authorization with password


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.Password.html


### `sendConfirmPhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $hash = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`

Send confirmation code to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)


Parameters:

* `$settings`: `array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool}` Phone code settings @see https://docs.madelineproto.xyz/API_docs/types/CodeSettings.html  
* `$hash`: `string` The hash from the service notification, for more info [click here »](https://core.telegram.org/api/account-deletion)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.html


### `confirmPhone(string $phone_code_hash = '', string $phone_code = ''): bool`

Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)


Parameters:

* `$phone_code_hash`: `string` Phone code hash, for more info [click here »](https://core.telegram.org/api/account-deletion)  
* `$phone_code`: `string` SMS code, for more info [click here »](https://core.telegram.org/api/account-deletion)  



### `getTmpPassword(string|array $password, int $period = 0): array{_: \"account.tmpPassword", tmp_password: string, valid_until: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.TmpPassword.htm}`

Get temporary payment password


Parameters:

* `$password`: `string|array` SRP password parameters @see https://docs.madelineproto.xyz/API_docs/types/InputCheckPasswordSRP.html  
* `$period`: `int` Time during which the temporary password will be valid, in seconds; should be between 60 and 86400  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.TmpPassword.html


### `getWebAuthorizations(): array{_: \"account.webAuthorizations", authorizations: list<array{_: \"webAuthorization", hash: list<int>, bot_id: int, domain: string, browser: string, platform: string, date_created: int, date_active: int, ip: string, region: string}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.WebAuthorizations.htm}`

Get web [login widget](https://core.telegram.org/widgets/login) authorizations


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.WebAuthorizations.html


### `resetWebAuthorization(list<int> $hash = []): bool`

Log out an active web [telegram login](https://core.telegram.org/widgets/login) session


Parameters:

* `$hash`: `list<int>` [Session](https://docs.madelineproto.xyz/API_docs/constructors/webAuthorization.html) hash  



### `resetWebAuthorizations(): bool`

Reset all active web [telegram login](https://core.telegram.org/widgets/login) sessions



### `getAllSecureValues(): \list<array{_: "secureValue", type: array{_: "secureValueTypePersonalDetails"}|array{_: "secureValueTypePassport"}|array{_: "secureValueTypeDriverLicense"}|array{_: "secureValueTypeIdentityCard"}|array{_: "secureValueTypeInternalPassport"}|array{_: "secureValueTypeAddress"}|array{_: "secureValueTypeUtilityBill"}|array{_: "secureValueTypeBankStatement"}|array{_: "secureValueTypeRentalAgreement"}|array{_: "secureValueTypePassportRegistration"}|array{_: "secureValueTypeTemporaryRegistration"}|array{_: "secureValueTypePhone"}|array{_: "secureValueTypeEmail"}, data?: array{_: "secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: "securePlainPhone", phone: string}|array{_: "securePlainEmail", email: string}, hash: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html`

Get all saved [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html


### `getSecureValue(list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}> $types = []): \list<array{_: "secureValue", type: array{_: "secureValueTypePersonalDetails"}|array{_: "secureValueTypePassport"}|array{_: "secureValueTypeDriverLicense"}|array{_: "secureValueTypeIdentityCard"}|array{_: "secureValueTypeInternalPassport"}|array{_: "secureValueTypeAddress"}|array{_: "secureValueTypeUtilityBill"}|array{_: "secureValueTypeBankStatement"}|array{_: "secureValueTypeRentalAgreement"}|array{_: "secureValueTypePassportRegistration"}|array{_: "secureValueTypeTemporaryRegistration"}|array{_: "secureValueTypePhone"}|array{_: "secureValueTypeEmail"}, data?: array{_: "secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: "secureFileEmpty"}|array{_: "secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: "securePlainPhone", phone: string}|array{_: "securePlainEmail", email: string}, hash: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html`

Get saved [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)


Parameters:

* `$types`: `list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}>` Array of Requested value types @see https://docs.madelineproto.xyz/API_docs/types/SecureValueType.html  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html


### `saveSecureValue(array{_: \"inputSecureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data?: string, data_hash?: string, secret?: string}, front_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, reverse_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, selfie?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, translation?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, files?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, plain_data?: array{_: \"securePlainPhone", phone?: string}|array{_: \"securePlainEmail", email?: string}} $value, int $secure_secret_id = 0): array{_: \"secureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: \"securePlainPhone", phone: string}|array{_: \"securePlainEmail", email: string}, hash: \string} @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.htm}`

Securely save [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)


Parameters:

* `$value`: `array{_: \"inputSecureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data?: string, data_hash?: string, secret?: string}, front_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, reverse_side?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, selfie?: array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}, translation?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, files?: list<array{_: \"inputSecureFileUploaded", id?: int, parts?: int, md5_checksum?: string, file_hash?: string, secret?: string}|array{_: \"inputSecureFile", id?: int, access_hash?: int}>, plain_data?: array{_: \"securePlainPhone", phone?: string}|array{_: \"securePlainEmail", email?: string}}` Secure value, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption) @see https://docs.madelineproto.xyz/API_docs/types/InputSecureValue.html  
* `$secure_secret_id`: `int` Passport secret hash, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/SecureValue.html


### `deleteSecureValue(list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}> $types = []): bool`

Delete stored [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)


Parameters:

* `$types`: `list<array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}>` Array of Document types to delete @see https://docs.madelineproto.xyz/API_docs/types/SecureValueType.html  



### `getAuthorizationForm(int $bot_id = 0, string $scope = '', string $public_key = ''): array{_: \"account.authorizationForm", required_types: list<array{_: \"secureRequiredType", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, native_names: bool, selfie_required: bool, translation_required: bool}>, values: list<array{_: \"secureValue", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data?: array{_: \"secureData", data: string, data_hash: string, secret: string}, front_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, reverse_side?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, selfie?: array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}, translation: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, files: list<array{_: \"secureFileEmpty"}|array{_: \"secureFile", id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: string, secret: string}>, plain_data?: array{_: \"securePlainPhone", phone: string}|array{_: \"securePlainEmail", email: string}, hash: string}>, errors: list<array{_: \"secureValueErrorData", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, data_hash: string, field: string, text: string}|array{_: \"secureValueErrorFrontSide", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorReverseSide", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorSelfie", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorFile", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorFiles", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: list<string>, text: string}|array{_: \"secureValueError", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, hash: string, text: string}|array{_: \"secureValueErrorTranslationFile", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: string, text: string}|array{_: \"secureValueErrorTranslationFiles", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, file_hash: list<string>, text: string}>, users: list<array|int|string>, privacy_policy_url: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.AuthorizationForm.htm}`

Returns a Telegram Passport authorization form for sharing data with a service


Parameters:

* `$bot_id`: `int` User identifier of the service's bot  
* `$scope`: `string` Telegram Passport element types requested by the service  
* `$public_key`: `string` Service's public key  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.AuthorizationForm.html


### `acceptAuthorization(array{_: \"secureCredentialsEncrypted", data?: string, hash?: string, secret?: string} $credentials, int $bot_id = 0, string $scope = '', string $public_key = '', list<array{_: \"secureValueHash", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, hash?: string}> $value_hashes = []): bool`

Sends a Telegram Passport authorization form, effectively sharing data with the service


Parameters:

* `$credentials`: `array{_: \"secureCredentialsEncrypted", data?: string, hash?: string, secret?: string}` Encrypted values @see https://docs.madelineproto.xyz/API_docs/types/SecureCredentialsEncrypted.html  
* `$bot_id`: `int` Bot ID  
* `$scope`: `string` Telegram Passport element types requested by the service  
* `$public_key`: `string` Service's public key  
* `$value_hashes`: `list<array{_: \"secureValueHash", type: array{_: \"secureValueTypePersonalDetails"}|array{_: \"secureValueTypePassport"}|array{_: \"secureValueTypeDriverLicense"}|array{_: \"secureValueTypeIdentityCard"}|array{_: \"secureValueTypeInternalPassport"}|array{_: \"secureValueTypeAddress"}|array{_: \"secureValueTypeUtilityBill"}|array{_: \"secureValueTypeBankStatement"}|array{_: \"secureValueTypeRentalAgreement"}|array{_: \"secureValueTypePassportRegistration"}|array{_: \"secureValueTypeTemporaryRegistration"}|array{_: \"secureValueTypePhone"}|array{_: \"secureValueTypeEmail"}, hash?: string}>` Array of Types of values sent and their hashes @see https://docs.madelineproto.xyz/API_docs/types/SecureValueHash.html  



### `sendVerifyPhoneCode(array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool} $settings, string $phone_number = ''): array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: \int}}} @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.h}}}`

Send the verification phone code for telegram [passport](https://core.telegram.org/passport).


Parameters:

* `$settings`: `array{_: \"codeSettings", allow_flashcall?: bool, current_number?: bool, allow_app_hash?: bool, allow_missed_call?: bool, allow_firebase?: bool, logout_tokens?: list<string>, token?: string, app_sandbox?: bool}` Phone code settings @see https://docs.madelineproto.xyz/API_docs/types/CodeSettings.html  
* `$phone_number`: `string` The phone number to verify  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/auth.SentCode.html


### `verifyPhone(string $phone_number = '', string $phone_code_hash = '', string $phone_code = ''): bool`

Verify a phone number for telegram [passport](https://core.telegram.org/passport).


Parameters:

* `$phone_number`: `string` Phone number  
* `$phone_code_hash`: `string` Phone code hash received from the call to [account.sendVerifyPhoneCode](https://docs.madelineproto.xyz/API_docs/methods/account.sendVerifyPhoneCode.html)  
* `$phone_code`: `string` Code received after the call to [account.sendVerifyPhoneCode](https://docs.madelineproto.xyz/API_docs/methods/account.sendVerifyPhoneCode.html)  



### `sendVerifyEmailCode(array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"} $purpose, string $email = ''): array{_: \"account.sentEmailCode", email_pattern: string, length: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.SentEmailCode.htm}`

Send an email verification code.


Parameters:

* `$purpose`: `array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"}` Verification purpose. @see https://docs.madelineproto.xyz/API_docs/types/EmailVerifyPurpose.html  
* `$email`: `string` The email where to send the code.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.SentEmailCode.html


### `verifyEmail(array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"} $purpose, array{_: \"emailVerificationCode", code?: string}|array{_: \"emailVerificationGoogle", token?: string}|array{_: \"emailVerificationApple", token?: string} $verification): array{_: \"account.emailVerified", email: string}|array{_: \"account.emailVerifiedLogin", sent_code: array{_: \"auth.sentCode", type: array{_: \"auth.sentCodeTypeApp", length: int}|array{_: \"auth.sentCodeTypeSms", length: int}|array{_: \"auth.sentCodeTypeCall", length: int}|array{_: \"auth.sentCodeTypeFlashCall", pattern: string}|array{_: \"auth.sentCodeTypeMissedCall", prefix: string, length: int}|array{_: \"auth.sentCodeTypeEmailCode", apple_signin_allowed: bool, google_signin_allowed: bool, email_pattern: string, length: int, reset_available_period: int, reset_pending_date: int}|array{_: \"auth.sentCodeTypeSetUpEmailRequired", apple_signin_allowed: bool, google_signin_allowed: bool}|array{_: \"auth.sentCodeTypeFragmentSms", url: string, length: int}|array{_: \"auth.sentCodeTypeFirebaseSms", nonce: string, receipt: string, push_timeout: int, length: int}, phone_code_hash: string, next_type?: array{_: \"auth.codeTypeSms"}|array{_: \"auth.codeTypeCall"}|array{_: \"auth.codeTypeFlashCall"}|array{_: \"auth.codeTypeMissedCall"}|array{_: \"auth.codeTypeFragmentSms"}, timeout: int}|array{_: \"auth.sentCodeSuccess", authorization: array{_: \"auth.authorization", user: array|int|string, setup_password_required: bool, otherwise_relogin_days: int, tmp_sessions: int, future_auth_token: string}|array{_: \"auth.authorizationSignUpRequired", terms_of_service?: array{_: \"help.termsOfService", id: mixed, popup: bool, text: string, entities: list<array{_: \"messageEntityUnknown", offset: int, length: int}|array{_: \"messageEntityMention", offset: int, length: int}|array{_: \"messageEntityHashtag", offset: int, length: int}|array{_: \"messageEntityBotCommand", offset: int, length: int}|array{_: \"messageEntityUrl", offset: int, length: int}|array{_: \"messageEntityEmail", offset: int, length: int}|array{_: \"messageEntityBold", offset: int, length: int}|array{_: \"messageEntityItalic", offset: int, length: int}|array{_: \"messageEntityCode", offset: int, length: int}|array{_: \"messageEntityPre", offset: int, length: int, language: string}|array{_: \"messageEntityTextUrl", offset: int, length: int, url: string}|array{_: \"messageEntityMentionName", offset: int, length: int, user_id: int}|array{_: \"inputMessageEntityMentionName", user_id: array|int|string, offset: int, length: int}|array{_: \"messageEntityPhone", offset: int, length: int}|array{_: \"messageEntityCashtag", offset: int, length: int}|array{_: \"messageEntityUnderline", offset: int, length: int}|array{_: \"messageEntityStrike", offset: int, length: int}|array{_: \"messageEntityBlockquote", offset: int, length: int}|array{_: \"messageEntityBankCard", offset: int, length: int}|array{_: \"messageEntitySpoiler", offset: int, length: int}|array{_: \"messageEntityCustomEmoji", offset: int, length: int, document_id: int}>, min_age_confirm: int}}}, email: \string} @see https://docs.madelineproto.xyz/API_docs/types/account.EmailVerified.htm}`

Verify an email address.


Parameters:

* `$purpose`: `array{_: \"emailVerifyPurposeLoginSetup", phone_number?: string, phone_code_hash?: string}|array{_: \"emailVerifyPurposeLoginChange"}|array{_: \"emailVerifyPurposePassport"}` Verification purpose @see https://docs.madelineproto.xyz/API_docs/types/EmailVerifyPurpose.html  
* `$verification`: `array{_: \"emailVerificationCode", code?: string}|array{_: \"emailVerificationGoogle", token?: string}|array{_: \"emailVerificationApple", token?: string}` Email verification code or token @see https://docs.madelineproto.xyz/API_docs/types/EmailVerification.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.EmailVerified.html


### `initTakeoutSession(bool $contacts = false, bool $message_users = false, bool $message_chats = false, bool $message_megagroups = false, bool $message_channels = false, bool $files = false, int $file_max_size = 0): array{_: \"account.takeout", id: \int} @see https://docs.madelineproto.xyz/API_docs/types/account.Takeout.htm}`

Initialize account takeout session


Parameters:

* `$contacts`: `bool` Whether to export contacts  
* `$message_users`: `bool` Whether to export messages in private chats  
* `$message_chats`: `bool` Whether to export messages in [basic groups](https://core.telegram.org/api/channel#basic-groups)  
* `$message_megagroups`: `bool` Whether to export messages in [supergroups](https://core.telegram.org/api/channel#supergroups)  
* `$message_channels`: `bool` Whether to export messages in [channels](https://core.telegram.org/api/channel#channels)  
* `$files`: `bool` Whether to export files  
* `$file_max_size`: `int` Maximum size of files to export  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.Takeout.html


### `finishTakeoutSession(bool $success = false): bool`

Finish account takeout session


Parameters:

* `$success`: `bool` Data exported successfully  



### `confirmPasswordEmail(string $code = ''): bool`

Verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).


Parameters:

* `$code`: `string` The phone code that was received after [setting a recovery email](https://core.telegram.org/api/srp#email-verification)  



### `resendPasswordEmail(): bool`

Resend the code to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).



### `cancelPasswordEmail(): bool`

Cancel the code that was sent to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).



### `getContactSignUpNotification(): bool`

Whether the user will receive notifications when contacts sign up



### `setContactSignUpNotification(bool $silent): bool`

Toggle contact sign up notifications


Parameters:

* `$silent`: `bool` Whether to disable contact sign up notifications  



### `getNotifyExceptions(bool $compare_sound = false, array|int|string $peer = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Returns list of chats with non-default notification settings


Parameters:

* `$compare_sound`: `bool` If true, chats with non-default sound will also be returned  
* `$peer`: `array|int|string` If specified, only chats of the specified category will be returned @see https://docs.madelineproto.xyz/API_docs/types/InputNotifyPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper): array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: \int}} @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.ht}}`

Get info about a certain [wallpaper](https://core.telegram.org/api/wallpapers)


Parameters:

* `$wallpaper`: `array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}` The [wallpaper](https://core.telegram.org/api/wallpapers) to get info about @see https://docs.madelineproto.xyz/API_docs/types/InputWallPaper.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.html


### `uploadWallPaper(mixed $file, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings, bool $for_chat = false, string $mime_type = ''): array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: \int}} @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.ht}}`

Create and upload a new [wallpaper](https://core.telegram.org/api/wallpapers)


Parameters:

* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$settings`: `array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}` Wallpaper settings @see https://docs.madelineproto.xyz/API_docs/types/WallPaperSettings.html  
* `$for_chat`: `bool` Set this flag when uploading wallpapers to be passed to [messages.setChatWallPaper](https://docs.madelineproto.xyz/API_docs/methods/messages.setChatWallPaper.html).  
* `$mime_type`: `string` MIME type of uploaded wallpaper  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.html


### `saveWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper, bool $unsave, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings): bool`

Install/uninstall [wallpaper](https://core.telegram.org/api/wallpapers)


Parameters:

* `$wallpaper`: `array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}` [Wallpaper](https://core.telegram.org/api/wallpapers) to install or uninstall @see https://docs.madelineproto.xyz/API_docs/types/InputWallPaper.html  
* `$unsave`: `bool` Uninstall wallpaper?  
* `$settings`: `array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}` Wallpaper settings @see https://docs.madelineproto.xyz/API_docs/types/WallPaperSettings.html  



### `installWallPaper(array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int} $wallpaper, array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int} $settings): bool`

Install [wallpaper](https://core.telegram.org/api/wallpapers)


Parameters:

* `$wallpaper`: `array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}` [Wallpaper](https://core.telegram.org/api/wallpapers) to install @see https://docs.madelineproto.xyz/API_docs/types/InputWallPaper.html  
* `$settings`: `array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}` [Wallpaper](https://core.telegram.org/api/wallpapers) settings @see https://docs.madelineproto.xyz/API_docs/types/WallPaperSettings.html  



### `resetWallPapers(): bool`

Delete all installed [wallpapers](https://core.telegram.org/api/wallpapers), reverting to the default wallpaper set.



### `getAutoDownloadSettings(): array{_: \"account.autoDownloadSettings", low: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int}, medium: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int}, high: array{_: \"autoDownloadSettings", disabled: bool, video_preload_large: bool, audio_preload_next: bool, phonecalls_less_data: bool, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: \int}} @see https://docs.madelineproto.xyz/API_docs/types/account.AutoDownloadSettings.ht}}`

Get media autodownload settings


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.AutoDownloadSettings.html


### `saveAutoDownloadSettings(array{_: \"autoDownloadSettings", disabled?: bool, video_preload_large?: bool, audio_preload_next?: bool, phonecalls_less_data?: bool, photo_size_max?: int, video_size_max?: int, file_size_max?: int, video_upload_maxbitrate?: int} $settings, bool $low = false, bool $high = false): bool`

Change media autodownload settings


Parameters:

* `$settings`: `array{_: \"autoDownloadSettings", disabled?: bool, video_preload_large?: bool, audio_preload_next?: bool, phonecalls_less_data?: bool, photo_size_max?: int, video_size_max?: int, file_size_max?: int, video_upload_maxbitrate?: int}` Media autodownload settings @see https://docs.madelineproto.xyz/API_docs/types/AutoDownloadSettings.html  
* `$low`: `bool` Whether to save media in the low data usage preset  
* `$high`: `bool` Whether to save media in the high data usage preset  



### `uploadTheme(mixed $file, mixed $thumb = [], string $file_name = '', string $mime_type = ''): array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>} @see https://docs.madelineproto.xyz/API_docs/types/Document.htm}`

Upload theme


Parameters:

* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$thumb`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$file_name`: `string` File name  
* `$mime_type`: `string` MIME type, must be `application/x-tgtheme-{format}`, where `format` depends on the client  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Document.html


### `createTheme(string $slug = '', string $title = '', array $document = [], list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}> $settings = []): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`

Create a theme


Parameters:

* `$slug`: `string` Unique theme ID used to generate [theme deep links](https://core.telegram.org/api/links#theme-links), can be empty to autogenerate a random ID.  
* `$title`: `string` Theme name  
* `$document`: `array` Theme file @see https://docs.madelineproto.xyz/API_docs/types/InputDocument.html  
* `$settings`: `list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}>` Array of Theme settings, multiple values can be provided for the different base themes (day/night mode, etc). @see https://docs.madelineproto.xyz/API_docs/types/InputThemeSettings.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Theme.html


### `updateTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, string $format = '', string $slug = '', string $title = '', array $document = [], list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}> $settings = []): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`

Update theme


Parameters:

* `$theme`: `array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string}` Theme to update @see https://docs.madelineproto.xyz/API_docs/types/InputTheme.html  
* `$format`: `string` Theme format, a string that identifies the theming engines supported by the client  
* `$slug`: `string` Unique theme ID  
* `$title`: `string` Theme name  
* `$document`: `array` Theme file @see https://docs.madelineproto.xyz/API_docs/types/InputDocument.html  
* `$settings`: `list<array{_: \"inputThemeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated?: bool, accent_color?: int, outbox_accent_color?: int, message_colors?: list<int>, wallpaper?: array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}, wallpaper_settings?: array{_: \"wallPaperSettings", blur?: bool, motion?: bool, background_color?: int, second_background_color?: int, third_background_color?: int, fourth_background_color?: int, intensity?: int, rotation?: int}}>` Array of Theme settings @see https://docs.madelineproto.xyz/API_docs/types/InputThemeSettings.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Theme.html


### `saveTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, bool $unsave): bool`

Save a theme


Parameters:

* `$theme`: `array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string}` Theme to save @see https://docs.madelineproto.xyz/API_docs/types/InputTheme.html  
* `$unsave`: `bool` Unsave  



### `installTheme(bool $dark = false, array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme = [], string $format = '', array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"} $base_theme = []): bool`

Install a theme


Parameters:

* `$dark`: `bool` Whether to install the dark version  
* `$theme`: `array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string}` Theme to install @see https://docs.madelineproto.xyz/API_docs/types/InputTheme.html  
* `$format`: `string` Theme format, a string that identifies the theming engines supported by the client  
* `$base_theme`: `array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}` Indicates a basic theme provided by all clients @see https://docs.madelineproto.xyz/API_docs/types/BaseTheme.html  



### `getTheme(array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string} $theme, string $format = ''): array{_: \"theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: \"themeSettings", base_theme: array{_: \"baseThemeClassic"}|array{_: \"baseThemeDay"}|array{_: \"baseThemeNight"}|array{_: \"baseThemeTinted"}|array{_: \"baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: \"wallPaper", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: \"wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: \"wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: \int} @see https://docs.madelineproto.xyz/API_docs/types/Theme.htm}`

Get theme information


Parameters:

* `$theme`: `array{_: \"inputTheme", id?: int, access_hash?: int}|array{_: \"inputThemeSlug", slug?: string}` Theme @see https://docs.madelineproto.xyz/API_docs/types/InputTheme.html  
* `$format`: `string` Theme format, a string that identifies the theming engines supported by the client  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Theme.html


### `getThemes(string $format = '', list<int> $hash = []): array{_: \"account.themesNotModified"}|array{_: \"account.themes", hash: list<int>, themes: \list<array{_: "theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: "themeSettings", base_theme: array{_: "baseThemeClassic"}|array{_: "baseThemeDay"}|array{_: "baseThemeNight"}|array{_: "baseThemeTinted"}|array{_: "baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.htm}`

Get installed themes


Parameters:

* `$format`: `string` Theme format, a string that identifies the theming engines supported by the client  
* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.html


### `setContentSettings(bool $sensitive_enabled = false): bool`

Set sensitive content settings (for viewing or hiding NSFW content)


Parameters:

* `$sensitive_enabled`: `bool` Enable NSFW content  



### `getContentSettings(): array{_: \"account.contentSettings", sensitive_enabled: bool, sensitive_can_change: \bool} @see https://docs.madelineproto.xyz/API_docs/types/account.ContentSettings.htm}`

Get sensitive content settings


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.ContentSettings.html


### `getMultiWallPapers(list<array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}> $wallpapers = []): \list<array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.html`

Get info about multiple [wallpapers](https://core.telegram.org/api/wallpapers)


Parameters:

* `$wallpapers`: `list<array{_: \"inputWallPaper", id?: int, access_hash?: int}|array{_: \"inputWallPaperSlug", slug?: string}|array{_: \"inputWallPaperNoFile", id?: int}>` Array of [Wallpapers](https://core.telegram.org/api/wallpapers) to fetch info about @see https://docs.madelineproto.xyz/API_docs/types/InputWallPaper.html  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/WallPaper.html


### `getGlobalPrivacySettings(): array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: \bool} @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.htm}`

Get global privacy settings


Return value: @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.html


### `setGlobalPrivacySettings(array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: bool} $settings): array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: \bool} @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.htm}`

Set global privacy settings


Parameters:

* `$settings`: `array{_: \"globalPrivacySettings", archive_and_mute_new_noncontact_peers?: bool}` Global privacy settings @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/GlobalPrivacySettings.html


### `reportProfilePhoto(array|int|string $peer, array $photo_id, array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"} $reason, string $message = ''): bool`

Report a profile photo of a dialog


Parameters:

* `$peer`: `array|int|string` The dialog @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$photo_id`: `array` Dialog photo ID @see https://docs.madelineproto.xyz/API_docs/types/InputPhoto.html  
* `$reason`: `array{_: \"inputReportReasonSpam"}|array{_: \"inputReportReasonViolence"}|array{_: \"inputReportReasonPornography"}|array{_: \"inputReportReasonChildAbuse"}|array{_: \"inputReportReasonOther"}|array{_: \"inputReportReasonCopyright"}|array{_: \"inputReportReasonGeoIrrelevant"}|array{_: \"inputReportReasonFake"}|array{_: \"inputReportReasonIllegalDrugs"}|array{_: \"inputReportReasonPersonalDetails"}` Report reason @see https://docs.madelineproto.xyz/API_docs/types/ReportReason.html  
* `$message`: `string` Comment for report moderation  



### `resetPassword(): array{_: \"account.resetPasswordFailedWait", retry_date: int}|array{_: \"account.resetPasswordRequestedWait", until_date: int}|array{_: \"account.resetPasswordOk"} @see https://docs.madelineproto.xyz/API_docs/types/account.ResetPasswordResult.htm}`

Initiate a 2FA password reset: can only be used if the user is already logged-in, [see here for more info »](https://core.telegram.org/api/srp#password-reset)


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.ResetPasswordResult.html


### `declinePasswordReset(): bool`

Abort a pending 2FA password reset, [see here for more info »](https://core.telegram.org/api/srp#password-reset)



### `getChatThemes(list<int> $hash = []): array{_: \"account.themesNotModified"}|array{_: \"account.themes", hash: list<int>, themes: \list<array{_: "theme", creator: bool, default: bool, for_chat: bool, id: int, access_hash: int, slug: string, title: string, document?: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, settings: list<array{_: "themeSettings", base_theme: array{_: "baseThemeClassic"}|array{_: "baseThemeDay"}|array{_: "baseThemeNight"}|array{_: "baseThemeTinted"}|array{_: "baseThemeArctic"}, message_colors_animated: bool, accent_color: int, outbox_accent_color: int, message_colors: list<int>, wallpaper?: array{_: "wallPaper", document: array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}, id: int, creator: bool, default: bool, pattern: bool, dark: bool, access_hash: int, slug: string, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}|array{_: "wallPaperNoFile", id: int, default: bool, dark: bool, settings?: array{_: "wallPaperSettings", blur: bool, motion: bool, background_color: int, second_background_color: int, third_background_color: int, fourth_background_color: int, intensity: int, rotation: int}}}>, emoticon: string, installs_count: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.htm}`

Get all available chat themes


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.Themes.html


### `setAuthorizationTTL(int $authorization_ttl_days = 0): bool`

Set time-to-live of current session


Parameters:

* `$authorization_ttl_days`: `int` Time-to-live of current session in days  



### `changeAuthorizationSettings(list<int> $hash = [], bool $encrypted_requests_disabled = false, bool $call_requests_disabled = false): bool`

Change authorization settings


Parameters:

* `$hash`: `list<int>` Session ID from the [authorization](https://docs.madelineproto.xyz/API_docs/constructors/authorization.html) constructor, fetchable using [account.getAuthorizations](https://docs.madelineproto.xyz/API_docs/methods/account.getAuthorizations.html)  
* `$encrypted_requests_disabled`: `bool` Whether to enable or disable receiving encrypted chats: if the flag is not set, the previous setting is not changed  
* `$call_requests_disabled`: `bool` Whether to enable or disable receiving calls: if the flag is not set, the previous setting is not changed  



### `getSavedRingtones(list<int> $hash = []): array{_: \"account.savedRingtonesNotModified"}|array{_: \"account.savedRingtones", hash: list<int>, ringtones: \list<array{_: "documentEmpty", id: array}|array{_: "document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: list<array>}>} @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtones.htm}`

Fetch saved notification sounds


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtones.html


### `saveRingtone(array $id, bool $unsave): array{_: \"account.savedRingtone"}|array{_: \"account.savedRingtoneConverted", document: array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>}} @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtone.ht}}`

Save or remove saved notification sound.
If the notification sound is already in MP3 format, [account.savedRingtone](https://docs.madelineproto.xyz/API_docs/constructors/account.savedRingtone.html) will be returned.  
Otherwise, it will be automatically converted and a [account.savedRingtoneConverted](https://docs.madelineproto.xyz/API_docs/constructors/account.savedRingtoneConverted.html) will be returned, containing a new [document](https://docs.madelineproto.xyz/API_docs/constructors/document.html) object that should be used to refer to the ringtone from now on (ie when deleting it using the `unsave` parameter, or when downloading it).

Parameters:

* `$id`: `array` Notification sound uploaded using [account.uploadRingtone](https://docs.madelineproto.xyz/API_docs/methods/account.uploadRingtone.html) @see https://docs.madelineproto.xyz/API_docs/types/InputDocument.html  
* `$unsave`: `bool` Whether to add or delete the notification sound  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.SavedRingtone.html


### `uploadRingtone(mixed $file, string $file_name = '', string $mime_type = ''): array{_: \"documentEmpty", id: array}|array{_: \"document", id: array, access_hash: array, file_reference: array, date: array, mime_type: array, size: array, thumbs: list<array>, video_thumbs: list<array>, dc_id: array, attributes: \list<array>} @see https://docs.madelineproto.xyz/API_docs/types/Document.htm}`

Upload notification sound, use [account.saveRingtone](https://docs.madelineproto.xyz/API_docs/methods/account.saveRingtone.html) to convert it and add it to the list of saved notification sounds.


Parameters:

* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$file_name`: `string` File name  
* `$mime_type`: `string` MIME type of file  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Document.html


### `updateEmojiStatus(array{_: \"emojiStatusEmpty"}|array{_: \"emojiStatus", document_id?: int}|array{_: \"emojiStatusUntil", document_id?: int, until?: int} $emoji_status): bool`

Set an [emoji status](https://core.telegram.org/api/emoji-status)


Parameters:

* `$emoji_status`: `array{_: \"emojiStatusEmpty"}|array{_: \"emojiStatus", document_id?: int}|array{_: \"emojiStatusUntil", document_id?: int, until?: int}` [Emoji status](https://core.telegram.org/api/emoji-status) to set @see https://docs.madelineproto.xyz/API_docs/types/EmojiStatus.html  



### `getDefaultEmojiStatuses(list<int> $hash = []): array{_: \"account.emojiStatusesNotModified"}|array{_: \"account.emojiStatuses", hash: list<int>, statuses: \list<array{_: "emojiStatusEmpty"}|array{_: "emojiStatus", document_id: int}|array{_: "emojiStatusUntil", document_id: int, until: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.htm}`

Get a list of default suggested [emoji statuses](https://core.telegram.org/api/emoji-status)


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.html


### `getRecentEmojiStatuses(list<int> $hash = []): array{_: \"account.emojiStatusesNotModified"}|array{_: \"account.emojiStatuses", hash: list<int>, statuses: \list<array{_: "emojiStatusEmpty"}|array{_: "emojiStatus", document_id: int}|array{_: "emojiStatusUntil", document_id: int, until: int}>} @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.htm}`

Get recently used [emoji statuses](https://core.telegram.org/api/emoji-status)


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.EmojiStatuses.html


### `clearRecentEmojiStatuses(): bool`

Clears list of recently used [emoji statuses](https://core.telegram.org/api/emoji-status)



### `reorderUsernames(list<string> $order = []): bool`

Reorder usernames associated with the currently logged-in user.


Parameters:

* `$order`: `list<string>` The new order for active usernames. All active usernames must be specified.  



### `toggleUsername(bool $active, string $username = ''): bool`

Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to the currently logged-in user.


Parameters:

* `$active`: `bool` Whether to activate or deactivate it  
* `$username`: `string` Username  



### `getDefaultProfilePhotoEmojis(list<int> $hash = []): array{_: \"emojiListNotModified"}|array{_: \"emojiList", hash: list<int>, document_id: \list<int>} @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.htm}`

Get a set of suggested [custom emoji stickers](https://core.telegram.org/api/custom-emoji) that can be [used as profile picture](https://core.telegram.org/api/files#sticker-profile-pictures)


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.html


### `getDefaultGroupPhotoEmojis(list<int> $hash = []): array{_: \"emojiListNotModified"}|array{_: \"emojiList", hash: list<int>, document_id: \list<int>} @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.htm}`

Get a set of suggested [custom emoji stickers](https://core.telegram.org/api/custom-emoji) that can be [used as group picture](https://core.telegram.org/api/files#sticker-profile-pictures)


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/EmojiList.html


### `getAutoSaveSettings(): array{_: \"account.autoSaveSettings", users_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, chats_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, broadcasts_settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}, exceptions: list<array{_: \"autoSaveException", peer: array|int|string, settings: array{_: \"autoSaveSettings", photos: bool, videos: bool, video_max_size: int}}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/account.AutoSaveSettings.htm}`

Get autosave settings


Return value: @see https://docs.madelineproto.xyz/API_docs/types/account.AutoSaveSettings.html


### `saveAutoSaveSettings(array{_: \"autoSaveSettings", photos?: bool, videos?: bool, video_max_size?: int} $settings, bool $users = false, bool $chats = false, bool $broadcasts = false, array|int|string $peer = []): bool`

Modify autosave settings


Parameters:

* `$settings`: `array{_: \"autoSaveSettings", photos?: bool, videos?: bool, video_max_size?: int}` The new autosave settings @see https://docs.madelineproto.xyz/API_docs/types/AutoSaveSettings.html  
* `$users`: `bool` Whether the new settings should affect all private chats  
* `$chats`: `bool` Whether the new settings should affect all groups  
* `$broadcasts`: `bool` Whether the new settings should affect all [channels](https://core.telegram.org/api/channel)  
* `$peer`: `array|int|string` Whether the new settings should affect a specific peer @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  



### `deleteAutoSaveExceptions(): bool`

Clear all peer-specific autosave settings.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)

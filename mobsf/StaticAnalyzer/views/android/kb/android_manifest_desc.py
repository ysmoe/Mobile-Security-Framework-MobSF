MANIFEST_DESC = {
    'well_known_assetlinks': {
        'title': ('未找到 App Link assetlinks.json 文件 [android:name=%s][android:host=%'
                  's]'),
        'level': 'high',
        'description': ('App Link 资源验证 URL (%s) 未找到或配置错误。(状态码: %s)。'
                  'App Links 允许用户从网页 URL/邮件跳转到移动应用。如果该文件缺失或针对 App Link 主机/域名配置错误，'
                  '恶意应用可以劫持这些 URL。'
                  '这可能导致钓鱼攻击、URI 中敏感数据（如 PII、OAuth 令牌、魔法链接/密码重置令牌等）泄露。'
                  '您必须通过托管 assetlinks.jso'
                  'n 文件并在该 Activity 的 intent-filter 中启用 [android:autoVerify="true"]'
                  ' 验证来验证 App Link 域名。'),
        'name': ('未找到 App Link assetlinks.json 文件 [android:name=%s],'
                  ' [android:host=%s]'),
    },
    'clear_text_traffic': {
        'title': '应用已启用明文流量 [android:usesCleartextTraffic=true]',
        'level': 'high',
        'description': ('该应用打算使用明文网络流量，例如明文 HTTP、FTP 协议栈、DownloadManager 和 MediaPlayer。'
                  '针对 API level 27 或更低版本的应用，其默认值为 "true"。针对 API level 28 或更高版本的应用，'
                  '其默认值为 "false"。应避免使用明文流量的主要原因是其缺乏机密性、真实性以及对篡改的防护；网络攻击者可以窃听传输的数据，'
                  '并且可以在不被察觉的情况下修改数据。'),
        'name': '应用已启用明文流量 [android:usesCleartextTraffic=true]',
    },
    'direct_boot_aware': {
        'title': '应用支持 Direct Boot [android:directBootAware=true]',
        'level': 'info',
        'description': ('此应用可以在用户解锁设备之前运行。如果您使用了 Application 的自定义子类，'
                  '并且您应用中的任何组件支持 direct-boot aware，'
                  '那么您整个自定义应用都会被认为是 direct-boot aware 的。在 Direct Boot 期间，'
                  '您的应用只能访问存储在设备保护存储区中的数据。'),
        'name': '应用支持 Direct Boot [android:directBootAware=true]',
    },
    'has_network_security': {
        'title': '应用具有网络安全配置 [android:networkSecurityConfig=%s]',
        'level': 'info',
        'description': ('网络安全配置 (Network Security Configuration) 功能允许应用在安全的声明式配置文件中自定义其网络'
                  '安全设置，而无需修改应用代码。这些设置可以针对特定域和特定应用进行配置。'),
        'name': '应用具有网络安全配置 [android:networkSecurityConfig=%s]',
    },
    'vulnerable_os_version': {
        'title': '应用可安装在不安全的未修补 Android 版本 %s 上, [minSdk=%s]',
        'level': 'high',
        'description': ('此应用可以安装在存在多个未修复漏洞的旧版 Android 系统上。这些设备将无法从 Google 获得合理的安全更新。'
                  '建议支持 Android 版本 => 10、API 29，以获得合理的安全更新。'),
        'name': '应用可安装在不安全的未修补 Android 版本 %s 上, [minSdk=%s]',
    },
    'vulnerable_os_version2': {
        'title': '应用可安装在不安全的 Android 版本 %s 上, minSdk=%s]',
        'level': 'warning',
        'description': ('此应用可以安装在存在多个漏洞的旧版 Android 系统上。建议支持 Android 版本 => 10、API 29，'
                  '以获得合理的安全更新。'),
        'name': '应用可安装在不安全的 Android 版本 %s 上, [minSdk=%s]',
    },
    'app_is_debuggable': {
        'title': '应用已启用调试 [android:debuggable=true]',
        'level': 'high',
        'description': '应用启用了调试，这使得逆向工程师更容易将调试器附加到该应用上。这允许转储堆栈跟踪并访问调试辅助类。',
        'name': '应用已启用调试 [android:debuggable=true]',
    },
    'app_allowbackup': {
        'title': '应用数据可被备份 [android:allowBackup=true]',
        'level': 'warning',
        'description': '此标志允许任何人通过 adb 备份您的应用数据。它允许已启用 USB 调试的用户将应用数据从设备复制出去。',
        'name': '应用数据可被备份 [android:allowBackup=true]',
    },
    'allowbackup_not_set': {
        'title': '应用数据可被备份 [android:allowBackup] 标志缺失。',
        'level': 'warning',
        'description': ('应将标志 [android:allowBackup] 设置为 false。默认情况下设置为 true，'
                  '允许任何人通过 adb 备份您的应用数据。它允许已启用 USB 调试的用户将应用数据从设备复制出去。'),
        'name': '应用数据可被备份 [android:allowBackup] 标志缺失。',
    },
    'app_in_test_mode': {
        'title': '应用处于测试模式 [android:testOnly=true]',
        'level': 'high',
        'description': '它可能会暴露其自身之外的功能或数据，从而造成安全漏洞。',
        'name': '应用处于测试模式 [android:testOnly=true]',
    },
    'task_affinity_set': {
        'title': '已为 Activity (%s) 设置 TaskAffinity',
        'level': 'warning',
        'description': ('如果设置了 taskAffinity，那么其他应用可以读取发送到属于另一个任务的 Activity 的 Intent。'
                  '应始终使用默认设置，将 affinity 保留为包名，以防止发送或接收的 Intent 中的敏感信息被其他应用读取。'),
        'name': '已为 Activity (%s) 设置 TaskAffinity',
    },
    'non_standard_launchmode': {
        'title': 'Activity (%s) 的启动模式不是标准的。',
        'level': 'warning',
        'description': ('Activity 不应将启动模式属性设置为 "singleTask/singleInstance"，'
                  '因为它会成为根 Activity，其他应用可以读取调用 Intent 的内容。因此，当 Intent 中包含敏感信息时，'
                  '需要使用 "standard" 启动模式属性。'),
        'name': 'Activity (%s) 的启动模式不是标准的。',
    },
    'task_hijacking': {
        'title': 'Activity (%s) 容易受到 Android 任务劫持/StrandHogg 攻击。',
        'level': 'high',
        'description': ('Activity 不应将启动模式属性设置为 "singleTask"。'
                  '这将使其他应用能够将恶意 Activity 放置在该 Activity 堆栈的顶部，'
                  '从而导致任务劫持/StrandHogg 1.0 漏洞。这使得该应用很容易成为钓鱼攻击的目标。'
                  '可以通过将'
                  '启动模式属性设置为 "singleInstance" 或设置空的 taskAffinity (taskAffinity="") '
                  '属性来修复该漏洞。您也可以将应用的目标 SDK 版本 (%s) 更新到 28 或更高版本，以在平台层面修复此问题。'),
        'name': 'Activity (%s) 容易受到 Android 任务劫持/StrandHogg 攻击。',
    },
    'task_hijacking2': {
        'title': 'Activity (%s) 容易受到 StrandHogg 2.0 攻击',
        'level': 'high',
        'description': ('发现该 Activity 容易受到 StrandHogg 2.0 任务劫持漏洞的影响。当存在漏洞时，'
                  '其他应用可以将恶意 Activity 放置在易受攻击应用的 Activity 堆栈顶部。这使得该应用很容易成为钓鱼攻击的目标。'
                  '可以通过将启动模式属性设置为 '
                  '"singleInstance" 并设置空的 taskAffinity (taskAffinity="") 来修复该漏洞。'
                  '您也可以将应用的目标 SDK 版本 (%s) 更新到 29 或更高版本，以在平台层面修复此问题。'),
        'name': 'Activity (%s) 容易受到 StrandHogg 2.0 攻击',
    },
    'improper_provider_permission': {
        'title': 'Content Provider 权限设置不当 [%s]',
        'level': 'warning',
        'description': ('Content Provider 的权限被设置为允许设备上任何其他应用访问。'
                  'Content Provider 可能包含关于应用的敏感信息，因此不应被共享。'),
        'name': 'Content Provider 权限设置不当',
    },
    'dialer_code_found': {
        'title': '拨号器代码: %s 已发现 [android:scheme="android_secret_code"]',
        'level': 'warning',
        'description': '在清单文件中发现了一个秘密代码。在拨号器中输入这些代码时，会授予对可能包含敏感信息的隐藏内容的访问权限。',
        'name': '拨号器代码: %s 已发现。 [android:scheme="android_secret_code"]',
    },
    'sms_receiver_port_found': {
        'title': '已在端口 %s 上设置数据 SMS 接收器 [android:port]',
        'level': 'warning',
        'description': ('已配置二进制 SMS 接收器以监听某个端口。发送到设备的二进制 SMS 消息以开发者选择的任何方式由应用处理。'
                  '此 SMS 中的数据应由应用进行适当的验证。此外，应用应假定接收到的 SMS 来自不受信任的来源。'),
        'name': '已在端口 %s 上设置数据 SMS 接收器。 [android:port]',
    },
    'high_intent_priority_found': {
        'title': 'Intent 优先级过高 (%s) - {%s} 次匹配 [android:priority]',
        'level': 'warning',
        'description': '通过将 intent 优先级设置为高于其他 intent，该应用实际上会覆盖其他请求。',
        'name': 'Intent 优先级过高 (%s) - {%s} 次匹配 [android:priority]',
    },
    'high_action_priority_found': {
        'title': 'Action 优先级过高 (%s)[android:priority] ',
        'level': 'warning',
        'description': '通过将 action 优先级设置为高于其他 action，该应用实际上会覆盖其他请求。',
        'name': 'Action 优先级过高 (%s)。 [android:priority]',
    },
    'exported_protected_permission_signature': {
        'title': '%s (%s) 受权限保护。%s [android:exported=true]',
        'level': 'info',
        'description': '发现%s %s 已导出，但受权限保护。',
        'name': '%s %s 受权限保护。[%s] [android:exported=true]',
    },
    'exported_protected_permission_normal': {
        'title': '%s (%s) 受权限保护，但应检查该权限的保护级别。%s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受权限保护。但是，'
                  '该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。如果设置为 signature，'
                  '则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_dangerous': {
        'title': '%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受权限保护。但是，'
                  '该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_signatureorsystem': {
        'title': '%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'info',
        'description': ('发现%s %s 已导出，但受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。'
                  '建议改用 signature 级别。对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': '%s %s 受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_not_defined': {
        'title': '%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受一个在所分析的应用中未定义的权限保护。因此，'
                  '应在定义该权限的地方检查其保护级别。如果设置为 normal 或 dangerous，'
                  '恶意应用可以请求并获得该权限并与该组件进行交互。如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_normal_app_level': {
        'title': '%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它在应用级别受权限保护。但是，'
                  '该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。如果设置为 signature，'
                  '则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_dangerous_app_level': {
        'title': '%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它在应用级别受权限保护。但是，'
                  '该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission': {
        'title': '%s (%s) 在应用级别受权限保护。 %s [android:exported=true]',
        'level': 'info',
        'description': '发现%s %s 已导出，但在应用级别受权限保护。',
        'name': '%s %s 在应用级别受权限保护。[%s] [android:exported=true]',
    },
    'exported_protected_permission_signatureorsystem_app_level': {
        'title': '%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'info',
        'description': ('发现%s %s 已导出，但在应用级别受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。'
                  '建议改用 signature 级别。对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': '%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'exported_protected_permission_app_level': {
        'title': '%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [android:exported=true]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受一个在所分析的应用中未定义的应用级别权限保护。'
                  '因此，应在定义该权限的地方检查其保护级别。如果设置为 normal 或 dangerous，'
                  '恶意应用可以请求并获得该权限并与该组件进行交互。如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': '%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [android:exported=true]',
    },
    'explicitly_exported': {
        'title': '%s (%s) 未受保护。 [android:exported=true]',
        'level': 'warning',
        'description': '发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。',
        'name': '%s %s 未受保护。 [android:exported=true]',
    },
    'exported_intent_filter_exists': {
        'title': '%s (%s) 未受保护。存在 intent-filter。',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。'
                  '存在 intent-filter 表明该 %s 已被显式导出。'),
        'name': '%s %s 未受保护。存在 intent-filter。',
    },
    'exported_provider': {
        'title': '%s (%s) 未受保护。 [Content Provider, targetSdkVersion < 17]',
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它是一个 Content Provider，'
                  '目标的 API level 低于 17，这使得它默认处于导出状态，无论应用运行所在系统的 API level 如何。'),
        'name': '%s %s 未受保护。 [Content Provider, targetSdkVersion < 17]',
    },
    'exported_provider_2': {
        'title': ('%s (%s) 在 API level 低于 17 的设备上将不受保护。 [Content Provider,'
                  ' targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider(%s %s) 在 API level 低于 17 的设备上运行，则将被导出。'
                  '在这种情况下，它将与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。'),
        'name': ('%s %s 在 API level 低于 17 的设备上将不受保护。 [Content Provider,'
                  ' targetSdkVersion >= 17]'),
    },
    'exported_provider_normal': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受权限保护。但是，'
                  '该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。如果设置为 signature，'
                  '则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_danger': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受权限保护。但是，'
                  '该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_signature': {
        'title': '%s (%s) 受权限保护。 %s [Content Provider, targetSdkVersion < 17]',
        'level': 'info',
        'description': '发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受权限保护。',
        'name': '%s %s 受权限保护。 [%s] [Content Provider, targetSdkVersion < 17]',
    },
    'exported_provider_signatureorsystem': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'info',
        'description': ('发现%s %s 已导出，但受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。'
                  '建议改用 signature 级别。对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_unknown': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受一个在所分析的应用中未定义的权限保护。因此，'
                  '应在定义该权限的地方检查其保护级别。如果设置为 normal 或 dangerous，'
                  '恶意应用可以请求并获得该权限并与该组件进行交互。如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_normal_app': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它在应用级别受权限保护。但是，'
                  '该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。如果设置为 signature，'
                  '则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_danger_appl': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它在应用级别受权限保护。但是，'
                  '该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_signature_appl': {
        'title': '%s (%s) 在应用级别受权限保护。 %s [Content Provider, targetSdkVersion < 17]',
        'level': 'info',
        'description': '发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它在应用级别受权限保护。',
        'name': '%s %s 在应用级别受权限保护。[%s] [Content Provider, targetSdkVersion < 17]',
    },
    'exported_provider_signatureorsystem_app': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'info',
        'description': ('发现%s %s 已导出，但在应用级别受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。'
                  '建议改用 signature 级别。对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_unknown_app': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion < 17]'),
        'level': 'warning',
        'description': ('发现%s %s 已与设备上的其他应用共享，因此设备上任何其他应用都可以访问它。它受一个在所分析的应用中未定义的应用级别权限保护。'
                  '因此，应在定义该权限的地方检查其保护级别。如果设置为 normal 或 dangerous，'
                  '恶意应用可以请求并获得该权限并与该组件进行交互。如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion < 17]'),
    },
    'exported_provider_normal_new': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider (%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
    'exported_provider_danger_new': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
    'exported_provider_signature_new': {
        'title': '%s (%s) 受权限保护。 %s [Content Provider, targetSdkVersion >= 17]',
        'level': 'info',
        'description': '如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。但它受权限保护。',
        'name': '%s %s 受权限保护。 [%s] [Content Provider, targetSdkVersion >= 17]',
    },
    'exported_provider_signatureorsystem_new': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion >= 17]'),
        'level': 'info',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。建议改用 signature 级别。'
                  '对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion >= 17]'),
    },
    'exported_provider_unknown_new': {
        'title': ('%s (%s) 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受一个在所分析的应用中未定义的权限保护。因此，应在定义该权限的地方检查其保护级别。'
                  '如果设置为 normal 或 dangerous，恶意应用可以请求并获得该权限并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
    'exported_provider_normal_app_new': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider (%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 normal。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
    'exported_provider_danger_app_new': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 dangerous。这意味着恶意应用可以请求并获得该权限，并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
    'exported_provider_signature_app_new': {
        'title': ('%s (%s) 在应用级别受权限保护。 %s [Content Provider,'
                  ' targetSdkVersion >= 17]'),
        'level': 'info',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。'
                  '但它在应用级别受权限保护。'),
        'name': ('%s %s 在应用级别受权限保护。 [%s] [Content Provider,'
                  ' targetSdkVersion >= 17]'),
    },
    'exported_provider_signatureorsystem_app_new': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别。 %s [Content Provider,'
                  ' targetSdkVersion >= 17]'),
        'level': 'info',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受权限保护。但是，该权限的保护级别设置为 signatureOrSystem。建议改用 signature 级别。'
                  '对于大多数用途，signature 级别应该足够，并且不依赖于应用在设备上的安装位置。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别。[%s] [Content Provider,'
                  ' targetSdkVersion >= 17]'),
    },
    'exported_provider_unknown_app_new': {
        'title': ('%s (%s) 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' %s [Content Provider, targetSdkVersion >= 17]'),
        'level': 'warning',
        'description': ('如果该 Content Provider(%s) 在 API level 低于 17 的设备上运行，则将被导出。在这种情况下，'
                  '它仍将受一个在所分析的应用中未定义的应用级别权限保护。因此，应在定义该权限的地方检查其保护级别。'
                  '如果设置为 normal 或 dangerous，恶意应用可以请求并获得该权限并与该组件进行交互。'
                  '如果设置为 signature，则只有使用相同证书签名的应用才能获得该权限。'),
        'name': ('%s %s 在应用级别受权限保护，但应检查该权限的保护级别（若应用在 API level 低于 17 的设备上运行）。'
                  ' [%s] [Content Provider, targetSdkVersion >= 17]'),
    },
}

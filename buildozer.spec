[app]
title = EDITH MARK 50 ULTRA
package.name = edithmark50ultra
package.domain = com.stark.edith
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 50.0
requirements = python3,kivy==2.3.0,requests,wikipedia,plyer,python-dateutil
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_FINE_LOCATION,WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.ant = auto
p4a.branch = master
p4a.bootstrap = sdl2

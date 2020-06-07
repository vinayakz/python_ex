from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Notification!", "Alert! Hi VinayakZ Your System is Hacked...", threaded=True, icon_path=None, duration=10)#3seconds

import time
while toaster.notification_active():
    time.sleep(1)
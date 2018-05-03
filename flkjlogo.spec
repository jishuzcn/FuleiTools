# -*- mode: python -*-

block_cipher = None


a = Analysis(['Life\\FuleiTools\\Resouces\\flkjlogo.ico', 'E:\\Python', 'Life\\FuleiTools\\Main.py'],
             pathex=['D:\\Soft\\Python36-32\\Lib', 'D:\\Soft\\Python36-32\\Lib\\site-packages', '', 'E:\\Python Life\\FuleiTools'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='flkjlogo',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='E:\\Python')

# -*- mode: python -*-

block_cipher = None


a = Analysis(['PythonPrimeApplication1.py'],
             pathex=['Z:\\Visual Studio 2017 projects\\PythonPrimeApplication1\\PythonPrimeApplication1'],
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
          name='PythonPrimeApplication1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='Z:\\Visual Studio 2017 projects\\PythonPrimeApplication1\\Sbstnblnd-Plateau-Apps-libreoffice-math.ico')

@echo off

echo --- �X�N���v�g���J�n���܂��B

cd /d %~dp0
cd ../
Convert_to_exe.py build
xcopy .\res .\build\exe.win-amd64-3.8\res /s/e/i/y
xcopy .\SE .\build\exe.win-amd64-3.8\SE /s/e/i/y
xcopy .\BGM .\build\exe.win-amd64-3.8\BGM /s/e/i/y
cd /d %~dp0

cscript shortcut.vbs

echo --- �X�N���v�g���������܂����B���s����ɂ͉����L�[�������Ă�������(�L�E�ցE`)
pause > NUL
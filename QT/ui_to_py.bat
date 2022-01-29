rem for文内で変数を使うために遅延環境変数の展開を有効化しておく
setlocal enabledelayedexpansion

rem ドラッグ＆ドロップされたファイルをforでまわす
for %%A in (%*) do (

    rem 拡張子が.uiだったら処理続行
    if "%%~xA"==".ui" (

        rem 変数OutpuFileにアウトプットしたいフルパスをセットする
        rem %%~dA = ドライブ名, %%~pA = パス, %%~nA = ファイル名
        set OutpuFile="%%~dA%%~pA%%~nA.py"

        rem %hoge%とすると中身がなくなるので遅延環境変数 !hoge! を使う
        C:\Users\beetl\PycharmProjects\QTPROJECT\test\Scripts\pyside2-uic.exe %%A -o !OutpuFile!

    )

)
rem pause
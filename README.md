# IE啟動事前設定 (使用chrome的話可以忽略)

1. 必須下載IEDriverServer 可執行文件並將其放置在您的PATH 中。

2. 在 Windows Vista、Windows 7 或 Windows 10 上的 IE 7 或更高版本上，您必須將每個區域的保護模式設置設置為相同的值。該值可以打開或關閉，只要每個區域都相同即 
   可。要設置保護模式設置，請從“工具”菜單中選擇“Internet 選項...”，然後單擊“安全”選項卡。對於每個區域，標籤底部都有一個標記為“啟用保護模式”的複選框。此外，必須 
   為 IE 10 及更高版本禁用“增強保護模式”。此選項位於 Internet 選項對話框的高級選項卡中。

3. 瀏覽器縮放級別必須設置為 100%，以便本地滑鼠可以設置為正確的坐標。對於 Windows 10，您還需要在顯示設置中將“更改文本、應用程序和其他項目的大小”設置為 100%。

4. 僅對於 IE 11 ，您需要在目標計算機上設置一個註冊表項，以便驅動程序可以保持與它創建的 Internet Explorer 實例的連接。對於 32 位 Windows 安裝，您必須在註冊表編
   輯器中檢查的密鑰是HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. 對於 64 位 Windows 安裝，關鍵是
   HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. 請注意，FEATURE_BFCACHE子項可能存在也可能
   不存在，如果不存在則應創建。重要提示：在此鍵內，創建一個名為iexplore.exe0的 DWORD 值。

# python 環境設定

1. 透過啟動虛擬環境的方式來跑python
-  cmd模式下，執行啟動`./venv/Script/activate.bat`，關閉的話則為`./venv/Script/deactivate.bat`
- gitbash模式下，執行`source ./venv/Script/activate` 關閉的話則為`source ./venv/Script/deactivate`

2. 執行`pip list`確認是否有在虛擬環境下看到安裝的套件，若無請執行`pip install --no-index --find-links=./resource -r requirements.txt`進行local install

# temperature crawler

1. 設定crawler.ini資料
-  Driver
-  LoginInfo
2. 可先執行test測試功能`
-  config
-  data
-  selenium
-  soup
3. 執行`python main.py`




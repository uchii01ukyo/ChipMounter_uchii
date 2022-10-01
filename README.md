# ChipMounter
電子部品を基板上の指定した位置に配置してくれる機構  
  
<img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/Picture0.png" width="400px">  <img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/Picture1.png" width="150px">
  
3つのステップモーターでXYZ軸移動、別モーターでZ軸回転、吸引ポンプと吐出ポンプで部品のピッキングをしている．  
（詳細：[ChipMounter_System.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/ChipMounter%20System.pdf)）
  
以下のコードを参考にさせていただきました．  
参考：https://github.com/akita11/ChipMounter  
  
## インストール
### 環境
+ MacOS Big Sur (11.6.8)
+ Python 2.7.18
+ ArduinoIDE 1.8.13
  
### 手順
1. ZIP形式でダウンロードして好きな場所で開く．   
2. 「src/start.command」と「src/start-2.command」内のコードを環境に合わせて変更する．  
3. コマンドプロンプトを開き、srcディレクトリに移動する．（cd -...-/Chipmounter_uchii/src）  
4. start.commandの実行権限を渡す．（「chmod u+x start.command」を入力する）
  
  
## 使い方
### CSVファイルの準備
実装部品の位置や角度はCSV形式のファイルから読みとる．  
1. KiCADから実装基板の部品情報（POSファイル）をCSVで出力する．  
2. CSVファイルの一番右に新しい行を挿入し、部品に対応するTrayIDを入力する．  
3. 「src/start-2.command」の以下の部分を、POSファイルにパスを通す．  
  
### 起動
1. M5Stackと使用するPCをUSBで接続する  
2. M5Stackを再起動する（画面に「Chip Mounter」が表示されている状態にする）  
3. start.commandを実行(クリックするだけでOK)  
  
起動後、PC上では２つのコマンドプロンプトが開かれ、GCODEの生成->送信が実行される．  
M5Stackではコマンドを受信し、それに合わせてアクチュエータ制御、画面表示等を実行する．  
  
  
## その他
### GRBLモジュールについて
非常にクセがあって苦労したので、ドキュメントを残すことにした．  
[M5Stack_GRBL_Module.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/M5Stack%20GRBL%20Module.pdf)  
  
### 注意
BOMおよびその他のデータは、著者によってのみテストされています。情報の不足や誤り、バグがある可能性があります。  
  
  
## Author
Uchii Ukyo　(https://github.com/uchii01ukyo)

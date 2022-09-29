## ChipMounter
電子部品を基板上の指定した位置に配置してくれる機構  
比較的小さいもの（チップ抵抗やチップコンデンサ等）ならば自動で配置してくれる  
  
以下のコードを参考にさせていただきました．  
参考：https://github.com/akita11/ChipMounter  
  
## システム
<img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/Picture0.png" width="400px"> . <img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/Picture1.png" width="150px">
  
[ChipMounter_System.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/ChipMounter%20System.pdf)
  
csv_gcode.pyで作ったGCODEを、udp_serial.py、M5grbl_serial.ino、GRBLモジュールとバケツリレーしながら、ステップモータ等を制御している。  
  
<img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/System.png" width="500px">
  
XYZ軸の機構は3Dプリンターのものをそのまま利用。
3つのステップモーターでXYZ軸移動、別モーターでZ軸回転、吸引ポンプと吐出ポンプで部品のピッキングをしている。
  
## 使い方
### 初期設定
1. ZIP形式でダンロードして好きな場所で解凍する．   
2. 「src/start.command」と「src/start-2.command」内のコードを環境に合わせて変更する．  
3. コマンドプロンプトを開き、srcディレクトリに移動する．（cd -...-/Chipmounter_uchii/src）  
4. コマンド「chmod u+x start.command」を入力する．（実行尾権限を渡す）  
  
### CSVファイルの準備
実装部品の位置や角度はCSV形式のファイルから読みとる．  
1. KiCADから実装基板の部品情報（POSファイル）をCSVで出力する．  
2. CSVファイルの一番右に新しい行を挿入し、部品に対応するTrayIDを入力する  
3. 「src/start-2.command」の以下の部分を、ファイルのパスに変更する．  
  
### 起動
1. M5Stackと使用PCをUSBで接続する  
2. M5Stackを再起動する（画面に「Chip Mounter」が表示されている状態にする）  
3. 以下の配線が適切に接続されているか確認する  
  (GRBL1:Grove３本+DC給電, GRBL2:Grove１本＋DC給電, Solenoid:ポンプ２組＋USB12V給電)  
4. start.commandを実行(クリックするだけでOK)  
  
起動後、PC上では２つのコマンドプロンプトが開かれ、GCODEの生成->送信が実行される．  
M5Stackではコマンドを受信し、それに合わせてアクチュエータ制御、画面表示等を実行する．  
  
## GRBLモジュールについて
非常にクセがあって苦労したので、ドキュメントを残すことにした。  
[M5Stack_GRBL_Module.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/M5Stack%20GRBL%20Module.pdf)
  
  
## Author
Uchii Ukyo  

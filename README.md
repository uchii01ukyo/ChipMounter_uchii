## ChipMounter
参考：https://github.com/akita11/ChipMounter  
とりあえず、メモ程度にReadMeをまとめる．  
  
## システム
csv_gcode.pyで作ったGCODEを、udp_serial.py、M5grbl_serial.ino、GRBLモジュールとバケツリレーしながら、ステップモータ等を制御している。  
  
<img src="https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/System.png" width="700px">
  
詳細は以下のドキュメントにまとめる。  
[ChipMounter_System.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/ChipMounter%20System.pdf)
  
  
## ファイル概要
#### ・start.command  
   = csv_serial.pyを実行するコマンドファイル  
  
#### ・start-2.command  
   = udp_serial.pyを実行するコマンドファイル  
  
#### ・M5grbl_serial.ino  
   = M5Stack本体に書き込んであるファームウェア  
   = Serial通信で受け取ったGCODEをGRBLモジュール等に受け渡す  
   = UI操作やその他細々とした調整コード  
  
#### ・udp_serial.py  
 = M5Stackと常時シリアルが開通させるためのコード  
 = UDP通信で受け取ったコマンドをM5Stackに受け渡す  
  
#### ・csv_gcode.py  
   = PC側のメインコード  
   = CSVファイルからGCODEを生成  
   = GCODEを決まったタイミングにUDP通信で送信する  
  
## 初期設定
### ダウンロード
GitHub上からZIP形式でダンロードして解凍する．  
ファイルはどこにおいてもいい．（後で置き場所のパスを指定する．）  
  
### CSVファイルの準備
セットする基板部品の位置はCSVファイルから読み取る。  
KiCADから部品位置をまとめたリストが出力できるので、それを少し修正して用いることにした。  
  
修正方法  
・KiCADから出力されたCSVファイルを開く  
・一番右に新しい行（Tray）を挿入し、部品に対応するTrayIDを入力する  
  
### プログラムの準備
実行環境に合わせてプログラムを少しだけ変更する必要がある。  
  
修正箇所１：  
udp_serial.pyの7行目  
→ M5Stackと接続できるポート名を指定する  
  
修正箇所２：  
csv_gcode.pyの７行目  
→ CSVファイルのあるパスを指定する  
  
修正箇所３：  
start.commandの１行目  
→ csv_gcode.pyがあるパスを指定する  
start-2.command  
→ udp_serial.pyがあるパスを指定する  
  
### コマンドプロンプトに権限を渡す
シェルスクリプトでコードを実行するために、用いるコマンドプロンプトに実行権限を付与する必要がある。  
用いるコマンドプロンプトを開いて、以下のコマンドを入力する。  
  
cd start.commandのあるディレクトリ  
chmod u+x start.command  
chmod u+x start-2.command  
  
commandファイルを実行してもエラーが出る場合は、権限が付与されているか確認する。  
  
## 使い方
### 確認
以下の状態になっているか確認する。  
・CSVファイルを作成して、コード内にパスを指定してある．  
・M5StackとPCはUSBで接続されている．  
・配線が全て繋がっている．(GRBL-1, GRBL-2, Solenoid)  
・M5Stackの画面に「Chip Mounter」の文字が表示されている  
  
### 手順
start-2.commandを実行する  
「Ready...」が出力されることを確認する  
start.commandを実行する  
（M5Stackの画面が切り替わり操作が実行される）  
  
## GRBLモジュールについて
非常にクセがあって、大変苦労したので、ドキュメントを残すことにした。  
[M5Stack_GRBL_Module.pdf](https://github.com/uchii01ukyo/ChipMounter_uchii/blob/master/doc/M5Stack%20GRBL%20Module.pdf)
  
  
## Author
Uchii Ukyo  

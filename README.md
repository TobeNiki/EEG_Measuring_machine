# EEG_Measuring_machine

## Mindwave mobile2 から脳波データを取得し，csvファイルとしてかき出す簡易ソフト

***

* 動作環境
  * python2.7

* 使用ライブラリ
  * NeuroPy (脳波取得ライブラリ(python2.7でしか動作しない))
  * Tkinter　(GUI)
  * pandas (csv出力するために使用)
  * threading
  * datetime　(タイムスタンプに使用)
 
***

## 使用方法
PORT:BluetoothのCOMを指定<br>
Data:取得するデータ(各帯域データしか現時点想定していないため "eeg" を入力してください)<br>
directory:保存先のフォルダを指定<br>
filename:保存されるファイルを識別するためのユニークな名前を設定<br>


***

## 注意点(問題点)

<font color="red">初回計測は正しく動作するが，次回の計測は正常に動作しないので，再起動をする必要がある</font>

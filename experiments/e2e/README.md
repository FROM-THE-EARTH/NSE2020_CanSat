# E2Eテスト


## 目的

作成したアプリケーションのミッション遂行能力を確かめる．


## テスト方法

### 概要

テストはコンテクストを次の2つに分けて行う．

1. MissionStandbyNode ~ ParaSeparateNode (C1)
2. FirstRunningNode ~ GoalDetectNode (C2)

2つのテストはその一部始終を動画で記録する．

### C1

C1 は[落下検知・パラシュート分離テスト](../falling/)で行った結果を利用する．

### C2

C2 は走行に関わるコンテクストである．
このテストで主に評価する部分は次の2つ:

1. 子機を定めた座標の半径$x$[m]以内に分離できるか
2. ゴール (三角コーン) へ向けて接近できているか


## 結果

### 第1実験

- 実施日時 : 2020/11/xx
- 実施場所 : 
- 設定値
    * $x = 1$
    * 子機放出座標 (latitude, longitude)
    * ゴール座標 (latitude, longitude)


## 考察
# Graph

## 強連結成分分解

### 強連結成分分解とは

有向グラフにおいて以下のようにグルーピングする

- 互いに行き来できる場合 -> 同じグループにする
- 互いに行き来できない場合 -> 違うグループにする

![image](https://user-images.githubusercontent.com/45358277/175283760-51cc3a61-590a-4646-b594-ccf2ce4ce9cc.png)

[出典](https://manabitimes.jp/math/1250)

上記図で強連結成分分解した場合、`{{a,b,c}, {d,e}, {f}, {g}}`となる

### アルゴリズム

#### STEP1

深さ優先探索（DFS）をして、最深部から順番に番号を記録

#### STEP2

グラフの向きをすべて逆向きにしたものに対して再度深さ優先探索を行う。スタートはSTEP1で記録した番号の大きいものから行う。辿れたところまでを一つのグループとする。

▼例

![image](https://user-images.githubusercontent.com/45358277/175303071-80dba23f-5f61-4568-bfbf-50cfea9d10f5.png)

[出典](https://manabitimes.jp/math/1250)

### 参考

- [https://twitter.com/e869120/status/1385363292739104775/photo/1](https://twitter.com/e869120/status/1385363292739104775/photo/1)
- [https://manabitimes.jp/math/1250](https://manabitimes.jp/math/1250)

### 補足

強連結成分分解を利用して同じグループを一つにまとめると、閉路のない有向グラフ（DAG）となる。
# テクスチャの書き換えガイド

このリソースパックの、アイテム・チップ・チップスロットの絵の一覧と、書き換え方です。

## 基本

| 項目 | 内容 |
|---|---|
| サイズ | **すべて 16×16 px**（PNG。透過あり = RGBA） |
| 置き場所 | `assets/minecraft/textures/item/<id>.png` |
| 対応バージョン | Minecraft 26.3（リソースパック形式 `97`） |

1 つの絵は、次の **3 つのファイル**（すべて同じ `<id>`）でできています。**絵を描き直すだけなら、PNG を上書きするだけ**で済みます（ファイル名は変えない）。

| ファイル | 役割 |
|---|---|
| `assets/minecraft/textures/item/<id>.png` | 絵そのもの（16×16） |
| `assets/minecraft/models/item/<id>.json` | モデル（平らなアイテム `item/generated`。絵を 1 枚貼るだけ） |
| `assets/minecraft/items/<id>.json` | アイテムの定義（プラグインが指定する `item_model` の `minecraft:<id>` が、これを指す） |

- プラグインは、アイテムに `item_model = minecraft:<id>` を付けて出します。**id は、そのまま `item_model` の名前**です。
- 描き直しのコツ: 背景は透過にする。縁は 1px の濃い色で囲むと、既存の絵と揃います。インベントリの枠は、うすいグレーです。
- 16×16 より大きい PNG（32×32 など）も使えますが、ほかのアイテムと、ドットの細かさが揃わなくなります。

## 使用アイテム（消耗品）

ベースのアイテムは、すべて `carrot_on_a_stick` です（見た目は `item_model` が決めます）。

| id | 表示名 | 絵のファイル |
|---|---|---|
| `magic_rod` | 魔法の杖 | `textures/item/magic_rod.png` |
| `thunder` | 雷落とし | `textures/item/thunder.png` |
| `position_ball` | 移動玉 | `textures/item/position_ball.png` |
| `target_position_ball` | 追跡型移動玉 | `textures/item/target_position_ball.png` |
| `poison_ball` | 毒弾 | `textures/item/poison_ball.png` |
| `controller` | 採掘速度低下装置 | `textures/item/controller.png` |
| `mine_drink` | 採掘ドリンク | `textures/item/mine_drink.png` |
| `mine_score_tank` | 掘削ポイントタンク | `textures/item/mine_score_tank.png` |
| `mine_score_drain_tank` | 掘削ポイント吸収タンク | `textures/item/mine_score_drain_tank.png` |
| `effect_clear` | 効果消去 | `textures/item/effect_clear.png` |
| `resistance_shield` | 耐性の盾 | `textures/item/resistance_shield.png` |
| `gather_scroll` | 集合の巻物 | `textures/item/gather_scroll.png` |
| `invisible_book` | 透明化の書 | `textures/item/invisible_book.png` |
| `heart_boost` | 体力強化 | `textures/item/heart_boost.png` |
| `strength_fire` | 攻撃の炎 | `textures/item/strength_fire.png` |
| `round_end_bell` | ラウンド終了の鈴 | `textures/item/round_end_bell.png` |
| `ward_charm` | 身代わりの札 | `textures/item/ward_charm.png` |
| `peek_crystal` | 手札のぞきの水晶 | `textures/item/peek_crystal.png` |
| `bluff_card` | ブラフの札 | `textures/item/bluff_card.png` |
| `counter_stance` | 迎撃の構え | `textures/item/counter_stance.png` |
| `steal_glove` | スリの手袋 | `textures/item/steal_glove.png` |
| `gacha` | ガチャ | `textures/item/gacha.png` |

`gacha` は、ホットバー 8 に常に配られるアイテムです。

## チップスロットの枠

インベントリの右側 3×3 の空きマスに置かれる目印です（ベースのアイテムは、グレーの色付きガラス板）。

| id | 表示名 | 絵のファイル | 備考 |
|---|---|---|---|
| `chip_slot` | チップスロット | `textures/item/chip_slot.png` | 空きマス 1 つぶんの絵。9 マスとも同じ絵が使われる。マスの背景（うすいグレー）の上に、そのまま重なる |

## チップ（12 種）

ひな型（仮の絵）が入っています。**絵を上書きするだけ**で、そのまま使われます。ベースのアイテムは、紙です。

| id（= `item_model`） | 表示名 | 系統 | 仮の絵 | 絵のファイル |
|---|---|---|---|---|
| `chip_echo` | 残響 | 使用 | 青のチップ + 「X 印」 | `textures/item/chip_echo.png` |
| `chip_rebate` | 還元 | 使用 | 青のチップ + 「P 型」 | `textures/item/chip_rebate.png` |
| `chip_trace` | 逆探知 | 使用 | 青のチップ + 「輪」 | `textures/item/chip_trace.png` |
| `chip_fuse` | 予兆短縮 | 使用 | 青のチップ + 「矢印」 | `textures/item/chip_fuse.png` |
| `chip_chain` | 連鎖採掘 | 採掘 | 金のチップ + 「ジグザグ」 | `textures/item/chip_chain.png` |
| `chip_vein` | 鉱脈 | 採掘 | 金のチップ + 「十字」 | `textures/item/chip_vein.png` |
| `chip_tailwind` | 追い風 | 採掘 | 金のチップ + 「波」 | `textures/item/chip_tailwind.png` |
| `chip_savings` | 貯蓄 | 採掘 | 金のチップ + 「袋」 | `textures/item/chip_savings.png` |
| `chip_tenacity` | 粘り | ダメージ | 赤のチップ + 「逆三角」 | `textures/item/chip_tenacity.png` |
| `chip_grit` | 痛み分け | ダメージ | 赤のチップ + 「市松」 | `textures/item/chip_grit.png` |
| `chip_fury` | 気迫 | ダメージ | 赤のチップ + 「稲妻」 | `textures/item/chip_fury.png` |
| `chip_solace` | 見舞い金 | ダメージ | 赤のチップ + 「四角の枠」 | `textures/item/chip_solace.png` |

チップの効果の一覧は、プラグインの `chips.yml` と README にあります。

### 画面下の表示（フォント）

置いているチップは、画面下（ホットバーの上の行）に、**同じ絵を小さく（約 10px）** 並べて出します（例: 絵 `×2`）。そのため、**`textures/item/chip_<id>.png` の絵が、そのまま画面下の表示にも使われます**。小さくしても見分けがつくように描いてください。

- 絵は、フォント定義 `assets/minecraft/font/chips.json`（フォント id `minecraft:chips`）に、文字として登録してあります。
- 文字と id の対応（プラグインの `chips.yml` の `glyph` と、同じ）:

| チップ id | 文字コード | チップ id | 文字コード |
|---|---|---|---|
| `chip_echo` | U+E000 | `chip_savings` | U+E007 |
| `chip_rebate` | U+E001 | `chip_tenacity` | U+E008 |
| `chip_trace` | U+E002 | `chip_grit` | U+E009 |
| `chip_fuse` | U+E003 | `chip_fury` | U+E00A |
| `chip_chain` | U+E004 | `chip_solace` | U+E00B |
| `chip_vein` | U+E005 | | |
| `chip_tailwind` | U+E006 | | |

- 絵を描き直すだけなら、フォント定義は触りません。
- 新しいチップを足すときは、`font/chips.json` に 1 つ足し（`file` は `minecraft:item/chip_<id>.png`、`chars` は次の空いている文字）、プラグインの `chips.yml` の `glyph` に同じ文字コードを書きます。

## 使っていないもの

| id | 備考 |
|---|---|
| `transparent` | 透明な絵（プラグインからは、今は使っていない） |
| `drink_bin` | 空き瓶の絵（プラグインからは、今は使っていない） |

## 手順

### 絵を描き直す

1. `assets/minecraft/textures/item/<id>.png` を、16×16 の PNG で上書きする。
2. `./build.sh` を実行して、`pack.zip` を作る（SHA1 も表示される）。
3. GitHub の Releases に、新しいタグで `pack.zip` を上げる。
4. サーバーの `docker-compose.yml` の `RESOURCE_PACK`（URL）と `RESOURCE_PACK_SHA1` を、新しい値にして、コンテナを作り直す。

手元で見た目だけ確かめるときは、フォルダごと（または `pack.zip`）を、クライアントの `resourcepacks/` に置いて選ぶと、サーバーを使わずに確認できます。

### 新しいアイテム・チップを足す

**リソースパック側**は、同じ `<id>` で、上の 3 つのファイルを足すだけです（既存の `.json` をコピーして、`<id>` を書き換える）。

**プラグイン側**は、次のとおりです。

- 使用アイテム: `items.yml` に行を足す。ただし、**効果は id ごとにプラグインの中にある**ので、新しい効果には、コードが必要です。
- チップ: `chips.yml` に行を足すと、見た目の id は自動で `chip_<id>` になります。効果は、コードが必要です。

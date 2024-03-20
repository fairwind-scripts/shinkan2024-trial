# 新歓2024 HP・PF担当体験会 <!-- omit in toc -->

## 環境構築

### Docker Desktop のインストール

[公式サイト](https://docs.docker.com/desktop/)を参考に Docker Desktop をインストールしてください。

- [macOS](https://docs.docker.com/desktop/install/mac-install/)
- [Windows](https://docs.docker.com/desktop/install/windows-install/)

macOS の場合、Homebrew を使用してインストールすることもできます。

```bash
brew install docker --cask
```

次のコマンドでバージョンが表示されれば、インストールは完了です。

```bash
docker --version
```

インストールが完了したら、Docker Desktop を起動してください。

### VSCode のインストール

[公式サイト](https://code.visualstudio.com/Download)を参考に VSCode をインストールしてください。

macOS の場合、Homebrew を使用してインストールすることもできます。

```bash
brew install visual-studio-code --cask
```

インストールが完了したら、VSCode を起動してください。

なお、以下の表記は、[Japanese Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja) がインストールされていることを前提としています。

### `code` コマンドのインストール

VSCode を起動したら、「表示」→「コマンドパレット」を選択し、`Shell Command: Install 'code' command in PATH` を実行してください。

これで、ターミナルから `code` コマンド（VSCode を起動するコマンド）が使用できるようになります。

### Git のインストール

[公式サイト](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)を参考に Git をインストールしてください。

macOS の場合、Homebrew を使用してインストールすることもできます。

```bash
brew install git
```

次のコマンドでバージョンが表示されれば、インストールは完了です。

```bash
git --version
```

### リポジトリのクローン

次のコマンドで、このリポジトリをクローンしてください。

```bash
git clone https://github.com/fairwind-scripts/shinkan2024-trial.git
```

クローンしたら、次のコマンドでディレクトリを移動してください。

```bash
cd shinkan2024-trial
```

### VSCode で開く

次のコマンドで、VSCode でこのリポジトリを開いてください。

```bash
code .
```

### Dev Container のインストール

VSCode でこのリポジトリを開いたら、拡張機能のパネルを開き、[Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストールしてください。

### Dev Container で開く

ウィンドウ左下の`><`のようなアイコンをクリックし、「コンテナで再度開く」を選択してください。

しばらく待つと、Dev Container が起動します。

この時点で、Flask の開発環境が整っていて、<http://localhost/> で開発用サーバにアクセスできるようになっています。

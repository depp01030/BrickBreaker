

# 如何優雅的啟動一個Python專案

>*鑑於最近vibe coding 越來越紅，我想很多人應該會想知道該怎麼正確啟動一個python 專案。
>包含怎麼正確安裝python、安裝工具、安裝套件等等。
>希望這篇文章可以幫助到還在學習的你！*


## 0. 大綱

- 1. 環境與工具準備 ：工欲善其事
	- 執行程式的工具
	- 環境管理工具 
	- 編輯程式的工具
	- 管理程式版本的工具
- 2. 專案初始化 ：做好專案的環境隔離
	- 建立一個github repository
	- 建立一個專案專用的虛擬環境
	- hello world !
- 3. 開始「打磚塊專案」：Here we go~
	- 安裝需要用到的python套件
	- 撰寫readme
	- 撰寫file_structure說明文件（讓ai知道你的檔案結構

## 1. 環境與工具準備

這個階段我們需要先準備好我們要使用的工具。
包含**執行程式的工具**、**管理環境的工具**、**編輯程式的工具**以及**管理程式版本**的工具四樣。
### 1.1 執行程式的工具
阿就是Python，通常你電腦預設就有了
你可以打開terminal (黑色框框，windows 叫做cmd)
輸入

```
python --version

> Python 3.10.3 # 如果回應是這個代表你已經裝好哩
```

如果是下列就比較麻煩，可能是你沒裝或是系統沒找到
```
> 'python' 不是內部或外部命令 # windows

> command not found: python # macOS

```

如果是找不到的情況了話，可以嘗試用下列指令搜尋
Windows：

```
where python
```

macOS：

```
which python
```

如果出現`/Users/.pyenv/shims/python` 代表你有裝在某個地方，但系統不知道。這邊我們要解釋一下，什麼叫做系統不知道。

**系統不知道什麼？**

當你在終端機輸入「python --version」這個指令時，系統預期是要去執行一個叫做python.exe的可執行檔（executable），並且把`--version` 作為參數傳入。
但現在系統「不知道」這個executable在哪。

**你的問題：**

>「怎麼把我的python 路徑設定到系統的環境變數中。」

好了，再來就是把你的問題丟去gpt了，加油！

### 1.2 管理環境的工具

在討論管理環境的工具有哪些前，我們先說一下為什麼要管理環境。
當我們在開發專案的時候，我們通常傾向**專案之間用到的東西彼此互不影響**
不論是套件，還是python版本。
![[TechWahle - Frame 3.jpg]]
也就是我們更傾向下方的圖示。

目前常見的環境管理工具有：
- anaconda （超厚重，我不太喜歡）
- pyenv （可以管理python 版本）
- uv (可以管理套件跟python版本，目前很紅)

有興趣的人可以看參考文章裡的uv介紹！

這裡我們採取的管理方案是：
- python版本：pyenv
- 套件版本：不另外安裝工具，直接用虛擬環境做隔離。

--- 
#### Windows：

Windows 不支援原生 `pyenv`，你可以使用【非官方版本】：  
**pyenv-win**

**安裝方式：用 pip 安裝**

```bash
pip install pyenv-win --target %USERPROFILE%\.pyenv
```

然後加入環境變數（手動）：

1. 新增環境變數（請到 Windows「編輯環境變數」）
2. 重新開啟命令提示字元，再輸入：
```bash
pyenv --version
```
#### macOS：

使用 `Homebrew` 安裝（macOS 推薦）

```bash
brew update
brew install pyenv
```

安裝後，加入 shell 初始化設定

開啟 zsh（macOS 預設）

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```


安裝完後測試，老樣子。
```bash
pyenv --version
```

> *補充：這個指令會在你的系統j環境變數 PATH 中找尋 `pyenv` 對應的可執行檔（在 `$PYENV_ROOT/bin` 中），並傳入 `--version` 作為參數來執行它。


---

### 1.3 編輯程式的工具

開發 Python 專案時，你需要一個好用的文字編輯器或 IDE（整合開發環境）。
這裡是一些常見工具簡介：
  
* **VSCode**（Visual Studio Code）
	* 最主流的選擇，免費、擴充豐富、對新手非常友善
	* 支援語法高亮、LSP（智能補全）、Git 整合等功能
* **Cursor**
	* 基於 VSCode 打造，但整合了 AI 助手，支援 GPT-4 協作開發
	* 主打 "vibe coding" 體驗，讓寫程式更順、更像對話
* **Spyder**
	* 適合資料分析、數值計算與科學運算（內建於 Anaconda）
	* 提供 Jupyter-like 體驗與變數總覽功能，但功能略偏科學用途
* **Notepad++**
	* 輕量級文字編輯器，支援 Python 基本語法高亮
	* 沒有智能提示與除錯功能，適合學習初期觀察程式結構用
	* 我開玩笑的...

所以這裡我們就直接選 **VSCode**！
### 1.4 管理程式版本

Git 是一個用來管理你程式版本的工具，網路上有太多教學文章，這邊就不贅述。
Git的好處很多，其中，對一個新手而言最重要的好處就是版本控制。

**沒有這個工具會怎樣？**

試想你今天，要增加一個新功能看看效果。為此你做出來Ｂ版本的程式。
沒有這個工具，你很難讓你Ａ版本的程式跟Ｂ版本的程式，同時存在於這個世界上。
除非你要把你的專案資料夾完整複製一份，取名叫做Ｂ版本。
但...先不要。

---
#### Windows：

1. 到 Git 官方網站下載安裝程式：https://git-scm.com/downloads
2. 執行下載好的安裝檔，**基本上一直按下一步即可**
3. 安裝完成後，打開 cmd 或 PowerShell 輸入：

```
git --version
```

你應該會看到像這樣的結果：

```
git version 2.42.0.windows.1
```

> *補充：再次，老樣子。git 就是會去連到一個executabl。
> 什麼時候設定到環境變數的？你剛剛執行安裝檔的時候。*
#### macOS：

你可以用 Homebrew 安裝：
```
brew install git
```

然後用一樣的方法測試是否安裝成功。

---
## 2. 專案初始化
### 2.1 建立一個github repository

這裡我們有幾個步驟，但網路上一大堆教學所以我們就簡單帶過
1. 註冊帳號
2. 新增repository
	專案名稱 : BrickBreaker
	記得勾選readme 跟 python gitignore
3. clone 到地端資料夾
	`git@github.com:<your_account>/BrickBreaker.git`
上述操作，你可以開cmd / terminal執行，也可以直接開vscode terminal執行唷。

### 2.2 建立一個專案專用的虛擬環境

依照前述，我們想針對這個專案安裝一個專屬的環境，這當中包含兩件事。
- 這個專案要用到的python 版本。
- 這個專案專用的虛擬環境。
聽起來很像，但其實是不同事情
![[Pasted image 20250609162935.png]]

**這裏補充一些常用的pyenv指令**
```bash
pyenv install --list        # 查看可安裝的版本
pyenv install 3.11.3        # 安裝特定版本
pyenv versions              # 查看透過pyenv管理的python版本有哪些
pyenv global 3.11.3         # 設定全域預設版本
pyenv local 3.10.7          # 設定目前資料夾專用版本（會建立 .python-version）
pyenv uninstall 3.10.8      # 刪除特定版本
```

#### 安裝專案用版本
這次的專案配置，我們安裝python 3.10，並且建立虛擬環境。

> *如果本來就有python 3.10就可以跳過*

安裝：
```
pyenv install 3.10
```

檢查是否有安裝成功

```
pyenv versions

>  system
>* 3.10.8 
>  3.10.16 # <- 多出這個
```

在這個資料夾中設定專用的版本

```
pyenv local 3.10.16
```

在terminal中執行看看版本是不是被切過去了

```
python

> Python 3.10.16 (main, Apr  7 2025, 13:59:11) # <- 版本成功被切換了！
> [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
> Type "help", "copyright", "credits" or "license" for more information.
```

**小結**
以防你不知道，下面那個就是vscode terminal。
快捷鍵是 ```ctrl + ` ```。
![[截圖 2025-06-09 下午3.10.28.png]]

到這邊，你電腦裡已經有一個python 3.10.16的版本。
接著，我們要來安裝虛擬環境。

#### 安裝專案虛擬環境

**建立**

```
python -m venv venv
```

因為剛剛已經把這個資料夾的python版本切成3.10.16。
所以這裡的虛擬環境就會直接透過這個版本建立。
建立完會多一個資料夾`venv`

**啟動虛擬環境**

Windows （CMD)
```
venv\Scripts\activate.bat

> (venv) C:\Users\you\project> # 看到這個就是成功哩
```

> *注意不要選到 powershell*

macOS 
```
source venv/bin/activate

> (venv) user@your-mac %  # 看到這個就是成功哩
```

**小結**

到這裡我們已經安裝好虛擬環境！
可以透過`which python` （mac) /  `where python` (windows) 來檢查現在的python來源是哪裡。
如果是`/<你的專案路徑>/BrickBreaker/venv/bin/python`，那就沒錯哩～


### 2.3 hello world !

終於是hello world 了啦！！！

參考文章：
https://mostly-machine.com/vibe-coding-python-tools-tutorial/
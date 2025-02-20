# Cannabis Hall Cryptocurrency Exchange

## 專案簡介
這是一個給泰國Pattya"大麻堂"用專業的加密貨幣匯率計算工具，通過整合幣安（Binance）API即時價格和TT Exchange泰銖匯率，為用戶提供便捷的加密貨幣交易價格計算服務。該工具特別適合需要快速計算加密貨幣兌換泰銖價格的場景。

## 主要功能
- 💹 即時加密貨幣價格查詢
  - 支援USDT、BTC、ETH、BNB等主流加密貨幣
  - 通過幣安API獲取實時價格數據
  
- 💱 匯率整合
  - 整合TT Exchange美元兌泰銖即時匯率
  - 實時顯示當前匯率信息
  
- 💰 靈活的手續費設置
  - USDT專屬手續費率設置
  - 其他加密貨幣統一手續費率設置
  
- 🖥️ 直觀的用戶界面
  - 簡潔清晰的操作介面
  - 即時價格顯示
  - 快速計算功能

## 快速開始
### 方法一：使用批次檔案（推薦）
1. 下載並解壓縮專案檔案
2. 複製 `.env.example` 為 `.env` 並設置您的Binance API密鑰
3. 雙擊運行 `setup.bat` 進行環境設置（僅首次使用需要）
4. 雙擊運行 `run.vbs` 啟動應用程序（推薦，無命令行窗口）
   或運行 `run.bat` 啟動應用程序（會顯示命令行窗口）

### 方法二：手動安裝
#### 系統要求
- Python 3.x
- 網絡連接（用於API調用）
- Binance API密鑰（可從[Binance開發者平台](https://www.binance.com/en/my/settings/api-management)獲取）

#### 安裝步驟
1. 克隆或下載專案到本地
```bash
git clone [repository-url]
cd marijuana-crypto-exchange
```

2. 創建並啟動虛擬環境
```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. 安裝依賴包
```bash
pip install -r requirements.txt
```

4. 配置環境變數
- 複製 `.env.example` 為 `.env`
- 編輯 `.env` 文件，填入您的Binance API密鑰：
  ```
  BINANCE_API_KEY=your_api_key_here
  BINANCE_API_SECRET=your_api_secret_here
  ```

5. 運行應用程序
```bash
python src/main.py
```

## 使用說明
### 基本操作流程
1. 啟動應用程序後，等待主界面加載完成
2. 在主界面輸入：
   - 泰銖金額
   - 選擇目標加密貨幣（USDT/BTC/ETH/BNB/DOGE）
3. 點擊計算按鈕獲取結果
4. 結果將顯示：
   - 換算後的加密貨幣數量
   - 當前匯率
   - 手續費金額

### 手續費設置
1. 進入設置界面
2. 配置：
   - USDT專屬手續費率
   - 其他加密貨幣統一手續費率
3. 保存設置後即時生效

## 依賴包說明
- requests (2.31.0): 用於HTTP請求
- python-binance (1.0.19): Binance API客戶端
- python-dotenv (1.0.0): 環境變數管理
- beautifulsoup4 (4.12.2): 網頁解析

## API參考
### Binance API
- 文檔地址：[Binance API Documentation](https://developers.binance.com/docs/binance-spot-api-docs/rest-api#market-data-endpoints)
- 使用端點：Market Data Endpoints
- 價格查詢：Symbol Price Ticker

### TT Exchange
- 網站地址：[TT Exchange](https://ttexchange.com/)
- 匯率數據：美元兌泰銖即時匯率

## 常見問題解答
### 1. 系統要求
- Windows 10或更新版本（需支援UTF-8編碼）
- Python 3.x
- 顯示器解析度建議1280x900以上

### 2. 無法啟動程序
- 確認已安裝Python 3.x
- 確認已運行 setup.bat 或完成手動環境設置
- 確認 .env 文件存在且配置正確
- 檢查網絡連接是否正常
- 如果出現亂碼：
  * 確認Windows系統地區設置為"泰國"
  * 確認系統已安裝Microsoft YaHei UI字體
  * 在控制台 -> 地區 -> 管理 -> 更改系統地區設置 -> 勾選"使用Unicode UTF-8提供全球語言支援"

### 2. API錯誤
- 確認Binance API密鑰配置正確
- 確認API密鑰具有讀取權限
- 檢查網絡連接是否正常

### 3. 價格顯示異常
- 刷新頁面重新獲取最新數據
- 確認網絡連接穩定
- 檢查Binance API服務是否正常

## 注意事項
- 💡 所有計算結果基於即時市場數據
- ⚠️ 匯率和加密貨幣價格可能存在短暫延遲
- 🔍 建議在進行實際交易前核實所有計算結果
- 📊 價格僅供參考，實際交易價格可能因市場波動而變化
- 🔒 請妥善保管您的API密鑰，不要分享給他人

## 技術支持
如遇到技術問題或需要支援，請通過以下方式聯繫：
- 提交 Issue
- 發送郵件至：[liupony2000@gmail.com]

## 免責聲明
本工具提供的所有數據僅供參考，不構成任何投資建議。使用者應自行承擔使用本工具進行交易決策的所有風險。開發團隊不對因使用本工具而導致的任何損失承擔責任。

## 更新日誌
### v1.0.0 (2025/02/20)
- 初始版本發布
- 支援主流加密貨幣價格查詢
- 整合TT Exchange匯率
- 提供基本計算功能

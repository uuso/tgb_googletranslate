# tgb_googletranslate
python tg bot with translation and google spreadsheets export
:x: Google Spreadsheets require too much security/API/Token stuff, it wont be implemented :(

### Right now it can:
- translates your text `RU <-> EN` in telegram
- responses with click-to-copy messages
- the code can be deployed as yandex cloud serverless app *(free 100K requests per month)* with no need to pay for VM time

##### TO DO
- [ ] use yandex cloud storage to store individual requests in csv files
- [ ] add action to send xlsx to user
- [ ] add action to drop csv
- [ ] create terraform files to automate ycloud deployment (practice)
- [X] ru-eng detection fails in some punctuation symbols
- [ ] add logging
- [ ] add ycloud logging



### Steps to launch this app
1. Create your bot via [@BotFather](https://t.me/BotFather) in telegram app. Copy your bot's token string.
2. Install requirements from file `requirements.txt` in your environment: 
```sh
pip install -r requirements.txt
```
3. run `python app.py $TOKEN` with your token string instead of `$TOKEN`.
4. `Ctrl`+`C` to stop app.
# Data Scraping Scripts
For Accountability Initiative, Centre for Policy Research

## Setting up
1. Download VSCode from [here](https://code.visualstudio.com/download)
2. Download [this zip file](https://github.com/gsidhu/ai_data_scraping_workshop/archive/refs/heads/main.zip) and extract it
3. Open the extracted folder in VSCode
4. Click on `Terminal > New Terminal`
5. Copy and run this code in the Terminal –
```bash
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```

## POSHAN Tracker
Copy and run this code in the Terminal –
```bash
python3 ./poshan-tracker/main.py 
```

This will create two new files `HCM_given_last_30_days.csv` and `THR_given_last_30_days.csv` in the `poshan-tracker` folder.

## PMJAY

**Top Speciality**
Copy and run this code in the Terminal –
```bash
python3 ./pmjay/main.py 
```

This will create a file `pmjay-top-speciality-statewise.csv` in the `pmjay` folder.

**EHCP Performance**
To get EHCP Performance data, simply select all the text in the dashboard and paste it in MS Excel / Google Sheets.

**Statewise Claims Pending/Payment**
1. Open the claims dashboard in your browser: [https://dashboard.pmjay.gov.in/pmj/#/pmjayclaims](https://dashboard.pmjay.gov.in/pmj/#/pmjayclaims)
2. Right click anywhere and click on `Inspect`. This will open the Developer Tools.
3. Click on the `Network` tab and refresh the page.
4. Scroll down till you find a bunch of rows with file name `1.0`.
5. Find the row that has the header `https://dashboard.pmjay.gov.in/pmjservice/api/pmjdashboard/tmsclaim_s_d_h_wise/1.0` for Claims Pending or `https://dashboard.pmjay.gov.in/pmjservice/api/pmjdashboard/tmsclaimtat/1.0` for Claims Payment.
6. Click on the row and then click on the `Response` tab.
7. Right click on the `list:` row and click on `Copy Value`.
8. Go to [JSON2CSV](https://csvjson.com/json2csv) and paste the copied value in the `JSON` box.
9. Delete `{"list": [` from the beginning of the text and the `}` at the end of the text.
10. Click convert and then download the data as CSV.
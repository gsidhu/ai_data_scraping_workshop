import requests

def convert_to_tuples(data):
		tuples = []
		for item in data:
				tuples.append((item["text"], item["value"]))
		return tuples

headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
		# 'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://dashboard.pmjay.gov.in/pmj/',
		'Content-Type': 'application/json',
		'Origin': 'https://dashboard.pmjay.gov.in',
		'DNT': '1',
		'Connection': 'keep-alive',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-GPC': '1',
}

states_dict = {35:"Andaman And Nicobar Islands",28:"Andhra Pradesh",12:"Arunachal Pradesh",18:"Assam",10:"Bihar",4:"Chandigarh",22:"Chhattisgarh",26:"Dadra And Nagar Haveli",25:"Daman And Diu",7:"Delhi",30:"Goa",24:"Gujarat",6:"Haryana",2:"Himachal Pradesh",1:"Jammu And Kashmir",20:"Jharkhand",29:"Karnataka",32:"Kerala",37:"Ladakh",31:"Lakshadweep",23:"Madhya Pradesh",27:"Maharashtra",14:"Manipur",17:"Meghalaya",15:"Mizoram",13:"Nagaland",21:"Odisha",34:"Puducherry",3:"Punjab",8:"Rajasthan",11:"Sikkim",33:"Tamil Nadu",36:"Telangana",16:"Tripura",5:"Uttarakhand",9:"Uttar Pradesh",19:"West Bengal"}
state_codes = list(states_dict.keys())

def get_top_speciality():
	for state_code in state_codes:
		print(states_dict[state_code])
		data = '{"type":"TMSSPEC","state_code":"' + str(state_code) + '","district_code":"","rpttype":"A"}'
		response = requests.post(
				'https://dashboard.pmjay.gov.in/pmjservice/api/pmjdashboard/datalist/1.0',
				headers=headers,
				data=data,
		)
		result = eval(response.text)
		# write tuples to a file
		with open("./pmjay/pmjay-top-speciality-statewise.csv", "a") as f:
			for item in convert_to_tuples(result["list"]):
				f.write(f"{states_dict[state_code]},{item[0]},{item[1]}\n")

if __name__ == "__main__":
	get_top_speciality()
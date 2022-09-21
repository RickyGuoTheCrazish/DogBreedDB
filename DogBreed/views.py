from django.shortcuts import render

# Create your views here.
# b5512dcf40mshd59d089ebff1562p1898a0jsnc99cf4a4a958

def home(request):
    if request.method == 'POST':
        import json
        import requests
        # query = request.POST['query']
        # api_url = 'url'
        # api_request = request.get(api_url + query, headers = {})_

        url = "https://dogbreeddb.p.rapidapi.com/"
        querystring = {"search":request.POST['query']}
        print(querystring)
        headers = {
        "X-RapidAPI-Key": "b5512dcf40mshd59d089ebff1562p1898a0jsnc99cf4a4a958",
        "X-RapidAPI-Host": "dogbreeddb.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            api = json.loads(response.content)
            print(response.content)
            # print(response.te xt)
        except Exception as e:
            api = "uhh..error occurred"
            print(e)
        return render(request,'searchResults.html',{'api':api})    
        # print(response.text)
    else:
        return render(request,'home.html',{'query':'Please enter a valid query'})    



   
def searchResults(request):
    if request.method == 'POST':
        import json
        import requests
        # query = request.POST['query']
        # api_url = 'url'
        # api_request = request.get(api_url + query, headers = {})_

        url = "https://dogbreeddb.p.rapidapi.com/"
        querystring = {"search":request.POST['query']}
        print(querystring)
        headers = {
        "X-RapidAPI-Key": "b5512dcf40mshd59d089ebff1562p1898a0jsnc99cf4a4a958",
        "X-RapidAPI-Host": "dogbreeddb.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            api = json.loads(response.content)
            print(response.content)
            # print(response.te xt)
        except Exception as e:
            api = "uhh..error occurred"
            print(e)
        return render(request,'searchResults.html',{'api':api})    
        # print(response.text)
    else:
        return render(request,'searchResults.html')    




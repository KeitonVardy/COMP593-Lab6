
import requests
from sys import argv

def main(): 

    poke_name = argv[1]
    poke_info = get_poke_info(poke_name)
    if poke_info:
        pb_strings = get_pastebin_strings(poke_info)
        pb_url = post_to_pastebin(pb_strings[0], pb_strings[1])
        print(pb_url)

    

def post_to_pastebin(title, body_text):

    print("Posting to Pastebin...", end='')

    pasteBinParams = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title
    }


    response = requests.post('https://pastebin.com/api/api_post.php', data = pasteBinParams)

    if response.status_code == 200:
        print('Success!')
        return response.text
    else:
        print('Error',response.status_code)
        return response.status_code


def get_poke_info(poke_name): 

    print("Getting Pokemon information...", end='')
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_name))

    if response.status_code == 200:
        print('Success!')
        return response.json()
    else:
        print('Error',response.status_code)
        return
    
def get_pastebin_strings(poke_info):
    
    title = poke_info['name'] + "'s Abilities"

    body_text = ""
    for x in poke_info['abilities']:
         print(x['ability']['name'])
    

    return (title, body_text)




main()

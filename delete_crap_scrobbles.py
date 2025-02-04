import copy
import json
import requests
import time

API_KEY = 'YOUR_API_KEY'
USERNAME = 'YOUR_USER_NAME'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
CSRFTOKEN = '1UHoPy15DXVMzbh0mAncNM0psDVgQcLf'
SESSIONID= '.eJyVVtmuq8YS_Zf9HO_DbDhSHrDBNtiAmaFfLKAxg5lsZqL8-228d-6gqyjJgwW4V1Wtqu611L993IK-S299G79uadCmHz8_wmvTno7zsqcpl5a4rWMGqTnp_C7LGSUOXh-_fLRx22Z1dcsgwkMCZ7ckF2xiKg43VBwTm4DdshuOo5kY24YYxrEo5r8KvcN-_vxpm6IhCegFx0iawjEU8L_AMIgecbWii3v5Ocbh5ziOn0HTtJ8r6PN7_dN-tbtvKIpv-leLQhQrmjRLwjRBGdX8QSvJr7-uy-3XcjzLaXiMMi2TTXuRcDWTWqnsGrCXGKmUg4vD4mCWuU8EbCJSWYE1PBljtNTDhVSLiFSbkKB6UBYzcOU0IuweENwAiKm4lOoQmlxzcac0Io0yNPEUekYtZWPme85DyussMPHW91QMlFiH_sOC_UrggMNjeofHogOmxKAeFsR_URceV1As9FDdgvsimSuTavmEaomzKvikYj3QU1xUwUY9J5giPAg110lV4Me1bkQ62VpXWURczX1cQbNR868ZKZaCqZZOaYI-amtOIULxfHbZy43v6ZmWi6SyJIuyRKNqrTwdKtp_87MkSl30Nz_g4mngjuus5uh4eAVHrgtJf0L8Z_0IO98t2q_ZvHO8vz0SFFFZlIG7zqXBosopUN0y8OTCLw_LOod1D8DR6dFcMIRbEG77Rzx6D6VKHn23q0MCH-DKVZB5QLy59D7BdVKBcyjnEriw94ii98jdHJJgzTmvM0Fcl4iEQ1Tqa88YcOk0rPS1DzyqlO_9wceo5B4X1xjgScSlCuc-he65B7xdJCBogRaO93TYsHB6lC8D5qWgMW4f85330sarFFXitXq10_Nq3JUrUSt9fiWTNgKEctFHdQ8lR90s0pUWSi1v9iEsfaew-DN7eh2SpOPctGm2znm-k_Wz7PGgIjq-zfKFtB2KJqkzsOK7VAC-ucV0VbbLhXIwBnvsqcF9PVGmKhxp6Nt9fzZdKT30G5V47VRnYZRjwh5vnSoG0iMbl96f6N1hAIF4AaLGt4bHlodrQI81ZR76w7U-k31HnDRlc_Lvm1GcD41yvtLMQ5t8Nj_4McTFxc3Ke3rg2zoh42d9rO61Hb3YhJtZ7HkbdqY1F-dbBTnSMDc3-NR35_FZKZwya0zOrzLt_oZM82Tyc3tW8kOhEiIOjvYILCcFuU6rhI1U46TqYmSKAB6aIGe-FVHaUXrvcOzxa86zg-vZXf9TkfukMwPPGALC6S8lHEICtsCk85DAhj8T8JeDPLoQHSp4BN3FXUWdrGXfJuCRRhO69v-LqnIW4Mn3wF0PnrQolo0EbE9KrhPqItLoOSlIaKqQUEjUNBIxhoQ3KmvdSsX97J-bQuAeMCQAJFCFUhYFCceeEc8iPvH_5oewxLfovwWHBFPt0oBIh9DlCGQCo_LYVaF7aML9ezZrr8X7-8ARqKcGmWSxzgWeZByYyCj-Y5qZVrWIh1GEldEggRfR_Bb8VzyKcee_MhMZ3lHOiCiqEJkj-q1CJdac0ToTxBWZNRmS8mPtGSIj8V167RsZqrx8708XneQB7PFHSBqTasocOhaXgu4tpSlOh-k561oDzZio-i1_tZ8erF7yE-wuhhNGW2dfPxvMZKfBf7Cvy6uUi9o7mnIQR1n56j3oP_M9xcm-a5KFRsOt04GyYSPZIjwy0G2afu6mp4ZNKQYL3IiVnWTl0eliG5ZA-QnkIK1blDhWe6t3hJOxE8ReE0MLDFcum8jz1ZcU3BWuWO-N5Ya_aMJe5EB3buiNLMXDjZwsh042-0XONu49YBnOZkFeG6A2W-qqs_Gw2TG9iDbSejZOW_RNZlFwK8LMqeZ-Q9cMJzeqpsstPQbw_txTScWYFHjZZ1720rlpYmxXzrNQRSfTDC9P0eKXABbMHAz36Lh7-g-igGWpGhmWIHkjcd9ecfJ1FSBxmmFonKCYLc4RFE5SNMWyFMYxDLWlMAzhmyKYi6ztsip53wpQ1I_1ivAjmIOqftR5VtYw_vEHrP34_V9RmP1M:1tf14r:_9Vw9MNuGJubb0YLfOYQVOO5dGGPT4MR6TIsW0-NDkk'

CSRFMIDDLEWARE='2qIXnqSzgWGUxxyI90G7m6QKwdK9AGHHTafb2OJuJJrwWyFylqT9ZIGZOGvfgIiM'

BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

def get_all_scrobbles():
    page = 1
    scrobbles = []
    while True:
        print(f"Parsing page {page}; Total scrobbles: {len(scrobbles)}")
        params = {
            'method': 'user.getrecenttracks',
            'user': USERNAME,
            'api_key': API_KEY,
            'format': 'json',
            'page': page,
            'limit': 200
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if 'recenttracks' not in data or 'track' not in data['recenttracks']:
            break
        scrobbles.extend(data['recenttracks']['track'])
        if int(data['recenttracks']['@attr']['page']) >= int(data['recenttracks']['@attr']['totalPages']):
            break
        page += 1
        time.sleep(0.25) # respect API!
    return scrobbles

def read_scrobbles_from_file(filename='scrobbles.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            scrobbles = json.load(file)
        print(f"Scrobbles have been read from {filename}")
        return scrobbles
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except json.JSONDecodeError:
        print(f"File {filename} contains invalid JSON.")
        return []

def write_scrobbles_to_file(scrobbles, filename='scrobbles.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(scrobbles, file, ensure_ascii=False, indent=4)
    print(f"Scrobbles have been written to {filename}")

def count_artist_listens(scrobbles):
    artist_counts = {}
    for scrobble in scrobbles:
        artist = scrobble['artist']['#text']
        if artist in artist_counts:
            artist_counts[artist] += 1
        else:
            artist_counts[artist] = 1
    return artist_counts

def filter_shitty_scrobbles(scrobbles, artist_counts):
    shitty_scrobbles = []
    for scrobble in scrobbles:
        artist = scrobble['artist']['#text']
        if artist_counts[artist] == 1:
            shitty_scrobbles.append(scrobble)
    return shitty_scrobbles

def delete_scrobble(scrobble):
    referer = 'https://www.last.fm/user/{USERNAME}'
    headers = {
        'Referer': referer,
        'User-Agent': USER_AGENT,
    }
    cookies = {
        'sessionid': SESSIONID,
        'csrftoken': CSRFTOKEN
    }
    data = {
        'artist_name': scrobble['artist']['#text'],
        'track_name': scrobble['name'],
        'timestamp': scrobble['date']['uts'],
        'csrfmiddlewaretoken': CSRFMIDDLEWARE
    }
    response = requests.post(f'https://www.last.fm/user/{USERNAME}/library/delete', data=data, headers=headers, cookies=cookies)
    time.sleep(0.25) # respect API!
    print(f'{scrobble["name"]}: {response.status_code}')
    return response.status_code == 200

def edit_scrobble(before_scrobble, after_scrobble):
    referer = 'https://www.last.fm/user/{USERNAME}'
    headers = {
        'Referer': referer,
        'User-Agent': USER_AGENT,
    }
    cookies = {
        'sessionid': SESSIONID,
        'csrftoken': CSRFTOKEN
    }
    data = {
        'artist_name_original': before_scrobble['artist']['#text'],
        'artist_name': after_scrobble['artist']['#text'],
        'track_name_original': before_scrobble['name'],        
        'track_name': after_scrobble['name'],
        'album_name_original': before_scrobble['album']['#text'],        
        'album_name': after_scrobble['album']['#text'],
        'timestamp': before_scrobble['date']['uts'],
        'submit': 'edit-scrobble',
        'ajax': 1,
        'csrfmiddlewaretoken': CSRFMIDDLEWARE
    }
    response = requests.post(f'https://www.last.fm/user/{USERNAME}/library/edit-track?edited-variation=library-scrobble', data=data, headers=headers, cookies=cookies)
    time.sleep(0.25) # respect API!
    print(f'{after_scrobble["artist"]["#text"]}>>>{after_scrobble["name"]}: {response.status_code}')
    return response.status_code == 200 

def write_scrobbles_to_file_readable(scrobbles, output_file='super_shitty_scrobbles.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for scrobble in scrobbles:
            artist = scrobble['artist']['#text']
            track_name = scrobble['name']
            file.write(f"{artist}/{track_name}\n")

def write_filtered_scrobbles_to_file(scrobbles, output_file='filtered_super_shitty_scrobbles.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for scrobble in scrobbles:
            file.write(f"{scrobble}\n")

def filter_ollama(client, data): # i tried using llm to track names :d 50/50 kinda
    filtered_names = []
    dropped_names = []
    for line in data:
        response = client.generate(
            model='llama3', 
            prompt=f"Does this title belong to a music or non-music content? Respond only with 'music' or 'non-music': {line}",
        )
        is_music = not "non-music" in response.response.lower()
        if is_music:
            filtered_names.append(line.strip())
        else:
            dropped_names.append(line.strip())
        print(f'{line.strip()} is{" not" if not is_music else ""} music')
    return filtered_names, dropped_names

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def filter_delete_simple(all_scrobbles):
    write_scrobbles_to_file(all_scrobbles, 'scrobbles.json')
    artist_counts = count_artist_listens(all_scrobbles)
    shitty_scrobbles = filter_shitty_scrobbles(all_scrobbles, artist_counts)
    write_scrobbles_to_file(shitty_scrobbles, 'shitty_scrobbles.json')
    write_scrobbles_to_file_readable(shitty_scrobbles, 'super_shitty_scrobbles.txt') # in human-readable format hopefully

    input(f'You are about to delete {len(shitty_scrobbles)} precious scrobbles!!!!!!!!!!\nPress enter to continue..........................')
    input(f'ARE YOU REALLY SURE?????')

    cleaned_scrobbles = []
    failed_scrobbles = []
    for scrobble in shitty_scrobbles:
        if delete_scrobble(scrobble):
            cleaned_scrobbles.append(scrobble)
        else:
            failed_scrobbles.append(scrobble)
    print(f'Failed: {len(failed_scrobbles)} Succeed: {len(cleaned_scrobbles)}')
    write_scrobbles_to_file(cleaned_scrobbles, 'cleaned_scrobbles.json')
    write_scrobbles_to_file(failed_scrobbles, 'failed_scrobbles.json') # you can retry

def needs_editing(artist1, artist2):
    return artist1.lower() in artist2.lower() and artist1.lower() != artist2.lower()

def rename_scrobbles(scrobbles, mappings):
    tuples = []
    for scrobble in scrobbles:
        artist_name = scrobble['artist']['#text']
        for patterns, corrected_name in mappings:
            if any(needs_editing(pattern, artist_name) for pattern in patterns):
                edited_scrobble = copy.deepcopy(scrobble)
                edited_scrobble['artist']['#text'] = corrected_name
                tuples.append((scrobble, edited_scrobble))
                break
    return tuples

def write_tuples_to_file_readable(tuples, output_file='tuples_changes.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for tuple in tuples:
            before = tuple[0]['artist']['#text']            
            after = tuple[1]['artist']["#text"]
            file.write(f"{before} >>>>>>>> {after}\n")


def rename_scrobble_artists(all_scrobbles):
    tuples = rename_scrobbles(all_scrobbles)
    write_tuples_to_file_readable(tuples, 'tuples_changes.txt')    
    write_scrobbles_to_file(tuples, 'tuples_changes.json')

    input(f'You are about potentially ruin {len(tuples)} precious scrobbles!!!!!!!!!!\nPress enter to continue..........................')
    input(f'ARE YOU REALLY SURE?????')

    cleaned_tuples = []
    failed_tuples = []
    for tuple in tuples:
        if edit_scrobble(tuple[0], tuple[1]):
            cleaned_tuples.append(tuple)
        else:
            failed_tuples.append(tuple)
    print(f'Failed: {len(failed_tuples)} Succeed: {len(cleaned_tuples)}')
    write_scrobbles_to_file(cleaned_tuples, 'cleaned_tuples.json')
    write_scrobbles_to_file(failed_tuples, 'failed_tuples.json') # you can retry

def main():
    all_scrobbles = get_all_scrobbles()
    #write_scrobbles_to_file(all_scrobbles)
    # if you parsed all of your scrobbles already you can read it from file
    # if you don't wan't to wait or to disturb api
    # all_scrobbles = read_scrobbles_from_file('scrobbles.json')
    filter_delete_simple(all_scrobbles)

    # entries in array are patterns, if they are detected
    # it will rename the artist inside the scrobble to the second item in tuple
    # sometime fails
    mappings = [
        (['Diabarha', 'Legion of'], 'Diabarha'),
        (['Aiobahn'], 'Aiobahn'),
        (['Atols'], 'Atols'),
        (['相対性理论', 'Sōtaisei Riron'], '相対性理论'),
        (['AVTechNO!'], 'AVTechNO!'),
        (['Kikuo'], 'Kikuo'),
        (['Cynthoni'], 'Cynthoni'),
        (["cosMo＠"], "cosMo＠暴走"),
    ]
    rename_scrobble_artists(all_scrobbles, mappings)

if __name__ == '__main__':
    main()
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

source_folder_id = '17V3Sg_UykHz_hEYdUUt4rVRGukCtNn6H'
target_folder_id = '12VpswLe2O7xsFpEJ_zU0vGoszyHi7XOG'
file_id = '1dUg57fmSCSeMTC20ta4R2UkCdpuqHs1Muu_umHN8q8U'
# query = f"parents = '{source_folder_id}'"
query = 'parents = 17V3Sg_UykHz_hEYdUUt4rVRGukCtNn6H'

response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query, pageToken=nextPageToken).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

for f in files:
    if f['mimeType'] != 'application/vnd.google-apps.folder':
        service.files().update(
            fileId=f.get('id'),
            addParents=target_folder_id,
            removeParents=source_folder_id
        ).execute()
